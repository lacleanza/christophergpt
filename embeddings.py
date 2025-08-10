"""
Text embedding system for ChristopherGPT
This module handles converting text into numerical vectors for semantic search
"""

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os
from personal_data import get_all_facts

class ChristopherEmbeddings:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        """
        Initialize the embedding system
        
        Args:
            model_name (str): Name of the sentence transformer model to use
        """
        print("Loading embedding model...")
        self.model = SentenceTransformer(model_name)
        self.facts = get_all_facts()
        self.embeddings = None
        self.embeddings_file = 'christopher_embeddings.pkl'
        
    def create_embeddings(self):
        """Create embeddings for all facts about Christopher"""
        print("Creating embeddings for Christopher's facts...")
        self.embeddings = self.model.encode(self.facts)
        print(f"Created embeddings for {len(self.facts)} facts")
        
    def save_embeddings(self):
        """Save embeddings to disk for faster loading"""
        if self.embeddings is not None:
            with open(self.embeddings_file, 'wb') as f:
                pickle.dump({
                    'embeddings': self.embeddings,
                    'facts': self.facts
                }, f)
            print(f"Embeddings saved to {self.embeddings_file}")
        
    def load_embeddings(self):
        """Load embeddings from disk if they exist"""
        if os.path.exists(self.embeddings_file):
            print("Loading existing embeddings...")
            with open(self.embeddings_file, 'rb') as f:
                data = pickle.load(f)
                self.embeddings = data['embeddings']
                self.facts = data['facts']
            print("Embeddings loaded successfully")
            return True
        return False
    
    def find_relevant_facts(self, question, top_k=3):
        """
        Find the most relevant facts for a given question
        
        Args:
            question (str): The user's question
            top_k (int): Number of top relevant facts to return
            
        Returns:
            list: Top relevant facts with their similarity scores
        """
        if self.embeddings is None:
            print("No embeddings found. Creating new ones...")
            self.create_embeddings()
            
        # Create embedding for the question
        question_embedding = self.model.encode([question])
        
        # Calculate similarity scores
        similarities = cosine_similarity(question_embedding, self.embeddings)[0]
        
        # Get top k most similar facts
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            results.append({
                'fact': self.facts[idx],
                'similarity': similarities[idx],
                'index': idx
            })
            
        return results
    
    def get_context_for_question(self, question, top_k=3):
        """
        Get context facts formatted for AI response generation
        
        Args:
            question (str): The user's question
            top_k (int): Number of facts to include in context
            
        Returns:
            str: Formatted context string
        """
        relevant_facts = self.find_relevant_facts(question, top_k)
        
        context = "Here are the most relevant facts about Christopher:\n\n"
        for i, result in enumerate(relevant_facts, 1):
            context += f"{i}. {result['fact']} (relevance: {result['similarity']:.3f})\n"
            
        return context

def test_embeddings():
    """Test the embedding system"""
    embedder = ChristopherEmbeddings()
    
    # Try to load existing embeddings, create if they don't exist
    if not embedder.load_embeddings():
        embedder.create_embeddings()
        embedder.save_embeddings()
    
    # Test with some sample questions
    test_questions = [
        "What are Christopher's hobbies?",
        "Does Christopher like sports?",
        "What does Christopher do for fun?",
        "Is Christopher interested in business?",
        "Tell me about Christopher's interests"
    ]
    
    print("\n" + "="*50)
    print("TESTING EMBEDDING SYSTEM")
    print("="*50)
    
    for question in test_questions:
        print(f"\nQuestion: {question}")
        print("-" * 40)
        
        relevant_facts = embedder.find_relevant_facts(question, top_k=3)
        
        for i, result in enumerate(relevant_facts, 1):
            print(f"{i}. {result['fact']}")
            print(f"   Similarity: {result['similarity']:.3f}")

if __name__ == "__main__":
    test_embeddings()
