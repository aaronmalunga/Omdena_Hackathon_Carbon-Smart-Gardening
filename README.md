
# **CINDS Carbon Intensity Visualization Platform**

## __Overview__

The **CINDS** Carbon Intensity Visualization Platform is a web-based application developed to provide real-time carbon intensity data from select countries with a strong commitment to low-carbon practices: **Costa Rica**, **Iceland**, **Norway**, **Denmark**, **and Sweden**. The platform maps the carbon emissions across these countries, allowing users to visually assess energy impact in specific regions and leverage data for sustainability discussions.

## **Features**

* **Live Carbon Intensity Data:** Integrated with the Electricity Maps API, providing up-to-date **gCO₂/kWh** values for each selected country.
* **Color-Coded Intensity Indicators:** The application uses dynamic color codes on location markers to indicate varying levels of carbon intensity, ranging from green (low) to red (high).
* **Country-Specific Information:** Detailed information on each country’s carbon profile, flag, and real-time intensity is displayed alongside the map for enhanced user insight.
* **Interactive World Map:** A folium-powered map providing visual insights into emission data, with landmasses of selected countries colorized according to their carbon intensity levels.

## **Countries in CINDS**

These countries are highlighted due to their exemplary progress toward low-carbon energy and sustainability:

* **Costa Rica (CR)**
* **Iceland (IS)**
* **Norway (NO)**
* **Denmark (DK)**
* **Sweden (SE)**
  
Each of these nations represents a significant case study in sustainable energy, ranging from extensive renewable energy use to pioneering carbon-neutrality initiatives.

## **Technology Stack**

* **Streamlit:** For interactive web interface.
* **Folium:** For map rendering and visualization.
* **Electricity Maps API:** For real-time carbon intensity data.
* **Python:** Primary language for backend processing.
* **Environment Management:** .env file for securely managing API keys.

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/aaronmalunga/Omdena_Hackathon_Real-Time-Emissions.git
cd Omdena_Hackathon_Real-Time-Emissions
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your Electricity Maps API key in the `.env` file:
```plaintext
ELECTRICITY_MAPS_API_KEY=your_api_key_here
```

4. Run the application:
```bash
streamlit run app.py
```

## **Usage**

Once the application is running, users can:

1. View real-time carbon intensity data by country on the map.
2. Access country-specific information on carbon intensity and sustainability initiatives, shown on the side panel.

   
![Carbon intensity Map](https://github.com/aaronmalunga/Omdena_Hackathon_Real-Time-Emissions/blob/main/Carbon%20intensity%20map.PNG)

## **Sample Output**

`Include the screenshot of the map here for visual reference.`

## **Future Improvements**

* **Expanded Country Data:** Adding more countries from different regions.
* **Historical Data Analysis:** Incorporating historical emission data to track trends.
* **Comparative Analytics:** Enabling comparison between current and past data.
  
## **License**

This project is licensed under the MIT License.

