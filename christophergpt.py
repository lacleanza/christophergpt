"""
ChristopherGPT - AI assistant trained on Christopher's personal data
Main class for the conversational AI system
"""

import os
from openai import OpenAI
from embeddings import ChristopherEmbeddings
from personal_data import get_personality_traits

class ChristopherGPT:
    def __init__(self):
        """Initialize ChristopherGPT with embeddings and optional OpenAI integration"""
        print("🤖 Initializing ChristopherGPT...")
        
        # Initialize embeddings system
        self.embedder = ChristopherEmbeddings()
        
        # Try to load existing embeddings, create if they don't exist
        if not self.embedder.load_embeddings():
            print("Creating new embeddings...")
            self.embedder.create_embeddings()
            self.embedder.save_embeddings()
        
        # Initialize OpenAI if API key is available
        self.openai_client = None
        self.openai_available = False
        self._setup_openai()
        
        # Get personality traits
        self.personality = get_personality_traits()
        
        print("✅ ChristopherGPT ready!")
    
    def _setup_openai(self):
        """Setup OpenAI client if API key is available"""
        api_key = os.getenv('OPENAI_API_KEY')
        if api_key:
            try:
                self.openai_client = OpenAI(api_key=api_key)
                self.openai_available = True
                print("✅ OpenAI API configured")
            except Exception as e:
                print(f"❌ OpenAI setup failed: {e}")
        else:
            print("⚠️  OpenAI API key not found in environment variables")
    
    def get_response(self, question, use_openai=True, top_k=3):
        """
        Get a response to a question about Christopher
        
        Args:
            question (str): The user's question
            use_openai (bool): Whether to use OpenAI for response generation
            top_k (int): Number of relevant facts to consider
            
        Returns:
            dict: Response with answer and metadata
        """
        # Get relevant facts
        relevant_facts = self.embedder.find_relevant_facts(question, top_k=top_k)
        
        if use_openai and self.openai_available:
            answer = self._generate_openai_response(question, relevant_facts)
        else:
            answer = self._generate_basic_response(question, relevant_facts)
        
        return {
            "answer": answer,
            "relevant_facts": relevant_facts,
            "method": "openai" if (use_openai and self.openai_available) else "basic"
        }
    
    def _generate_openai_response(self, question, relevant_facts):
        """Generate response using OpenAI API"""
        try:
            # Prepare context from relevant facts
            context = "Here's what I know about Christopher:\n\n"
            for fact in relevant_facts:
                context += f"- {fact['fact']}\n"
            
            # Create the prompt
            personality_info = f"""
You are Christopher, responding as yourself. Your personality is {self.personality['tone']}.
Your communication style is {self.personality['communication_style']}.
Your main interests include: {', '.join(self.personality['interests'])}.
You value: {', '.join(self.personality['values'])}.
Your goals include: {', '.join(self.personality['goals'])}.

Based on the context below, answer the question as Christopher would, in first person.
Keep responses natural, personal, and engaging. Don't mention that you're an AI or that this is from a database.

Context about Christopher:
{context}

Question: {question}

Response as Christopher:"""

            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Christopher, a computer science and business student passionate about AI and technology. Respond as Christopher would, in first person, based on the provided context."},
                    {"role": "user", "content": personality_info}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"❌ OpenAI API error: {e}")
            return self._generate_basic_response(question, relevant_facts)
    
    def _generate_basic_response(self, question, relevant_facts):
        """Generate basic response without OpenAI"""
        if not relevant_facts:
            return "I don't have specific information about that. Feel free to ask me about my interests, studies, or projects!"
        
        # Simple template-based response
        response = "Based on what I can tell you about myself:\n\n"
        
        for i, fact in enumerate(relevant_facts, 1):
            response += f"{i}. {fact['fact']}\n"
        
        response += "\nFeel free to ask me more specific questions!"
        return response
    
    def chat_loop(self):
        """Interactive chat loop for testing"""
        print("\n" + "="*50)
        print("🤖 ChristopherGPT Chat Interface")
        print("="*50)
        print("Ask me anything about Christopher! Type 'quit' to exit.")
        print()
        
        while True:
            try:
                question = input("You: ").strip()
                
                if question.lower() in ['quit', 'exit', 'bye']:
                    print("👋 Goodbye!")
                    break
                
                if not question:
                    continue
                
                print("🤖 ChristopherGPT: ", end="")
                response = self.get_response(question)
                print(response['answer'])
                print()
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Create and test ChristopherGPT
    bot = ChristopherGPT()
    bot.chat_loop()
