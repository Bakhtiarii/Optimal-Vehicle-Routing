import csv
                                        # Show the list of places and get input
print("The Names of Places :")
print("1- Mellat Park   2- Arghavan Park    3- Baqiatallah Hospital    4- ICRO     5- Pazriz Hotel\n6- Sadaf Swimming Pool     7- Dey General Hospital    8- Tehran Heart Center   9- Salmas Square\n10- Tehran Museum of Contemporary Art    11- Enghelab Sports Complex     12- Paris Center\n13- Sheikh Bahaei Square    14- Mom Fertility and Infertility Center    15- Raees Coffe\n")
Starting_Point = input("Enter exactly the name of your starting point :")
Destination_Point = input("Enter exactly the name of your destination point :")
                                        # Read the Dataset
File = open('Dataset.csv')
Csvreader = csv.reader(File)
Rows = []
for Row in Csvreader:
        Rows.append(Row)
                                        # Define edges of the graph
from collections import defaultdict
class Graph():
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}
    def addEdge(self, fromVerex, toVertex, weight):
        self.edges[fromVerex].append(toVertex)
        self.edges[toVertex].append(fromVerex)
        self.weights[(fromVerex, toVertex)] = weight
        self.weights[(toVertex, fromVerex)] = weight
                                         # Find shortest Path Function
def dijkstra(myGraph, initial, end):
    shortestPaths = {initial: (None, 0)}
    currentVertex = initial
    visited = set()
    while currentVertex != end:
        visited.add(currentVertex)
        destinations = graph.edges[currentVertex]
        weightToCurrentVertex = shortestPaths[currentVertex][1]
        for nextVertex in destinations:
            weight = graph.weights[(currentVertex, nextVertex)] + weightToCurrentVertex
            if nextVertex not in shortestPaths:
                shortestPaths[nextVertex] = (currentVertex, weight)
            else:
                currentShortestWeight = shortestPaths[nextVertex][1]
                if currentShortestWeight > weight:
                    shortestPaths[nextVertex] = (currentVertex, weight)        
        nextDestinations = {vertex: shortestPaths[vertex] for vertex in shortestPaths if vertex not in visited}
        if not nextDestinations:
            return "Route Not Possible"
        currentVertex = min(nextDestinations, key=lambda k: nextDestinations[k][1])
    path = []
    while currentVertex is not None:
        path.append(currentVertex)
        nextVertex = shortestPaths[currentVertex][0]
        currentVertex = nextVertex
    path = path[: : -1]
    return path
                                        # Edges of the graph
graph = Graph()
edges = [
        (1, 5, 1), (1, 11, 1), (1, 13, 2), (2, 5, 2), (2, 12, 1), (3, 6, 1), (3, 13, 1),
        (3, 14, 2), (4, 5, 2), (4, 7, 2), (4, 12, 1), (5, 1, 2), (5, 4, 1), (5, 12, 1),
        (5, 13, 2), (6, 3, 2), (6, 8, 1), (6, 14, 2), (7, 4, 4), (7, 9, 1), (7, 14, 1),
        (8, 6, 2), (8, 10, 2), (9, 7, 1), (9, 10, 1), (9, 15, 1), (10, 8, 3), (10, 9, 2),
        (10, 15, 1), (11, 1, 1), (11, 13, 2), (12, 2, 2), (12, 4, 1), (12, 5, 1), (13, 1, 2),
        (13, 3, 1), (13, 5, 2), (14, 3, 3), (14, 6, 2), (14, 7, 1), (15, 9, 1), (15, 10, 1),
]
for edge in edges:
    graph.addEdge(*edge)
                                        # Find Cordinates
Starting_Point_Number = 0
Starting_Point_Cordinate = []
Destination_Point_Number = 0
Destination_Point_Cordinate = []
for Place in Rows:
    if Place[1] == Starting_Point:
        Starting_Point_Number = Place[0]
        Starting_Point_Cordinate = Place[2]
    if Place[1] == Destination_Point:
        Destination_Point_Number = Place[0]
        Destination_Point_Cordinate = Place[2]
path = dijkstra(graph, int(Starting_Point_Number), int(Destination_Point_Number))
                                        # Calculate the total cost of the optimal rout
Total_Cost = 0
for Counter in range(len(path)-1):
    for Item in edges:
        if (Item[0] == path[Counter])&(Item[1] == path[Counter+1]):
            Total_Cost = Total_Cost + Item[2]
                                        # Print desired output
print('\nIndex of starting point is : ',Starting_Point_Number,' and the cordinate is : ',Starting_Point_Cordinate)
print('Index of destination point is : ',Destination_Point_Number,' and the cordinate is : ',Destination_Point_Cordinate)
print('\nThe indices of all places on the way of the optimal rout is : ',path)
print('\nThe total cost of the optimal rout is : ',Total_Cost)



