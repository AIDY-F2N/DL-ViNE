import random
import os
import copy
import networkx as nx
import json

def generate_waxman_graph(num_nodes, alpha, beta):
    G = nx.waxman_graph(num_nodes, alpha=alpha, beta=beta)
    while not nx.is_connected(G):
        G = nx.waxman_graph(num_nodes, alpha=alpha, beta=beta)  # Réessayer jusqu'à ce qu'un graphe connexe soit généré
    return G

def create_network(n_nodes, cap_min, cap_max):
    # Générer un graphe complet
    complete_graph = nx.complete_graph(n_nodes)
    n_edges = n_nodes * (n_nodes - 1) // 2

    # Créer le réseau à partir du graphe complet généré
    network = {
        "n": n_nodes,
        "nodes_cap": {},
        "edges": [],
        "m": n_edges
    }

    # Ajouter les capacités des nœuds
    for node in complete_graph.nodes():
        network['nodes_cap'][str(node)] = random.randint(cap_min, cap_max)

    # Ajouter les arêtes avec des poids aléatoires
    for edge in complete_graph.edges():
        network['edges'].append({
            "e": [edge[0], edge[1]],
            "weight": random.randint(cap_min, cap_max)
        })

    return network


def create_slices(num_slices, n):
    slices = []

    for i in range(num_slices):
        num_nodes = random.randint(n, n+4)
        connexe = num_nodes - 1
        complet = num_nodes*connexe/2
        n_edges = random.randint(connexe, complet)
        network = {
            "n": num_nodes,
            "nodes_cap": {},
            "edges": [],
            "m": n_edges  # Pour un graphe connecté, le nombre d'arêtes est égal au nombre de noeuds - 1
        }
    
        # Créer les capacités des noeuds
        for i in range(num_nodes):
            network['nodes_cap'][str(i)] = random.randint(1, 50)
    
        # Générer un graphe Waxman connexe
        G = generate_waxman_graph(num_nodes, alpha=0.5, beta=0.2)
        
        # Convertir le graphe en liste d'arêtes pour l'ajouter à la slice
        edges = list(G.edges())
        for edge in edges:
            a, b = edge
            network['edges'].append({
                "e": [a, b],
                "weight": random.randint(1, 50)
            })
        
         # Ajouter des arêtes supplémentaires pour atteindre le nombre d'arêtes souhaité
        while len(network['edges']) < n_edges:
            a = random.randint(0, num_nodes - 1)
            b = random.randint(0, num_nodes - 1)
            if a != b and (a, b) not in network['edges'] and (b, a) not in network['edges']:
                network['edges'].append({
                    "e": [a, b],
                    "weight": random.randint(1, 50)
                })

        slices.append(network)

    return slices


def create_events(num_slices, arrival_rate, departure_rate):
    events = []
    current_time = 0

    # Générer les événements d'arrivée et de départ pour chaque slice
    for slice_number in range(num_slices):
        arrival_time = random.expovariate(arrival_rate) + current_time
        events.append((arrival_time, 'arrival', slice_number))

        departure_time = random.expovariate(departure_rate) + arrival_time
        events.append((departure_time, 'departure', slice_number))

        current_time = arrival_time  # Mettre à jour le temps courant pour la prochaine slice

    # Trier les événements par le temps d'occurrence
    events.sort(key=lambda x: x[0])

    # Formater les événements en chaîne de caractères
    events_str = "n_evt=" + str(len(events)) + "\n"
    for event in events:
        events_str += f"({event[0]:.2f}, '{event[1]}', {event[2]})\n"

    return events_str

def save_files(network, events, slices,  directory):
    instance_path = os.path.join(directory, f'test7')
    os.makedirs(instance_path, exist_ok=True)

    with open(os.path.join(instance_path, 'test_network'), 'w') as f:
        json.dump(network, f, indent=4)
    
    with open(os.path.join(instance_path, 'events.txt'), 'w') as f:
        f.write(events)

    for i, slice_network in enumerate(slices):
        with open(os.path.join(instance_path, f'slice {i}'), 'w') as f:
            json.dump(slice_network, f, indent=4)
    
def generate_instances(num_instances, directory):
    for i in range(1, num_instances + 1):
        network = create_network(30, 60, 100) #Nb de noeud , capacité CPU&BW min et max
        events = create_events(50, arrival_rate=0.03, departure_rate=0.005) #nb de slices
        slices = create_slices(50, 8)  # Générer n_slices avec variation de capacités et poids
        save_files(network, events, slices, directory)

# Appel de la fonction pour générer les instances
generate_instances(1, '/home/yasser/Documents/RHO_notFixed/instances/50_slices/')