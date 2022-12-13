from google_images_search import GoogleImagesSearch
from dotenv import load_dotenv, dotenv_values

load_dotenv()  # take environment variables from .env.

config = dict(dotenv_values(".env"))

# print(config)
