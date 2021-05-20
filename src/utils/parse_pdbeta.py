
import numpy as np
def parse_flucts(path):
    flucts = np.array([],dtype=float)
    with open(path, 'r') as f:
        for line in f:
            if line.strip() == 'Fluctuation caluculated from temp. factor':
                break
        next(f)
        for line in f:
            temp = line.split()
            flucts = np.append(flucts, float(temp[-4]))
    return flucts**2

def parse_corr(path):
    with open(path, 'r') as f:
        for line in f:
            if line.strip() == '# Time average of correlations between atomic fluctuations (normalized).':
                break
        next(f)
        n_residues = int(next(f).split()[-1])
        corr = np.empty((n_residues, n_residues), dtype=np.float)
        corr[:] = np.nan
        for i in range(3):
            next(f)
        for i in range(1, n_residues+1):
            line = next(f).split()
            sub = np.array([line[-i:]])
            sub = sub.astype(np.float)
            corr[i-1, 0:i] = sub
    return corr
