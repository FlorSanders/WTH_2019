import json
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations


def pathLength(graph, path):
    length = 0
    lastnode = path[0]
    for node in path[1:]:
        length = length + graph[lastnode][node]["weight"]
        lastnode = node
    return length

def splitEdge(vertices, edges, targetEdge):
 
    targetWeight = targetEdge["length"]/2
    edges.remove(targetEdge)
    newx,newy = 0,0
    for vert in vertices:
        if (vert["id"] == targetEdge["u"] or vert["id"] == targetEdge["v"]):
            newx += vert["x"]
            newy += vert["y"]
    newx = newx/2
    newy = newy/2
    name = targetEdge["u"] + "_" + targetEdge["v"]
    newvert = {"id":(name),"x":newx,"y":newy}
    vertices.append(newvert)
    edges.append({"id":(len(edges)),"u":targetEdge["u"],"v":name,"length":targetWeight})
    edges.append({"id":(len(edges)),"u":targetEdge["v"],"v":name,"length":targetWeight})
    return name


#Load Market Schematics - enables switching to different store layouts
with open('market.json') as json_file:
    marketdata = json.load(json_file)
    superstore = marketdata["superstore"]
    edges = superstore["edges"]
    vertices = superstore["vertices"]

    #Test values for testing
    #edges that have to be visited
    groceryStops = [2,14,11]

    intersections = {"a","b"}
    #for edge in edges:
     #   if edge["id"] in groceryStops:
      #      intersections.add(splitEdge(vertices,edges,edge))


    # We define visiting an Aisle as going from one end to the other - i.e. visiting both vertices.
    # This also allows for defining an aisle as several smaller segments, allowing to enter an aisle for a bit and then returning.
    targetaisles = set()
    #entry and exit will always be visited
    for aisle in groceryStops:
        for edge in edges:
            if edge["id"] == aisle:
                intersections.add(edge["u"])
                intersections.add(edge["v"])
                targetaisles.add((edge["u"],edge["v"]))

    #Make relevant graph:
    G=nx.Graph()
    #fill graph
    for vert in vertices:
        G.add_node(vert["id"], pos=(vert["y"],vert["x"]))
    for edge in edges:
        G.add_edge(edge["v"],edge["u"],weight=edge["length"])


    #set positions and add weight labels, and draw
    pos=nx.get_node_attributes(G,'pos')
    edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
    plt.figure(1)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    nx.draw_networkx_edges(G,pos=pos,edgelist=targetaisles,edge_color = "g", width=4)
    nx.draw(G,pos,with_labels = True)

    #Take relevant verticies and build a complete graph from it - each edge having the shortest path in G between the two vertices.
    TSP=nx.Graph()
    for intersec in intersections:
        for vert in vertices:
            if vert["id"] == intersec:
                TSP.add_node(vert["id"], pos=(vert["y"],vert["x"]))

    for i,startvert in enumerate(intersections):
        for j,targetvert in enumerate(intersections):
            if i > j:
                TSP.add_edge(startvert,targetvert,weight=nx.shortest_path_length(G, startvert, targetvert, "weight"))

    # Draw the intermediary result for debugging purposes.

    pos=nx.get_node_attributes(TSP,'pos')

    edge_labels=dict([((u,v,),d['weight']) for u,v,d in TSP.edges(data=True)])
    plt.figure(2)
    nx.draw_networkx_edge_labels(TSP,pos,edge_labels=edge_labels)
    nx.draw(TSP,pos,with_labels=True)


    # Traveling Salesman Problem - throw some brute force at this problem.
    # Might be inefficient in large stores with a long shopping list, but it'll do for the prototype
    shortest = 10000
    for path in permutations(TSP.nodes):
        if (path[0] == "b" and path[-1] == "a"):
            length = pathLength(TSP,path)
            
            #In the spirit of the hackathon: A hack.
            pathpermutations = set()
            [pathpermutations.add((path[n],path[n+1])) for n in range(len(path)-1)]
            [pathpermutations.add((path[n+1],path[n])) for n in range(len(path)-1)]


            if length < shortest and targetaisles.issubset(pathpermutations):
                shortest = length
                bestPath = path

    # Take that best path and find the matching route in the original graph.
    lastnode = bestPath[0]
    completepath = [bestPath[0]]
    for waypoint in bestPath[1:]:
        for node in nx.shortest_path(G,lastnode,waypoint,"weight")[1:]:
            completepath.append(node)
        lastnode = waypoint

    #VIsualize the route
    route_edges = [(completepath[n],completepath[n+1]) for n in range(len(completepath)-1)]

    plt.figure(3)
    pos=nx.get_node_attributes(G,'pos')
    edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    nx.draw_networkx_edges(G,pos=pos,edgelist=route_edges,edge_color = "r", width=5)
    nx.draw_networkx_edges(G,pos=pos,edgelist=targetaisles,edge_color = "b", width=4)

    nx.draw(G,pos,with_labels = True)
    plt.show()
