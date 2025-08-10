"""
Web interface for ChristopherGPT
Flask web application for localhost server
"""

from flask import Flask, render_template, request, jsonify
from christophergpt import ChristopherGPT
import os

app = Flask(__name__)

# Initialize ChristopherGPT
print("Starting ChristopherGPT web server...")
bot = ChristopherGPT()

@app.route('/')
def index():
    """Main chat interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint for chat messages"""
    try:
        data = request.get_json()
        question = data.get('message', '').strip()
        
        if not question:
            return jsonify({'error': 'No message provided'}), 400
        
        # Get response from ChristopherGPT
        response = bot.get_response(question)
        
        return jsonify({
            'answer': response['answer'],
            'method': response['method'],
            'relevant_facts': [fact['fact'] for fact in response['relevant_facts']],
            'success': True
        })
        
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500

@app.route('/api/status')
def status():
    """API endpoint to check system status"""
    return jsonify({
        'status': 'running',
        'openai_available': bot.openai_available,
        'embeddings_loaded': bot.embedder.embeddings is not None,
        'total_facts': len(bot.embedder.facts) if bot.embedder.facts else 0
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"🌐 Starting web server on http://localhost:{port}")
    print("💡 Visit the URL above to chat with ChristopherGPT!")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
