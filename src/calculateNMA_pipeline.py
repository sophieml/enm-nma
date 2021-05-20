import os
import sys

import utils.file_utils as file_utils
import utils.model as model
import utils.plot as plot
import utils.parse_pdbeta as parse_pdbeta

def step1(pdb_path):
    n_modes = input("======================\nSTEP 1: Number of lowest modes to calculate? ")
    if not n_modes.isdecimal():
        print("Invalid number of modes")
        quit()
    else:
        n_modes = int(n_modes)
        print("Parsing PDB...")
        calphas, code = model.parse_pdb(pdb_path)
        return calphas, code, n_modes

def step2(calphas, code, nma_list, n_modes):
    continue2 = input("======================\nSTEP 2: Calculate Anistropic Network Model? y, n, or q: ")
    if continue2 == "q" or continue2 == "Q":
        quit()  
    elif continue2 == "Y" or continue2 == "y":
        anm  = model.calc_anm(calphas, code, n_modes)
        nma_list.append(anm)

def step3(calphas, code, nma_list, n_modes):
    continue3 = input("======================\nSTEP 4: Calculate Gaussian Network Model? y, n, or q: ")
    if continue3 == "q" or continue3 == "Q":
        quit()  
    elif continue3 == "Y" or continue3 == "y":
        gnm  = model.calc_gnm(calphas, code, n_modes)
        nma_list.append(gnm)

def step4(nma_list):
    continue4 = input("======================\nSTEP 4: Include Dihedral Elastic Network Model from PDBETA? y, n, or q: ")
    if continue4 == "q" or continue4 == "Q":
        quit()  
    elif continue4 == "Y" or continue4 == "y":
        enm = []
        fluct_path = input("Enter path to .flcatmA file: ")
        fluct_path = os.path.realpath(fluct_path)
        flucts = parse_pdbeta.parse_flucts(fluct_path)
        enm.append(flucts)
        corr_path = input("Enter path to .crratmA file: ")
        corr_path = os.path.realpath(corr_path)
        corr = parse_pdbeta.parse_corr(corr_path)
        enm.append(corr)
        nma_list.append(enm)

def step5(nma_list, outputFolderPath, prot_name):
    continue5 = input("======================\nSTEP 5: Show and save fluctuation plots? y, n, or q: ")
    if continue5 == "q" or continue5 == "Q":
        quit()  
    elif continue5 == "Y" or continue5 == "y":
        plot.show_all(nma_list, outputFolderPath, prot_name)

def step6(nma_list, outputFolderPath, prot_name, calphas):
    continue6 = input("======================\nSTEP 6: Write modes? y, n, or q: ")
    if continue6 == "q" or continue6 == "Q":
        quit()  
    elif continue6 == "Y" or continue6 == "y":
        model.write_modes(nma_list, outputFolderPath, prot_name, calphas)
def main(inputFilePath, outputFolderPath):
    nma_list = []
    calphas, code, n_modes = step1(inputFilePath)
    step2(calphas, code, nma_list, n_modes)
    step3(calphas, code, nma_list, n_modes)
    step4(nma_list)
    if len(nma_list) > 0:
        step5(nma_list, outputFolderPath, code)
        step6(nma_list, outputFolderPath, code, calphas)
    else:
        print("Did not calculate any modes. Quitting.")

if __name__ == "__main__":
    # parse arguments: input file, output folder

    inputFilePath = os.path.realpath(sys.argv[1]) 
    outputFolderPath = os.path.realpath(sys.argv[2])
    
    file_utils.createFolderIfNotPresentOrQuit(outputFolderPath)
    print(inputFilePath, outputFolderPath)
    main(inputFilePath, outputFolderPath)
