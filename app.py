import streamlit as st
import pandas as pd
from dotenv import dotenv_values
from openai import OpenAI
from hashlib import md5
from pycaret.clustering import setup
# from audiorecorder import audiorecorder
from ydata_profiling import ProfileReport
# from pydub import AudioSegment
# from io import BytesIO
# import json
# import plotly.express as px
import dtale
import streamlit.components.v1 as components
# from qdrant_client import QdrantClient
# from qdrant_client.models import PointStruct, Distance, VectorParams

env = dotenv_values('.env')

df = pd.read_csv('welcome_survey_simple_v2.csv', sep=';')

l, c, r = st.columns([2,6,2])
with c:
    st.title('Alike')
    st.markdown('### Social matching, but smarter.')
    st.markdown("&nbsp;", unsafe_allow_html=True)

main_page, explore = st.tabs(['Alike', 'Explore Your Data'])

with explore:
    d = dtale.show(df)
    st.write("Open D-Tale in a new tab:")
    st.markdown(f'''
    <a href="{d._main_url}" title="If any issues occur, please refresh the page." target="_blank">
        Click here to explore your data
    </a>
    ''', unsafe_allow_html=True)

    st.markdown('#### Ydata report')
    profile = ProfileReport(df, title="YData Profiling Report", explorative=True)
    profile_html = profile.to_html()
    components.html(profile_html, height=1000, scrolling=True)

with main_page:
    st.header('Describe yourself using this form:')
    age = st.selectbox('Age', ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>=65', 'unknown'])

    education_map = {
        'Primary': 'Podstawowe',
        'Secondary': 'Średnie',
        'Higher': 'Wyższe'
    }
    edu_level_sel = st.selectbox('Educatonal level', list(education_map.keys()))
    edu_level = education_map[edu_level_sel]

    animal_map = {
        'I dont like animals': 'Brak ulubionych',
        'Dogs': 'Psy',
        'Cats': 'Koty',
        'Other': 'Inne',
        'Dogs and cats': 'Koty i Psy'
    }

    fav_animals_sel = st.selectbox('Favorite animal', list(animal_map.keys()))
    fav_animals = animal_map[fav_animals_sel]

    place_map = {
        'By the water': 'Nad wodą',
        'In the forest': 'W lesie',
        'In the mountains': 'W górach',
        'Other': 'Inne'
    }

    fav_place_sel = st.selectbox('Favorite place', list(place_map.keys()))
    fav_place = place_map[fav_place_sel]

    gender_map = {
        'Women': 'Kobieta',
        'Men': 'Mężczyzna'
    }

    gender_sel = st.selectbox('Gender', list(gender_map.keys()))
    gender = gender_map[gender_sel]

    person_df = pd.DataFrame([
        {
            'age': age,
            'edu_level': edu_level,
            'fav_animals': fav_animals,
            'fav_place': fav_place,
            'gender': gender
        }
    ])