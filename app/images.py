from dotenv import load_dotenv
from imagekitio import ImageKit
import os

#Look for the env variable and use it.
load_dotenv()

#use image kit in the backend to upload the image

imagekit = ImageKit(
    private_key = os.getenv("IMAGEKIT_PRIVATE_KEY"),
    public_key=os.getenv("IMAGEKIT_PUBLIC_KEY"),   
    url_endpoint = os.getenv("IMAGEKIT_URL")

)