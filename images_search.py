from google_images_search import GoogleImagesSearch
from dotenv import load_dotenv, dotenv_values
import os

if os.path.exists(".env"):
  load_dotenv()  # take environment variables from .env.
else:
  print(".env file missing")

DEVELOPER_KEY = os.environ.get("GCS_DEVELOPER_KEY")
CX = os.environ.get("GCS_CX")

# print(DEVELOPER_KEY, CX)

# gis = GoogleImagesSearch(DEVELOPER_KEY, CX)


def fetch_images(searchfor, dominantColor):
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
    gis.search(search_params=_search_params)
    return gis.results()


print([image.url for image in fetch_images('urban houes', 'white')])

# image0 = fetch_images("monkey")[0]
# print(image0.url)
# print(image0.referrer_url)