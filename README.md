
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


The countries within the **CINDS group—Costa Rica, Iceland, Norway, Denmark, and Sweden**—are leveraging **Artificial Intelligence (AI)** to advance their energy sectors and environmental sustainability. Below is an overview of each nation's initiatives:

**Costa Rica**

**Costa Rica** is utilizing AI to monitor deforestation and analyze ecological data, aiding in the ![protection](https://ticotimes.net/2023/11/08/ai-and-eco-acoustics-safeguard-macaws-in-costa-rica) of its rich ![biodiversity](https://www.mcgill.ca/desautels/channels/news/artificial-intelligence-helping-costa-rica-ngos-preserve-biodiversity-351756). The integration of AI in these areas presents an innovative narrative that highlights the intersection of technology and environmental stewardship.

**Iceland**

Leveraging its geothermal resources, **Iceland** has invested in **AI** to optimize energy production and consumption. The country is also exploring **AI** applications in managing ![fisheries](https://vericatch.com/the-rise-of-ai-in-fisheries-technology/), ensuring sustainable practices that protect marine ecosystems. This narrative illustrates the role of **AI** in supporting sustainable practices in unique environmental contexts. 

**Norway**

**Norway** is a global leader in electric vehicle ![(EV)](https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/what-norways-experience-reveals-about-the-ev-charging-market) adoption and has implemented AI-driven solutions for managing its energy grid. The country utilizes predictive analytics to forecast energy demand and optimize the dispatch of renewable resources. This synergy between **AI** and energy management provides a compelling narrative about how technology can facilitate the transition to a low-carbon economy. 

***Denmark**

**Denmark** is recognized for its ambitious climate goals and has integrated **AI** into its wind energy sector to enhance predictive maintenance and operational efficiency. The country's focus on smart grids and energy storage solutions showcases the transformative potential of ![**AI**](https://www.energycluster.dk/en/new-drone-technology-uses-artificial-intelligence-to-examine-offshore-wind-turbine-blades/) in maximizing renewable energy output and achieving carbon neutrality. 

**Sweden**

Known for its advanced energy policies, **Sweden** has made significant strides in reducing carbon emissions through the use of ![**AI**](https://www.ai.se/en/sector-initiatives/energy). The country is leveraging machine learning algorithms to optimize energy consumption, improve renewable energy integration, and enhance public transportation systems. This positions Sweden as a leader in utilizing **AI** for climate action, making it a pertinent case study in the **AI** domain.
  
Each of these nations represents a significant case study in sustainable energy, ranging from extensive renewable energy use to pioneering **carbon-neutrality initiatives*.

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
```
```
cd Omdena_Hackathon_Real-Time-Emissions
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your [Electricity Maps API key](https://api-portal.electricitymaps.com/) in the `.streamlit/secrets.toml` file:
```plaintext
[api_keys]
ELECTRICITY_MAPS_API_KEY = "your_api_key_here"
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

![Carbon intensity CINDS](https://github.com/aaronmalunga/Omdena_Hackathon_Real-Time-Emissions/blob/main/carbon%20intensity%20CINDS.PNG)

## **Future Improvements**

* **Expanded Country Data:** Adding more countries from different regions.
* **Historical Data Analysis:** Incorporating historical emission data to track trends.
* **Comparative Analytics:** Enabling comparison between current and past data.
  
## **License**

This project is licensed under the MIT License.

