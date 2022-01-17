import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)
st.dataframe(df)
st.write(df.describe(()))
#print(pd.__version__) #verifier version package  (de meme plotly.express , stremlit,seaborn

#hist_fig = px.histogram(df, x=hist_x, nbins=hist_bins)
hist_x = st.selectbox("Histogram variable", options=df.columns, index=df.columns.get_loc('cylinders'))
st.write('You selected:', hist_x)
hist_bins = st.slider(label="Histogram bins", min_value=5, max_value=50, value=25, step=1)

hist_fig = px.histogram(df, x=hist_x, nbins=hist_bins, title="Histogram of " + hist_x,
                        template="plotly_white")
st.write(hist_fig)
###Deuxième figure :Boxplot avec filtre variable X

###
box_cat = st.selectbox("Categorical variable", ["continent"], 0)
box_x = st.selectbox("Boxplot variable", options=df.columns, index=df.columns.get_loc("cylinders"))
box_fig = px.box(df, y=box_x, title="Box plot of " + box_x, template="plotly_white")
st.write(box_fig)
### Troisième figure boxplot avec filtre région/variableX
box_fig1 = px.box(df, x=box_cat, y=box_x, title="Box plot of " + box_x, template="plotly_white", category_orders={"continent": ["US", "Europe","Japon"]})
st.write(box_fig1)
###

corr_x = st.selectbox("Correlation - X variable", options=df.columns, index=df.columns.get_loc("cylinders"))
corr_y = st.selectbox("Correlation - Y variable", options=df.columns, index=df.columns.get_loc("cylinders"))
corr_col = st.radio("Correlation - color variable", options=["continent", "year"], index=1)

fig4 = px.scatter(df, x=corr_x, y=corr_y, template="plotly_white", color=corr_col, color_continuous_scale=px.colors.sequential.OrRd)
st.write(fig4)
###Pour écrire en couleur
#st.markdown(f'<h1 style="color:#33ff33;font-size:24px;">{"ColorMeBlue text”"}</h1>', unsafe_allow_html=True)

Region= st.selectbox("Region", options=df.continent.unique())