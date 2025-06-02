import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '')
    API_ID = int(os.environ.get("API_ID", ''))
    API_HASH = os.environ.get("API_HASH", '')
    AUTH_USER = os.environ.get('AUTH_USERS', '6890400066,5744263553').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "꧁•⊹٭@𝚂𝚘𝚗𝚞porsa٭⊹•꧂™"#Here You Can Change with Your Name  or any custom name or title you prefer
    

port = int(os.environ.get("PORT", 1000))

