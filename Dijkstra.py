from Graph import Graph
from datetime import datetime, timedelta
import sys
import heapq

class Dijkstra:
    def __init__(self):
        self.graph = None

    def run(self):
        graph = Graph()
        self.graph = graph.create_graph()
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
        print('11. Gedung Kuliah D          28. Labtek I A')
        print('12. Gerbang Samping          29. Perpustakaan')
        print('13. GKU II                   30. Labtek III')
        print('14. GKU I')
        print('------------------------------------------------------------')
    
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
