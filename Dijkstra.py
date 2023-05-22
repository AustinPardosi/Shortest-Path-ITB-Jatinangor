from Graph import Graph
from datetime import datetime, timedelta
import sys
import heapq

class Dijkstra:
    def __init__(self):
        self.graph = None

    def run(self):
        self.graph = self.create_graph()
        self.show_info()

        start = input("Posisi awal: ")
        finish = input("Posisi tujuan: ")

        distance, path = self.dijkstra(start, finish)
        if distance is not None:
            print("Jarak terpendek:", distance)
            print("Path:", ' -> '.join(path))
            print("Waktu tempuh pejalan kaki: {:.2f} menit".format((distance/80.5)))
            arrival_time = self.calculate_arrival_time(distance)
            print("Perkiraan waktu sampai: {}".format(arrival_time))

    def calculate_arrival_time(self, distance):
        current_time = datetime.now()
        travel_time_minutes = distance / 100
        travel_time = timedelta(minutes=travel_time_minutes)

        arrival_datetime = current_time + travel_time
        arrival_time = arrival_datetime.strftime("%H:%M:%S")
        return arrival_time
    
    def show_info(self):
        print('------------------------------------------------------------')
        print('Selamat Datang Di Aplikasi Jalur Terpendek ITB Jatinangor')
        print('')
        print('Silahkan Pilih Posisi Awal dan Tujuan Anda!')
        print('1. Gerbang Utama             18. Korea Cyber Security R&D Center')
        print('2. Prasasti                  19. Rusun Dosen')
        print('3. GOR                       20. Asrama TB')
        print('4. Situ II                   21. Water Treatment Plant')
        print('5. Pool Kendaraan            22. GSG')
        print('6. Masjid Al-Jabbara         23. Labtek IV')
        print('7. Labtek I C                24. Labtek II B')
        print('8. Labtek I B                25. Labtek II A')
        print('9. Gedung Utama Rektorat     26. Gedung Kuliah B')
        print('10. Gedung Kuliah E          27. Gedung Kuliah A')
        print('11. IPST                     28. Labtek I A')
        print('12. Gerbang Samping          29. Perpustakaan')
        print('13. GKU II                   30. Labtek III')
        print('14. GKU I                    31. Gedung Kuliah D')
        print('------------------------------------------------------------')
    
    def create_graph(self):
        # Create Object Graph
        graph = Graph()

        # Adding nodes to the graph according to ITB Jatinangor's Map
        graph.add_node('Gerbang Utama')
        graph.add_node('Prasasti')
        graph.add_node('GOR')
        graph.add_node('Situ II')
        graph.add_node('Pool Kendaraan')
        graph.add_node('Masjid Al-Jabbar')
        graph.add_node('Labtek I C')
        graph.add_node('Labtek I B')
        graph.add_node('Labtek V A')
        graph.add_node('Mushola As-Sajaroh')
        graph.add_node('IPST')
        graph.add_node('Gerbang Samping')
        graph.add_node('GKU II')
        graph.add_node('GKU I')
        graph.add_node('Gedung Utama Rektorat')
        graph.add_node('Gedung Kuliah E')
        graph.add_node('Gedung Kuliah D')
        graph.add_node('Labtek III')
        graph.add_node('Perpustakaan')
        graph.add_node('Labtek I A')
        graph.add_node('Gedung Kuliah B')
        graph.add_node('Labtek II A')
        graph.add_node('Labtek II B')
        graph.add_node('Labtek IV')
        graph.add_node('GSG')
        graph.add_node('Water Treatment Plant')
        graph.add_node('Asrama TB')
        graph.add_node('Rusun Dosen')
        graph.add_node('Korea Cyber Security R&D Center')

        # Adding edges between nodes with its weight in km
        graph.add_edge('Gerbang Utama', 'Situ II', 82)
        graph.add_edge('Situ II', 'Gerbang Utama', 82)
        graph.add_edge('Gerbang Utama', 'Masjid Al-Jabbar', 700)
        graph.add_edge('Masjid Al-Jabbar', 'Gerbang Utama', 700)
        graph.add_edge('Situ II', 'Prasasti', 210)
        graph.add_edge('Prasasti', 'Situ II', 210)
        graph.add_edge('Gerbang Utama', 'Pool Kendaraan', 91)
        graph.add_edge('Pool Kendaraan', 'Gerbang Utama', 91)
        graph.add_edge('Pool Kendaraan', 'Prasasti', 220)
        graph.add_edge('Prasasti', 'Pool Kendaraan', 220)
        graph.add_edge('Gerbang Utama', 'Prasasti', 210)
        graph.add_edge('Prasasti','Gerbang Utama',  210)
        graph.add_edge('Prasasti', 'Labtek IV', 54)
        graph.add_edge('Labtek IV', 'Prasasti', 54)
        graph.add_edge('Prasasti', 'Rusun Dosen', 200)
        graph.add_edge('Rusun Dosen', 'Prasasti', 200)
        graph.add_edge('Labtek IV', 'Labtek I C', 300)
        graph.add_edge('Labtek I C', 'Labtek IV', 300)
        graph.add_edge('Labtek I C', 'GKU II', 240)
        graph.add_edge('GKU II', 'Labtek I C', 240)
        graph.add_edge('Labtek I C', 'Labtek I B', 87)
        graph.add_edge('Labtek I B', 'Labtek I C', 87)
        graph.add_edge('Labtek I C', 'Labtek I A', 16)
        graph.add_edge('Labtek I A', 'Labtek I C', 16)
        graph.add_edge('Labtek I C', 'Asrama TB', 99)
        graph.add_edge('Asrama TB', 'Labtek I C', 99)
        graph.add_edge('GKU II', 'Labtek I B', 230)
        graph.add_edge('Labtek I B', 'GKU II', 230)
        graph.add_edge('Labtek I B', 'Labtek I A', 100)
        graph.add_edge('Labtek I A', 'Labtek I B', 100)
        graph.add_edge('Labtek I A', 'Asrama TB', 83)
        graph.add_edge('Asrama TB', 'Labtek I A', 83)
        graph.add_edge('Asrama TB', 'Water Treatment Plant', 190)
        graph.add_edge('Water Treatment Plant', 'Asrama TB', 190)
        graph.add_edge('Asrama TB', 'Labtek II A', 110)
        graph.add_edge('Labtek II A', 'Asrama TB', 110)
        graph.add_edge('Labtek II A', 'Gedung Kuliah B', 50)
        graph.add_edge('Gedung Kuliah B', 'Labtek II A', 50)
        graph.add_edge('Labtek II A', 'Labtek II B', 31)
        graph.add_edge('Labtek II B', 'Labtek II A', 31)
        graph.add_edge('Labtek II A', 'GOR', 280)
        graph.add_edge('GOR', 'Labtek II A', 280)
        graph.add_edge('GOR', 'GSG', 130)
        graph.add_edge('GSG', 'GOR', 130)
        graph.add_edge('GSG', 'Perpustakaan', 180)
        graph.add_edge('Perpustakaan', 'GSG', 180)
        graph.add_edge('Perpustakaan', 'Korea Cyber Security R&D Center', 20)
        graph.add_edge('Korea Cyber Security R&D Center', 'Perpustakaan', 20)
        graph.add_edge('Korea Cyber Security R&D Center', 'Gedung Utama Rektorat', 77)
        graph.add_edge('Gedung Utama Rektorat', 'Korea Cyber Security R&D Center', 77)
        graph.add_edge('Gedung Utama Rektorat', 'GKU I', 77)
        graph.add_edge('GKU I', 'Gedung Utama Rektorat', 77)
        graph.add_edge('GKU I', 'GKU II', 77)
        graph.add_edge('GKU II', 'GKU I', 77)
        graph.add_edge('Gedung Kuliah E', 'GKU I', 28)
        graph.add_edge('GKU I', 'Gedung Kuliah E', 28)
        graph.add_edge('GKU I', 'Gedung Kuliah D', 170)
        graph.add_edge('Gedung Kuliah D', 'GKU I', 170)
        graph.add_edge('Gedung Kuliah D', 'Gedung Utama Rektorat', 170)
        graph.add_edge('Gedung Utama Rektorat', 'Gedung Kuliah D', 170)
        graph.add_edge('Labtek V A', 'Masjid Al-Jabbar', 190)
        graph.add_edge('Masjid Al-Jabbar', 'Labtek V A', 190)
        graph.add_edge('Labtek V A', 'Gedung Utama Rektorat', 450)
        graph.add_edge('Gedung Utama Rektorat', 'Labtek V A', 450)

        return graph
    
    def dijkstra(self, start, finish):
        # Save the shortest distance from start node to every node
        dist = {v: sys.maxsize for v in self.graph.vertices}

        # Initialize distance from start node to start node
        dist[start] = 0

        # Save the previous node that had found earlier
        prev = {}

        # Save the tuple of (latest distance, node) in priority queue
        queue = [(0, start)]

        while queue:
            # Take a node with the smallest distance from the queue
            curr_dist, curr_node = heapq.heappop(queue)

            if curr_dist > dist[curr_node]:
                continue

            if curr_node == finish:
                break

            for neighbor, weight in self.graph.edges[curr_node].items():
                # Calculate new distance
                new_dist = curr_dist + weight

                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    prev[neighbor] = curr_node
                    heapq.heappush(queue, (new_dist, neighbor))

        if finish not in prev:
            print("Tidak ada jalur yang tersedia.")
            return None, None

        path = []
        curr_node = finish
        while curr_node != start:
            # Add node to the path
            path.append(curr_node)
            curr_node = prev[curr_node]
        path.append(start)

        path.reverse()
        return dist[finish], path
