from collections import defaultdict
from pdbx.reader import PdbxReader
from pdbx.containers import *
import math
import sys
import networkx as nx
import matplotlib.pyplot as plt
def load_cif(fpath):
    cif = open(fpath)
    # Create a list to store data blocks
    data = []
    # Create a PdbxReader object
    pRd = PdbxReader(cif)
    # Read the CIF file, propagating the data list
    pRd.read(data)
    # Close the CIF file, as it is no longer needed
    cif.close()
    # Retrieve the first data block
    block = data[0]
    return block

def load_radii(fpath):
    radii = {}
    with open(fpath) as f:
        for line in f:
            l = line.split()
            radii[l[1]] = float(l[2])
    return radii

def build_graph(atoms, edges):
    G = nx.Graph()
    residues = defaultdict(list)
    for i in range(atoms.row_count):
        resid = atoms.get_value('auth_seq_id', i)
        residues[resid].append(i)
        data = {
            'id': atoms.get_value('id', i),
            'elename': atoms.get_value('type_symbol', i),
            'altid': atoms.get_value('label_alt_id', i),
            'resid': resid,
            'resname': atoms.get_value('auth_comp_id', i)
        }
        G.add_node(i, attr_dict=data)
    G.add_edges_from(edges)
    print("Graph connected:", nx.is_connected(G))
    for resid in residues:
        subg = G.subgraph(residues[resid])
        try:
            while (nx.find_cycle(subg, orientation='ignore')):
                cycle = list(nx.find_cycle(subg, orientation='ignore'))
                print(cycle[0])
                G.remove_edge(cycle[0][0], cycle[0][1])
        except:
            continue
    print("Graph is a tree:", nx.algorithms.tree.recognition.is_tree(G))
    return G

def is_bonded(atoms, radii, i, j):
    keys = ['Cartn_x', 'Cartn_y', 'Cartn_z']
    a_ele = atoms.get_value('type_symbol', i)
    b_ele = atoms.get_value('type_symbol', j)
    a = [float(atoms.get_value(k, i)) for k in keys]
    b = [float(atoms.get_value(k, j)) for k in keys]
    return (0.4 <= math.dist(a, b) <= (radii[a_ele] + radii[b_ele] + 0.56))

def get_edges(atoms, radii):
    edges = set()
    for i in range(atoms.row_count):
        for j in range(atoms.row_count):
            if is_bonded(atoms, radii, i, j) and (j, i) not in edges:
                # print(i, j)
                edges.add((i, j))
    return edges

def main():
    f = sys.argv[1]
    block = load_cif(f)
    radii = load_radii(sys.argv[2])
    atom_site = block.get_object("atom_site")
    edges = get_edges(atom_site, radii)
    G = build_graph(atom_site, edges)
    nx.draw(G, node_size=2)
    plt.show()


if __name__ == "__main__":
    main()