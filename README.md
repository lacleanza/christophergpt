# ChristopherGPT

An AI chatbot trained on personal data about Christopher, built with Python, Flask, and OpenAI integration.

## Features

- 🤖 **AI-Powered Responses**: Uses OpenAI GPT for natural conversations
- 🔍 **Semantic Search**: Finds relevant facts using sentence embeddings
- 🌐 **Web Interface**: Clean, modern chat interface
- 📚 **Personal Knowledge Base**: Custom facts and information about Christopher
- ⚡ **Fast Response**: Pre-computed embeddings for quick fact retrieval

## Quick Start

### 1. Install Dependencies

```bash
# Create virtual environment (recommended)
python -m venv christophergpt_env
source christophergpt_env/bin/activate  # On Windows: christophergpt_env\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 2. Configure Environment

Copy `.env` file and add your OpenAI API key:

```bash
# Edit .env file
OPENAI_API_KEY=your_actual_api_key_here
```

### 3. Run the Application

```bash
# Start the web server
python app.py
```

Visit `http://localhost:5000` to chat with ChristopherGPT!

## Project Structure

```
christophergpt/
├── app.py                          # Flask web server
├── christophergpt.py               # Main chatbot class
├── embeddings.py                   # Embedding system for semantic search
├── personal_data.py                # Facts and data about Christopher
├── templates/
│   └── index.html                  # Web chat interface
├── requirements.txt                # Python dependencies
├── .env                           # Environment configuration
└── README.md                      # This file
```

## How It Works

1. **Knowledge Base**: Personal facts stored in `personal_data.py`
2. **Embeddings**: Uses sentence-transformers to create semantic vectors
3. **Semantic Search**: Finds relevant facts using cosine similarity
4. **Response Generation**: Uses OpenAI GPT or basic templates
5. **Web Interface**: Flask serves a modern chat UI

## Testing

Run individual test files:

```bash
# Test embedding system
python embeddings.py

# Test basic functionality
python test_questions.py

# Test with OpenAI integration
python test_with_openai.py

# Interactive chat in terminal
python christophergpt.py
```

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (optional)
- `FLASK_DEBUG`: Enable Flask debug mode (True/False)
- `PORT`: Port for web server (default: 5000)

### Customization

- **Add Facts**: Edit `personal_data.py` to add more information
- **Adjust Response Style**: Modify personality traits in `personal_data.py`
- **Change UI**: Edit `templates/index.html` for different styling

## Requirements

- Python 3.8+
- OpenAI API key (optional, for enhanced responses)
- 2GB+ RAM (for embedding models)

## License

This project is for personal/educational use.

## Support

For issues or questions about this project, please check the code documentation or create an issue in the repository.
