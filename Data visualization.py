import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff

# Defining the Dataset
chart_data = pd.DataFrame(np.random.randn(20,3), columns = ['L-1','L-2','L-3'])

# Plotting Line Chart
st.title('1. Line Chart')
st.line_chart(chart_data)

# Plotting Area Chart
st.title('2. Area Chart')
st.area_chart(chart_data)

# Plotting Bar Chart
st.title('3. Bar Chart')
st.bar_chart(chart_data)


st.subheader('Data Visualization with Seaborn and Matplotlib')

st.text('1. Displaying the Dataset')
df = pd.read_csv('\\Users\\Satyam Jha\\Desktop\\DATA SCIENCE\\STREAMLIT\\iris.csv')
st.dataframe(df)

st.text('2. Bar Plot using Matplotlib')
fig = plt.figure(figsize = (15,8))
df['species'].value_counts().plot(kind = 'bar')
st.pyplot(fig)

st.text('3. DistPlot with Seaborn')
fig = plt.figure(figsize = (15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)


st.text('4. Display Multiple Graphs')
col1 , col2 = st.columns(2)
with col1:
    col1.write('KDE = False')
    fig1 = plt.figure()
    sns.distplot(df['sepal_length'], kde = False)
    st.pyplot(fig1)
with col2:
    col2.write('Hist = False')
    fig2 = plt.figure()
    sns.distplot(df['sepal_length'], hist = False)
    st.pyplot(fig2)

st.text('5. Changing the Style of the Graphs')
col1 , col2 = st.columns(2)
with col1:
    fig1 = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['petal_length'], hist = False)
    st.pyplot(fig1)
with col2:
    fig2 = plt.figure()
    sns.set_theme(context = 'poster', style = 'darkgrid')
    sns.distplot(df['petal_length'], hist = False)
    st.pyplot(fig2)

st.text('6. Scatter Plot')
fig,ax = plt.subplots(figsize  = (15,8))
ax.scatter(*np.random.random(size = (2,100)))
st.pyplot(fig)

st.text('7. Count Plot')
fig = plt.figure(figsize = (15,8))
sns.countplot(data = df, x = 'species')
st.pyplot(fig)

st.text('8. Box Plot')
fig = plt.figure(figsize = (15,8))
sns.boxplot(data = df, x = 'species', y = 'petal_length')
st.pyplot(fig)

st.text('9. Violin Plot')
fig = plt.figure(figsize = (15,8))
sns.violinplot(data = df, x = 'species', y = 'petal_length')
st.pyplot(fig)

#Visualization with Plotly

st.title('Visualizations with Plotly')
df = pd.read_csv('\\Users\\Satyam Jha\\Desktop\\DATA SCIENCE\\STREAMLIT\\tips.csv')
st.dataframe(df.head())

st.text('1. Pie Chart')
fig = px.pie(df , values = 'total_bill', names = 'day')
st.plotly_chart(fig)

st.text('2. Pie Chart with Hole')
fig = px.pie(df , values = 'total_bill', names = 'day', opacity = .8, hole = .5,
            color_discrete_sequence = px.colors.sequential.RdBu)
st.plotly_chart(fig)


st.text('3. Multiple Dist_plots')
x1 = np.random.randn(200) + 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) - 2
hist_data = [x1,x2,x3]

group_lbls = ['G1','G2','G3']
fig = ff.create_distplot(hist_data, group_lbls, bin_size = [.1, .1,.1])
st.plotly_chart(fig, use_container_width = True)
