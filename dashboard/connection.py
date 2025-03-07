import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os 

load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
DATABASE = os.getenv("DB")

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}")

query = """
SELECT 
    technology, 
    YEAR(application_date) AS year, 
    seniority, 
    country,
    COUNT(*) AS hires
FROM candidates
WHERE code_challenge_score >= 7 AND technical_interview_score >= 7
GROUP BY technology, year, seniority, country
ORDER BY year
"""

@st.cache_data
def get_data():
    with engine.connect() as conn:
        return pd.read_sql(query, conn)

df = get_data()

st.title("Dashboard de Contrataciones")


st.subheader("Contrataciones por Tecnología")
df_tech = df.groupby("technology", as_index=False)["hires"].sum()
fig_tech = px.pie(df_tech, names='technology', values='hires', 
                  labels={"technology": "Tecnología", "hires": "Contrataciones"})
st.plotly_chart(fig_tech)


st.subheader("Contrataciones por Año")
df_year = df.groupby("year", as_index=False)["hires"].sum()
fig_year = px.bar(df_year, x='year', y='hires', color="year", 
                  labels={"year": "Año", "hires": "Contrataciones"})
st.plotly_chart(fig_year)


st.subheader("Contrataciones por Antigüedad")
df_seniority = df.groupby("seniority", as_index=False)["hires"].sum()
fig_seniority = px.bar(df_seniority, x='seniority', y='hires', color="seniority",
                       labels={"seniority": "Antigüedad", "hires": "Contrataciones"})
st.plotly_chart(fig_seniority)

st.subheader("Contrataciones por País a lo largo del Tiempo")
df_country = df[df["country"].isin(["USA", "Brazil", "Colombia", "Ecuador"])]
df_country = df_country.groupby(["year", "country"], as_index=False)["hires"].sum()
fig_country = px.line(df_country, x="year", y="hires", color="country", 
                      labels={"year": "Año", "hires": "Contrataciones", "country": "País"})
st.plotly_chart(fig_country)
