import streamlit as st
import requests
from datetime import datetime

def generate_links(course, sessions, start_year, current_year, subject_code):
    if subject_code:
        st.text("Click to open.")
        for session in sessions:
            for year in range(start_year, current_year):
                url = format_url(course=course, session=session, year=year, subject_code=subject_code)
                req = requests.get(url)
                if req.status_code == 200:
                    st.link_button(label=f"{subject_code}_{session}{year}", url=url)

        st.text("Links generated successfully.")
    else:
        st.error("Something went wrong.")


def format_url(course, session, year, subject_code):
    return f"https://gtu.ac.in/uploads/{session}{year}/{course}/{subject_code}.pdf"


st.title("JustClic!")

courses = ['AF', 'BA', 'BB', 'BC', 'BD', 'BE', 'BESP', 'BH', 'BI', 'BL', 'BM', 'BN', 'BP', 'BPSP', 'BS', 'BT', 'BV', 'CI', 'CS', 'DA', 'DB', 'DH', 'DI', 'DISP', 'DM', 'DP', 'DS', 'DV', 'EP', 'FD', 'HM', 'IB', 'IC', 'IM', 'MA', 'MB', 'MC', 'MCSP', 'MD', 'ME', 'MH', 'ML', 'MN', 'MP', 'MR', 'MS', 'MT', 'MV', 'PB', 'PD', 'PH', 'PM', 'PP', 'PR', 'TE', 'VP']
sessions = ('W', 'S')
start_year = 2018
current_year = datetime.now().year

course_option = st.selectbox("Enter your course", options=courses)
subject_code = st.text_input("Enter subject code")

if st.button("Generate"):
    generate_links(course=course_option, sessions=sessions, start_year=start_year, current_year=current_year, subject_code=subject_code)
