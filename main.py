import streamlit as st
import requests
import os
from datetime import datetime

def process_path(download_path):
    # change '\' to '/'
    download_path = download_path.replace("\\", '/')

    if download_path[-1] == '/':
        download_path = download_path[:-1]

    return download_path


def format_url(session, year, subject_code):
    return f"https://gtu.ac.in/uploads/{session}{year}/BE/{subject_code}.pdf"


st.title("JustClic!")

# Ask the user to enter a download directory path
download_path = st.text_input("Enter the path where you want to save the downloaded files:")
subject_code = st.text_input("Enter subject code")

sessions = ('W', 'S')
start_year = 2018
current_year = datetime.now().year

# Check if the directory exists then download, otherwise display a message
if st.button("Download"):
    if download_path and subject_code:
        download_path = process_path(download_path=download_path)

        if os.path.isdir(download_path):
            for session in sessions:
                for year in range(start_year, current_year):
                    url = format_url(session=session, year=year, subject_code=subject_code)
                    
                    # download paper
                    req = requests.get(url)
                    if req.status_code == 200:
                        with open(f"{download_path}/{subject_code}_{session}{year}.pdf", 'wb') as file:
                            file.write(req.content)

            st.text("Papers downloaded successfully.")
        else:
            st.error("Something went wrong.")