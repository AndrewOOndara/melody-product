import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask config
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    
    # API Keys
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    DISCOGS_TOKEN = os.getenv('DISCOGS_TOKEN')
    MAILCHIMP_API_KEY = os.getenv('MAILCHIMP_API_KEY')
    MAILCHIMP_LIST_ID = os.getenv('MAILCHIMP_LIST_ID')
    
    # Model Config
    CLAUDE_MODEL = "claude-3-opus-20240229"
    
    # API Endpoints
    SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI', 'http://localhost:5000/callback')
    SPOTIFY_SCOPE = 'user-read-private user-read-email playlist-read-private'
    
    # Database
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///app.db') 