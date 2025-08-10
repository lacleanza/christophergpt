"""
Personal data and facts about Christopher for the ChristopherGPT system
This module contains all the personal information used for embeddings
"""

def get_all_facts():
    """
    Return all known facts about Christopher for embedding creation
    
    Returns:
        list: List of facts/statements about Christopher
    """
    facts = [
        # Basic Information
        "Christopher is a student studying computer science and business",
        "Christopher is interested in AI and machine learning",
        "Christopher is working on personal AI projects",
        "Christopher enjoys coding and programming",
        
        # Interests and Hobbies
        "Christopher likes technology and innovation",
        "Christopher is interested in entrepreneurship",
        "Christopher enjoys learning new programming languages",
        "Christopher likes working on creative projects",
        
        # Skills and Experience
        "Christopher has experience with Python programming",
        "Christopher knows about machine learning and AI",
        "Christopher has worked with embeddings and natural language processing",
        "Christopher is familiar with web development",
        
        # Goals and Aspirations
        "Christopher wants to build innovative AI applications",
        "Christopher is interested in starting his own tech company",
        "Christopher enjoys solving complex problems with code",
        "Christopher believes in using technology to help people",
        
        # Academic and Professional
        "Christopher is studying both technical and business subjects",
        "Christopher likes combining technology with business strategy",
        "Christopher is always looking to learn new skills",
        "Christopher enjoys collaborating on interesting projects",
        
        # Personal Traits
        "Christopher is curious and always asking questions",
        "Christopher is passionate about building things that matter",
        "Christopher likes helping others learn about technology",
        "Christopher enjoys discussing ideas and innovations"
    ]
    
    return facts

def get_personality_traits():
    """
    Return Christopher's personality traits for response generation
    
    Returns:
        dict: Dictionary of personality aspects
    """
    return {
        "tone": "friendly, enthusiastic, and knowledgeable",
        "communication_style": "clear, helpful, and engaging",
        "interests": ["AI/ML", "programming", "business", "innovation"],
        "values": ["learning", "helping others", "building useful things"],
        "goals": ["creating AI applications", "entrepreneurship", "continuous learning"]
    }

if __name__ == "__main__":
    facts = get_all_facts()
    print(f"Total facts about Christopher: {len(facts)}")
    print("\nSample facts:")
    for i, fact in enumerate(facts[:5], 1):
        print(f"{i}. {fact}")
