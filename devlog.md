# Elastic Network Model - Normal Mode Analysis from PDB data

## Sophie Li

### 04/23/21

- Started writing pseudocode for tree construction
  - Covalent bond detection rules from Rasmol: https://www.umass.edu/microbio/rasmol/rasbonds.htm
- Potential issues: how do we identify rings? is it better to use write a graph data structure from scratch or use a pre-existing one?

```
class Node:
	int atomid
	str element
	int resid
	str residue
	int unitid
	float[] coords
	Node[] neighbors

Node[len(pdb)] atoms;
Node[] residues;

for i = 0:len(pdb) in pdb:
	# extract
	atom = Node(atomid, element, resid, residue, unitid=i, coords, [])
	atoms.append(atom)
	if i == 0 or atom.resid != atom[i-1].resid:
		# append if
		residues.append([atom])
	else: # otherwise we're on the same residue
		residues[-1].append(atom)

for i= 0:len(atoms):
	for j = 0:len(atoms):
		if atoms[i] != atoms[j]:
			if 0.4 <= dist(atoms[i], atoms[j]) <= (cov[atoms[i].element] + cov[atoms[j].element] + 0.56):
				atoms[i].neighbors.append(atoms[j])
				atoms[j].neighbors.append(atoms[i])
```



### 04/21/21

- Downloaded PDBETA software and attempted to run (didn't work)
- Examined .dat file that came with the software
- Started looking into creating the tree structure
	- https://www.researchgate.net/post/How_can_I_determine_the_bonding_between_Atoms_in_a_PDB_file

