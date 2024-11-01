# Import necessary libraries
import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

# Define the API key from Streamlit secrets
api_key = st.secrets["api_keys"]["ELECTRICITY_MAPS_API_KEY"]

if api_key is None:
    st.error("API key is not set in Streamlit secrets.")
    st.stop()

# Base URL and headers for API requests
base_url = "https://api.electricitymap.org/v3/carbon-intensity/latest"
headers = {"auth-token": api_key}

# List of zones with latitude and longitude coordinates for mapping
zones = {
    "CR": {
        "name": "Costa Rica", 
        "coords": [9.7489, -83.7534], 
        "color": "blue",
        "flag_url": "https://flagcdn.com/w320/cr.png",
        "info": "Costa Rica is renowned for its focus on renewable energy, with nearly 99% of its electricity generated from renewable sources."
    },
    "IS": {
        "name": "Iceland", 
        "coords": [64.9631, -19.0208], 
        "color": "purple",
        "flag_url": "https://flagcdn.com/w320/is.png",
        "info": "Iceland is a global leader in geothermal and hydroelectric energy, powering almost all of its energy needs sustainably."
    },
    "NO": {
        "name": "Norway", 
        "coords": [60.4720, 8.4689], 
        "color": "green",
        "flag_url": "https://flagcdn.com/w320/no.png",
        "info": "Norway's energy grid is over 95% hydroelectric, making it one of the lowest carbon emitters in Europe."
    },
    "DK": {
        "name": "Denmark", 
        "coords": [56.2639, 9.5018], 
        "color": "orange",
        "flag_url": "https://flagcdn.com/w320/dk.png",
        "info": "Denmark is known for its wind energy, with wind turbines generating nearly 47% of its electricity."
    },
    "SE": {
        "name": "Sweden", 
        "coords": [60.1282, 18.6435], 
        "color": "red",
        "flag_url": "https://flagcdn.com/w320/se.png",
        "info": "Sweden has a highly diversified energy portfolio, with a strong focus on hydropower, nuclear energy, and growing renewables."
    }
}

# Dictionary to store the fetched data
global_data = {}

# Fetch data for each zone and store it in global_data
for zone, info in zones.items():
    try:
        response = requests.get(base_url, headers=headers, params={"zone": zone})
        response.raise_for_status()  # Raise an error for bad responses
        global_data[zone] = response.json()
        global_data[zone]["coords"] = info["coords"]
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error for zone {zone}: {http_err}")
    except requests.exceptions.RequestException as req_err:
        st.error(f"Request error for zone {zone}: {req_err}")
    except Exception as e:
        st.error(f"An unexpected error occurred for zone {zone}: {e}")

# Initialize the map centered on the world
world_map = folium.Map(location=[0, 0], zoom_start=2)

# Add markers to the map for each zone
for zone, data in global_data.items():
    if "carbonIntensity" in data:  # Ensure the key exists in the data
        intensity = data["carbonIntensity"]
        coords = data["coords"]
        popup_text = f"{zones[zone]['name']}\nCarbon Intensity: {intensity} gCO2/kWh"
        
        # Assign each country its specified color
        color = zones[zone]["color"]
        
        folium.Marker(
            location=coords,
            popup=popup_text,
            icon=folium.Icon(color=color)
        ).add_to(world_map)

# Display the map in Streamlit
st.title("Carbon Intensity Map of CINDS")
st_folium(world_map, width=700, height=500)

# Display the sidebar with flags and information
st.sidebar.title("Country Information")

for zone, info in zones.items():
    st.sidebar.subheader(info["name"])
    st.sidebar.image(info["flag_url"], width=150)
    st.sidebar.write(info["info"])









