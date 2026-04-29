import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Global Food Finder", page_icon="🌎")

# Custom CSS for the "Pro" Look
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
    .stButton>button { border-radius: 10px; height: 3em; background-color: #FF4B4B; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- THE GLOBAL DATABASE ---
data = {
    "London": [
        {"name": "Saravana Bhavan", "type": "South India", "dish": "Ghee Roast Dosa", "area": "Leicester Square", "tip": "Just like Chennai!"},
        {"name": "Dishoom", "type": "North India", "dish": "Chicken Ruby", "area": "Covent Garden", "tip": "Long queues, but worth the wait."}
    ],
    "Paris": [
        {"name": "Chennai Dosa", "type": "South India", "dish": "Masala Dosa", "area": "Gare du Nord", "tip": "The hub for Tamil flavors in France."}
    ],
    "Dubai": [
        {"name": "Sangeetha Vegetarian", "type": "South India", "dish": "Mini Tiffin", "area": "Karama", "tip": "Best breakfast spot for families."},
        {"name": "Gazebo", "type": "North India", "dish": "Lucknowi Biryani", "area": "Multiple Locations", "tip": "Very royal and authentic."}
    ],
    "Singapore": [
        {"name": "Komala Vilas", "type": "South India", "dish": "Bhattura", "area": "Little India", "tip": "Legendary spot since 1947."}
    ]
}

# --- SIDEBAR & IDENTITY ---
st.sidebar.title("🍱 Preferences")
home_region = st.sidebar.selectbox("Where are you from?", ["South India", "North India"])

# THE BIG FLEX
st.sidebar.markdown("---")
st.sidebar.write("🚀 Developed by:")
st.sidebar.subheader("Mutta Nishanth") 

# --- MAIN UI ---
st.title("🌍 Global Food Finder")
st.write("Find a taste of home in top tourist cities across the world.")

current_city = st.text_input("Which city are you in?", placeholder="e.g. London, Dubai, Paris...")

if st.button("Find My Food 🔍"):
    # .title() ensures "london" and "London" both work!
    city_key = current_city.title()
    
    if city_key in data:
        results = [res for res in data[city_key] if res["type"] == home_region]
        if results:
            st.success(f"Found {len(results)} {home_region} spots in {city_key}!")
            for place in results:
                st.markdown(f"""
                <div class="restaurant-card">
                    <h3>🏠 {place['name']}</h3>
                    <p><b>🍲 Signature Dish:</b> {place['dish']}</p>
                    <p><b>📍 Neighborhood:</b> {place['area']}</p>
                    <p><b>💡 Pro Tip:</b> {place['tip']}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning(f"We know {city_key}, but we haven't found a {home_region} spot there yet!")
    else:
        st.error(f"Sorry! Our scouts haven't reached {city_key} yet.")

# --- THE INFINITE GROWTH FORM ---
st.markdown("---")
st.subheader("📩 Help us go Infinite!")
with st.expander("Is your favorite restaurant missing? Add it here:"):
    with st.form("add_form"):
        user_city = st.text_input("City Name")
        user_res = st.text_input("Restaurant Name")
        user_type = st.selectbox("Type", ["South India", "North India"])
        submitted = st.form_submit_with_button("Submit to Mutta Nishanth")
        if submitted:
            st.success("Thanks! I'll verify and add this to the global database.")