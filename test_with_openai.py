"""
Test ChristopherGPT with OpenAI integration
"""

from christophergpt import ChristopherGPT

def test_openai_responses():
    """Test ChristopherGPT with OpenAI-generated responses"""
    bot = ChristopherGPT()
    
    if not bot.openai_available:
        print("❌ OpenAI API not configured. Please check your .env file.")
        return
    
    test_questions = [
        "Hi! What's your name and what do you study?",
        "What kind of music do you listen to?",
        "Tell me about your business experience",
        "What are you working on right now?",
        "What are your career goals?",
        "Are you dating anyone?"
    ]
    
    print("\n" + "="*60)
    print("🤖 TESTING CHRISTOPHERGPT WITH OPENAI")
    print("="*60)
    
    for question in test_questions:
        print(f"\n❓ You: {question}")
        print("-" * 50)
        
        # Test with OpenAI
        response = bot.get_response(question, use_openai=True)
        print(f"🤖 ChristopherGPT: {response['answer']}")
        
        # Show the context facts used
        print(f"\n📊 Context facts used:")
        for i, fact in enumerate(response['relevant_facts'], 1):
            print(f"  {i}. {fact['fact']} (similarity: {fact['similarity']:.3f})")
        
        print()

if __name__ == "__main__":
    test_openai_responses()
