import heapq

class Graph:

    def __init__(self):
        self.graph = {}

    def addConnection(self, station1, station2, time):
        if station1 not in self.graph:
            self.graph[station1] = {}
        if station2 not in self.graph:
            self.graph[station2] = {}
        self.graph[station1][station2] = time
        self.graph[station2][station1] = time

    def dijkstra(self, start):

        pq = [(0, start)]

        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0

        shortest_path_tree = {}

        while pq:

            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    shortest_path_tree[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        return distances, shortest_path_tree

    def print_shortest_path_tree(self, tree, start, end):
        path = []
        current = end
        while current != start:
            path.append(current)
            current = tree[current]
        path.append(start)
        path.reverse()
        return path

    def initialize_graph(self):
        self.addConnection("Majlis Park", "Azadpur", 3)
        self.addConnection("Azadpur", "Shalimar Bagh", 3)
        self.addConnection("Shalimar Bagh", "Netaji Subhash Place", 2)
        self.addConnection("Netaji Subhash Place", "Shakurpur", 2)
        self.addConnection("Shakurpur", "Punjabi Bagh West", 3)
        self.addConnection("Punjabi Bagh West", "ESI - Basaidarapur", 3)
        self.addConnection("ESI - Basaidarapur", "Rajouri Garden", 2)
        self.addConnection("Rajouri Garden", "Mayapuri", 2)
        self.addConnection("Mayapuri", "Naraina Vihar", 3)
        self.addConnection("Naraina Vihar", "Delhi Cantonment", 3)
        self.addConnection("Delhi Cantonment", "Durgabai Deshmukh South Campus", 5)
        self.addConnection("Durgabai Deshmukh South Campus", "Sir M. Vishweshwaraiah Moti Bagh", 2)
        self.addConnection("Sir M. Vishweshwaraiah Moti Bagh", "Bhikaji Cama Place", 3)
        self.addConnection("Bhikaji Cama Place", "Sarojini Nagar", 2)
        self.addConnection("Sarojini Nagar", "Dilli Haat - INA", 2)
        self.addConnection("Dilli Haat - INA", "South Extension", 2)
        self.addConnection("South Extension", "Lajpat Nagar", 3)
        self.addConnection("Lajpat Nagar", "Vinobapuri", 3)
        self.addConnection("Vinobapuri", "Ashram", 3)
        self.addConnection("Ashram", "Sarai Kale Khan - Nizamuddin", 3)
        self.addConnection("Sarai Kale Khan - Nizamuddin", "Mayur Vihar-I", 5)
        self.addConnection("Mayur Vihar-I", "Mayur Vihar Pocket I", 1)
        self.addConnection("Mayur Vihar Pocket I", "Trilokpuri Sanjay Lake", 6)
        self.addConnection("Trilokpuri Sanjay Lake", "East Vinod Nagar - Mayur Vihar-II", 2)
        self.addConnection("East Vinod Nagar - Mayur Vihar-II", "Mandawali - West Vinod Nagar", 3)
        self.addConnection("Mandawali - West Vinod Nagar", "IP Extension", 3)
        self.addConnection("IP Extension", "Anand Vihar", 4)
        self.addConnection("Anand Vihar", "Karkarduma", 2)
        self.addConnection("Karkarduma", "Karkarduma Court", 2)
        self.addConnection("Karkarduma Court", "Krishna Nagar", 2)
        self.addConnection("Krishna Nagar", "East Azad Nagar", 2)
        self.addConnection("East Azad Nagar", "Welcome", 2)
        self.addConnection("Welcome", "Jaffrabad", 3)
        self.addConnection("Jaffrabad", "Maujpur - Babarpur", 2)
        self.addConnection("Maujpur - Babarpur", "Gokulpuri", 2)
        self.addConnection("Gokulpuri", "Johri Enclave", 3)
        self.addConnection("Johri Enclave", "Shiv Vihar", 1)

        self.addConnection("Samaypur Badli", "Rohini Sector 18-19", 2)
        self.addConnection("Rohini Sector 18-19", "Haiderpur Badli Mor", 2)
        self.addConnection("Haiderpur Badli Mor", "Jahangirpuri", 3)
        self.addConnection("Jahangirpuri", "Adarsh Nagar", 2)
        self.addConnection("Adarsh Nagar", "Azadpur", 2)
        self.addConnection("Azadpur", "Model Town", 2)
        self.addConnection("Model Town", "GTB Nagar", 2)
        self.addConnection("GTB Nagar", "Vishwa Vidyalaya", 2)
        self.addConnection("Vishwa Vidyalaya", "Vidhan Sabha", 3)
        self.addConnection("Vidhan Sabha", "Civil Lines", 2)
        self.addConnection("Civil Lines", "Kashmere Gate", 2)
        self.addConnection("Kashmere Gate", "Chandni Chowk", 2)
        self.addConnection("Chandni Chowk", "Chawri Bazar", 3)
        self.addConnection("Chawri Bazar", "New Delhi", 1)
        self.addConnection("New Delhi", "Rajiv Chowk", 3)
        self.addConnection("Rajiv Chowk", "Patel Chowk", 2)   
        self.addConnection("Patel Chowk", "Central Secretariat", 2)
        self.addConnection("Central Secretariat", "Udyog Bhawan", 2)
        self.addConnection("Udyog Bhawan", "Lok Kalyan Marg", 2)
        self.addConnection("Lok Kalyan Marg", "Jor Bagh", 2)
        self.addConnection("Jor Bagh", "Dilli Haat - INA", 3)
        self.addConnection("Dilli Haat - INA", "AIIMS", 1)
        self.addConnection("AIIMS", "Green Park", 3)
        self.addConnection("Green Park", "Hauz Khas", 2)
        self.addConnection("Hauz Khas", "Malviya Nagar", 3)
        self.addConnection("Malviya Nagar", "Saket", 2)
        self.addConnection("Saket", "Qutab Minar", 3)
        self.addConnection("Qutab Minar", "Chhatarpur", 3)
        self.addConnection("Chhatarpur", "Sultanpur", 2)
        self.addConnection("Sultanpur", "Ghitorni", 3)
        self.addConnection("Ghitorni", "Arjan Garh", 3)
        self.addConnection("Arjan Garh", "Guru Dronacharya", 3)
        self.addConnection("Guru Dronacharya", "Sikanderpur", 2)
        self.addConnection("Sikanderpur", "MG Road", 2)
        self.addConnection("MG Road", "IFFCO Chowk", 3)
        self.addConnection("IFFCO Chowk", "HUDA City Centre", 2)
