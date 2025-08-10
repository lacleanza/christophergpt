"""
Fix and test the embeddings system for favorite food questions
"""

from embeddings import ChristopherEmbeddings
from christophergpt import ChristopherGPT

def fix_and_test_embeddings():
    print("🔧 FIXING EMBEDDINGS SYSTEM")
    print("=" * 50)
    
    # Initialize embeddings system
    print("1. Creating new embeddings...")
    embedder = ChristopherEmbeddings()
    
    # Force creation of new embeddings
    embedder.create_embeddings()
    embedder.save_embeddings()
    print("✅ New embeddings created and saved")
    
    # Test the specific favorite food question
    print("\n2. Testing favorite food question...")
    test_questions = [
        "What is Christopher's favorite food?",
        "What does Christopher like to eat?",
        "What kind of food does Christopher prefer?",
        "What is Christopher's favorite dish?"
    ]
    
    for question in test_questions:
        print(f"\n❓ Question: {question}")
        print("-" * 40)
        
        results = embedder.find_relevant_facts(question, top_k=3)
        
        for i, fact in enumerate(results, 1):
            print(f"{i}. {fact['fact']}")
            print(f"   Similarity: {fact['similarity']:.4f}")
    
    # Test with full ChristopherGPT system
    print("\n3. Testing with full ChristopherGPT system...")
    bot = ChristopherGPT()
    
    response = bot.get_response("What is Christopher's favorite food?", use_openai=False)
    print(f"\n🤖 ChristopherGPT Response:")
    print(response['answer'])
    
    print(f"\n📊 Context facts used:")
    for i, fact in enumerate(response['relevant_facts'], 1):
        print(f"  {i}. {fact['fact']} (similarity: {fact['similarity']:.4f})")

if __name__ == "__main__":
    fix_and_test_embeddings()
