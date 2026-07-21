                                                          # Needed Modules


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

