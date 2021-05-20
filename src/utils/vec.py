import numpy as np

def unit(vec, n_residues):
    """
    :param: vec: 3*n vector, where n is the number of atoms
    :return: magnitude, unit_vec: magnitude vector and unit displacement vector
    """
    mag = np.linalg.norm(vec.reshape(-1, n_residues, 3), axis=-1)
    unit_vec = vec.reshape(-1, n_residues, 3) / mag[:, :, np.newaxis]
    return mag, unit_vec

def inner_product(unit_vec):
    mat = np.inner(unit_vec, unit_vec)
    res = np.zeros([mat.shape[1], mat.shape[1]], dtype=float)
    for i in range(mat.shape[0]):
        res = np.add(res, mat[i, :, i, :])
    res = res / mat.shape[0]
    res_tril = np.tril(res)
    res_tril[np.triu_indices(res_tril.shape[0], -1)] = np.nan

    return res_tril