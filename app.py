import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv", engine="python")

df = df.dropna(subset=['model_year', 'odometer'])
df['model_year'] = df['model_year'].astype(int)

# Header
st.header("Car Sales Dashboard")

# Checkbox to show/hide raw data
if st.checkbox("Show raw data"):
    st.write(df)

# Histogram
st.subheader("Distribution of Car Prices")
fig_hist = px.histogram(df, x="price", nbins=50, title="Price Distribution")
st.plotly_chart(fig_hist)

# Scatter plot
st.subheader("Odometer vs Price by Condition")
fig_scatter = px.scatter(df, x="odometer", y="price", color="condition")
st.plotly_chart(fig_scatter)

vehicle_types = df['type'].dropna().unique()
selected_type = st.selectbox("Choose vehicle type", sorted(vehicle_types))

filtered_df = df[df['type'] == selected_type]

st.subheader(f"Price Distribution for {selected_type.title()}s")
fig_type_price = px.histogram(filtered_df, x="price", nbins=50)
st.plotly_chart(fig_type_price)

min_year = int(df['model_year'].min())
max_year = int(df['model_year'].max())

year_range = st.slider("Select model year range", min_year, max_year, (min_year, max_year))

filtered_df = df[(df['model_year'] >= year_range[0]) & (df['model_year'] <= year_range[1])]

st.subheader(f"Odometer vs Price for {selected_type.title()}s ({year_range[0]}–{year_range[1]})")
fig_filtered = px.scatter(
    filtered_df[filtered_df['type'] == selected_type],
    x="odometer", y="price", color="condition"
)
st.plotly_chart(fig_filtered)