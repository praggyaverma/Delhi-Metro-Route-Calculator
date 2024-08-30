import streamlit as st
from graph_utils import Graph

g = Graph()
g.initialize_graph()

stations = sorted(g.graph.keys())

st.set_page_config(
    page_title="Metro Route Calculator",
    page_icon="🚝",
)

st.write("# Welcome to Delhi Metro Route Calculator! 🚝")
st.write("Select your source and destination")

source = st.selectbox('Select Source', options=stations)
st.write(f"Source: {source}")

destination = st.selectbox('Select Destination', options=stations)
st.write(f"Destination: {destination}")

if (st.button("Calculate Route")):
    if source == destination:
        st.write(f"Start and end stations are the same: {source}")

    distances, shortest_path_tree = g.dijkstra(source)

    if destination in distances:
        path = g.print_shortest_path_tree(shortest_path_tree, source, destination)
        st.write(f"Shortest path from {source} to {destination}:")
        for path_station in path:
            st.write(path_station)
            st.write("↓")

        st.write(f"Total travel time: {distances[destination]} minutes")
    else:
        st.write(f"No path from {source} to {destination}")