import prody
import os
from pathlib import Path

def parse_pdb(pdb_path):
    prot = prody.parsePDB(pdb_path)
    code = Path(pdb_path).stem
    calphas = prot.select('protein and chain A and name CA')
    return calphas, code

def calc_anm(calphas, code, n_modes):
    anm = prody.ANM(code)
    anm.buildHessian(calphas)
    anm.calcModes(n_modes)
    return anm

def calc_gnm(calphas, code, n_modes):
    gnm = prody.GNM(code)
    gnm.buildKirchhoff(calphas)
    gnm.calcModes(n_modes)
    return gnm

def write_modes(nma_list, output_path, code, calphas):
    for nma in nma_list:
        name = type(nma).__name__
        if name != 'list':
            prody.writeNMD(os.path.join(output_path, code + "_" + name + "_modes.nmd"), nma, calphas)