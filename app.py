import streamlit as st
import pandas as pd
from dotenv import dotenv_values
from openai import OpenAI
from hashlib import md5
# from pycaret.clustering import load_model
from audiorecorder import audiorecorder
# from ydata_profiling import ProfileReport
from pydub import AudioSegment
from io import BytesIO
import json
import plotly.express as px
import dtale
# from qdrant_client import QdrantClient
# from qdrant_client.models import PointStruct, Distance, VectorParams

env = dotenv_values('.env')

df = pd.read_csv('welcome_survey_simple_v2.csv', sep=';')

l, c, r = st.columns([2,6,2])
with c:
    st.title('Alike')
    st.markdown('### Social matching, but smarter.')

with st.sidebar:

    st.markdown('### Look into your data:')

    ydata_view, dtale_view = st.tabs(['Ydata raport', 'D-Tale'])

    with ydata_view:
        st.markdown('#### Ydata raport')

    with dtale_view:
        d = dtale.show(df)
        st.write("Open D-Tale in a new tab:")
        st.markdown(f"[Click here to explore your data]({d._main_url})")