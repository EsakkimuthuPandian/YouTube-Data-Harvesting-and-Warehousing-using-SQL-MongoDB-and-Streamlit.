{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "57e0f675-9f8d-492b-960c-fcedb443e47b",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: google-api-python-client in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (2.198.0)\n",
      "Requirement already satisfied: httplib2<1.0.0,>=0.19.0 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from google-api-python-client) (0.32.0)\n",
      "Requirement already satisfied: google-auth!=2.24.0,!=2.25.0,<3.0.0,>=1.32.0 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from google-api-python-client) (2.55.2)\n",
      "Requirement already satisfied: google-auth-httplib2<1.0.0,>=0.2.0 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from google-api-python-client) (0.4.0)\n",
      "Requirement already satisfied: google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0,>=1.31.5 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from google-api-python-client) (2.31.0)\n",
      "Requirement already satisfied: uritemplate<5,>=3.0.1 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from google-api-python-client) (4.2.0)\n",
      "Requirement already satisfied: googleapis-common-protos<2.0.0,>=1.63.2 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0,>=1.31.5->google-api-python-client) (1.75.0)\n",
      "Requirement already satisfied: protobuf<8.0.0,>=5.29.6 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0,>=1.31.5->google-api-python-client) (7.35.1)\n",
      "Requirement already satisfied: proto-plus<2.0.0,>=1.24.0 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0,>=1.31.5->google-api-python-client) (1.28.1)\n",
      "Requirement already satisfied: requests<3.0.0,>=2.33.0 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0,>=1.31.5->google-api-python-client) (2.34.2)\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from google-auth!=2.24.0,!=2.25.0,<3.0.0,>=1.32.0->google-api-python-client) (0.2.8)\n",
      "Requirement already satisfied: cryptography>=38.0.3 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from google-auth!=2.24.0,!=2.25.0,<3.0.0,>=1.32.0->google-api-python-client) (44.0.1)\n",
      "Requirement already satisfied: pyparsing<4,>=3.1 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from httplib2<1.0.0,>=0.19.0->google-api-python-client) (3.2.0)\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from requests<3.0.0,>=2.33.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0,>=1.31.5->google-api-python-client) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from requests<3.0.0,>=2.33.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0,>=1.31.5->google-api-python-client) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.26 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from requests<3.0.0,>=2.33.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0,>=1.31.5->google-api-python-client) (2.3.0)\n",
      "Requirement already satisfied: certifi>=2023.5.7 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from requests<3.0.0,>=2.33.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0,>=1.31.5->google-api-python-client) (2025.4.26)\n",
      "Requirement already satisfied: cffi>=1.12 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from cryptography>=38.0.3->google-auth!=2.24.0,!=2.25.0,<3.0.0,>=1.32.0->google-api-python-client) (1.17.1)\n",
      "Requirement already satisfied: pycparser in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from cffi>=1.12->cryptography>=38.0.3->google-auth!=2.24.0,!=2.25.0,<3.0.0,>=1.32.0->google-api-python-client) (2.21)\n",
      "Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in c:\\users\\sathishemp\\anaconda3\\lib\\site-packages (from pyasn1-modules>=0.2.1->google-auth!=2.24.0,!=2.25.0,<3.0.0,>=1.32.0->google-api-python-client) (0.4.8)\n"
     ]
    }
   ],
   "source": [
    "!pip install google-api-python-client"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e0d23b61-27fc-457b-8a33-7eb15079c520",
   "metadata": {},
   "outputs": [],
   "source": [
    "import googleapiclient.discovery\n",
    "from pprint import pprint"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a3353e17-cf80-4701-88a5-63a28706edaf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your channel id UC6tFdGonAyrHPcKbL4Kft_w\n"
     ]
    }
   ],
   "source": [
    "Channel_id = input(\"Enter your channel id\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "167a6553-6829-4832-a5fe-24ad0084fb95",
   "metadata": {},
   "outputs": [],
   "source": [
    "api_key = \"AIzaSyChE4T4uSHuX_ADI8sR9DXdBEZS0-zxyzU\"\n",
    "api_service_name = \"youtube\"\n",
    "api_version = \"v3\"\n",
    "\n",
    "youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = api_key )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "843f5749-47ec-4a6d-a01c-aa443505c604",
   "metadata": {},
   "outputs": [],
   "source": [
    "request = youtube.channels().list(\n",
    "    part=\"snippet,contentDetails,statistics\",\n",
    "    id= Channel_id\n",
    ")\n",
    "\n",
    "response = request.execute()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "446a7e7b-085b-4aab-a7a9-0b17daa24580",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_channel_details (channel_response):\n",
    "    for values in channel_response[\"items\"]:\n",
    "        return {\n",
    "                 \"channel_details\": {\n",
    "                    \"Channel_Name\": values[\"snippet\"][\"title\"],\n",
    "                    \"Channel_Id\": values[\"id\"],\n",
    "                    \"Subscription_Count\":int(values[\"statistics\"][\"subscriberCount\"]),\n",
    "                    \"Channel_Views\": int(values[\"statistics\"][\"viewCount\"]),\n",
    "                    \"Channel_Description\": str.replace(values[\"snippet\"][\"description\"], \"\\n\",\" \",),\n",
    "                    \"Playlist_Id\":values[\"contentDetails\"][\"relatedPlaylists\"][\"uploads\"]}\n",
    "                }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0d9c3d4f-126f-4867-89de-ecf85510278d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'channel_details': {'Channel_Name': 'Rubi_informations',\n",
       "  'Channel_Id': 'UC6tFdGonAyrHPcKbL4Kft_w',\n",
       "  'Subscription_Count': 1440,\n",
       "  'Channel_Views': 16448,\n",
       "  'Channel_Description': 'Welcome to Rubi_info! Join me on a journey filled with real stories, raw moments, and tech insights. From personal vlogs that capture everyday experiences to the ups and downs that shaped my path—failures, lessons, and success stories—I share it all honestly. Stay tuned for the latest tech updates, productivity tips, and behind-the-scenes glimpses into the world of growth and learning. Let’s learn, grow, and build a meaningful digital journey together!  For queries: rubi_informations@gmail.com',\n",
       "  'Playlist_Id': 'UU6tFdGonAyrHPcKbL4Kft_w'}}"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "channel_details = get_channel_details(response)\n",
    "channel_details"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "913b4961-8634-4d91-8b24-5b64fd1a6832",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_video_id (playlist_id, page_token=None):\n",
    "    video_ids = []\n",
    "\n",
    "    while True:\n",
    "        request_videos_id = youtube.playlistItems().list(\n",
    "            part= \"contentDetails\",\n",
    "            maxResults= 50,\n",
    "            playlistId= playlist_id,\n",
    "            pageToken= page_token\n",
    "        )\n",
    "        response_videos_id = request_videos_id.execute()\n",
    "    \n",
    "        for item in response_videos_id[\"items\"]:\n",
    "            video_ids.append(item[\"contentDetails\"][\"videoId\"])\n",
    "                 \n",
    "        page_token = response_videos_id.get(\"nextPageToken\")\n",
    "    \n",
    "        if not page_token:\n",
    "            break\n",
    "\n",
    "    return video_ids"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "6ee8249b-1f97-4933-b765-c3f053d78e68",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['D8CmPtKj3Oc',\n",
       " '6I64IX7jsfU',\n",
       " 'QcaN0Jn9Gc0',\n",
       " 'zyB_OZZZyXk',\n",
       " 'WPSYYuZW7dw',\n",
       " 'ju7LsglhEpA',\n",
       " 'oT4rxI_xVhw',\n",
       " 'CvLiumk3WSo',\n",
       " 'jMRtRpABauY',\n",
       " 's_qpssCRVCI',\n",
       " 'OmtvAUulqYg',\n",
       " 'VDAdcRewKzg',\n",
       " 'v5-_e2XDJoc',\n",
       " 'F7BPOZ3GqwE',\n",
       " 'q7-w9tnHQdA',\n",
       " '8APEF4kGuIM',\n",
       " 'JuzLahCUnpE',\n",
       " 'AEFihIoWvww',\n",
       " 'Ts3iQ_h7VOA',\n",
       " 'CV50sXMKCG8',\n",
       " 'EiT86_IIuuk',\n",
       " '_sfSgxgH12Q',\n",
       " 'MBbMogFVsi0',\n",
       " 'ZqLDKG469NE',\n",
       " 'lT4JIbxknG0',\n",
       " 'PFeqeOMNhN0']"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "video_ids = get_video_id(playlist_id = channel_details[\"channel_details\"][\"Playlist_Id\"])\n",
    "video_ids"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f8b941dc-0986-44f2-ac38-9ab655185109",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "26"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(video_ids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62df5fdc-9d45-4cc6-a153-872535325d51",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
