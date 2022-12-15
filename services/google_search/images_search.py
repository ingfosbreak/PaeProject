from google_images_search import GoogleImagesSearch
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
import os

if os.path.exists(".env"):
  load_dotenv()  # take environment variables from .env.
else:
  print(".env file missing")

DEVELOPER_KEY = os.environ.get("GCS_DEVELOPER_KEY")
CX = os.environ.get("GCS_CX")

def fetch_images(searchfor, dominantColor):
  print(f'images_search: fetch_images("{searchfor}", "{dominantColor}")')

  with GoogleImagesSearch(DEVELOPER_KEY, CX) as gis:
    _search_params = {
      "q": searchfor, 
      "num": 5, 
      "safe": "high", 
      "fileType": "jpg|png",
      "imgType": "photo",
      "rights": "cc_publicdomain",
      "imgDominantColor": dominantColor 
      }
    try:
      gis.search(search_params=_search_params)
      images = gis.results()
      return [image.url for image in images]
    except HttpError as err:
      return err.resp.status

# print(fetch_images('urban houes', 'white'))