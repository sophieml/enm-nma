# Elastic Network Model - Normal Mode Analysis from PDB data

## Sophie Li

### 05/12/21

Final project update

So far, I have begun writing scripts to run the CP2K vibrational analysis. I decided to use a third-party binary, so I am using PYCP2K to modify a template file that I have set up. One concern I have is that even energy minimization/geometric optimization takes a long time for even small molecules (~15 minutes on my laptop for a water molecule). Another concern I have is that the binary I'm using sometimes runs into segmentation faults when used with valid input files (the analysis will run once, but not again, even after deleting output files). However, I believe that I can at least create a pipeline to produce the working final input files.

Outline (from FP presentation)

- **In progress**: PYCP2K: Generate vibrational analysis
  - Load PDB file
    - ASE module -> convert PDB to XYZ
    - Write into template file
  - Run vibrational analysis according to TAMkin 
    - Step 1: Write XYZ file for geometry optimization (includes energy)
    - Step 2: Run vibrational analysis
    - Add coords, basis, potential constants from XYZ file (write script to add basis and potential to input file)
    - Write out CP2K file
  - TAMkin: Run NMA on generated CP2K file
  - Plot fluctuation data
  - **IF TIME** compare to dihedral ENM analysis using PDBETA

### 05/03/21
- Wrote most methods for tree construction (parse input, find covalent bonds, break cycles in each residue)
- current usage: `python src/build_graphs.py path/to/input.cif path/to/radii.cif` (use depends on activating conda environment)

To-do
- Finish writing tree
  - Break cycles, if any, in overall tree structure
  - Fix omega and chi bonds by creating units (see paper)
  - begin work/further research on elastic network model
- Change structure of file (move methods to `utils` folder)
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

