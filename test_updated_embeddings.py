"""
Test the updated embeddings with specific questions
"""

from embeddings import ChristopherEmbeddings

def test_updated_facts():
    embedder = ChristopherEmbeddings()
    embedder.load_embeddings()
    
    # Test with some specific questions to verify latest facts
    test_questions = [
        'Where is Christopher from?',
        'What does Christopher study?', 
        'What languages does Christopher speak?',
        'What kind of music does Christopher like?',
        'Tell me about Christopher\'s travel experiences',
        'What cologne does Christopher wear?',
        'What are Christopher\'s favorite restaurants?',
        'What books has Christopher read?'
    ]
    
    print("🧪 TESTING UPDATED EMBEDDINGS")
    print("=" * 60)
    
    for question in test_questions:
        print(f'\n❓ Question: {question}')
        print('-' * 50)
        facts = embedder.find_relevant_facts(question, top_k=3)
        for i, fact in enumerate(facts, 1):
            print(f'{i}. {fact["fact"]} (similarity: {fact["similarity"]:.3f})')

if __name__ == "__main__":
    test_updated_facts()
