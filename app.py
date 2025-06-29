import streamlit as st
import pickle
import pandas as pd

# Load models
kmeans = pickle.load(open('../models/kmeans_model.pkl', 'rb'))
scaler = pickle.load(open('../models/scaler.pkl', 'rb'))
similarity_df = pd.read_pickle('../models/product_similarity.pkl')

st.sidebar.title("Home")
page = st.sidebar.radio("Choose Module", ["Clustering", "Recommendation"])

if page == "Recommendation":
    st.title("Product Recommender")
    product = st.text_input("Enter Product Name")
    if st.button("Recommend"):
        try:
            recommendations = similarity_df[product].sort_values(ascending=False)[1:6].index.tolist()
            st.subheader("Recommended Products:")
            for item in recommendations:
                st.write(item)
        except KeyError:
            st.error("Product not found. Try a different name.")

elif page == "Clustering":
    st.title("Customer Segmentation")
    r = st.number_input("Recency (days since last purchase)", value=100)
    f = st.number_input("Frequency (number of purchases)", value=10)
    m = st.number_input("Monetary (total spend)", value=500.0)
    
    if st.button("Predict Segment"):
        features = scaler.transform([[r, f, m]])
        cluster = kmeans.predict(features)[0]
        segment = ['High-Value', 'Regular', 'Occasional', 'At-Risk'][cluster]
        st.success(f"This customer belongs to: **{segment}**")

# PATH:  cd "/Users/eraiyanbu/Desktop/Projects/Shopper spectrum/app"

