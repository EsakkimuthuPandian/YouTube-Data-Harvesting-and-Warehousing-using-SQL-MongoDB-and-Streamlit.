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
Channel_id = input("Enter your channel id") 

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
                    "Channel_Description": values["snippet"]["description"].replace("\n","").strip(),
                    "Playlist_Id":values["contentDetails"]["relatedPlaylists"]["uploads"]}
                }
details = get_channel_details(response)

                                                        # Getting  Details    

def get_video_id (playlist_id, page_token=None):
    video_ids = []

    while True:
        request_videos_id = youtube.playlistItems().list(
            part= "contentDetails",
            maxResults= 50,
            playlistId= playlist_id,
            pageToken= page_token
        )
        response_videos_id = request_videos_id.execute()
    
        for item in response_videos_id["items"]:
            video_ids.append(item["contentDetails"]["videoId"])
                 
        page_token = response_videos_id.get("nextPageToken")
    
        if not page_token:
            break

    return video_ids

all_video_ids = get_video_id(playlist_id = details["channel_details"]["Playlist_Id"])

                                                        # Getting  Details    

def get_video_details (channel_detail,all_ids,):

    count = 1
    
    for video_id in all_ids :
        request_video_details = youtube.videos().list(
            part= "snippet,contentDetails, statistics",
            id= video_id
    )
        response_video_details = request_video_details.execute()
    
        for values in response_video_details["items"]:
            
            video_key = "Video_Id_" + str(count)

            channel_detail[video_key] = {
                            "Video_Id": video_id , 
                            "Video_Name": values["snippet"]["title"].split('#')[0].strip(),
                            "Video_Description": values["snippet"]["description"].replace('\n',' '),
                            "PublishedAt": values["snippet"]["publishedAt"],
                            "View_Count": int(values["statistics"]["viewCount"]),
                            "Like_Count": int(values["statistics"]["likeCount"]),
                            "Favorite_Count":int(values["statistics"]["favoriteCount"]),
                            "Comment_Count": int(values["statistics"]["commentCount"]),
                            "Duration": f"{int((re.search(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', values['contentDetails']['duration']).group(1) if re.search(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', values['contentDetails']['duration']) else 0) or 0):02d}:{int((re.search(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', values['contentDetails']['duration']).group(2) if re.search(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', values['contentDetails']['duration']) else 0) or 0):02d}:{int((re.search(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', values['contentDetails']['duration']).group(3) if re.search(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', values['contentDetails']['duration']) else 0) or 0):02d}",
                            "Thumbnail": values["snippet"]["thumbnails"]["default"]["url"],
                            "Caption_Status":"Not Available" if values["contentDetails"]["caption"] == "false" else "Available",
                            "Comments":{}
                            
            }

            comment_count = 1
            
            try:
                
                request_comments_details = youtube.commentThreads().list(
                    part="snippet,id",
                    maxResults = 100,
                    videoId= video_id
                    )
                response_comments_details = request_comments_details.execute()

                if response_comments_details["items"]:

                    for values in response_comments_details["items"]:
        
                        comment_key = "Comment_Id_" + str(comment_count)
                
                        channel_detail[video_key]["Comments"][comment_key] = {
                                            "Comment_Id": values["id"] , 
                                            "Comment_Text": values["snippet"]["topLevelComment"]["snippet"]["textOriginal"],
                                            "Comment_Author": values["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
                                            "Comment_PublishedAt": values["snippet"]["topLevelComment"]["snippet"]["publishedAt"]
                            }
                        
                        comment_count = comment_count + 1


                else:
                    channel_detail[video_key]["Comments"] = "Comments is None'O'"

            except:
                channel_detail[video_key]["Comments"] = "Comments Disabled"

                
            count = count + 1
                
               

    return channel_detail

get_video_details(details,all_video_ids)

