class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}
    
    def add_node(self, node):
        self.vertices.add(node)
        self.edges[node] = {}
    
    def add_edge(self, node1, node2, weight):
        self.edges[node1][node2] = weight
        self.edges[node2][node1] = weight

    def create_graph(self):
        # Adding nodes to the graph according to ITB Jatinangor's Map
        self.add_node('Gerbang Utama')
        self.add_node('Prasasti')
        self.add_node('GOR')
        self.add_node('Situ II')
        self.add_node('Pool Kendaraan')
        self.add_node('Masjid Al-Jabbar')
        self.add_node('Labtek I C')
        self.add_node('Labtek I B')
        self.add_node('Labtek V A')
        self.add_node('Gedung Utama Rektorat')
        self.add_node('Gedung Kuliah E')
        self.add_node('Gedung Kuliah D')
        self.add_node('GKU II')
        self.add_node('GKU I')
        self.add_node('Korea Cyber Security R&D Center')
        self.add_node('Rusun Dosen')
        self.add_node('Asrama TB')
        self.add_node('Water Treatment Plant')
        self.add_node('GSG')
        self.add_node('Labtek IV')
        self.add_node('Labtek II B')
        self.add_node('Labtek II A')
        self.add_node('Gedung Kuliah B')
        self.add_node('Labtek I A')
        self.add_node('Perpustakaan')
        self.add_node('Labtek III')

        # Adding edges between nodes with its weight in km
        self.add_edge('Gerbang Utama', 'Situ II', 82)
        self.add_edge('Situ II', 'Gerbang Utama', 82)
        self.add_edge('Gerbang Utama', 'Masjid Al-Jabbar', 700)
        self.add_edge('Masjid Al-Jabbar', 'Gerbang Utama', 700)
        self.add_edge('Situ II', 'Prasasti', 210)
        self.add_edge('Prasasti', 'Situ II', 210)
        self.add_edge('Gerbang Utama', 'Pool Kendaraan', 91)
        self.add_edge('Pool Kendaraan', 'Gerbang Utama', 91)
        self.add_edge('Pool Kendaraan', 'Prasasti', 220)
        self.add_edge('Prasasti', 'Pool Kendaraan', 220)
        self.add_edge('Gerbang Utama', 'Prasasti', 210)
        self.add_edge('Prasasti','Gerbang Utama',  210)
        self.add_edge('Prasasti', 'Labtek IV', 54)
        self.add_edge('Labtek IV', 'Prasasti', 54)
        self.add_edge('Prasasti', 'Rusun Dosen', 200)
        self.add_edge('Rusun Dosen', 'Prasasti', 200)
        self.add_edge('Labtek IV', 'Labtek I C', 300)
        self.add_edge('Labtek I C', 'Labtek IV', 300)
        self.add_edge('Labtek I C', 'GKU II', 240)
        self.add_edge('GKU II', 'Labtek I C', 240)
        self.add_edge('Labtek I C', 'Labtek I B', 87)
        self.add_edge('Labtek I B', 'Labtek I C', 87)
        self.add_edge('Labtek I C', 'Labtek I A', 16)
        self.add_edge('Labtek I A', 'Labtek I C', 16)
        self.add_edge('Labtek I C', 'Asrama TB', 99)
        self.add_edge('Asrama TB', 'Labtek I C', 99)
        self.add_edge('GKU II', 'Labtek I B', 230)
        self.add_edge('Labtek I B', 'GKU II', 230)
        self.add_edge('Labtek I B', 'Labtek I A', 100)
        self.add_edge('Labtek I A', 'Labtek I B', 100)
        self.add_edge('Labtek I A', 'Asrama TB', 83)
        self.add_edge('Asrama TB', 'Labtek I A', 83)
        self.add_edge('Asrama TB', 'Water Treatment Plant', 190)
        self.add_edge('Water Treatment Plant', 'Asrama TB', 190)
        self.add_edge('Asrama TB', 'Labtek II A', 110)
        self.add_edge('Labtek II A', 'Asrama TB', 110)
        self.add_edge('Labtek II A', 'Gedung Kuliah B', 50)
        self.add_edge('Gedung Kuliah B', 'Labtek II A', 50)
        self.add_edge('Labtek II A', 'Labtek II B', 31)
        self.add_edge('Labtek II B', 'Labtek II A', 31)
        self.add_edge('Labtek II A', 'GOR', 280)
        self.add_edge('GOR', 'Labtek II A', 280)
        self.add_edge('GOR', 'GSG', 130)
        self.add_edge('GSG', 'GOR', 130)
        self.add_edge('GSG', 'Perpustakaan', 180)
        self.add_edge('Perpustakaan', 'GSG', 180)
        self.add_edge('Perpustakaan', 'Korea Cyber Security R&D Center', 20)
        self.add_edge('Korea Cyber Security R&D Center', 'Perpustakaan', 20)
        self.add_edge('Korea Cyber Security R&D Center', 'Gedung Utama Rektorat', 77)
        self.add_edge('Gedung Utama Rektorat', 'Korea Cyber Security R&D Center', 77)
        self.add_edge('Gedung Utama Rektorat', 'GKU I', 190)
        self.add_edge('GKU I', 'Gedung Utama Rektorat', 190)
        self.add_edge('GKU I', 'GKU II', 120)
        self.add_edge('GKU II', 'GKU I', 120)
        self.add_edge('Gedung Kuliah E', 'GKU I', 28)
        self.add_edge('GKU I', 'Gedung Kuliah E', 28)
        self.add_edge('GKU I', 'Gedung Kuliah D', 21)
        self.add_edge('Gedung Kuliah D', 'GKU I', 21)
        self.add_edge('Gedung Kuliah D', 'Gedung Utama Rektorat', 170)
        self.add_edge('Gedung Utama Rektorat', 'Gedung Kuliah D', 170)
        self.add_edge('Labtek V A', 'Masjid Al-Jabbar', 190)
        self.add_edge('Masjid Al-Jabbar', 'Labtek V A', 190)
        self.add_edge('Labtek V A', 'Gedung Utama Rektorat', 450)
        self.add_edge('Gedung Utama Rektorat', 'Labtek V A', 450)

        return self