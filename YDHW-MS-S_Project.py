                                                          # Needed Modules

import googleapiclient.discovery
from pprint import pprint
import pandas as pd
import pymongo as pm
import streamlit as st
import pyodbc

                                                         # API service Connection
    
api_key = 'AIzaSyC8C6Sx1i25VJzDzDe-XdxRrA76kUpOpwQ'
api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = api_key)

                                                        # Getting Channel Details    
request = youtube.channels().list(
    part="snippet,contentDetails,statistics",
    id= Channel_id
)

response = request.execute()

def get_channel_details (channel_response):
    for values in channel_response["items"]:
        return {
                 "channel_details": {
                    "Channel_Name": values["snippet"]["title"],
                    "Channel_Id": values["id"],
                    "Subscription_Count":int(values["statistics"]["subscriberCount"]),
                    "Channel_Views": int(values["statistics"]["viewCount"]),
                    "Channel_Description": str.replace(values["snippet"]["description"], "\n"," ",),
                    "Playlist_Id":values["contentDetails"]["relatedPlaylists"]["uploads"]}
                }
