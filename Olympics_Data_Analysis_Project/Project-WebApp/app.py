import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import preprocessor,helper

df = pd.read_csv("C:/Machine Learning/Machine_Learning/Olympics_Data_Analysis_Project/Dataset/athlete_events.csv")               #Relative Path of dataset
df_region = pd.read_csv("C:/Machine Learning/Machine_Learning/Olympics_Data_Analysis_Project/Dataset/noc_regions.csv")           #Relative Path of dataset


df = preprocessor.preprocess(df,df_region)

st.sidebar.title("1896-2016 Olympics Analysis")
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete-wise Analysis')
)

#st.dataframe(df)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country",country)

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    if (selected_year == "Overall" and selected_country == "Overall"):
        st.title("Overall Medal Tally")
    elif(selected_year != "Overall" and selected_country == "Overall"):
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    elif(selected_year == "Overall" and selected_country != "Overall"):
        st.title(selected_country + "Overall Performance")
    elif(selected_year != "Overall" and selected_country != "Overall"):
        st.title(selected_country + "Medal Tally in " + str(selected_year) + " Olympics")

    st.dataframe(medal_tally)



