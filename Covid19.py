import streamlit as st  
import pandas as pd  
df=pd.read_csv('/home/arif/Desktop/ML_projects/Covid_19_Dashboard/Covid_data.csv')
st.title('Covid-19 Data Dashboard')

st.subheader('Covid-19 Dataset')
st.dataframe(df)

#filtere by country
countries=df['Country'].unique()
select_country=st.selectbox('Select a country to filter by:',countries)
filtered_df=df[df['Country']==select_country]
st.subheader(f'Data for {select_country}')
st.dataframe(filtered_df.head())

#show summary statistics
st.subheader('Summary Statistics')
st.write('Total Confirmed Cases:',filtered_df['Confirmed'].sum())
st.write('Total Deaths:',filtered_df['Deaths'].sum())
st.write('Total Recovered Cases:',filtered_df['Recovered'].sum())

#plotting
st.subheader('Trends Over Time')
if not filtered_df.empty:
    filtered_df['Date']=pd.to_datetime(filtered_df['Date'])
    filtered_df=filtered_df.sort_values(by='Date')
    st.line_chart(filtered_df.set_index('Date')[['Confirmed','Deaths','Recovered']])
else:
    st.write('No Data available')
