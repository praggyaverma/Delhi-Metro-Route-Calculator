import streamlit as st
import pandas as pd
import numpy as np
from graph_utils import Graph
st.set_page_config(
    page_title="Metro Route Calculator",
    page_icon="🚝",
)

g = Graph()
g.initialize_graph()

stations = sorted(g.graph.keys())

# st.write("# Delhi Metro Route Calculator! 🚝")
st.write('<h1 style="color:#a82f2f;">Delhi Metro Route Calculator 🚝</h1>', unsafe_allow_html=True)

st.write("Select source and destination")

source = st.selectbox('Select Source', options=stations)
st.write(f"Source --> {source}")

destination = st.selectbox('Select Destination', options=stations)
st.write(f"Destination --> {destination}")

if (st.button("Calculate Route")):

    distances, shortest_path_tree = g.dijkstra(source)

    if destination in distances:
        path = g.print_shortest_path_tree(shortest_path_tree, source, destination)
        st.subheader(f"Shortest path from {source} to {destination}:")
        path = pd.DataFrame(path, columns=["Stations"])
        st.table(data=path)

        st.write(f"Total travel time: {distances[destination]} minutes")
    else:
        st.write(f"No path from {source} to {destination}")