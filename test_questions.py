"""
Test ChristopherGPT with more specific questions about Christopher
"""

from embeddings import ChristopherEmbeddings

def test_specific_questions():
    """Test with more specific questions about Christopher"""
    embedder = ChristopherEmbeddings()
    
    # Load embeddings
    if not embedder.load_embeddings():
        embedder.create_embeddings()
        embedder.save_embeddings()
    
    # More specific test questions
    test_questions = [
        "Where does Christopher go to school?",
        "What did Christopher study?",
        "What does Christopher do for work?",
        "What music does Christopher like?",
        "What books has Christopher read?",
        "What is ChristopherGPT?",
        "What languages does Christopher speak?",
        "What kind of cologne does Christopher wear?",
        "What is Christopher working on?",
        "What are Christopher's career goals?",
        "Is Christopher in a relationship?",
        "What business did Christopher start?",
        "What watch brand is Christopher interested in?"
    ]
    
    print("\n" + "="*60)
    print("TESTING SPECIFIC QUESTIONS ABOUT CHRISTOPHER")
    print("="*60)
    
    for question in test_questions:
        print(f"\nQuestion: {question}")
        print("-" * 50)
        
        relevant_facts = embedder.find_relevant_facts(question, top_k=2)
        
        for i, result in enumerate(relevant_facts, 1):
            print(f"{i}. {result['fact']}")
            print(f"   Similarity: {result['similarity']:.3f}")

if __name__ == "__main__":
    test_specific_questions()
