import prody
import numpy as np
import matplotlib.pyplot as plt
import os

def show_sqflucts(nma, ax, prot_name):
    if type(nma) != list:
        vals = prody.calcSqFlucts(nma)
        lab = str(nma)
    else:
        vals = nma[0]
        lab = "Dihedral ENM " + prot_name
    ax.plot(np.arange(len(vals)),
    vals, label=lab)
    ax.title.set_text('Squared fluctuation values by residue')
    ax.set_xlabel('Residue number')
    ax.set_ylabel('Squared fluctuation')

def show_corr(nma, ax, prot_name):
    if type(nma) != list:
        mat = prody.calcCrossCorr(nma)
        mat[np.triu_indices(mat.shape[0], -1)] = np.nan
        lab = str(nma)
    else:
        mat = nma[1]
        lab = 'Dihedral ENM ' + prot_name
    corr = ax.imshow(mat, cmap='RdBu_r', interpolation='bilinear', label="lab", vmin=-1, vmax=1)
    ax.set_title(lab + ' Residue Correlations', size=8)
    return corr

def show_all(nma_list, outputFolderPath, prot_name):
    fig = plt.figure(figsize=(17, 12))
    ax_sqflucts = fig.add_subplot(1, 2, 1)
    for i in range(len(nma_list)):
        show_sqflucts(nma_list[i], ax_sqflucts, prot_name)
        ax = fig.add_subplot(len(nma_list), 2, 2+i*2)
        corr = show_corr(nma_list[i], ax, prot_name)
    ax_sqflucts.legend()
    ax.set_xlabel('Residue number')
    fig.colorbar(corr, ax=fig.axes[1:])
    [ax.tick_params(axis='both', which='major', labelsize=6) for ax in fig.axes]
    plt.savefig(os.path.join(outputFolderPath, prot_name + '_plots.png'))
    plt.show()