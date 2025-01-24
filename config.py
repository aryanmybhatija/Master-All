import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '7278285241:AAFN4fugdg2wYR8eDQrUWv8Eg7C5tT0hw8Y')
    API_ID = int(os.environ.get("API_ID", '23147177'))
    API_HASH = os.environ.get("API_HASH", '6c1b34bf3c56b9957aab7da8a0dd3482')
    AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "𝗥𝗼𝘆 𝗝𝗮𝗮𝘁™"#Here You Can Change with Your Name  or any custom name or title you prefer
