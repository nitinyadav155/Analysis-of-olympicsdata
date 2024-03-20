import streamlit as st
import pandas as pd
import preprocessor
import helper
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

st.sidebar.image("data:image/jpeg;base64,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")
st.sidebar.title(':blue[Olympics Analysis]')
df = preprocessor.preprocess(df,region_df)

user_menu = st.sidebar.radio(
    label=':rainbow[Select an Option]',
   options =('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete-wise Analysis','medal data')
)
st.markdown(
    """<style>
    div[class*="st.radio"]>label>div[data-testid="stMarkdownContainer"]>p{
    fon-size: 32px;
    }
    </style>
      """,unsafe_allow_html=True)
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color:   #D8F2FF;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    "## This is the sidebar"
if user_menu == 'Medal Tally':
    st.sidebar.header(":red[Medal  Tally]")
    years,country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select year",years)
    selected_country = st.sidebar.selectbox("Select country", country)
    medal_tally = helper.medal_fetch_tally(df,selected_year,selected_country)
    if selected_year=='Overall' and selected_country=='Overall':
        st.title(':rainbow[Overall Tally]')
    if selected_year=='Overall' and selected_country!='Overall':
        st.title("Medal Tally of " + selected_country + " in all years")
    if selected_year!='Overall' and selected_country=='Overall':
        st.title("Medal Tally in " + str(selected_year) + " Olympics " + " of all countries")
    if selected_year!='Overall' and selected_country!='Overall':
        st.title("Medal Tally of " + selected_country + " in " + str(selected_year) + " Olympics")

    st.table(medal_tally)
if user_menu=='Overall Analysis':
    editions=df['Year'].unique().shape[0]-1
    cities=df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]
    st.title(":violet[Top statistics]")
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

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    nations_over_time=helper.data_over_time(df,'region')
    fig = px.line(nations_over_time, x="Year", y="count",title='Participation of Countries Over the Years ').update_layout(xaxis_title="Edition",yaxis_title="No of Countries",yaxis_range=[10,250],xaxis_range=[1894,2020],title_font_color="#6F2DA8",title_font_size=25)
    fig.update_xaxes(title_font_color="black",title_font_size=20)
    fig.update_yaxes(title_font_color="black", title_font_size=20)
    st.plotly_chart(fig)

    events_over_time=helper.data_over_time(df,'Event')
    fig = px.line(events_over_time, x="Year", y="count",title='No of events  Over the Years ').update_layout(xaxis_title="Edition",yaxis_title="No of Events",xaxis_range=[1894,2020],title_font_color="#6F2DA8",title_font_size=25)
    fig.update_xaxes(title_font_color="black",title_font_size=20)
    fig.update_yaxes(title_font_color="black", title_font_size=20)
    st.plotly_chart(fig)

    athletes_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athletes_over_time, x="Year", y="count", title='Participation of Athletes Over the Years ').update_layout(xaxis_title="Edition", yaxis_title="No of Athletes", xaxis_range=[1894, 2020], title_font_color="#6F2DA8",title_font_size=25)
    fig.update_xaxes(title_font_color="black", title_font_size=20)
    fig.update_yaxes(title_font_color="black", title_font_size=20)
    st.plotly_chart(fig)


    st.title("No. of Sport events over time")
    fig,ax=plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
    annot=True, cmap='Greens', square=True, linecolor='black')
    st.pyplot(fig)

    st.title("Most Successful Athletes")
    sport_list=df["Sport"].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')
    selected_sport=st.selectbox("Select a Sport",sport_list)
    x=helper.most_successful(df,selected_sport)
    st.table(x)

if user_menu=='Country-wise Analysis':
    st.sidebar.title('Country-wise Analysis')
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()
    selected_country = st.sidebar.selectbox("Select the  Country",country_list)
    country_df = helper.yearwise_medal_tally(df,selected_country)
    fig = px.line(country_df, x="Year", y="Medal")
    st.title(selected_country + " Medal Tally over the years")
    st.plotly_chart(fig)

    st.title(selected_country + " excels in following sports")
    new_df = helper.country_event_heatmap(df,selected_country)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax= sns.heatmap(new_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0).astype('int'),
    annot=True, cmap='BuPu', square=True, linecolor='black')
    st.pyplot(fig)

    st.title("Top 10 Athletes of "+ selected_country + " in particular sport")
    merged_df = helper.most_successful_athlete(df,selected_country)
    st.table(merged_df)


if user_menu =='Athlete-wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()
    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                             show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=800,height=600)
    st.title("Distribution of Age ")
    st.plotly_chart(fig)

    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Equestrianism', 'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Modern Pentathlon', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Trampolining', 'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']

    x = []
    name = []
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x,name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=800, height=600)
    st.title("Distribution of Age with respect to sports(Gold Medal)")
    st.plotly_chart(fig)

    sport_list = df["Sport"].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    st.title("Height vs Weight")
    selected_sport = st.selectbox("Select a Sport", sport_list)
    temp_df=helper.weight_v_height(df,selected_sport)
    fig,ax=plt.subplots()
    ax =sns.scatterplot(x='Weight', y='Height', data=temp_df,hue=temp_df['Medal'],style=temp_df['Sex'],s=60)
    st.pyplot(fig)




    st.title("Men vs Women participation over the years ")
    final=helper.men_vs_women(df)
    fig = px.line(final, x='Year', y=["Male", "Female"],markers=True)
    st.plotly_chart(fig)
















