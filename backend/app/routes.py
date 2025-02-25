from flask import Blueprint, request, jsonify
from .email_generator import EmailGenerator

api = Blueprint('api', __name__)
email_generator = EmailGenerator()

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