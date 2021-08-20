from bsimbulk import bsimbulk
import matplotlib.pyplot as plt
import numpy as np
import re

def read_mdl(file):
    mdl = {}
    with open(file,'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        pair = re.findall(r"\w+\s*=\s*[+-]*\d+\.*\d*[Ee]*[+-]*\d*", line)
        for item in pair:
            par, val = re.split(r"\s*=\s*", item)
            mdl[par] = float(val)
    return mdl

def run_test():
    model = read_mdl("modelcard.l")
    biasT = {
        "VD": 1.0,
        "VG": 1.0,
        "VS": 0.0,
        "VB": 0.0,
        "TEMP": -40.0,
        "W": 1e-5,
        "L": 1e-5,
    }
    yy=bsimbulk()
    yy._calc(**model, **biasT, **{"A21":-0.01,"RDSMOD":0})
    print(f"For RDSMOD=0: ids={yy.get_id()}, Rsource={yy.Rsource}, Rdrain={yy.Rdrain}, Rdsi={yy.Rdsi}")
    yy._calc(**{"RDSMOD":1})
    print(f"For RDSMOD=1: ids={yy.get_id()}, Rsource={yy.Rsource}, Rdrain={yy.Rdrain}, Rdsi={yy.Rdsi}")
    yy._calc(**{"RDSMOD":2})
    print(f"For RDSMOD=2: ids={yy.get_id()}, Rsource={yy.Rsource}, Rdrain={yy.Rdrain}, Rdsi={yy.Rdsi}")

    sweep = np.arange(0,1.1,0.001)
    #print(f"{'VG':4}", f"{'ids':15}", f"{'ueff':15}")
    #for x in sweep:
    #    yy.param_update(**{'VG':x})
    #    print(f"{x:.2f}", f"{yy.ids:.9e}", f"{yy.ueff:.9e}")

if __name__ == '__main__':
    run_test()