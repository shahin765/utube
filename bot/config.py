import os


class Config:

    BOT_TOKEN = os.environ.get("7729856277:AAHc42dKhXukrfB927dKK_iDxiGZMFFZ0lk")

    SESSION_NAME = os.environ.get("@jerryislivebot", ":memory:")

    API_ID = int(os.environ.get("17075537"))

    API_HASH = os.environ.get("c4d7dfa13dc7768416b0548cc6e4186d")

    CLIENT_ID = os.environ.get("392450193762-h4f7173lfgeibuh4n78bs7eec1rk26lh.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = int(os.environ.get("@jerryislivebot"))

    AUTH_USERS_TEXT = os.environ.get("5680942491", "")

    AUTH_USERS = [BOT_OWNER, 5680942491] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
