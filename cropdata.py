import streamlit as st
import random
from datetime import datetime, timedelta

# Title
st.markdown("<h2 style='text-align: center;'>Crop price prediction</h2>", unsafe_allow_html=True)

# Input form
with st.container():
    col1, col2, col3 = st.columns([1.5, 1, 1])
    with col1:
        crop = st.selectbox("Crop", ["Select Crop", "Rice", "Wheat", "Maize", "Cotton"])
    with col2:
        month = st.selectbox("Month", list(range(1, 13)))
    with col3:
        year = st.selectbox("Year", list(range(2020, datetime.now().year + 2)))

predict = st.button("PREDICT")

# On prediction
if predict and crop != "Select Crop":
    today = datetime(year, month, 1)
    
    # Generate fake predictions for next 7 days
    future_prices = []
    for i in range(1, 8):
        future_date = today + timedelta(days=i)
        fake_price = round(random.uniform(1500, 3000), 2)
        future_prices.append((future_date.strftime("%d-%b-%Y"), i, fake_price))

    # CSS Styling
    st.markdown("""
        <style>
            .custom-table {
                background-color: #c0392b;
                color: white;
                border-radius: 15px;
                padding: 10px 0;
                text-align: center;
                font-family: 'Segoe UI', sans-serif;
                font-size: 18px;
                font-weight: 600;
            }
            .row {
                display: flex;
                justify-content: space-around;
                padding: 10px 0;
            }
            .row-data {
                background-color: #fdfdfd;
                color: black;
                border-radius: 10px;
                padding: 10px;
                margin-top: 10px;
                font-size: 16px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Header row
    st.markdown("""
        <div class='custom-table row'>
            <div style='flex:1;'>Date</div>
            <div style='flex:1;'>Days Ahead</div>
            <div style='flex:1;'>Market Price (₹)</div>
        </div>
    """, unsafe_allow_html=True)

    # Data rows
    for date, day_ahead, price in future_prices:
        st.markdown(f"""
            <div class='row row-data'>
                <div style='flex:1;'>{date}</div>
                <div style='flex:1;'>{day_ahead}</div>
                <div style='flex:1;'>₹ {price}</div>
            </div>
        """, unsafe_allow_html=True)
