import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import preprocessor,helper
import plotly.express as px # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns # type: ignore

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

    st.table(medal_tally)


if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title("Overall Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)

    with col2:
        st.header("Hosts")
        st.title(cities)

    with col3:
        st.header("Sports")
        st.title(sports)

    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)

    with col2:
        st.header("Nations")
        st.title(nations)

    with col3:
        st.header("Athletes")
        st.title(athletes)
 
    nations_over_time = helper.data_nations_over_time(df,'region')
    fig = px.line(nations_over_time, x="Edition", y="region")
    st.title("Graph of Participating Nations over the years")
    st.plotly_chart(fig)

    events_over_time = helper.data_nations_over_time(df,'Event')
    fig = px.line(events_over_time, x="Edition", y="Event")
    st.title("Graph of Events over the years")
    st.plotly_chart(fig)

    athletes_over_time = helper.data_nations_over_time(df,'Name')
    fig = px.line(athletes_over_time, x="Edition", y="Name")
    st.title("Graph of Athletes over the years")
    st.plotly_chart(fig)

    st.title("No. of Events Over Time(Every Sport)")
    fig,ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year','Sport','Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport',columns='Year',values='Event',aggfunc='count').fillna(0).astype('int'),annot=True)
    st.pyplot(fig)

    st.title("Most Successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport = st.selectbox("Select s Sport",sport_list)
    x = helper.most_successful(df,selected_sport)
    st.table(x)

if user_menu == 'Country-wise Analysis':

    st.sidebar.title("Country-wise Analysis")

    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox('Select a Country',country_list)

    country_df = helper.yearwise_medal_tally(df,selected_country)
    fig = px.line(country_df,x='Year',y='Medal')
    st.title(selected_country + " Medal Tally over the Years")
    st.plotly_chart(fig)

    st.title(selected_country + " excels in the following sports")
    pt = helper.country_event_heatmap(df,selected_country)
    fig,ax = plt.subplots(figsize=(20,20))
    ax = sns.heatmap(pt,annot=True)
    st.pyplot(fig)

