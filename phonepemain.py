import json
import pandas as pd
import requests
import psycopg2
import plotly.express as px
import plotly.graph_objects as go


#getting details from sql:

postgres_conn=psycopg2.connect(host="localhost",
                            user="postgres",
                            password="sql",
                            database="phonepe_db",
                            port="5432"
                        )
cursor=postgres_conn.cursor() 

t1='select * from agg_transaction'
cursor.execute(t1)
tab1=cursor.fetchall()
agg_trans_df=pd.DataFrame(tab1,columns=["states","years","quarter", "transaction_name","transaction_count", "transaction_amount"])
postgres_conn.commit()

t2='select * from agg_user'
cursor.execute(t2)
tab2=cursor.fetchall()
agg_user_df=pd.DataFrame(tab2,columns=["states","years","quarter", "user_brand","user_count","user_percentage"])
postgres_conn.commit()

t3='select * from agg_insurance'
cursor.execute(t3)
tab3=cursor.fetchall()
agg_ins_df=pd.DataFrame(tab3,columns=["states","years","quarter", "insure_type","insure_count", "insure_amount"])
postgres_conn.commit()

t4='select * from map_transaction'
cursor.execute(t4)
tab4=cursor.fetchall()
map_trans_df=pd.DataFrame(tab4,columns=["states","years","quarter", "district_name","transaction_count", "transaction_amount"])
postgres_conn.commit()

t5='select * from map_user'
cursor.execute(t5)
tab5=cursor.fetchall()
map_user_df=pd.DataFrame(tab5,columns=["states","years","quarter", "district_name","registered_users", "app_opens"])
postgres_conn.commit()

t6='select * from map_insurance'
cursor.execute(t6)
tab6=cursor.fetchall()
map_ins_df=pd.DataFrame(tab6,columns=["states","years","quarter", "district_name","transaction_count", "transaction_amount"])
postgres_conn.commit()

t7='select * from top_transaction'
cursor.execute(t7)
tab7=cursor.fetchall()
top_trans_df=pd.DataFrame(tab7,columns=["states","years","quarter", "district_name","transaction_count", "transaction_amount"])
postgres_conn.commit()

t8='select * from top_user'
cursor.execute(t8)
tab8=cursor.fetchall()
top_user_df=pd.DataFrame(tab8,columns=["states","years","quarter", "district_name","registered_users"])
postgres_conn.commit()

t9='select * from top_insurance'
cursor.execute(t9)
tab9=cursor.fetchall()
top_ins_df=pd.DataFrame(tab9,columns=["states","years","quarter", "district_name","transaction_count", "transaction_amount"])
postgres_conn.commit()

#aggregated transaction graphing

def agg_trans_graphing(df,year):
    tt=df[df['years']==year]
    ff1=tt.groupby("states")["transaction_count"].sum()
    new_df1=ff1.reset_index()
    
    url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(url)
    data1=json.loads(response.content)
    state_name=[]
    for i in data1['features']:
        x=i['properties']['ST_NM']
        state_name.append(x)
    state_name.sort()
        
    fig_india_1=px.choropleth (new_df1, geojson=data1,
                                locations='states',
                                featureidkey='properties.ST_NM',
                                color="transaction_count",
                                range_color=(new_df1["transaction_count"].min(),new_df1["transaction_count"].max()),
                                color_continuous_scale="turbid",
                                hover_name="states",fitbounds="locations",
                                title="Transaction count for State")
    
    ff2=tt.groupby('states')['transaction_amount'].sum()
    new_df2=ff2.reset_index()
    fig_india_2=px.choropleth (new_df2, geojson=data1,
                                locations='states',
                                featureidkey='properties.ST_NM',
                                color="transaction_amount",
                                range_color=(new_df2["transaction_amount"].min(),new_df2["transaction_amount"].max()),
                                color_continuous_scale="turbid",
                                hover_name="states",fitbounds="locations",
                                title="Transaction amount for State")
    fig_india_1.update_geos(visible =False)
    fig_india_2.update_geos(visible =False)

    return fig_india_1,fig_india_2

#aggregated user graphing:

def agg_user_graphing(df,year):
    tt=df[df['years']==year]
    ff1=tt.groupby("states")["user_count"].sum()
    new_df3=ff1.reset_index()
    
    url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(url)
    data1=json.loads(response.content)
    state_name=[]
    for i in data1['features']:
        x=i['properties']['ST_NM']
        state_name.append(x)
    state_name.sort()
    
    fig_india_3=px.choropleth (new_df3, geojson=data1,
                                locations='states',
                                featureidkey='properties.ST_NM',
                                color="user_count",
                                range_color=(new_df3["user_count"].min(),new_df3["user_count"].max()),
                                color_continuous_scale="turbid",
                                hover_name="states",fitbounds="locations",
                                title="User Count for State")
    fig_india_3.update_geos(visible =False)
    
    return fig_india_3

#aggregated insurance graphing

def agg_ins_graphing(df,year):
    tt=df[df['years']==year]
    ff1=tt.groupby("states")["insure_count"].sum()
    new_df5=ff1.reset_index()
    
    url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(url)
    data1=json.loads(response.content)
    state_name=[]
    for i in data1['features']:
        x=i['properties']['ST_NM']
        state_name.append(x)
    state_name.sort()
        
    fig_india_5=px.choropleth (new_df5, geojson=data1,
                                locations='states',
                                featureidkey='properties.ST_NM',
                                color="insure_count",
                                range_color=(new_df5["insure_count"].min(),new_df5["insure_count"].max()),
                                color_continuous_scale="turbid",
                                hover_name="states",fitbounds="locations",
                                title="Insurance Count for State")
    
    ff2=tt.groupby('states')['insure_amount'].sum()
    new_df6=ff2.reset_index()
    
    fig_india_6=px.choropleth (new_df6, geojson=data1,
                                locations='states',
                                featureidkey='properties.ST_NM',
                                color="insure_amount",
                                range_color=(new_df6["insure_amount"].min(),new_df6["insure_amount"].max()),
                                color_continuous_scale="turbid",
                                hover_name="states",fitbounds="locations",
                                title="Insurance amount for State") 
    fig_india_5.update_geos(visible =False)
    fig_india_6.update_geos(visible =False)
    # fig_india_5.show()
    # fig_india_6.show()
    
    return fig_india_5, fig_india_6
# agg_ins_graphing(agg_ins_df,2021)

def map_trans_graphing(df,year):
    mm=df[df["years"]==year]
    mm1=mm.groupby("district_name")["transaction_count"].sum()
    mm2=mm1.sort_values(ascending=False)
    new_df6=mm2.reset_index().head(10)
    fig_map1_trans=px.pie(new_df6,values='transaction_count', names='district_name', title='Top 10 Districts have highest transaction Count in Map Analysis',color='district_name')
    
    nn1=mm.groupby("district_name")["transaction_amount"].sum()
    nn2=nn1.sort_values(ascending=False)
    new_df7=nn2.reset_index().head(10)
    fig_map2_trans=px.pie(new_df7,values='transaction_amount', names='district_name', title='Top 10 Districts have highest Transaction amount in Map Analysis',color='district_name')
    
    return fig_map1_trans,fig_map2_trans

def map_user_graphing(df,year):
    mm=df[df["years"]==year]
    mm1=mm.groupby("district_name")["registered_users"].sum()
    mm2=mm1.sort_values(ascending=False)
    new_df8=mm2.reset_index().head(10)
    fig_map1_user=px.pie(new_df8,values='registered_users', names='district_name', title='Top 10 Districts have user Count in Map Analysis',color='district_name')
    
    nn1=mm.groupby("district_name")["registered_users"].sum()
    nn2=nn1.sort_values(ascending=False)
    new_df9=nn2.reset_index().head(10)
    fig_map2_user=px.pie(new_df9,values='registered_users', names='district_name', title='Top 10 Districts have app open count in Map Analysis',color='district_name')
    
    return fig_map2_user,fig_map1_user

def map_ins_graphing(df,year):
    mm=df[df["years"]==year]
    mm1=mm.groupby("district_name")["transaction_count"].sum()
    mm2=mm1.sort_values(ascending=False)
    new_df10=mm2.reset_index().head(10)
    fig_map1_ins=px.pie(new_df10,values='transaction_count', names='district_name', title='Top 10 Districts have highest insurance Count',color='district_name')
    
    nn1=mm.groupby("district_name")["transaction_amount"].sum()
    nn2=nn1.sort_values(ascending=False)
    new_df11=nn2.reset_index().head(10)
    fig_map2_ins=px.pie(new_df11,values='transaction_amount', names='district_name', title='Top 10 Districts have highest insurance amount',color='district_name')
    
    return fig_map1_ins,fig_map2_ins

def top_trans_graphing(df,year):
    mm=df[df["years"]==year]
    mm1=mm.groupby("district_name")['transaction_count'].sum()
    new_df12=mm1.reset_index()
    fig_top_trans1=px.bar(new_df12,y='transaction_count', x='district_name', title='Top 10 Districts have top transaction Count',color='district_name')
    
    nn1=mm.groupby("district_name")["transaction_amount"].sum()
    new_df13=nn1.reset_index()
    fig_top_trans2=px.bar(new_df13,y='transaction_amount', x='district_name', title='Top Districts have top transaction amount',color='district_name')
    
    return fig_top_trans1,fig_top_trans2

def top_user_graphing(df,year):
    mm=df[df["years"]==year]
    mm1=mm.groupby("district_name")["registered_users"].sum()
    new_df14=mm1.reset_index()
    fig_top1_user=px.bar(new_df14,y='registered_users', x='district_name', title='Top 10 Districts have user Count in top Analysis',color='district_name')
    
    nn1=mm.groupby("district_name")["registered_users"].sum()
    new_df15=nn1.reset_index()
    fig_top2_user=px.bar(new_df15,y='registered_users', x='district_name', title='Top 10 Districts have app open count in top Analysis',color='district_name')
    
    return fig_top1_user,fig_top2_user

def top_ins_graphing(df,year):
    mm=df[df["years"]==year]
    mm1=mm.groupby("district_name")['transaction_count'].sum()
    new_df16=mm1.reset_index()
    fig_top_ins1=px.bar(new_df16,y='transaction_count', x='district_name', title='Top 10 Districts have top insurance Count',color='district_name')
    
    nn1=mm.groupby("district_name")["transaction_amount"].sum()
    new_df17=nn1.reset_index()
    fig_top_ins2=px.bar(new_df17,y='transaction_amount', x='district_name', title='Top 10 Districts have top insurance amount',color='district_name')

    return fig_top_ins1,fig_top_ins2

def question1(year):
    mm=agg_trans_df[agg_trans_df['years']==year]
    mm1=mm.groupby('states')['transaction_amount'].sum()
    mm2=mm1.sort_values(ascending=False)
    q1_df=mm2.reset_index().head(10)

    fig_ques1=px.bar(q1_df,x='states',y='transaction_amount',color='states',title='Top 10 States in Highest Transaction Amount')
    return fig_ques1
    
def question2(year):
    mm=agg_trans_df[agg_trans_df['years']==year]
    mm1=mm.groupby('states')['transaction_amount'].sum()
    mm2=mm1.sort_values()
    q1_df=mm2.reset_index().head(10)
    
    fig_ques2=px.bar(q1_df,x='states',y='transaction_amount',color='states',title='Top 10 States in least Transaction Amount')
    return fig_ques2
    
def question3(year):
    mm=agg_user_df[agg_user_df['years']==year]
    mm1=mm.groupby('user_brand')['user_count'].sum()
    mm2=mm1.sort_values(ascending=False)
    q3_df=mm2.reset_index().head(10)

    fig_ques3=px.pie(q3_df,values='user_count',names='user_brand',color='user_count',title='Top 10 Mobile Brands used in PhonePe')
    return fig_ques3

def question4(year):
    mm=map_trans_df[map_trans_df["years"]==year]
    nn1=mm.groupby("district_name")["transaction_amount"].sum()
    nn2=nn1.sort_values(ascending=False)
    q4_df=nn2.reset_index().head(10)
    fig_ques4=px.bar(q4_df,y='transaction_amount', x='district_name', title='Top 10 Districts have top transaction amount',color='district_name')
    return fig_ques4
    
def question5(year):
    mm=map_trans_df[map_trans_df["years"]==year]
    nn1=mm.groupby("district_name")["transaction_amount"].sum()
    nn2=nn1.sort_values()
    q5_df=nn2.reset_index().head(10)
    fig_ques5=px.bar(q5_df,y='transaction_amount', x='district_name', title='Top 10 Districts have least transaction amount',color='district_name')
    return fig_ques5

def question6(year):
    mm=map_trans_df[map_trans_df['years']==year]
    mm1=mm[mm['states']=='Tamil Nadu']
    mm2=mm1.groupby("district_name")['transaction_amount'].sum()
    mm3=mm2.sort_values(ascending=False)
    q6_df=mm3.reset_index().head(10)
    
    fig_ques6 = px.line(q6_df, x="district_name", y="transaction_amount",markers=True, title='Top 10 Districts have top transaction amount in Tamil Nadu')
    return fig_ques6
def question7(year):
    mm=map_trans_df[map_trans_df['years']==year]
    mm1=mm[mm['states']=='Tamil Nadu']
    mm2=mm1.groupby("district_name")['transaction_amount'].sum()
    mm3=mm2.sort_values()
    q7_df=mm3.reset_index().head(10)
    
    fig_ques7 = px.line(q7_df, x="district_name", y="transaction_amount",markers=True, title='least 10 Districts have low transaction amount in Tamil Nadu')
    return fig_ques7
    
def question8(year):
    mm=map_user_df[map_user_df['years']==year]
    mm1=mm.groupby('states')['app_opens'].sum()
    mm2=mm1.sort_values(ascending=False)
    q8_df=mm2.reset_index().head(10)

    fig_ques8 = px.scatter(q8_df, y="app_opens",color="states",hover_name="states", log_x=True,  size="app_opens",size_max=60)
    return fig_ques8
    
def question9(year):
    mm=map_user_df[map_user_df['years']==year]
    mm1=mm.groupby('states')['app_opens'].sum()
    mm2=mm1.sort_values()
    q9_df=mm2.reset_index().head(10)

    fig_ques9 = px.scatter(q9_df, y="app_opens",color="states",hover_name="states", log_x=True,  size="app_opens",size_max=60)
    return fig_ques9
    
def question10(year):
    mm=map_user_df[map_user_df['years']==year]
    mm1=mm.groupby('states')['registered_users'].sum()
    mm2=mm1.sort_values(ascending=False)
    q10_df=mm2.reset_index().head(10)

    fig_ques10 = px.scatter(q10_df, y="registered_users",color="states",hover_name="states", log_x=True,  size="registered_users",size_max=60)
    return fig_ques10
