from anthropic import Anthropic
from config import Config

class EmailGenerator:
    def __init__(self):
        self.client = Anthropic(api_key=Config.ANTHROPIC_API_KEY)

    def generate_email(self, template_type, inputs):
        prompt = self._construct_prompt(template_type, inputs)
        
        response = self.client.messages.create(
            model=Config.CLAUDE_MODEL,
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        return response.content[0].text

    def _construct_prompt(self, template_type, inputs):
        if template_type == "business_email":
            return f"""You are an expert business communication assistant. 
Generate a professional email based on the following details:

Recipient Name: {inputs.get('recipient_name')}
Subject: {inputs.get('subject')}
Details: {inputs.get('details')}

Please write a clear, professional, and engaging email. Use a friendly yet formal tone.
The email should be well-structured with:
1. Professional greeting
2. Clear purpose in the opening paragraph
3. Detailed body with relevant information
4. Professional closing
5. Signature line""" 