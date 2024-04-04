import streamlit as st
import streamlit_option_menu
from phonepemain import *
import plotly.graph_objects as go
import plotly.express as px

st.title(":red[PHONEPE DATA VISUALIZATION AND EXPLORATION]")
with st.sidebar:
    option=st.selectbox("select any one",
        ("Aggregated Analysis", 'Map Analysis', 'Top Analysis','Query Part'))
    
if option=="Aggregated Analysis":
    option=st.selectbox("Select any one",
        ("Aggregated Transaction Analysis", 'Aggregated User Analysis', 'Aggregated Insurance Analysis'))
    if option=="Aggregated Transaction Analysis":
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        
        view1,view2=agg_trans_graphing(agg_trans_df,yr)
        st.plotly_chart(view1,theme="streamlit", use_container_width=True)
        st.plotly_chart(view2,theme="streamlit", use_container_width=True)
        
    elif option=="Aggregated User Analysis":
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        
        view3=agg_user_graphing(agg_user_df,yr)
        st.plotly_chart(view3,theme="streamlit",use_container_width=True)
        
    elif option=="Aggregated Insurance Analysis":
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        
        view4,view5=agg_ins_graphing(agg_ins_df,yr)
        st.plotly_chart(view4,theme="streamlit",use_container_width=True)
        st.plotly_chart(view5,theme="streamlit",use_container_width=True)
        
        

elif option=="Map Analysis":
    option=st.selectbox("Select any one",
        ("Map Transaction Analysis", 'Map User Analysis', 'Map Insurance Analysis'))
    if option=="Map Transaction Analysis":
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        view6,view7=map_trans_graphing(map_trans_df,yr)
        st.plotly_chart(view6,theme="streamlit",use_container_width=True)
        st.plotly_chart(view7,theme="streamlit",use_container_width=True)
        
    elif option=="Map User Analysis":
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        view8,view9=map_user_graphing(map_user_df,yr)
        st.plotly_chart(view8,theme="streamlit",use_container_width=True)
        st.plotly_chart(view9,theme="streamlit",use_container_width=True)
    elif option=="Map Insurance Analysis":
        yr=st.selectbox('select year',
                        (2020,2021,2022,2023))
        
        view10,view11=map_ins_graphing(map_ins_df,yr)
        st.plotly_chart(view10,theme="streamlit",use_container_width=True)
        st.plotly_chart(view11,theme="streamlit",use_container_width=True)
        
elif option=="Top Analysis":
    option=st.selectbox("Select any one",
        ("Top Transaction Analysis", 'Top User Analysis', 'Top Insurance Analysis'))
    if option=="Top Transaction Analysis":
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        view12,view13=top_trans_graphing(top_trans_df,yr)
        st.plotly_chart(view12,theme="streamlit",use_container_width=True)
        st.plotly_chart(view13,theme="streamlit",use_container_width=True)
        
    if option=="Top User Analysis":
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        view14,view15=top_trans_graphing(top_trans_df,yr)
        st.plotly_chart(view14,theme="streamlit",use_container_width=True)
        st.plotly_chart(view15,theme="streamlit",use_container_width=True)
    if option=="Top Insurance Analysis":
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        view16,view17=top_ins_graphing(top_trans_df,yr)
        st.plotly_chart(view16,theme="streamlit",use_container_width=True)
        st.plotly_chart(view17,theme="streamlit",use_container_width=True)
elif option=='Query Part':
    ques=st.selectbox('Select a Question for Visualization',
                        ('Top 10 States in Highest Transaction Amount',
                        '10 states have Least Transaction Count',
                        'Top 10 Mobile Brands used in PhonePe',
                        'Top 10 Districts have maximum Transaction Amount',
                        'Least Transaction done by 10 Districts',
                        'Top 10 Districts in Transaction in Tamil Nadu',
                        'Least 10 districts in Transaction in Tamil Nadu',
                        'Top 10 states in App Open',
                        'Least 10 States with App Open',
                        'Top 10 states for Registered Users'))
    
    if ques=='Top 10 States in Highest Transaction Amount':
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        myview1=question1(yr)
        st.plotly_chart(myview1,theme="streamlit",use_container_width=True)
        
    elif ques=='10 states have Least Transaction Count':
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        myview2=question2(yr)
        st.plotly_chart(myview2,theme="streamlit",use_container_width=True)
        
    elif ques=='Top 10 Mobile Brands used in PhonePe':
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        myview3=question3(yr)
        st.plotly_chart(myview3,theme="streamlit",use_container_width=True)
    elif ques=='Top 10 Districts have maximum Transaction Amount':
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        myview4=question4(yr)
        st.plotly_chart(myview4,theme="streamlit",use_container_width=True)
    elif ques=='Least Transaction done by 10 Districts':
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        myview5=question5(yr)
        st.plotly_chart(myview5,theme="streamlit",use_container_width=True)
        
    elif ques=='Top 10 Districts in Transaction in Tamil Nadu':
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        myview6=question6(yr)
        st.plotly_chart(myview6,theme="streamlit",use_container_width=True)
    elif ques=='Least 10 districts in Transaction in Tamil Nadu':
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        myview7=question7(yr)
        st.plotly_chart(myview7,theme="streamlit",use_container_width=True)
    elif ques=='Top 10 states in App Open':
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        myview8=question8(yr)
        st.plotly_chart(myview8,theme="streamlit",use_container_width=True)
    elif ques=='Least 10 States with App Open':
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        myview9=question9(yr)
        st.plotly_chart(myview9,theme="streamlit",use_container_width=True)
    elif ques=='Top 10 states for Registered Users':
        yr=st.selectbox('select year',
                        (2018,2019,2020,2021,2022,2023))
        myview10=question10(yr)
        st.plotly_chart(myview10,theme="streamlit",use_container_width=True)
            
    
    
    
    