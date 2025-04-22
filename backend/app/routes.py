from flask import Blueprint, request, jsonify
from .email_generator import EmailGenerator
from .music_service import MusicService
from flask_cors import CORS

api = Blueprint('api', __name__)
CORS(api)

email_generator = EmailGenerator()
music_service = MusicService()

@api.route('/templates/generate', methods=['POST'])
def generate_template():
    try:
        data = request.get_json()
        template_type = data.get('template_type')
        inputs = data.get('inputs')

        if not template_type or not inputs:
            return jsonify({
                'status': 'error',
                'message': 'Missing required fields'
            }), 400

        generated_text = email_generator.generate_email(template_type, inputs)

        return jsonify({
            'status': 'success',
            'generated_text': generated_text
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@api.route('/api/search', methods=['POST'])
async def search():
    data = request.get_json()
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
    
    try:
        results = await music_service.process_prompt(prompt)
        return jsonify({'results': results})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/api/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    email = data.get('email')
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    try:
        music_service.subscribe_to_beta(email)
        return jsonify({'message': 'Successfully subscribed to beta'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}) 