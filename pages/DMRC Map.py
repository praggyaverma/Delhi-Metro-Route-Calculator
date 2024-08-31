# st.image("dmrc.jpg",caption="Delhi Metro Route Map",use_column_width=True)
import streamlit as st
import pydeck as pdk

st.markdown("## DRMC Map 🗺️")

locations = {'Adarsh Nagar': {'line': 'yellow line', 'lat': 28.7144008, 'lon': 77.1672884}, 
             'AIIMS': {'line': 'yellow line', 'lat': 28.5668602, 'lon': 77.2078058}, 
             'Arjan Garh': {'line': 'yellow line', 'lat': 28.4807352, 'lon': 77.1257622}, 
             'Ashram': {'line': 'pink line', 'lat': 28.5724231, 'lon': 77.2585979}, 
             'Azadpur': {'line': 'yellow line', 'lat': 28.7076568, 'lon': 77.1755473}, 
             'Bhikaji Cama Place': {'line': 'pink line', 'lat': 28.56790025, 'lon': 77.18701648353385}, 
             'Central Secretariat': {'line': 'yellow line', 'lat': 28.6158794, 'lon': 77.2122822}, 
             'Chandni Chowk': {'line': 'yellow line', 'lat': 28.6605039, 'lon': 77.2297797}, 
             'Chawri Bazar': {'line': 'yellow line', 'lat': 28.6501605, 'lon': 77.2295008}, 
             'Chhatarpur': {'line': 'yellow line', 'lat': 28.5067242, 'lon': 77.1750019}, 
             'Civil Lines': {'line': 'yellow line', 'lat': 28.6768508, 'lon': 77.2250299}, 
             'Delhi Cantonment': {'line': 'pink line', 'lat': 28.60871, 'lon': 77.140423}, 
             'Durgabai Deshmukh South Campus': {'line': 'pink line', 'lat': 28.5894384, 'lon': 77.1690817}, 
             'East Azad Nagar': {'line': 'pink line', 'lat': 28.6646964, 'lon': 77.284881},  
             'Ghitorni': {'line': 'yellow line', 'lat': 28.493751, 'lon': 77.1491866}, 
             'Gokulpuri': {'line': 'pink line', 'lat': 28.7024752, 'lon': 77.2861253}, 
             'Green Park': {'line': 'yellow line', 'lat': 28.5585815, 'lon': 77.2067183}, 
             'GTB Nagar': {'line': 'yellow line', 'lat': 28.6981317, 'lon': 77.2064113}, 
             'Guru Dronacharya': {'line': 'yellow line', 'lat': 28.4820212, 'lon': 77.1022685}, 
             'Hauz Khas': {'line': 'yellow line', 'lat': 28.5442564, 'lon': 77.2067072}, 
             'Hazrat Nizamuddin': {'line': 'pink line', 'lat': 28.5887494, 'lon': 77.2572494}, 
             'HUDA City Centre': {'line': 'yellow line', 'lat': 28.4593429, 'lon': 77.0726571}, 
             'IFFCO Chowk': {'line': 'yellow line', 'lat': 28.4723277, 'lon': 77.0724222}, 
             'IP Extension': {'line': 'pink line', 'lat': 28.6288991, 'lon': 77.31019787919774}, 
             'Jaffrabad': {'line': 'pink line', 'lat': 28.6826822, 'lon': 77.2748055}, 
             'Jahangirpuri': {'line': 'yellow line', 'lat': 28.7259717, 'lon': 77.162658}, 
             'Jor Bagh': {'line': 'yellow line', 'lat': 28.586111, 'lon': 77.212222}, 
             'Krishna Nagar': {'line': 'pink line', 'lat': 28.6578461, 'lon': 77.2901853}, 
             'Lok Kalyan Marg': {'line': 'yellow line', 'lat': 28.597658, 'lon': 77.211177}, 
             'Majlis Park': {'line': 'pink line', 'lat': 28.7244312, 'lon': 77.181964}, 
             'Malviya Nagar': {'line': 'yellow line', 'lat': 28.5339201, 'lon': 77.2124474}, 
             'Mayapuri': {'line': 'pink line', 'lat': 28.6371795, 'lon': 77.1297333}, 
             'MG Road': {'line': 'yellow line', 'lat': 28.4794579, 'lon': 77.0804652}, 
             'Model Town': {'line': 'yellow line', 'lat': 28.7027136, 'lon': 77.1939912}, 
             'Naraina Vihar': {'line': 'pink line', 'lat': 28.6273375, 'lon': 77.1403175}, 
             'New Delhi': {'line': 'yellow line', 'lat': 28.6436415, 'lon': 77.2217373}, 
             'Patel Chowk': {'line': 'yellow line', 'lat': 28.6229664, 'lon': 77.214031}, 
             'Punjabi Bagh West': {'line': 'pink line', 'lat': 28.6703201, 'lon': 77.1420875}, 
             'Qutab Minar': {'line': 'yellow line', 'lat': 28.512951, 'lon': 77.186319}, 
             'Rajiv Chowk': {'line': 'yellow line', 'lat': 28.6327804, 'lon': 77.2196996}, 
             'Rohini Sector 18': {'line': 'yellow line', 'lat': 28.7383477, 'lon': 77.1398323}, 
             'Saket': {'line': 'yellow line', 'lat': 28.520492, 'lon': 77.201535}, 
             'Samaypur Badli': {'line': 'yellow line', 'lat': 28.7446158, 'lon': 77.1382654}, 
             'Sarojini Nagar': {'line': 'pink line', 'lat': 28.5741575, 'lon': 77.1953703}, 
             'Shakurpur': {'line': 'pink line', 'lat': 28.6857668, 'lon': 77.1496094}, 
             'Shalimar Bagh': {'line': 'pink line', 'lat': 28.701819, 'lon': 77.165191}, 
             'Shiv Vihar': {'line': 'pink line', 'lat': 28.721612, 'lon': 77.289494}, 
             'Sir Vishweshwaraiah Moti Bagh': {'line': 'pink line', 'lat': 28.5785326, 'lon': 77.175741}, 
             'Sultanpur': {'line': 'yellow line', 'lat': 28.49919, 'lon': 77.161389}, 
             'Trilokpuri Sanjay Lake': {'line': 'pink line', 'lat': 28.613453, 'lon': 77.3088549}, 
             'Udyog Bhawan': {'line': 'yellow line', 'lat': 28.6105302, 'lon': 77.2131076}, 
             'Vidhan Sabha': {'line': 'yellow line', 'lat': 28.6863222, 'lon': 77.2217271}, 
             'Vinobapuri': {'line': 'pink line', 'lat': 28.5669763, 'lon': 77.2491906}, 
             'Vishwa Vidyalaya': {'line': 'yellow line', 'lat': 28.6950369, 'lon': 77.2147192}, 
             'Anand Vihar': {'line': 'pink line', 'lat': 28.646886, 'lon': 77.315878}, 
             'Dilli Haat - INA': {'line': 'yellow line', 'lat': 28.575, 'lon': 77.207222}, 
             'ESI - Basaidarapur': {'line': 'pink line', 'lat': 28.658271, 'lon': 77.127391}, 
             'East Vinod Nagar - Mayur Vihar-II': {'line': 'pink line', 'lat': 28.620039, 'lon': 77.305266}, 
             'Haiderpur Badli Mor': {'line': 'yellow line', 'lat': 28.729923, 'lon': 77.14913}, 
             'Johri Enclave': {'line': 'pink line', 'lat': 28.713167, 'lon': 77.290107}, 
             'Karkarduma': {'line': 'pink line', 'lat': 28.648539, 'lon': 77.30556}, 
             'Kashmere Gate': {'line': 'yellow line', 'lat': 28.6675, 'lon': 77.228}, 
             'Lajpat Nagar': {'line': 'pink line', 'lat': 28.570566, 'lon': 77.23646}, 
             'Mandawali - West Vinod Nagar': {'line': 'pink line', 'lat': 28.624977, 'lon': 77.304583}, 
             'Maujpur - Babarpur': {'line': 'pink line', 'lat': 28.692073, 'lon': 77.279585}, 
             'Mayur Vihar-I': {'line': 'pink line', 'lat': 28.604134, 'lon': 77.289526}, 
             'Netaji Subhash Place': {'line': 'pink line', 'lat': 28.695889, 'lon': 77.1525}, 
             'Rajouri Garden': {'line': 'pink line', 'lat': 28.649, 'lon': 77.122611}, 
             'Rohini Sector 18-19': {'line': 'yellow line', 'lat': 28.738318, 'lon': 77.139875}, 
             'Sarai Kale Khan - Nizamuddin': {'line': 'pink line', 'lat': 28.589356, 'lon': 77.257128}, 
             'Sikanderpur': {'line': 'yellow line', 'lat': 28.481389, 'lon': 77.093056}, 
             'Sir M. Vishweshwaraiah Moti Bagh': {'line': 'pink line', 'lat': 28.578504, 'lon': 77.175726}, 
             'South Extension': {'line': 'pink line', 'lat': 28.568611, 'lon': 77.220265}, 
             'Welcome': {'line': 'pink line', 'lat': 28.672111, 'lon': 77.277889}}

line_colors = {
    'pink line': [255, 105, 180, 160],  
    'yellow line': [255, 255, 0, 160]  
}

data = [
    {
        'name': name,
        'line': coord['line'],
        'lat': coord['lat'],
        'lon': coord['lon'],
        'color': line_colors.get(coord['line'], [0, 0, 0, 160]) 
    }
    for name, coord in locations.items()
]

view_state = pdk.ViewState(
    latitude=28.6139,
    longitude=77.2090,
    zoom=10,
    pitch=0
)

deck = pdk.Deck(
    initial_view_state=view_state,
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=data,
            get_position=['lon', 'lat'],
            get_fill_color='color',  
            get_radius=190, 
            pickable=True,
            auto_highlight=True
        )
    ],
    tooltip={"text": "{name}"}
)

st.pydeck_chart(deck)