import numpy as np
from scipy.optimize import fsolve

def ids(Vd, Vs):
    return (Vd - Vs)**2

def bsimbulk(Vd, Vs, Rd, Rs):    
    def F(z):
        x, y = z
        f = np.zeros(2)
        f[0] = Vd - x - ids(x, y) * Rd
        f[1] = y - Vs - ids(x, y) * Rs
        return f

    Vdi, Vsi = fsolve(F, [0.0, 0.0])
    print(Vdi, Vsi)
    return ids(Vdi, Vsi)

print(bsimbulk(1,0,0.5,0.1))