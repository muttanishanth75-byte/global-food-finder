import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Global Food Finder", page_icon="🌎")

# Custom CSS for a professional "Startup" look
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .restaurant-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #FF4B4B;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .stButton>button { border-radius: 10px; height: 3em; background-color: #FF4B4B; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- THE DATABASE ---
data = {
    "London": [
        {"name": "Saravana Bhavan", "type": "South India", "dish": "Ghee Roast Dosa", "area": "Leicester Square", "tip": "Just like Chennai!"},
        {"name": "Dishoom", "type": "North India", "dish": "Chicken Ruby", "area": "Covent Garden", "tip": "Expect a wait, but it's worth it."}
    ],
    "Paris": [
        {"name": "Chennai Dosa", "type": "South India", "dish": "Masala Dosa", "area": "Gare du Nord", "tip": "Authentic hub for Tamil food."}
    ],
    "Dubai": [
        {"name": "Sangeetha", "type": "South India", "dish": "Mini Tiffin", "area": "Karama", "tip": "Great for families."},
        {"name": "Gazebo", "type": "North India", "dish": "Lucknowi Biryani", "area": "City Centre", "tip": "Very royal vibes."}
    ]
}

# --- UI ---
st.title("🌍 Global Food Finder")
st.write("Find authentic home-style food in top tourist cities.")

home_region = st.sidebar.selectbox("Where are you from?", ["South India", "North India"])
current_city = st.text_input("Enter city (e.g., London, Paris, Dubai):")

if st.button("Search Restaurants 🔍"):
    city_key = current_city.title()
    if city_key in data:
        results = [r for r in data[city_key] if r['type'] == home_region]
        if results:
            for place in results:
                st.markdown(f"""
                <div class="restaurant-card">
                    <h3>🏠 {place['name']}</h3>
                    <p><b>🍲 Dish:</b> {place['dish']} | <b>📍 Area:</b> {place['area']}</p>
                    <p><i>"{place['tip']}"</i></p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning(f"We don't have {home_region} spots in {city_key} yet!")
    else:
        st.error("City not found in our current database.")
        st.info("We are adding 50+ new countries soon!")

# --- THE "INFINITE" FEATURE ---
st.markdown("---")
st.subheader("📩 Help us expand!")
with st.expander("Can't find a city? Suggest a restaurant here"):
    with st.form("suggestion_form"):
        new_city = st.text_input("City Name")
        new_res = st.text_input("Restaurant Name")
        submitted = st.form_submit_with_button("Submit Suggestion")
        if submitted:
            st.success("Thanks! Our scouts will verify this restaurant soon.")