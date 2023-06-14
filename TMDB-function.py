import base64
from io import BytesIO
import requests
from pymongo import MongoClient
from gridfs import GridFS, GridFSBucket
from config_file import Config

CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'
KEY = Config.TMDB_API_KEY

# connect to the mongoDB
client = MongoClient("mongodb://localhost:27017")
db = client['mov_img']
fs = GridFS(db)
bucket = GridFSBucket(db)
