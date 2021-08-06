from math import *

# Clamped exponential function
def lexp(x):
    if (x > 80.0):
        return 5.540622384e34 * (1.0 + x - 80.0)
    elif (x < -80.0):
        return 1.804851387e-35
    else:
        return exp(x)

# Smoothing def for (max of x, x0 with deltax)
def Smooth(x, x0, deltax):
    return 0.5 * (x + x0 + sqrt((x - x0) * (x - x0) + 0.25 * deltax * deltax))

# Smoothing def for (min of x, x0 with deltax)
def Smooth2(x, x0, deltax):
    return 0.5 * (x + x0 - sqrt((x - x0) * (x - x0) + 0.25 * deltax * deltax)) + 0.25 * deltax

# Clamped log function
def lln(x):
    return log(max(x, 1.0e-38))

# Hyperbolic smoothing function
def hypsmooth(x, c):
    return 0.5 * (x + sqrt(x * x + 4.0 * c * c))

# Junction capacitance macro between S/D and bulk
def JunCap(Czbx, Vbx_jct, PBX_t, MJX, czbx_p1, czbx_p2):
    if (Czbx > 0.0):
        T1 = Vbx_jct / PBX_t
        if (T1 < 0.9):
            arg = 1.0 - T1
            if (MJX == 0.5):
                sarg = 1.0 / sqrt(arg)
            else:
                sarg = lexp(-MJX * lln(arg))
            return PBX_t * Czbx * (1.0 - arg * sarg) / (1.0 - MJX)
        else:
            T2 = czbx_p1 * (T1 - 1.0) * (5.0 * MJX * (T1 - 1.0) + (1.0 + MJX))
            return PBX_t * Czbx * (T2 + czbx_p2)
    else:
        return 0.0

# Normalized pinch-off voltage including PD
def PO_psip(vg_vfb, gamma, DPD):
    T1       = 1.0 + DPD
    vgfbPD   = vg_vfb / T1
    gammaPD  = gamma / T1
    T1       = 0.5 * vgfbPD - 3.0 * (1.0 + gammaPD / 1.41421356237309504880)
    T2       = T1 + sqrt(T1 * T1 + 6.0 * vgfbPD)
    if (vgfbPD < 0.0):
        T3   = (vgfbPD - T2) / gammaPD
        return -lln(1.0 - T2 + T3 * T3)
    else:
        T3   = lexp(-T2)
        T1   = 0.5 * gammaPD
        T2   = sqrt(vgfbPD - 1.0 + T3 + T1 * T1) - T1
        return T2 * T2 + 1.0 - T3

# Normalized charge-voltage relationship
def BSIM_q(psip, phib, vch, gam):
    T8 = 0.5 * (psip + 1.0 + sqrt((psip - 1.0) * (psip - 1.0) + 0.25 * 2.0 * 2.0))
    sqrtpsip = sqrt(T8)
    T9 = 1.0 + gam / (2.0 * sqrtpsip)
    T0 = (1.0 + (gam / (2.0 * sqrtpsip))) / gam
    T1 = psip - 2.0 * phib - vch
    T2 = T1 - lln(4.0 * T0 * sqrtpsip)
    T8 = 0.5 * (T2 - 0.201491 - sqrt(T2 * (T2 + 0.402982) + 2.446562))
    sqrtpsisa = sqrtpsip
    if (T8 <= -68.0):
        T4 = -100.0
        T5 = 20.0
        if (T8 < T4 - 0.5 * T5):
            T3 = lexp(T4)
        else:
            if (T8 > T4 + 0.5 * T5):
                T3 = lexp(T8)
            else:
                T2 = (T8 - T4) / T5
                T6 = T2 * T2
                T3 = lexp(T4 + T5 * ((5.0 / 64.0) + 0.5 * T2 + T6 * ((15.0 / 16.0) - T6 * (1.25 - T6))))
        return T3 * (1.0 + T1 - T8 - lln(2.0 * T0 * (T3 * 2.0 * T0 + 2.0 * sqrtpsisa)))
    else:
        T3 = lexp(T8)
        sqrtpsisainv = 1.0 / sqrtpsisa
        T4 = 2.0 * T3 + lln(T3 * 2.0 * T0 * (T3 *  2.0 * T0 + 2.0 * sqrtpsisa)) - T1
        T5 = 2.0 + (1.0 / T3) + (T0 + sqrtpsisainv) / (T0 * T3 + sqrtpsisa)
        T3 = T3 - T4 / T5
        T4 = 2.0 * T3 + lln(T3 * 2.0 * T0 * (T3 * 2.0 * T0 + 2.0 * sqrtpsisa)) - T1
        T5 = 2.0 + (1.0 / T3) + (T0 + sqrtpsisainv) / (T0 * T3 + sqrtpsisa)
        T6 = ((T0 + sqrtpsisainv) / (T0 * T3 + sqrtpsisa)) * ((T0 + sqrtpsisainv) / (T0 * T3 + sqrtpsisa))
        T7 = -((1.0 / T3) * (1.0 / T3)) - (1.0 / (sqrtpsisa * sqrtpsisa * sqrtpsisa * (T0 * T3 + sqrtpsisa))) - T6
        return T3 - (T4 / T5) * (1.0 + T4 * T7 / (2.0 * T5 * T5))

# Define GEOMOD and RGEOMOD in the modelcard
def BSIMBULKNumFingerDiff(nf, minSD):
    if (nf % 2) != 0:
        nuEndD = 1
        nuIntD = 2 * max((nf - 1) / 2, 0)
        nuEndS = 1
        nuIntS = nuIntD
    else:
        if (minSD == 1):
            nuEndD = 2
            nuIntD = 2 * max((nf / 2 - 1), 0.0)
            nuEndS = 0
            nuIntS = nf
        else:
            nuEndD = 0
            nuIntD = nf
            nuEndS = 2
            nuIntS = 2 * max((nf / 2 - 1), 0)
    return nuEndD, nuIntD, nuEndS, nuIntS

def BSIMBULKRdsEndIso(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEnd, rgeo, SRCFLAG):
    if (SRCFLAG == 1):
        if (rgeo == 1) or (rgeo == 2) or (rgeo == 5):
            if (nuEnd == 0):
                Rend = 0.0
            else:
                Rend = Rsh * DMCG / (Weffcj * nuEnd)
        elif (rgeo == 3) or (rgeo == 4) or (rgeo == 6):
            if ((DMCG + DMCI) == 0.0):
                print("(DMCG + DMCI) can not be equal to zero")
            if (nuEnd == 0):
                Rend = 0.0
            else:
                Rend = Rsh * Weffcj / (3.0 * nuEnd * (DMCG + DMCI))
        else:
            print("Warning: (instance %M) Specified RGEO = %d not matched (BSIMBULKRdsEndIso), Rend is set to zero.", rgeo)
            Rend = 0.0
    else:
        if (rgeo == 1) or (rgeo == 3) or (rgeo == 7):
            if (nuEnd == 0):
                Rend = 0.0
            else:
                Rend = Rsh * DMCG / (Weffcj * nuEnd)
        elif (rgeo == 2) or (rgeo == 4) or (rgeo == 8):
            if ((DMCG + DMCI) == 0.0):
                print("(DMCG + DMCI) can not be equal to zero")
            if (nuEnd == 0):
                Rend = 0.0
            else:
                Rend = Rsh * Weffcj / (3.0 * nuEnd * (DMCG + DMCI))
        else:
            print("Warning: (instance %M) Specified RGEO=%d not matched (BSIMBULKRdsEndIso type 2), Rend is set to zero.", rgeo)
            Rend = 0.0
    return Rend

def BSIMBULKRdsEndSha(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEnd, rgeo, SRCFLAG):
    if (SRCFLAG == 1):
        if (rgeo == 1) or (rgeo == 2) or (rgeo == 5):
            if (nuEnd == 0):
                Rend = 0.0
            else:
                Rend = Rsh * DMCG / (Weffcj * nuEnd)
        elif (rgeo == 3) or (rgeo == 4) or (rgeo == 6):
            if (DMCG == 0.0):
                print("DMCG can not be equal to zero")
            if (nuEnd == 0):
                Rend = 0.0
            else:
                Rend = Rsh * Weffcj / (6.0 * nuEnd * DMCG)
        else:
            print("Warning: (instance %M) Specified RGEO = %d not matched (BSIMBULKRdsEndSha), Rend is set to zero.", rgeo)
            Rend = 0.0
    else:
        if (rgeo == 1) or (rgeo == 3) or (rgeo == 7):
            if (nuEnd == 0):
                Rend = 0.0
            else:
                Rend = Rsh * DMCG / (Weffcj * nuEnd)
        elif (rgeo == 2) or (rgeo == 4) or (rgeo == 8):
            if (DMCG == 0.0):
                print("DMCG can not be equal to zero")
            if (nuEnd == 0):
                Rend = 0.0
            else:
                Rend = Rsh * Weffcj / (6.0 * nuEnd * DMCG)
        else:
            print("Warning: (instance %M) Specified RGEO=%d not matched (BSIMBULKRdsEndSha type 2), Rend is set to zero.", rgeo)
            Rend = 0.0
    return Rend

def BSIMBULKRdseffGeo(nf, geo, rgeo, minSD, Weffcj, Rsh, DMCG, DMCI, DMDG, SRCFLAG):
    if (geo < 9):
        nuEndD, nuIntD, nuEndS, nuIntS = BSIMBULKNumFingerDiff(nf, minSD)
        if (SRCFLAG == 1):
            if (nuIntS == 0):
                Rint = 0.0
            else:
                Rint = Rsh * DMCG / ( Weffcj * nuIntS)
        else:
            if (nuIntD == 0):
                Rint = 0.0
            else:
                Rint = Rsh * DMCG / ( Weffcj * nuIntD)
    if (geo == 0):
        if (SRCFLAG == 1):
            Rend = BSIMBULKRdsEndIso(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndS, rgeo, 1)
        else:
            Rend = BSIMBULKRdsEndIso(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndD, rgeo, 0)
    elif (geo == 1):
        if (SRCFLAG == 1):
            Rend = BSIMBULKRdsEndIso(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndS, rgeo, 1)
        else:
            Rend = BSIMBULKRdsEndSha(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndD, rgeo, 0)
    elif (geo == 2):
        if (SRCFLAG == 1):
            Rend = BSIMBULKRdsEndSha(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndS, rgeo, 1)
        else:
            Rend = BSIMBULKRdsEndIso(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndD, rgeo, 0)
    elif (geo == 3):
        if (SRCFLAG == 1):
            Rend = BSIMBULKRdsEndSha(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndS, rgeo, 1)
        else:
            Rend = BSIMBULKRdsEndSha(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndD, rgeo, 0)
    elif (geo == 4):
        if (SRCFLAG == 1):
            Rend = BSIMBULKRdsEndIso(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndS, rgeo, 1)
        else:
            Rend = Rsh * DMDG / Weffcj
    elif (geo == 5):
        if (SRCFLAG == 1):
            Rend = BSIMBULKRdsEndSha(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndS, rgeo, 1)
        else:
            if (nuEndD == 0):
                Rend = 0.0
            else:
                Rend = Rsh * DMDG / (Weffcj * nuEndD)
    elif (geo == 6):
        if (SRCFLAG == 1):
            Rend = Rsh * DMDG / Weffcj
        else:
            Rend = BSIMBULKRdsEndIso(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndD, rgeo, 0)
    elif (geo == 7):
        if (SRCFLAG == 1):
            if (nuEndS == 0):
                Rend = 0.0
            else:
                Rend = Rsh * DMDG / (Weffcj * nuEndS)
        else:
            Rend = BSIMBULKRdsEndSha(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndD, rgeo, 0)
    elif (geo == 8):
        Rend = Rsh * DMDG / Weffcj
    elif (geo == 9):        # all wide contacts assumed for geo = 9 and 10
        if (SRCFLAG == 1):
            Rend = 0.5 * Rsh * DMCG / Weffcj
            if (nf == 2):
                Rint = 0.0
            else:
                Rint = Rsh * DMCG / (Weffcj * (nf - 2.0))
        else:
            Rend = 0.0
            Rint = Rsh * DMCG / (Weffcj * nf)
    elif (geo == 10):
        if (SRCFLAG == 1):
            Rend = 0.0
            Rint = Rsh * DMCG / (Weffcj * nf)
        else:
            Rend = 0.5 * Rsh * DMCG / Weffcj
            if (nf == 2):
                Rint = 0.0
            else:
                Rint = Rsh * DMCG / (Weffcj * (nf - 2.0))
    else:
        print("Warning: (instance %M) Specified GEO=%d not matched (BSIMBULKRdseffGeo), Rint is set to zero.", geo)
        Rint = 0.0
    if (Rint <= 0.0):
        Rtot = Rend
    elif (Rend <= 0.0):
        Rtot = Rint
    else:
        Rtot = Rint * Rend / (Rint + Rend)
    if (Rtot == 0.0):
        print("Warning: (instance %M) Zero resistance returned from RdseffGeo")
    return Rtot

# Effective PS, PD, AS, AD calculation, Ref: BSIM4
def BSIMBULKPAeffGeo(nf, geo, minSD, Weffcj, DMCG, DMCI, DMDG):
    if (geo < 9):
        nuEndD, nuIntD, nuEndS, nuIntS = BSIMBULKNumFingerDiff(nf, minSD)
        T0 = DMCG + DMCI
        T1 = DMCG + DMCG
        T2 = DMDG + DMDG
        PSiso = T0 + T0 + Weffcj
        PDiso = T0 + T0 + Weffcj
        PSsha = T1
        PDsha = T1
        PSmer = T2
        PDmer = T2
        ASiso = T0 * Weffcj
        ADiso = T0 * Weffcj
        ASsha = DMCG * Weffcj
        ADsha = DMCG * Weffcj
        ASmer = DMDG * Weffcj
        ADmer = DMDG * Weffcj
    if (geo == 0):
        Ps = nuEndS * PSiso + nuIntS * PSsha
        Pd = nuEndD * PDiso + nuIntD * PDsha
        As = nuEndS * ASiso + nuIntS * ASsha
        Ad = nuEndD * ADiso + nuIntD * ADsha
    elif (geo == 1):
        Ps = nuEndS * PSiso + nuIntS * PSsha
        Pd = (nuEndD + nuIntD) * PDsha
        As = nuEndS * ASiso + nuIntS * ASsha
        Ad = (nuEndD + nuIntD) * ADsha
    elif (geo == 2):
        Ps = (nuEndS + nuIntS) * PSsha
        Pd = nuEndD * PDiso + nuIntD * PDsha
        As = (nuEndS + nuIntS) * ASsha
        Ad = nuEndD * ADiso + nuIntD * ADsha
    elif (geo == 3):
        Ps = (nuEndS + nuIntS) * PSsha
        Pd = (nuEndD + nuIntD) * PDsha
        As = (nuEndS + nuIntS) * ASsha
        Ad = (nuEndD + nuIntD) * ADsha
    elif (geo == 4):
        Ps = nuEndS * PSiso + nuIntS * PSsha
        Pd = nuEndD * PDmer + nuIntD * PDsha
        As = nuEndS * ASiso + nuIntS * ASsha
        Ad = nuEndD * ADmer + nuIntD * ADsha
    elif (geo == 5):
        Ps = (nuEndS + nuIntS) * PSsha
        Pd = nuEndD * PDmer + nuIntD * PDsha
        As = (nuEndS + nuIntS) * ASsha
        Ad = nuEndD * ADmer + nuIntD * ADsha
    elif (geo == 6):
        Ps = nuEndS * PSmer + nuIntS * PSsha
        Pd = nuEndD * PDiso + nuIntD * PDsha
        As = nuEndS * ASmer + nuIntS * ASsha
        Ad = nuEndD * ADiso + nuIntD * ADsha
    elif (geo == 7):
        Ps = nuEndS * PSmer + nuIntS * PSsha
        Pd = (nuEndD + nuIntD) * PDsha
        As = nuEndS * ASmer + nuIntS * ASsha
        Ad = (nuEndD + nuIntD) * ADsha
    elif (geo == 8):
        Ps = nuEndS * PSmer + nuIntS * PSsha
        Pd = nuEndD * PDmer + nuIntD * PDsha
        As = nuEndS * ASmer + nuIntS * ASsha
        Ad = nuEndD * ADmer + nuIntD * ADsha
    elif (geo == 9):
        Ps = PSiso + (nf - 1.0) * PSsha
        Pd = nf * PDsha
        As = ASiso + (nf - 1.0) * ASsha
        Ad = nf * ADsha
    elif (geo == 10):
        Ps = nf * PSsha
        Pd = PDiso + (nf - 1.0) * PDsha
        As = nf * ASsha
        Ad = ADiso + (nf - 1.0) * ADsha
    else:
        print("Warning: (instance %M) Specified GEO=%d not matched (BSIMBULKPAeffGeo), PS,PD,AS,AD set to zero.", geo)
        Ps = 0
        Pd = 0
        As = 0
        Ad = 0
    return Ps, Pd, As, Ad

def bsimbulk():
    param = {
        "L": 1e-6,
        "TOXP": 1e-9,
        "Temp": 125.0,
        "Vg": 0.0
    }
    ntype = 1
    ptype = -1
    q = 1.60219e-19
    EPS0 = 8.85418e-12
    KboQ = 8.617087e-5      # Joule/degree
    P_CELSIUS0 = 273.15
    Oneby3 = 0.33333333333333333
    DELTA_1 = 0.02
    REFTEMP = 300.15       # 27 degrees C
    EXPL_THRESHOLD = 80.0
    MAX_EXPL = 5.540622384e34
    M_PI = 3.14159265358979323846

    # Bias and temperature
    Vd = param.get("Vd", 1.0)
    Vg = param.get("Vg", 1.0)
    Vs = param.get("Vs", 0.0)
    Vb = param.get("Vb", 0.0)
    Temp = param.get("Temp", 25.0)

    # Pure instance parameters
    L = param.get("L", 1.0e-5)
    W = param.get("W", 1.0e-5)
    NF = param.get("NF", 1)
    NRS = param.get("NRS", 1.0)
    NRD = param.get("NRD", 1.0)
    VFBSDOFF = param.get("VFBSDOFF", 0.0)
    MINZ = param.get("MINZ", 0)
    RGATEMOD = param.get("RGATEMOD", 0)
    RBODYMOD = param.get("RBODYMOD", 0)
    GEOMOD = param.get("GEOMOD", 0)
    RGEOMOD = param.get("RGEOMOD", 0)
    RBPB = param.get("RBPB", 50.0)
    RBPD = param.get("RBPD", 50.0)
    RBPS = param.get("RBPS", 50.0)
    RBDB = param.get("RBDB", 50.0)
    RBSB = param.get("RBSB", 50.0)
    SA = param.get("SA", 0.0)
    SB = param.get("SB", 0.0)
    SD = param.get("SD", 0.0)
    SCA = param.get("SCA", 0.0)
    SCB = param.get("SCB", 0.0)
    SCC = param.get("SCC", 0.0)
    SC = param.get("SC", 0.0)
    AS = param.get("AS", 0.0)
    AD = param.get("AD", 0.0)
    PS = param.get("PS", 0.0)
    PD = param.get("PD", 0.0)

    # Both model and instance parameters
    XGW = param.get("XGW", 0.0)
    NGCON = param.get("NGCON", 1)
    DTEMP = param.get("DTEMP", 0.0)
    MULU0 = param.get("MULU0", 1.0)
    DELVTO = param.get("DELVTO", 0.0)
    IDS0MULT = param.get("IDS0MULT", 1.0)
    EDGEFET = param.get("EDGEFET", 0)
    SSLMOD = param.get("SSLMOD", 0)

    # Pure model parameters
    TYPE = param.get("TYPE", ntype)
    CVMOD = param.get("CVMOD", 0)
    COVMOD = param.get("COVMOD", 0)
    RDSMOD = param.get("RDSMOD", 0)
    WPEMOD = param.get("WPEMOD", 0)
    ASYMMOD = param.get("ASYMMOD", 0)
    GIDLMOD = param.get("GIDLMOD", 0)
    IGCMOD = param.get("IGCMOD", 0)
    IGBMOD = param.get("IGBMOD", 0)
    TNOIMOD = param.get("TNOIMOD", 0)
    SHMOD = param.get("SHMOD", 0)
    MOBSCALE = param.get("MOBSCALE", 0)

    # Device parameters
    LLONG = param.get("LLONG", 1.0e-5)
    LMLT = param.get("LMLT", 1.0)
    WMLT = param.get("WMLT", 1.0)
    XL = param.get("XL", 0.0)
    WWIDE = param.get("WWIDE", 1.0e-5)
    XW = param.get("XW", 0.0)
    LINT = param.get("LINT", 0.0)
    LL = param.get("LL", 0.0)
    LW = param.get("LW", 0.0)
    LWL = param.get("LWL", 0.0)
    LLN = param.get("LLN", 1.0)
    LWN = param.get("LWN", 1.0)
    WINT = param.get("WINT", 0.0)
    WL = param.get("WL", 0.0)
    WW = param.get("WW", 0.0)
    WWL = param.get("WWL", 0.0)
    WLN = param.get("WLN", 1.0)
    WWN = param.get("WWN", 1.0)
    DLC = param.get("DLC", 0.0)
    LLC = param.get("LLC", 0.0)
    LWC = param.get("LWC", 0.0)
    LWLC = param.get("LWLC", 0.0)
    DWC = param.get("DWC", 0.0)
    WLC = param.get("WLC", 0.0)
    WWC = param.get("WWC", 0.0)
    WWLC = param.get("WWLC", 0.0)
    TOXE = param.get("TOXE", 3.0e-9)
    TOXP = param.get("TOXP", TOXE)
    DTOX = param.get("DTOX", 0.0)
    NDEP = param.get("NDEP", 1e24)
    NDEPL1 = param.get("NDEPL1", 0.0)
    NDEPLEXP1 = param.get("NDEPLEXP1", 1.0)
    NDEPL2 = param.get("NDEPL2", 0.0)
    NDEPLEXP2 = param.get("NDEPLEXP2", 2.0)
    NDEPW = param.get("NDEPW", 0.0)
    NDEPWEXP = param.get("NDEPWEXP", 1.0)
    NDEPWL = param.get("NDEPWL", 0.0)
    NDEPWLEXP = param.get("NDEPWLEXP", 1.0)
    LNDEP = param.get("LNDEP", 0.0)
    WNDEP = param.get("WNDEP", 0.0)
    PNDEP = param.get("PNDEP", 0.0)
    NDEPCV = param.get("NDEPCV", 1e24)
    NDEPCVL1 = param.get("NDEPCVL1", 0.0)
    NDEPCVLEXP1 = param.get("NDEPCVLEXP1", 1.0)
    NDEPCVL2 = param.get("NDEPCVL2", 0.0)
    NDEPCVLEXP2 = param.get("NDEPCVLEXP2", 2.0)
    NDEPCVW = param.get("NDEPCVW", 0.0)
    NDEPCVWEXP = param.get("NDEPCVWEXP", 1.0)
    NDEPCVWL = param.get("NDEPCVWL", 0.0)
    NDEPCVWLEXP = param.get("NDEPCVWLEXP", 1.0)
    LNDEPCV = param.get("LNDEPCV", 0.0)
    WNDEPCV = param.get("WNDEPCV", 0.0)
    PNDEPCV = param.get("PNDEPCV", 0.0)
    NGATE = param.get("NGATE", 5e25)
    LNGATE = param.get("LNGATE", 0.0)
    WNGATE = param.get("WNGATE", 0.0)
    PNGATE = param.get("PNGATE", 0.0)
    EASUB = param.get("EASUB", 4.05)
    NI0SUB = param.get("NI0SUB", 1.1e16)
    BG0SUB = param.get("BG0SUB", 1.17)
    EPSRSUB = param.get("EPSRSUB", 11.9)
    EPSROX = param.get("EPSROX", 3.9)
    XJ = param.get("XJ", 1.5e-7)
    LXJ = param.get("LXJ", 0.0)
    WXJ = param.get("WXJ", 0.0)
    PXJ = param.get("PXJ", 0.0)
    VFB = param.get("VFB", -0.5)
    LVFB = param.get("LVFB", 0.0)
    WVFB = param.get("WVFB", 0.0)
    PVFB = param.get("PVFB", 0.0)
    VFBCV = param.get("VFBCV", -0.5)
    LVFBCV = param.get("LVFBCV", 0.0)
    WVFBCV = param.get("WVFBCV", 0.0)
    PVFBCV = param.get("PVFBCV", 0.0)
    VFBCVL = param.get("VFBCVL", 0.0)
    VFBCVLEXP = param.get("VFBCVLEXP", 1.0)
    VFBCVW = param.get("VFBCVW", 0.0)
    VFBCVWEXP = param.get("VFBCVWEXP", 1.0)
    VFBCVWL = param.get("VFBCVWL", 0.0)
    VFBCVWLEXP = param.get("VFBCVWLEXP", 1.0)
    DELVFBACC = param.get("DELVFBACC", 0.0)

    # Diode parameters
    PERMOD = param.get("PERMOD", 1)
    DWJ = param.get("DWJ", DWC)

    # Short channel effects
    NSD = param.get("NSD", 1e26)
    LNSD = param.get("LNSD", 0.0)
    WNSD = param.get("WNSD", 0.0)
    PNSD = param.get("PNSD", 0.0)
    DVTP0 = param.get("DVTP0", 0.0)
    LDVTP0 = param.get("LDVTP0", 0)
    WDVTP0 = param.get("WDVTP0", 0)
    PDVTP0 = param.get("PDVTP0", 0)
    DVTP1 = param.get("DVTP1", 0.0)
    LDVTP1 = param.get("LDVTP1", 0)
    WDVTP1 = param.get("WDVTP1", 0)
    PDVTP1 = param.get("PDVTP1", 0)
    DVTP2 = param.get("DVTP2", 0.0)
    LDVTP2 = param.get("LDVTP2", 0)
    WDVTP2 = param.get("WDVTP2", 0)
    PDVTP2 = param.get("PDVTP2", 0)
    DVTP3 = param.get("DVTP3", 0.0)
    LDVTP3 = param.get("LDVTP3", 0)
    WDVTP3 = param.get("WDVTP3", 0)
    PDVTP3 = param.get("PDVTP3", 0)
    DVTP4 = param.get("DVTP4", 0.0)
    LDVTP4 = param.get("LDVTP4", 0)
    WDVTP4 = param.get("WDVTP4", 0)
    PDVTP4 = param.get("PDVTP4", 0)
    DVTP5 = param.get("DVTP5", 0.0)
    LDVTP5 = param.get("LDVTP5", 0)
    WDVTP5 = param.get("WDVTP5", 0)
    PDVTP5 = param.get("PDVTP5", 0)
    PHIN = param.get("PHIN", 0.045)
    LPHIN = param.get("LPHIN", 0.0)
    WPHIN = param.get("WPHIN", 0.0)
    PPHIN = param.get("PPHIN", 0.0)
    ETA0 = param.get("ETA0", 0.08)
    LETA0 = param.get("LETA0", 0.0)
    WETA0 = param.get("WETA0", 0.0)
    PETA0 = param.get("PETA0", 0.0)
    ETA0R = param.get("ETA0R", ETA0)
    LETA0R = param.get("LETA0R", LETA0)
    WETA0R = param.get("WETA0R", WETA0)
    PETA0R = param.get("PETA0R", PETA0)
    DSUB = param.get("DSUB", 1.0)
    ETAB = param.get("ETAB", -0.07)
    ETABEXP = param.get("ETABEXP", 1.0)
    LETAB = param.get("LETAB", 0.0)
    WETAB = param.get("WETAB", 0.0)
    PETAB = param.get("PETAB", 0.0)
    K1 = param.get("K1", 0.0)
    K1L = param.get("K1L", 0.0)
    K1LEXP = param.get("K1LEXP", 1.0)
    K1W = param.get("K1W", 0.0)
    K1WEXP = param.get("K1WEXP", 1.0)
    K1WL = param.get("K1WL", 0.0)
    K1WLEXP = param.get("K1WLEXP", 1.0)
    LK1 = param.get("LK1", 0.0)
    WK1 = param.get("WK1", 0.0)
    PK1 = param.get("PK1", 0.0)
    K2 = param.get("K2", 0.0)
    K2L = param.get("K2L", 0.0)
    K2LEXP = param.get("K2LEXP", 1.0)
    K2W = param.get("K2W", 0.0)
    K2WEXP = param.get("K2WEXP", 1.0)
    K2WL = param.get("K2WL", 0.0)
    K2WLEXP = param.get("K2WLEXP", 1.0)
    LK2 = param.get("LK2", 0.0)
    WK2 = param.get("WK2", 0.0)
    PK2 = param.get("PK2", 0.0)

    # Quantum mechanical effects
    ADOS = param.get("ADOS", 0.0)
    BDOS = param.get("BDOS", 1.0)
    QM0 = param.get("QM0", 1.0e-3)
    ETAQM = param.get("ETAQM", 0.54)

    # Sub-threshold swing factor
    CIT = param.get("CIT", 0.0)
    LCIT = param.get("LCIT", 0.0)
    WCIT = param.get("WCIT", 0.0)
    PCIT = param.get("PCIT", 0.0)
    NFACTOR = param.get("NFACTOR", 0.0)
    NFACTORL = param.get("NFACTORL", 0.0)
    NFACTORLEXP = param.get("NFACTORLEXP", 1.0)
    NFACTORW = param.get("NFACTORW", 0.0)
    NFACTORWEXP = param.get("NFACTORWEXP", 1.0)
    NFACTORWL = param.get("NFACTORWL", 0.0)
    NFACTORWLEXP = param.get("NFACTORWLEXP", 1.0)
    LNFACTOR = param.get("LNFACTOR", 0.0)
    WNFACTOR = param.get("WNFACTOR", 0.0)
    PNFACTOR = param.get("PNFACTOR", 0.0)
    CDSCD = param.get("CDSCD", 1e-9)
    CDSCDL = param.get("CDSCDL", 0.0)
    CDSCDLEXP = param.get("CDSCDLEXP", 1.0)
    LCDSCD = param.get("LCDSCD", 0.0)
    WCDSCD = param.get("WCDSCD", 0.0)
    PCDSCD = param.get("PCDSCD", 0.0)
    CDSCDR = param.get("CDSCDR", CDSCD)
    CDSCDLR = param.get("CDSCDLR", CDSCDL)
    LCDSCDR = param.get("LCDSCDR", LCDSCD)
    WCDSCDR = param.get("WCDSCDR", WCDSCD)
    PCDSCDR = param.get("PCDSCDR", PCDSCD)
    CDSCB = param.get("CDSCB", 0.0)
    CDSCBL = param.get("CDSCBL", 0.0)
    CDSCBLEXP = param.get("CDSCBLEXP", 1.0)
    LCDSCB = param.get("LCDSCB", 0.0)
    WCDSCB = param.get("WCDSCB", 0.0)
    PCDSCB = param.get("PCDSCB", 0.0)

    # Drain saturation voltage
    VSAT = param.get("VSAT", 1e5)
    LVSAT = param.get("LVSAT", 0.0)
    WVSAT = param.get("WVSAT", 0.0)
    PVSAT = param.get("PVSAT", 0.0)
    VSATL = param.get("VSATL", 0.0)
    VSATLEXP = param.get("VSATLEXP", 1.0)
    VSATW = param.get("VSATW", 0.0)
    VSATWEXP = param.get("VSATWEXP", 1.0)
    VSATWL = param.get("VSATWL", 0.0)
    VSATWLEXP = param.get("VSATWLEXP", 1.0)
    VSATR = param.get("VSATR", VSAT)
    LVSATR = param.get("LVSATR", LVSAT)
    WVSATR = param.get("WVSATR", WVSAT)
    PVSATR = param.get("PVSATR", PVSAT)
    DELTA = param.get("DELTA", 0.125)
    LDELTA = param.get("LDELTA", 0.0)
    WDELTA = param.get("WDELTA", 0.0)
    PDELTA = param.get("PDELTA", 0.0)
    DELTAL = param.get("DELTAL", 0.0)
    DELTALEXP = param.get("DELTALEXP", 1.0)
    VSATCV = param.get("VSATCV", 1e5)
    LVSATCV = param.get("LVSATCV", 0.0)
    WVSATCV = param.get("WVSATCV", 0.0)
    PVSATCV = param.get("PVSATCV", 0.0)
    VSATCVL = param.get("VSATCVL", 0.0)
    VSATCVLEXP = param.get("VSATCVLEXP", 1.0)
    VSATCVW = param.get("VSATCVW", 0.0)
    VSATCVWEXP = param.get("VSATCVWEXP", 1.0)
    VSATCVWL = param.get("VSATCVWL", 0.0)
    VSATCVWLEXP = param.get("VSATCVWLEXP", 1.0)

    # Mobility degradation
    UP1 = param.get("UP1", 0.0)
    LP1 = param.get("LP1", 1.0e-8)
    UP2 = param.get("UP2", 0.0)
    LP2 = param.get("LP2", 1.0e-8)
    U0 = param.get("U0", 67.0e-3)
    U0L = param.get("U0L", 0.0)
    U0LEXP = param.get("U0LEXP", 1.0)
    LU0 = param.get("LU0", 0.0)
    WU0 = param.get("WU0", 0.0)
    PU0 = param.get("PU0", 0.0)
    U0R = param.get("U0R", U0)
    LU0R = param.get("LU0R", LU0)
    WU0R = param.get("WU0R", WU0)
    PU0R = param.get("PU0R", PU0)
    ETAMOB = param.get("ETAMOB", 1.0)
    UA = param.get("UA", 0.001)
    UAL = param.get("UAL", 0.0)
    UALEXP = param.get("UALEXP", 1.0)
    UAW = param.get("UAW", 0.0)
    UAWEXP = param.get("UAWEXP", 1.0)
    UAWL = param.get("UAWL", 0.0)
    UAWLEXP = param.get("UAWLEXP", 1.0)
    LUA = param.get("LUA", 0.0)
    WUA = param.get("WUA", 0.0)
    PUA = param.get("PUA", 0.0)
    UAR = param.get("UAR", UA)
    LUAR = param.get("LUAR", LUA)
    WUAR = param.get("WUAR", WUA)
    PUAR = param.get("PUAR", PUA)
    EU = param.get("EU", 1.5)
    LEU = param.get("LEU", 0.0)
    WEU = param.get("WEU", 0.0)
    PEU = param.get("PEU", 0.0)
    EUL = param.get("EUL", 0.0)
    EULEXP = param.get("EULEXP", 1.0)
    EUW = param.get("EUW", 0.0)
    EUWEXP = param.get("EUWEXP", 1.0)
    EUWL = param.get("EUWL", 0.0)
    EUWLEXP = param.get("EUWLEXP", 1.0)
    UD = param.get("UD", 0.001)
    UDL = param.get("UDL", 0.0)
    UDLEXP = param.get("UDLEXP", 1.0)
    LUD = param.get("LUD", 0.0)
    WUD = param.get("WUD", 0.0)
    PUD = param.get("PUD", 0.0)
    UDR = param.get("UDR", UD)
    LUDR = param.get("LUDR", LUD)
    WUDR = param.get("WUDR", WUD)
    PUDR = param.get("PUDR", PUD)
    UCS = param.get("UCS", 2.0)
    LUCS = param.get("LUCS", 0.0)
    WUCS = param.get("WUCS", 0.0)
    PUCS = param.get("PUCS", 0.0)
    UCSR = param.get("UCSR", UCS)
    LUCSR = param.get("LUCSR", LUCS)
    WUCSR = param.get("WUCSR", WUCS)
    PUCSR = param.get("PUCSR", PUCS)
    UC = param.get("UC", 0.0)
    UCL = param.get("UCL", 0.0)
    UCLEXP = param.get("UCLEXP", 1.0)
    UCW = param.get("UCW", 0.0)
    UCWEXP = param.get("UCWEXP", 1.0)
    UCWL = param.get("UCWL", 0.0)
    UCWLEXP = param.get("UCWLEXP", 1.0)
    LUC = param.get("LUC", 0.0)
    WUC = param.get("WUC", 0.0)
    PUC = param.get("PUC", 0.0)
    UCR = param.get("UCR", UC)
    LUCR = param.get("LUCR", LUC)
    WUCR = param.get("WUCR", WUC)
    PUCR = param.get("PUCR", PUC)

    # Channel length modulation
    PCLM = param.get("PCLM", 0.0)
    PCLML = param.get("PCLML", 0.0)
    PCLMLEXP = param.get("PCLMLEXP", 1.0)
    LPCLM = param.get("LPCLM", 0.0)
    WPCLM = param.get("WPCLM", 0.0)
    PPCLM = param.get("PPCLM", 0.0)
    PCLMR = param.get("PCLMR", PCLM)
    LPCLMR = param.get("LPCLMR", LPCLM)
    WPCLMR = param.get("WPCLMR", WPCLM)
    PPCLMR = param.get("PPCLMR", PPCLM)
    PCLMG = param.get("PCLMG", 0.0)
    PCLMCV = param.get("PCLMCV", PCLM)
    PCLMCVL = param.get("PCLMCVL", PCLML)
    PCLMCVLEXP = param.get("PCLMCVLEXP", PCLMLEXP)
    LPCLMCV = param.get("LPCLMCV", LPCLM)
    WPCLMCV = param.get("WPCLMCV", WPCLM)
    PPCLMCV = param.get("PPCLMCV", PPCLM)
    PSCBE1 = param.get("PSCBE1", 4.24e8)
    LPSCBE1 = param.get("LPSCBE1", 0.0)
    WPSCBE1 = param.get("WPSCBE1", 0.0)
    PPSCBE1 = param.get("PPSCBE1", 0.0)
    PSCBE2 = param.get("PSCBE2", 1.0e-8)
    LPSCBE2 = param.get("LPSCBE2", 0.0)
    WPSCBE2 = param.get("WPSCBE2", 0.0)
    PPSCBE2 = param.get("PPSCBE2", 0.0)
    PDITS = param.get("PDITS", 0.0)
    LPDITS = param.get("LPDITS", 0.0)
    WPDITS = param.get("WPDITS", 0.0)
    PPDITS = param.get("PPDITS", 0.0)
    PDITSL = param.get("PDITSL", 0.0)
    PDITSD = param.get("PDITSD", 0.0)
    LPDITSD = param.get("LPDITSD", 0.0)
    WPDITSD = param.get("WPDITSD", 0.0)
    PPDITSD = param.get("PPDITSD", 0.0)

    # S/D series resistances
    RSH = param.get("RSH", 0.0)
    PRWG = param.get("PRWG", 1.0)
    LPRWG = param.get("LPRWG", 0.0)
    WPRWG = param.get("WPRWG", 0.0)
    PPRWG = param.get("PPRWG", 0.0)
    PRWB = param.get("PRWB", 0.0)
    LPRWB = param.get("LPRWB", 0.0)
    WPRWB = param.get("WPRWB", 0.0)
    PPRWB = param.get("PPRWB", 0.0)
    PRWBL = param.get("PRWBL", 0.0)
    PRWBLEXP = param.get("PRWBLEXP", 1.0)
    WR = param.get("WR", 1.0)
    LWR = param.get("LWR", 0.0)
    WWR = param.get("WWR", 0.0)
    PWR = param.get("PWR", 0.0)
    RSWMIN = param.get("RSWMIN", 0.0)
    LRSWMIN = param.get("LRSWMIN", 0.0)
    WRSWMIN = param.get("WRSWMIN", 0.0)
    PRSWMIN = param.get("PRSWMIN", 0.0)
    RSW = param.get("RSW", 10.0)
    LRSW = param.get("LRSW", 0.0)
    WRSW = param.get("WRSW", 0.0)
    PRSW = param.get("PRSW", 0.0)
    RSWL = param.get("RSWL", 0.0)
    RSWLEXP = param.get("RSWLEXP", 1.0)
    RDWMIN = param.get("RDWMIN", RSWMIN)
    LRDWMIN = param.get("LRDWMIN", LRSWMIN)
    WRDWMIN = param.get("WRDWMIN", WRSWMIN)
    PRDWMIN = param.get("PRDWMIN", PRSWMIN)
    RDW = param.get("RDW", RSW)
    LRDW = param.get("LRDW", LRSW)
    WRDW = param.get("WRDW", WRSW)
    PRDW = param.get("PRDW", PRSW)
    RDWL = param.get("RDWL", RSWL)
    RDWLEXP = param.get("RDWLEXP", RSWLEXP)
    RDSWMIN = param.get("RDSWMIN", 0.0)
    LRDSWMIN = param.get("LRDSWMIN", 0.0)
    WRDSWMIN = param.get("WRDSWMIN", 0.0)
    PRDSWMIN = param.get("PRDSWMIN", 0.0)
    RDSW = param.get("RDSW", 20.0)
    RDSWL = param.get("RDSWL", 0.0)
    RDSWLEXP = param.get("RDSWLEXP", 1.0)
    LRDSW = param.get("LRDSW", 0.0)
    WRDSW = param.get("WRDSW", 0.0)
    PRDSW = param.get("PRDSW", 0.0)

    # Velocity saturation
    PSAT = param.get("PSAT", 1.0)
    LPSAT = param.get("LPSAT", 0.0)
    WPSAT = param.get("WPSAT", 0.0)
    PPSAT = param.get("PPSAT", 0.0)
    PSATL = param.get("PSATL", 0.0)
    PSATLEXP = param.get("PSATLEXP", 1.0)
    PSATB = param.get("PSATB", 0.0)
    PSATR = param.get("PSATR", PSAT)
    LPSATR = param.get("LPSATR", LPSAT)
    WPSATR = param.get("WPSATR", WPSAT)
    PPSATR = param.get("PPSATR", PPSAT)
    LPSATB = param.get("LPSATB", 0.0)
    WPSATB = param.get("WPSATB", 0.0)
    PPSATB = param.get("PPSATB", 0.0)
    PSATX = param.get("PSATX", 1.0)
    PTWG = param.get("PTWG", 0.0)
    LPTWG = param.get("LPTWG", 0.0)
    WPTWG = param.get("WPTWG", 0.0)
    PPTWG = param.get("PPTWG", 0.0)
    PTWGL = param.get("PTWGL", 0.0)
    PTWGLEXP = param.get("PTWGLEXP", 1.0)
    PTWGR = param.get("PTWGR", PTWG)
    LPTWGR = param.get("LPTWGR", LPTWG)
    WPTWGR = param.get("WPTWGR", WPTWG)
    PPTWGR = param.get("PPTWGR", PPTWG)
    PTWGLR = param.get("PTWGLR", PTWGL)
    PTWGLEXPR = param.get("PTWGLEXPR", PTWGLEXP)

    # Velocity non-saturation effect
    A1 = param.get("A1", 0.0)
    LA1 = param.get("LA1", 0.0)
    WA1 = param.get("WA1", 0.0)
    PA1 = param.get("PA1", 0.0)
    A11 = param.get("A11", 0.0)
    LA11 = param.get("LA11", 0.0)
    WA11 = param.get("WA11", 0.0)
    PA11 = param.get("PA11", 0.0)
    A2 = param.get("A2", 0.0)
    LA2 = param.get("LA2", 0.0)
    WA2 = param.get("WA2", 0.0)
    PA2 = param.get("PA2", 0.0)
    A21 = param.get("A21", 0.0)
    LA21 = param.get("LA21", 0.0)
    WA21 = param.get("WA21", 0.0)
    PA21 = param.get("PA21", 0.0)

    # Output conductance
    PDIBLC = param.get("PDIBLC", 0.0)
    PDIBLCL = param.get("PDIBLCL", 0.0)
    PDIBLCLEXP = param.get("PDIBLCLEXP", 1.0)
    LPDIBLC = param.get("LPDIBLC", 0.0)
    WPDIBLC = param.get("WPDIBLC", 0.0)
    PPDIBLC = param.get("PPDIBLC", 0.0)
    PDIBLCR = param.get("PDIBLCR", PDIBLC)
    PDIBLCLR = param.get("PDIBLCLR", PDIBLCL)
    PDIBLCLEXPR = param.get("PDIBLCLEXPR", PDIBLCLEXP)
    LPDIBLCR = param.get("LPDIBLCR", LPDIBLC)
    WPDIBLCR = param.get("WPDIBLCR", WPDIBLC)
    PPDIBLCR = param.get("PPDIBLCR", PPDIBLC)
    PDIBLCB = param.get("PDIBLCB", 0.0)
    LPDIBLCB = param.get("LPDIBLCB", 0.0)
    WPDIBLCB = param.get("WPDIBLCB", 0.0)
    PPDIBLCB = param.get("PPDIBLCB", 0.0)
    PVAG = param.get("PVAG", 1.0)
    LPVAG = param.get("LPVAG", 0.0)
    WPVAG = param.get("WPVAG", 0.0)
    PPVAG = param.get("PPVAG", 0.0)
    FPROUT = param.get("FPROUT", 0.0)
    FPROUTL = param.get("FPROUTL", 0.0)
    FPROUTLEXP = param.get("FPROUTLEXP", 1.0)
    LFPROUT = param.get("LFPROUT", 0.0)
    WFPROUT = param.get("WFPROUT", 0.0)
    PFPROUT = param.get("PFPROUT", 0.0)

    # Impact ionization current
    ALPHA0 = param.get("ALPHA0", 0.0)
    ALPHA0L = param.get("ALPHA0L", 0.0)
    ALPHA0LEXP = param.get("ALPHA0LEXP", 1.0)
    LALPHA0 = param.get("LALPHA0", 0.0)
    WALPHA0 = param.get("WALPHA0", 0.0)
    PALPHA0 = param.get("PALPHA0", 0.0)
    BETA0 = param.get("BETA0", 0.0)
    LBETA0 = param.get("LBETA0", 0.0)
    WBETA0 = param.get("WBETA0", 0.0)
    PBETA0 = param.get("PBETA0", 0.0)

    # Gate dielectric tunnelling current model parameters
    AIGBACC = param.get("AIGBACC", 1.36e-2)
    BIGBACC = param.get("BIGBACC", 1.71e-3)
    CIGBACC = param.get("CIGBACC", 0.075)
    NIGBACC = param.get("NIGBACC", 1.0)
    AIGBINV = param.get("AIGBINV", 1.11e-2)
    BIGBINV = param.get("BIGBINV", 9.49e-4)
    CIGBINV = param.get("CIGBINV", 0.006)
    EIGBINV = param.get("EIGBINV", 1.1)
    NIGBINV = param.get("NIGBINV", 3.0)
    AIGC = param.get("AIGC", (1.36e-2 if (TYPE == ntype) else 9.8e-3))
    BIGC = param.get("BIGC", (1.71e-3 if (TYPE == ntype) else 7.59e-4))
    CIGC = param.get("CIGC", (0.075 if (TYPE == ntype) else 0.03))
    AIGS = param.get("AIGS", (1.36e-2 if (TYPE == ntype) else 9.8e-3))
    BIGS = param.get("BIGS", (1.71e-3 if (TYPE == ntype) else 7.59e-4))
    CIGS = param.get("CIGS", (0.075 if (TYPE == ntype) else 0.03))
    AIGD = param.get("AIGD", (1.36e-2 if (TYPE == ntype) else 9.8e-3))
    BIGD = param.get("BIGD", (1.71e-3 if (TYPE == ntype) else 7.59e-4))
    CIGD = param.get("CIGD", (0.075 if (TYPE == ntype) else 0.03))
    DLCIG = param.get("DLCIG", LINT)
    DLCIGD = param.get("DLCIGD", DLCIG)
    POXEDGE = param.get("POXEDGE", 1.0)
    NTOX = param.get("NTOX", 1.0)
    TOXREF = param.get("TOXREF", 3.0e-9)
    PIGCD = param.get("PIGCD", 1.0)
    AIGCL = param.get("AIGCL", 0.0)
    AIGCW = param.get("AIGCW", 0.0)
    AIGSL = param.get("AIGSL", 0.0)
    AIGSW = param.get("AIGSW", 0.0)
    AIGDL = param.get("AIGDL", 0.0)
    AIGDW = param.get("AIGDW", 0.0)
    PIGCDL = param.get("PIGCDL", 0.0)
    LAIGBINV = param.get("LAIGBINV", 0.0)
    WAIGBINV = param.get("WAIGBINV", 0.0)
    PAIGBINV = param.get("PAIGBINV", 0.0)
    LBIGBINV = param.get("LBIGBINV", 0.0)
    WBIGBINV = param.get("WBIGBINV", 0.0)
    PBIGBINV = param.get("PBIGBINV", 0.0)
    LCIGBINV = param.get("LCIGBINV", 0.0)
    WCIGBINV = param.get("WCIGBINV", 0.0)
    PCIGBINV = param.get("PCIGBINV", 0.0)
    LEIGBINV = param.get("LEIGBINV", 0.0)
    WEIGBINV = param.get("WEIGBINV", 0.0)
    PEIGBINV = param.get("PEIGBINV", 0.0)
    LNIGBINV = param.get("LNIGBINV", 0.0)
    WNIGBINV = param.get("WNIGBINV", 0.0)
    PNIGBINV = param.get("PNIGBINV", 0.0)
    LAIGBACC = param.get("LAIGBACC", 0.0)
    WAIGBACC = param.get("WAIGBACC", 0.0)
    PAIGBACC = param.get("PAIGBACC", 0.0)
    LBIGBACC = param.get("LBIGBACC", 0.0)
    WBIGBACC = param.get("WBIGBACC", 0.0)
    PBIGBACC = param.get("PBIGBACC", 0.0)
    LCIGBACC = param.get("LCIGBACC", 0.0)
    WCIGBACC = param.get("WCIGBACC", 0.0)
    PCIGBACC = param.get("PCIGBACC", 0.0)
    LNIGBACC = param.get("LNIGBACC", 0.0)
    WNIGBACC = param.get("WNIGBACC", 0.0)
    PNIGBACC = param.get("PNIGBACC", 0.0)
    LAIGC = param.get("LAIGC", 0.0)
    WAIGC = param.get("WAIGC", 0.0)
    PAIGC = param.get("PAIGC", 0.0)
    LBIGC = param.get("LBIGC", 0.0)
    WBIGC = param.get("WBIGC", 0.0)
    PBIGC = param.get("PBIGC", 0.0)
    LCIGC = param.get("LCIGC", 0.0)
    WCIGC = param.get("WCIGC", 0.0)
    PCIGC = param.get("PCIGC", 0.0)
    LAIGS = param.get("LAIGS", 0.0)
    WAIGS = param.get("WAIGS", 0.0)
    PAIGS = param.get("PAIGS", 0.0)
    LBIGS = param.get("LBIGS", 0.0)
    WBIGS = param.get("WBIGS", 0.0)
    PBIGS = param.get("PBIGS", 0.0)
    LCIGS = param.get("LCIGS", 0.0)
    WCIGS = param.get("WCIGS", 0.0)
    PCIGS = param.get("PCIGS", 0.0)
    LAIGD = param.get("LAIGD", 0.0)
    WAIGD = param.get("WAIGD", 0.0)
    PAIGD = param.get("PAIGD", 0.0)
    LBIGD = param.get("LBIGD", 0.0)
    WBIGD = param.get("WBIGD", 0.0)
    PBIGD = param.get("PBIGD", 0.0)
    LCIGD = param.get("LCIGD", 0.0)
    WCIGD = param.get("WCIGD", 0.0)
    PCIGD = param.get("PCIGD", 0.0)
    LPOXEDGE = param.get("LPOXEDGE", 0.0)
    WPOXEDGE = param.get("WPOXEDGE", 0.0)
    PPOXEDGE = param.get("PPOXEDGE", 0.0)
    LDLCIG = param.get("LDLCIG", 0.0)
    WDLCIG = param.get("WDLCIG", 0.0)
    PDLCIG = param.get("PDLCIG", 0.0)
    LDLCIGD = param.get("LDLCIGD", 0.0)
    WDLCIGD = param.get("WDLCIGD", 0.0)
    PDLCIGD = param.get("PDLCIGD", 0.0)
    LNTOX = param.get("LNTOX", 0.0)
    WNTOX = param.get("WNTOX", 0.0)
    PNTOX = param.get("PNTOX", 0.0)

    # GIDL and GISL currents
    AGIDL = param.get("AGIDL", 0.0)
    AGIDLL = param.get("AGIDLL", 0.0)
    AGIDLW = param.get("AGIDLW", 0.0)
    LAGIDL = param.get("LAGIDL", 0.0)
    WAGIDL = param.get("WAGIDL", 0.0)
    PAGIDL = param.get("PAGIDL", 0.0)
    BGIDL = param.get("BGIDL", 2.3e9)
    LBGIDL = param.get("LBGIDL", 0.0)
    WBGIDL = param.get("WBGIDL", 0.0)
    PBGIDL = param.get("PBGIDL", 0.0)
    CGIDL = param.get("CGIDL", 0.5)
    LCGIDL = param.get("LCGIDL", 0.0)
    WCGIDL = param.get("WCGIDL", 0.0)
    PCGIDL = param.get("PCGIDL", 0.0)
    EGIDL = param.get("EGIDL", 0.8)
    LEGIDL = param.get("LEGIDL", 0.0)
    WEGIDL = param.get("WEGIDL", 0.0)
    PEGIDL = param.get("PEGIDL", 0.0)
    AGISL = param.get("AGISL", AGIDL)
    AGISLL = param.get("AGISLL", AGIDLL)
    AGISLW = param.get("AGISLW", AGIDLW)
    LAGISL = param.get("LAGISL", LAGIDL)
    WAGISL = param.get("WAGISL", WAGIDL)
    PAGISL = param.get("PAGISL", PAGIDL)
    BGISL = param.get("BGISL", BGIDL)
    LBGISL = param.get("LBGISL", LBGIDL)
    WBGISL = param.get("WBGISL", WBGIDL)
    PBGISL = param.get("PBGISL", PBGIDL)
    CGISL = param.get("CGISL", CGIDL)
    LCGISL = param.get("LCGISL", LCGIDL)
    WCGISL = param.get("WCGISL", WCGIDL)
    PCGISL = param.get("PCGISL", PCGIDL)
    EGISL = param.get("EGISL", EGIDL)
    LEGISL = param.get("LEGISL", LEGIDL)
    WEGISL = param.get("WEGISL", WEGIDL)
    PEGISL = param.get("PEGISL", PEGIDL)

    # Overlap capacitance and fringing capacitance
    CF = param.get("CF", 0.0)
    LCF = param.get("LCF", 0.0)
    WCF = param.get("WCF", 0.0)
    PCF = param.get("PCF", 0.0)
    CFRCOEFF = param.get("CFRCOEFF", 1.0)
    CGSO = param.get("CGSO", 0.0)
    CGDO = param.get("CGDO", 0.0)
    CGBO = param.get("CGBO", 0.0)
    CGSL = param.get("CGSL", 0.0)
    LCGSL = param.get("LCGSL", 0.0)
    WCGSL = param.get("WCGSL", 0.0)
    PCGSL = param.get("PCGSL", 0.0)
    CGDL = param.get("CGDL", 0.0)
    LCGDL = param.get("LCGDL", 0.0)
    WCGDL = param.get("WCGDL", 0.0)
    PCGDL = param.get("PCGDL", 0.0)
    CKAPPAS = param.get("CKAPPAS", 0.6)
    LCKAPPAS = param.get("LCKAPPAS", 0.0)
    WCKAPPAS = param.get("WCKAPPAS", 0.0)
    PCKAPPAS = param.get("PCKAPPAS", 0.0)
    CKAPPAD = param.get("CKAPPAD", 0.6)
    LCKAPPAD = param.get("LCKAPPAD", 0.0)
    WCKAPPAD = param.get("WCKAPPAD", 0.0)
    PCKAPPAD = param.get("PCKAPPAD", 0.0)

    # Layout-dependent parasitics model parameters (resistance only)
    DMCG = param.get("DMCG", 0.0)
    DMCI = param.get("DMCI", DMCG)
    DMDG = param.get("DMDG", 0.0)
    DMCGT = param.get("DMCGT", 0.0)
    XGL = param.get("XGL", 0.0)
    RSHG = param.get("RSHG", 0.1)

    # Junction capacitance
    CJS = param.get("CJS", 5.0e-4)
    CJD = param.get("CJD", CJS)
    CJSWS = param.get("CJSWS", 5.0e-10)
    CJSWD = param.get("CJSWD", CJSWS)
    CJSWGS = param.get("CJSWGS", 0.0)
    CJSWGD = param.get("CJSWGD", CJSWGS)
    PBS = param.get("PBS", 1.0)
    PBD = param.get("PBD", PBS)
    PBSWS = param.get("PBSWS", 1.0)
    PBSWD = param.get("PBSWD", PBSWS)
    PBSWGS = param.get("PBSWGS", PBSWS)
    PBSWGD = param.get("PBSWGD", PBSWGS)
    MJS = param.get("MJS", 0.5)
    MJD = param.get("MJD", MJS)
    MJSWS = param.get("MJSWS", 0.33)
    MJSWD = param.get("MJSWD", MJSWS)
    MJSWGS = param.get("MJSWGS", MJSWS)
    MJSWGD = param.get("MJSWGD", MJSWGS)

    # Junction current
    JSS = param.get("JSS", 1.0e-4)
    JSD = param.get("JSD", JSS)
    JSWS = param.get("JSWS", 0.0)
    JSWD = param.get("JSWD", JSWS)
    JSWGS = param.get("JSWGS", 0.0)
    JSWGD = param.get("JSWGD", JSWGS)
    NJS = param.get("NJS", 1.0)
    NJD = param.get("NJD", NJS)
    IJTHSFWD = param.get("IJTHSFWD", 0.1)
    IJTHDFWD = param.get("IJTHDFWD", IJTHSFWD)
    IJTHSREV = param.get("IJTHSREV", 0.1)
    IJTHDREV = param.get("IJTHDREV", IJTHSREV)
    BVS = param.get("BVS", 10.0)
    BVD = param.get("BVD", BVS)
    XJBVS = param.get("XJBVS", 1.0)
    XJBVD = param.get("XJBVD", XJBVS)

    # Tunneling component of junction current
    JTSS = param.get("JTSS", 0.0)
    JTSD = param.get("JTSD", JTSS)
    JTSSWS = param.get("JTSSWS", 0.0)
    JTSSWD = param.get("JTSSWD", JTSSWS)
    JTSSWGS = param.get("JTSSWGS", 0.0)
    JTSSWGD = param.get("JTSSWGD", JTSSWGS)
    JTWEFF = param.get("JTWEFF", 0.0)
    NJTS = param.get("NJTS", 20.0)
    NJTSD = param.get("NJTSD", NJTS)
    NJTSSW = param.get("NJTSSW", 20.0)
    NJTSSWD = param.get("NJTSSWD", NJTSSW)
    NJTSSWG = param.get("NJTSSWG", 20.0)
    NJTSSWGD = param.get("NJTSSWGD", NJTSSWG)
    VTSS = param.get("VTSS", 10.0)
    VTSD = param.get("VTSD", VTSS)
    VTSSWS = param.get("VTSSWS", 10.0)
    VTSSWD = param.get("VTSSWD", VTSSWS)
    VTSSWGS = param.get("VTSSWGS", 10.0)
    VTSSWGD = param.get("VTSSWGD", VTSSWGS)

    # High-speed/RF model parameters
    XRCRG1 = param.get("XRCRG1", 12.0)
    XRCRG2 = param.get("XRCRG2", 1.0)
    GBMIN = param.get("GBMIN", 1.0e-12)
    RBPS0 = param.get("RBPS0", 50.0)
    RBPSL = param.get("RBPSL", 0.0)
    RBPSW = param.get("RBPSW", 0.0)
    RBPSNF = param.get("RBPSNF", 0.0)
    RBPD0 = param.get("RBPD0", 50.0)
    RBPDL = param.get("RBPDL", 0.0)
    RBPDW = param.get("RBPDW", 0.0)
    RBPDNF = param.get("RBPDNF", 0.0)
    RBPBX0 = param.get("RBPBX0", 100.0)
    RBPBXL = param.get("RBPBXL", 0.0)
    RBPBXW = param.get("RBPBXW", 0.0)
    RBPBXNF = param.get("RBPBXNF", 0.0)
    RBPBY0 = param.get("RBPBY0", 100.0)
    RBPBYL = param.get("RBPBYL", 0.0)
    RBPBYW = param.get("RBPBYW", 0.0)
    RBPBYNF = param.get("RBPBYNF", 0.0)
    RBSBX0 = param.get("RBSBX0", 100.0)
    RBSBY0 = param.get("RBSBY0", 100.0)
    RBDBX0 = param.get("RBDBX0", 100.0)
    RBDBY0 = param.get("RBDBY0", 100.0)
    RBSDBXL = param.get("RBSDBXL", 0.0)
    RBSDBXW = param.get("RBSDBXW", 0.0)
    RBSDBXNF = param.get("RBSDBXNF", 0.0)
    RBSDBYL = param.get("RBSDBYL", 0.0)
    RBSDBYW = param.get("RBSDBYW", 0.0)
    RBSDBYNF = param.get("RBSDBYNF", 0.0)

    # Flicker noise
    EF = param.get("EF", 1.0)
    EM = param.get("EM", 4.1e7)
    NOIA = param.get("NOIA", 6.250e40)
    NOIB = param.get("NOIB", 3.125e25)
    NOIC = param.get("NOIC", 8.750e8)
    LINTNOI = param.get("LINTNOI", 0.0)
    NOIA1 = param.get("NOIA1", 0.0)
    NOIAX = param.get("NOIAX", 1.0)

    # Thermal noise
    NTNOI = param.get("NTNOI", 1.0)
    RNOIA = param.get("RNOIA", 0.577)
    RNOIB = param.get("RNOIB", 0.5164)
    RNOIC = param.get("RNOIC", 0.395)
    TNOIA = param.get("TNOIA", 1.5)
    TNOIB = param.get("TNOIB", 3.5)
    TNOIC = param.get("TNOIC", 0.0)

    # Binning parameters
    BINUNIT = param.get("BINUNIT", 1)
    DLBIN = param.get("DLBIN", 0.0)
    DWBIN = param.get("DWBIN", 0.0)

    # Temperature dependence parameters
    TNOM = param.get("TNOM", 27.0)
    TBGASUB = param.get("TBGASUB", 4.73e-4)
    TBGBSUB = param.get("TBGBSUB", 636.0)
    TNFACTOR = param.get("TNFACTOR", 0.0)
    UTE = param.get("UTE", -1.5)
    LUTE = param.get("LUTE", 0.0)
    WUTE = param.get("WUTE", 0.0)
    PUTE = param.get("PUTE", 0.0)
    UTEL = param.get("UTEL", 0.0)
    UA1 = param.get("UA1", 1.0e-3)
    LUA1 = param.get("LUA1", 0.0)
    WUA1 = param.get("WUA1", 0.0)
    PUA1 = param.get("PUA1", 0.0)
    UA1L = param.get("UA1L", 0.0)
    UC1 = param.get("UC1", 0.056e-9)
    LUC1 = param.get("LUC1", 0.0)
    WUC1 = param.get("WUC1", 0.0)
    PUC1 = param.get("PUC1", 0.0)
    UD1 = param.get("UD1", 0.0)
    LUD1 = param.get("LUD1", 0.0)
    WUD1 = param.get("WUD1", 0.0)
    PUD1 = param.get("PUD1", 0.0)
    UD1L = param.get("UD1L", 0.0)
    EU1 = param.get("EU1", 0.0)
    LEU1 = param.get("LEU1", 0.0)
    WEU1 = param.get("WEU1", 0.0)
    PEU1 = param.get("PEU1", 0.0)
    UCSTE = param.get("UCSTE", -4.775e-3)
    LUCSTE = param.get("LUCSTE", 0.0)
    WUCSTE = param.get("WUCSTE", 0.0)
    PUCSTE = param.get("PUCSTE", 0.0)
    TETA0 = param.get("TETA0", 0.0)
    PRT = param.get("PRT", 0.0)
    LPRT = param.get("LPRT", 0.0)
    WPRT = param.get("WPRT", 0.0)
    PPRT = param.get("PPRT", 0.0)
    AT = param.get("AT", -1.56e-3)
    LAT = param.get("LAT", 0.0)
    WAT = param.get("WAT", 0.0)
    PAT = param.get("PAT", 0.0)
    ATL = param.get("ATL", 0.0)
    TDELTA = param.get("TDELTA", 0.0)
    PTWGT = param.get("PTWGT", 0.0)
    LPTWGT = param.get("LPTWGT", 0.0)
    WPTWGT = param.get("WPTWGT", 0.0)
    PPTWGT = param.get("PPTWGT", 0.0)
    PTWGTL = param.get("PTWGTL", 0.0)
    KT1 = param.get("KT1", -0.11)
    KT1EXP = param.get("KT1EXP", 1.0)
    KT1L = param.get("KT1L", 0.0)
    LKT1 = param.get("LKT1", 0.0)
    WKT1 = param.get("WKT1", 0.0)
    PKT1 = param.get("PKT1", 0.0)
    KT2 = param.get("KT2", 0.022)
    LKT2 = param.get("LKT2", 0.0)
    WKT2 = param.get("WKT2", 0.0)
    PKT2 = param.get("PKT2", 0.0)
    IIT = param.get("IIT", 0.0)
    LIIT = param.get("LIIT", 0.0)
    WIIT = param.get("WIIT", 0.0)
    PIIT = param.get("PIIT", 0.0)
    IGT = param.get("IGT", 2.5)
    LIGT = param.get("LIGT", 0.0)
    WIGT = param.get("WIGT", 0.0)
    PIGT = param.get("PIGT", 0.0)
    TGIDL = param.get("TGIDL", 0.0)
    LTGIDL = param.get("LTGIDL", 0.0)
    WTGIDL = param.get("WTGIDL", 0.0)
    PTGIDL = param.get("PTGIDL", 0.0)
    TCJ = param.get("TCJ", 0.0)
    TCJSW = param.get("TCJSW", 0.0)
    TCJSWG = param.get("TCJSWG", 0.0)
    TPB = param.get("TPB", 0.0)
    TPBSW = param.get("TPBSW", 0.0)
    TPBSWG = param.get("TPBSWG", 0.0)
    XTIS = param.get("XTIS", 3.0)
    XTID = param.get("XTID", XTIS)
    XTSS = param.get("XTSS", 0.02)
    XTSD = param.get("XTSD", XTSS)
    XTSSWS = param.get("XTSSWS", 0.02)
    XTSSWD = param.get("XTSSWD", XTSSWS)
    XTSSWGS = param.get("XTSSWGS", 0.02)
    XTSSWGD = param.get("XTSSWGD", XTSSWGS)
    TNJTS = param.get("TNJTS", 0.0)
    TNJTSD = param.get("TNJTSD", TNJTS)
    TNJTSSW = param.get("TNJTSSW", 0.0)
    TNJTSSWD = param.get("TNJTSSWD", TNJTSSW)
    TNJTSSWG = param.get("TNJTSSWG", 0.0)
    TNJTSSWGD = param.get("TNJTSSWGD", TNJTSSWG)

    # Self heating parameters
    RTH0 = param.get("RTH0", 0.0)
    CTH0 = param.get("CTH0", 1.0e-5)
    WTH0 = param.get("WTH0", 0.0)

    # Stress related parameters
    SAREF = param.get("SAREF", 1.0e-6)
    SBREF = param.get("SBREF", 1.0e-6)
    WLOD = param.get("WLOD", 0.0)
    KU0 = param.get("KU0", 0.0)
    KVSAT = param.get("KVSAT", 0.0)
    TKU0 = param.get("TKU0", 0.0)
    LKU0 = param.get("LKU0", 0.0)
    WKU0 = param.get("WKU0", 0.0)
    PKU0 = param.get("PKU0", 0.0)
    LLODKU0 = param.get("LLODKU0", 0.0)
    WLODKU0 = param.get("WLODKU0", 0.0)
    KVTH0 = param.get("KVTH0", 0.0)
    LKVTH0 = param.get("LKVTH0", 0.0)
    WKVTH0 = param.get("WKVTH0", 0.0)
    PKVTH0 = param.get("PKVTH0", 0.0)
    LLODVTH = param.get("LLODVTH", 0.0)
    WLODVTH = param.get("WLODVTH", 0.0)
    STK2 = param.get("STK2", 0.0)
    LODK2 = param.get("LODK2", 0.0)
    STETA0 = param.get("STETA0", 0.0)
    LODETA0 = param.get("LODETA0", 0.0)

    # Well proximity parameters
    WEB = param.get("WEB", 0.0)
    WEC = param.get("WEC", 0.0)
    KVTH0WE = param.get("KVTH0WE", 0.0)
    LKVTH0WE = param.get("LKVTH0WE", 0.0)
    WKVTH0WE = param.get("WKVTH0WE", 0.0)
    PKVTH0WE = param.get("PKVTH0WE", 0.0)
    K2WE = param.get("K2WE", 0.0)
    LK2WE = param.get("LK2WE", 0.0)
    WK2WE = param.get("WK2WE", 0.0)
    PK2WE = param.get("PK2WE", 0.0)
    KU0WE = param.get("KU0WE", 0.0)
    LKU0WE = param.get("LKU0WE", 0.0)
    WKU0WE = param.get("WKU0WE", 0.0)
    PKU0WE = param.get("PKU0WE", 0.0)
    SCREF = param.get("SCREF", 1.0e-6)

    # Sub-surface leakage drain current
    SSL0 = param.get("SSL0", 4.0e2)
    SSL1 = param.get("SSL1", 3.36e8)
    SSL2 = param.get("SSL2", 0.185)
    SSL3 = param.get("SSL3", 0.3)
    SSL4 = param.get("SSL4", 1.4)
    SSL5 = param.get("SSL5", 0)
    SSLEXP1 = param.get("SSLEXP1", 0.490)
    SSLEXP2 = param.get("SSLEXP2", 1.42)

    # Vdsx smoothing
    AVDSX = param.get("AVDSX", 20.0)

    # STI edge FET device parameters
    WEDGE = param.get("WEDGE", 10.0e-9)
    DGAMMAEDGE = param.get("DGAMMAEDGE", 0.0)
    DGAMMAEDGEL = param.get("DGAMMAEDGEL", 0.0)
    DGAMMAEDGELEXP = param.get("DGAMMAEDGELEXP", 1.0)
    DVTEDGE = param.get("DVTEDGE", 0.0)
    NDEPEDGE = param.get("NDEPEDGE", 1e24)
    LNDEPEDGE = param.get("LNDEPEDGE", 0.0)
    WNDEPEDGE = param.get("WNDEPEDGE", 0.0)
    PNDEPEDGE = param.get("PNDEPEDGE", 0.0)
    NFACTOREDGE = param.get("NFACTOREDGE", 0.0)
    LNFACTOREDGE = param.get("LNFACTOREDGE", 0.0)
    WNFACTOREDGE = param.get("WNFACTOREDGE", 0.0)
    PNFACTOREDGE = param.get("PNFACTOREDGE", 0.0)
    CITEDGE = param.get("CITEDGE", 0.0)
    LCITEDGE = param.get("LCITEDGE", 0.0)
    WCITEDGE = param.get("WCITEDGE", 0.0)
    PCITEDGE = param.get("PCITEDGE", 0.0)
    CDSCDEDGE = param.get("CDSCDEDGE", 1e-9)
    LCDSCDEDGE = param.get("LCDSCDEDGE", 0.0)
    WCDSCDEDGE = param.get("WCDSCDEDGE", 0.0)
    PCDSCDEDGE = param.get("PCDSCDEDGE", 0.0)
    CDSCBEDGE = param.get("CDSCBEDGE", 0.0)
    LCDSCBEDGE = param.get("LCDSCBEDGE", 0.0)
    WCDSCBEDGE = param.get("WCDSCBEDGE", 0.0)
    PCDSCBEDGE = param.get("PCDSCBEDGE", 0.0)
    ETA0EDGE = param.get("ETA0EDGE", 0.08)
    LETA0EDGE = param.get("LETA0EDGE", 0.0)
    WETA0EDGE = param.get("WETA0EDGE", 0.0)
    PETA0EDGE = param.get("PETA0EDGE", 0.0)
    ETABEDGE = param.get("ETABEDGE", -0.07)
    LETABEDGE = param.get("LETABEDGE", 0.0)
    WETABEDGE = param.get("WETABEDGE", 0.0)
    PETABEDGE = param.get("PETABEDGE", 0.0)
    KT1EDGE = param.get("KT1EDGE", -0.11)
    LKT1EDGE = param.get("LKT1EDGE", 0.0)
    WKT1EDGE = param.get("WKT1EDGE", 0.0)
    PKT1EDGE = param.get("PKT1EDGE", 0.0)
    KT1LEDGE = param.get("KT1LEDGE", 0.0)
    LKT1LEDGE = param.get("LKT1LEDGE", 0.0)
    WKT1LEDGE = param.get("WKT1LEDGE", 0.0)
    PKT1LEDGE = param.get("PKT1LEDGE", 0.0)
    KT2EDGE = param.get("KT2EDGE", 0.022)
    LKT2EDGE = param.get("LKT2EDGE", 0.0)
    WKT2EDGE = param.get("WKT2EDGE", 0.0)
    PKT2EDGE = param.get("PKT2EDGE", 0.0)
    KT1EXPEDGE = param.get("KT1EXPEDGE", 1.0)
    LKT1EXPEDGE = param.get("LKT1EXPEDGE", 0.0)
    WKT1EXPEDGE = param.get("WKT1EXPEDGE", 0.0)
    PKT1EXPEDGE = param.get("PKT1EXPEDGE", 0.0)
    TNFACTOREDGE = param.get("TNFACTOREDGE", 0.0)
    LTNFACTOREDGE = param.get("LTNFACTOREDGE", 0.0)
    WTNFACTOREDGE = param.get("WTNFACTOREDGE", 0.0)
    PTNFACTOREDGE = param.get("PTNFACTOREDGE", 0.0)
    TETA0EDGE = param.get("TETA0EDGE", 0.0)
    LTETA0EDGE = param.get("LTETA0EDGE", 0.0)
    WTETA0EDGE = param.get("WTETA0EDGE", 0.0)
    PTETA0EDGE = param.get("PTETA0EDGE", 0.0)
    DVT0EDGE = param.get("DVT0EDGE", 2.2)
    DVT1EDGE = param.get("DVT1EDGE", 0.53)
    DVT2EDGE = param.get("DVT2EDGE", 0.0)
    K2EDGE = param.get("K2EDGE", 0.0)
    LK2EDGE = param.get("LK2EDGE", 0.0)
    WK2EDGE = param.get("WK2EDGE", 0.0)
    PK2EDGE = param.get("PK2EDGE", 0.0)
    KVTH0EDGE = param.get("KVTH0EDGE", 0.0)
    LKVTH0EDGE = param.get("LKVTH0EDGE", 0.0)
    WKVTH0EDGE = param.get("WKVTH0EDGE", 0.0)
    PKVTH0EDGE = param.get("PKVTH0EDGE", 0.0)
    STK2EDGE = param.get("STK2EDGE", 0.0)
    LSTK2EDGE = param.get("LSTK2EDGE", 0.0)
    WSTK2EDGE = param.get("WSTK2EDGE", 0.0)
    PSTK2EDGE = param.get("PSTK2EDGE", 0.0)
    STETA0EDGE = param.get("STETA0EDGE", 0.0)
    LSTETA0EDGE = param.get("LSTETA0EDGE", 0.0)
    WSTETA0EDGE = param.get("WSTETA0EDGE", 0.0)
    PSTETA0EDGE = param.get("PSTETA0EDGE", 0.0)
    IGCLAMP = param.get("IGCLAMP", 1)
    LP = param.get("LP", 1.0e-5)
    RNOIK = param.get("RNOIK", 0.0)
    TNOIK = param.get("TNOIK", 0.0)
    TNOIK2 = param.get("TNOIK2", 0.1)
    K0 = param.get("K0", 0.0)
    LK0 = param.get("LK0", 0.0)
    WK0 = param.get("WK0", 0.0)
    PK0 = param.get("PK0", 0.0)
    K01 = param.get("K01", 0.0)
    LK01 = param.get("LK01", 0.0)
    WK01 = param.get("WK01", 0.0)
    PK01 = param.get("PK01", 0.0)
    M0 = param.get("M0", 1.0)
    LM0 = param.get("LM0", 0.0)
    WM0 = param.get("WM0", 0.0)
    PM0 = param.get("PM0", 0.0)
    M01 = param.get("M01", 0.0)
    LM01 = param.get("LM01", 0.0)
    WM01 = param.get("WM01", 0.0)
    PM01 = param.get("PM01", 0.0)

    # Flicker noise model parameter for EDGE FET transistor
    NEDGE = param.get("NEDGE", 1)
    NOIA1_EDGE = param.get("NOIA1_EDGE", 0.0)
    NOIAX_EDGE = param.get("NOIAX_EDGE", 1.0)


    # Flicker noise model parameter for Halo transistor
    FNOIMOD = param.get("FNOIMOD", 0)
    LH = param.get("LH", 1.0e-8)
    NOIA2 = param.get("NOIA2", NOIA)
    HNDEP = param.get("HNDEP", NDEP)

    # Flexibility of tuning Cgg in strong inversion
    ABULK = param.get("ABULK", 1.0)

    # To enhance the fitting flexiblity for the gm/Id
    C0 = param.get("C0", 0.0)
    LC0 = param.get("LC0", 0.0)
    WC0 = param.get("WC0", 0.0)
    PC0 = param.get("PC0", 0.0)
    C01 = param.get("C01", 0.0)
    LC01 = param.get("LC01", 0.0)
    WC01 = param.get("WC01", 0.0)
    PC01 = param.get("PC01", 0.0)
    C0SI = param.get("C0SI", 1.0)
    LC0SI = param.get("LC0SI", 0.0)
    WC0SI = param.get("WC0SI", 0.0)
    PC0SI = param.get("PC0SI", 0.0)
    C0SI1 = param.get("C0SI1", 0.0)
    LC0SI1 = param.get("LC0SI1", 0.0)
    WC0SI1 = param.get("WC0SI1", 0.0)
    PC0SI1 = param.get("PC0SI1", 0.0)
    C0SISAT = param.get("C0SISAT", 0.0)
    LC0SISAT = param.get("LC0SISAT", 0.0)
    WC0SISAT = param.get("WC0SISAT", 0.0)
    PC0SISAT = param.get("PC0SISAT", 0.0)
    C0SISAT1 = param.get("C0SISAT1", 0.0)
    LC0SISAT1 = param.get("LC0SISAT1", 0.0)
    WC0SISAT1 = param.get("WC0SISAT1", 0.0)
    PC0SISAT1 = param.get("PC0SISAT1", 0.0)

    # Minimum resistance value
    minr = param.get("minr", 1.0e-3)
    # High Voltage Model Parameters

    # --- Mod selectors -----
    HVMOD = param.get("HVMOD", 0)
    HVCAP = param.get("HVCAP", 0)
    HVCAPS = param.get("HVCAPS", 0)
    IIMOD = param.get("IIMOD", 0)

    # --- Other parameters -----
    NDRIFTD = param.get("NDRIFTD", 5.0e16)
    VDRIFT = param.get("VDRIFT", 1.0e5)
    MDRIFT = param.get("MDRIFT", 1.0)
    NDRIFTS = param.get("NDRIFTS", NDRIFTD)
    RDLCW = param.get("RDLCW", 100.0)
    RSLCW = param.get("RSLCW", 0)
    PDRWB = param.get("PDRWB", 0)
    VFBDRIFT = param.get("VFBDRIFT", -1)
    VFBOV = param.get("VFBOV", -1)
    LOVER = param.get("LOVER", 500e-9)
    LOVERACC = param.get("LOVERACC", LOVER)
    NDR = param.get("NDR", NDEP)
    SLHV = param.get("SLHV", 0)
    SLHV1 = param.get("SLHV1", 1.0)
    ALPHADR = param.get("ALPHADR", ALPHA0)
    BETADR = param.get("BETADR", BETA0)
    PRTHV = param.get("PRTHV", 0.0)
    ATHV = param.get("ATHV", 0)
    HVFACTOR = param.get("HVFACTOR", 1e-3)
    DRII1 = param.get("DRII1", 1.0)
    DRII2 = param.get("DRII2", 5)
    DELTAII = param.get("DELTAII", 0.5)

    # Bias-independent calculations
    if (TYPE == ntype):
        devsign = 1
    else:
        devsign = -1

    # Constants
    epssi    = EPSRSUB * EPS0
    epsox    = EPSROX * EPS0
    Cox      = EPSROX * EPS0 / TOXE
    epsratio = EPSRSUB / EPSROX

    # Physical oxide thickness
    if ("TOXP" not in keys(param)):
        BSIMBULKTOXP = (TOXE * EPSROX / 3.9) - DTOX
    else:
        BSIMBULKTOXP = TOXP
    L_mult = L * LMLT
    W_mult = W * WMLT
    Lnew = L_mult + XL
    if (Lnew <= 0.0):
        print("Fatal: Ldrawn * LMLT + XL = %e for %M is non-positive", Lnew)    
    W_by_NF = W_mult / NF
    Wnew    = W_by_NF + XW
    if (Wnew <= 0.0):
        print("Fatal: W / NF * WMLT + XW = %e for %M is non-positive", Wnew)    

    # Leff and Weff for I-V
    L_LLN      = Lnew**-LLN
    W_LWN      = Wnew**-LWN
    LW_LLN_LWN = L_LLN * W_LWN
    dLIV       = LINT + LL * L_LLN + LW * W_LWN + LWL * LW_LLN_LWN
    L_WLN      = Lnew**-WLN
    W_WWN      = Wnew**-WWN
    LW_WLN_WWN = L_WLN * W_WWN
    dWIV       = WINT + WL * L_WLN + WW * W_WWN + WWL * LW_WLN_WWN
    Leff       = Lnew - 2.0 * dLIV
    if (Leff <= 0.0):
        print("Fatal: Effective channel length = %e for  %M is non-positive", Leff)
    elif (Leff <= 1.0e-9):
        print("Warning: Effective channel length = %e for %M is <= 1.0e-9. Recommended Leff >= 1e-8", Leff)    
    Weff = Wnew - 2.0 * dWIV
    if (Weff <= 0.0):
         print("Fatal: Effective channel Width = %e for %M is non-positive", Weff)
    elif (Weff <= 1.0e-9):
        print("Warning: Effective channel width = %e for %M is <= 1.0e-9. Recommended Weff >= 1e-8", Weff)    

    # Leff and Weff for C-V
    dLCV = DLC + LLC * L_LLN + LWC * W_LWN + LWLC * LW_LLN_LWN
    dWCV = DWC + WLC * L_WLN + WWC * W_WWN + WWLC * LW_WLN_WWN
    Lact = Lnew - 2.0 * dLCV
    if (Lact <= 0.0):
         print("Fatal: Effective channel length for C-V = %e for %M is non-positive", Lact)
    elif (Lact <= 1.0e-9):
        print("Warning: Effective channel length for C-V = %e for %M is <= 1.0e-9. Recommended Lact >= 1e-8", Lact)
    Wact = Wnew - 2.0 * dWCV
    if (Wact <= 0.0):
        print("Fatal: Effective channel width for C-V = %e for %M is non-positive", Wact)
    elif (Wact <= 1.0e-9):
        print("Warning: Effective channel width for C-V = %e for %M is <= 1.0e-9. Recommended Wact >= 1e-8", Wact)    

    # Weffcj for diode, GIDL etc.
    dWJ    = DWJ + WLC / Lnew**WLN + WWC / Wnew**WWN + WWLC / Lnew**WLN / Wnew**WWN
    Weffcj = Wnew - 2.0 * dWJ
    if (Weffcj <= 0.0):
        print("Fatal: Effective channel width for S/D junctions = %e for %M is non-positive", Weffcj)
    Inv_L     = 1.0e-6 / Leff
    Inv_W     = 1.0e-6 / Weff
    Inv_Lact  = 1.0e-6 / Lact
    Inv_Wact  = 1.0e-6 / Wact
    Inv_Llong = 1.0e-6 / LLONG
    Inv_Wwide = 1.0e-6 / WWIDE
    Inv_WL    = Inv_L * Inv_W

    # Effective length and width for binning
    L_LLN1 = L_LLN
    L_WLN1 = L_WLN
    if (DLBIN != 0.0):
        if (DLBIN <= -Lnew):
            print("Fatal: DLBIN for %M = %e is <= -Ldrawn * LMLT", DLBIN)
        else:
            L_LLN1 = (Lnew + DLBIN)**-LLN
            L_WLN1 = (Lnew + DLBIN)**-WLN
    W_LWN1 = W_LWN
    W_WWN1 = W_WWN
    if (DWBIN != 0.0):
        if (DWBIN <= -Wnew):
            print("Fatal: DWBIN for %M = %e is <= -Wdrawn * WMLT", DWBIN)
        else:
            W_LWN1 = (Wnew + DWBIN)**-LWN
            W_WWN1 = (Wnew + DWBIN)**-WWN
    LW_LLN_LWN1 = L_LLN1 * W_LWN1
    dLB         = LINT + LL * L_LLN1 + LW * W_LWN1 + LWL * LW_LLN_LWN1
    LW_WLN_WWN1 = L_WLN1 * W_WWN1
    dWB         = WINT + WL * L_WLN1 + WW * W_WWN1 + WWL * LW_WLN_WWN1
    Leff1 = Lnew - 2.0 * dLB + DLBIN
    if (Leff1 <= 0.0):
        print("Fatal: Effective channel length for binning = %e for %M is non-positive", Leff1)    
    Weff1 = Wnew - 2.0 * dWB + DWBIN
    if (Weff1 <= 0.0):
        print("Fatal: Effective channel width for binning = %e for %M is non-positive", Weff1)    
    if (BINUNIT == 1):
        BIN_L = 1.0e-6 / Leff1
        BIN_W = 1.0e-6 / Weff1
    else:
        BIN_L = 1.0 / Leff1
        BIN_W = 1.0 / Weff1    
    BIN_WL         = BIN_L * BIN_W
    VFB_i          = VFB + BIN_L * LVFB + BIN_W * WVFB + BIN_WL * PVFB
    VFBCV_i        = VFBCV + BIN_L * LVFBCV + BIN_W * WVFBCV + BIN_WL * PVFBCV
    NSD_i          = NSD + BIN_L * LNSD + BIN_W * WNSD + BIN_WL * PNSD
    NDEP_i         = NDEP + BIN_L * LNDEP + BIN_W * WNDEP + BIN_WL * PNDEP
    NDEPCV_i       = NDEPCV + BIN_L * LNDEPCV + BIN_W * WNDEPCV + BIN_WL * PNDEPCV
    NGATE_i        = NGATE + BIN_L * LNGATE + BIN_W * WNGATE + BIN_WL * PNGATE
    CIT_i          = CIT + BIN_L * LCIT + BIN_W * WCIT + BIN_WL * PCIT
    NFACTOR_i      = NFACTOR + BIN_L * LNFACTOR + BIN_W * WNFACTOR + BIN_WL * PNFACTOR
    CDSCD_i        = CDSCD + BIN_L * LCDSCD + BIN_W * WCDSCD + BIN_WL * PCDSCD
    CDSCB_i        = CDSCB + BIN_L * LCDSCB + BIN_W * WCDSCB + BIN_WL * PCDSCB
    DVTP0_i        = DVTP0 + BIN_L * LDVTP0 + BIN_W * WDVTP0 + BIN_WL * PDVTP0
    DVTP1_i        = DVTP1 + BIN_L * LDVTP1 + BIN_W * WDVTP1 + BIN_WL * PDVTP1
    DVTP2_i        = DVTP2 + BIN_L * LDVTP2 + BIN_W * WDVTP2 + BIN_WL * PDVTP2
    DVTP3_i        = DVTP3 + BIN_L * LDVTP3 + BIN_W * WDVTP3 + BIN_WL * PDVTP3
    DVTP4_i        = DVTP4 + BIN_L * LDVTP4 + BIN_W * WDVTP4 + BIN_WL * PDVTP4
    DVTP5_i        = DVTP5 + BIN_L * LDVTP5 + BIN_W * WDVTP5 + BIN_WL * PDVTP5
    K2_i           = K2 + BIN_L * LK2 + BIN_W * WK2 + BIN_WL * PK2
    K1_i           = K1 + BIN_L * LK1 + BIN_W * WK1 + BIN_WL * PK1
    XJ_i           = XJ + BIN_L * LXJ + BIN_W * WXJ + BIN_WL * PXJ
    PHIN_i         = PHIN + BIN_L * LPHIN + BIN_W * WPHIN + BIN_WL * PPHIN
    ETA0_i         = ETA0 + BIN_L * LETA0 + BIN_W * WETA0 + BIN_WL * PETA0
    ETAB_i         = ETAB + BIN_L * LETAB + BIN_W * WETAB + BIN_WL * PETAB
    DELTA_i        = DELTA + BIN_L * LDELTA + BIN_W * WDELTA + BIN_WL * PDELTA
    U0_i           = U0 + BIN_L * LU0 + BIN_W * WU0 + BIN_WL * PU0
    UA_i           = UA + BIN_L * LUA + BIN_W * WUA + BIN_WL * PUA
    UD_i           = UD + BIN_L * LUD + BIN_W * WUD + BIN_WL * PUD
    EU_i           = EU + BIN_L * LEU + BIN_W * WEU + BIN_WL * PEU
    UCS_i          = UCS + BIN_L * LUCS + BIN_W * WUCS + BIN_WL * PUCS
    UC_i           = UC + BIN_L * LUC + BIN_W * WUC + BIN_WL * PUC
    PCLM_i         = PCLM + BIN_L * LPCLM + BIN_W * WPCLM + BIN_WL * PPCLM
    PCLMCV_i       = PCLMCV + BIN_L * LPCLMCV + BIN_W * WPCLMCV + BIN_WL * PPCLMCV
    RSW_i          = RSW + BIN_L * LRSW + BIN_W * WRSW + BIN_WL * PRSW
    RDW_i          = RDW + BIN_L * LRDW + BIN_W * WRDW + BIN_WL * PRDW
    PRWG_i         = PRWG + BIN_L * LPRWG + BIN_W * WPRWG + BIN_WL * PPRWG
    PRWB_i         = PRWB + BIN_L * LPRWB + BIN_W * WPRWB + BIN_WL * PPRWB
    WR_i           = WR + BIN_L * LWR + BIN_W * WWR + BIN_WL * PWR
    RSWMIN_i       = RSWMIN + BIN_L * LRSWMIN + BIN_W * WRSWMIN + BIN_WL * PRSWMIN
    RDWMIN_i       = RDWMIN + BIN_L * LRDWMIN + BIN_W * WRDWMIN + BIN_WL * PRDWMIN
    RDSW_i         = RDSW + BIN_L * LRDSW + BIN_W * WRDSW + BIN_WL * PRDSW
    RDSWMIN_i      = RDSWMIN + BIN_L * LRDSWMIN + BIN_W * WRDSWMIN + BIN_WL * PRDSWMIN
    PTWG_i         = PTWG + BIN_L * LPTWG + BIN_W * WPTWG + BIN_WL * PPTWG
    PDIBLC_i       = PDIBLC + BIN_L * LPDIBLC + BIN_W * WPDIBLC + BIN_WL * PPDIBLC
    PDIBLCB_i      = PDIBLCB + BIN_L * LPDIBLCB + BIN_W * WPDIBLCB + BIN_WL * PPDIBLCB
    PSCBE1_i       = PSCBE1 + BIN_L * LPSCBE1 + BIN_W * WPSCBE1 + BIN_WL * PPSCBE1
    PSCBE2_i       = PSCBE2 + BIN_L * LPSCBE2 + BIN_W * WPSCBE2 + BIN_WL * PPSCBE2
    PDITS_i        = PDITS + BIN_L * LPDITS + BIN_W * WPDITS + BIN_WL * PPDITS
    PDITSD_i       = PDITSD + BIN_L * LPDITSD + BIN_W * WPDITSD + BIN_WL * PPDITSD
    FPROUT_i       = FPROUT + BIN_L * LFPROUT + BIN_W * WFPROUT + BIN_WL * PFPROUT
    PVAG_i         = PVAG + BIN_L * LPVAG + BIN_W * WPVAG + BIN_WL * PPVAG
    VSAT_i         = VSAT + BIN_L * LVSAT + BIN_W * WVSAT + BIN_WL * PVSAT
    PSAT_i         = PSAT + BIN_L * LPSAT + BIN_W * WPSAT + BIN_WL * PPSAT
    VSATCV_i       = VSATCV + BIN_L * LVSATCV + BIN_W * WVSATCV + BIN_WL * PVSATCV
    CF_i           = CF + BIN_L * LCF + BIN_W * WCF + BIN_WL * PCF
    CGSL_i         = CGSL + BIN_L * LCGSL + BIN_W * WCGSL + BIN_WL * PCGSL
    CGDL_i         = CGDL + BIN_L * LCGDL + BIN_W * WCGDL + BIN_WL * PCGDL
    CKAPPAS_i      = CKAPPAS + BIN_L * LCKAPPAS + BIN_W * WCKAPPAS + BIN_WL * PCKAPPAS
    CKAPPAD_i      = CKAPPAD + BIN_L * LCKAPPAD + BIN_W * WCKAPPAD + BIN_WL * PCKAPPAD
    ALPHA0_i       = ALPHA0 + BIN_L * LALPHA0 + BIN_W * WALPHA0 + BIN_WL * PALPHA0
    BETA0_i        = BETA0 + BIN_L * LBETA0 + BIN_W * WBETA0 + BIN_WL * PBETA0
    KVTH0WE_i      = KVTH0WE + BIN_L * LKVTH0WE  + BIN_W * WKVTH0WE + BIN_WL * PKVTH0WE
    K2WE_i         = K2WE + BIN_L * LK2WE + BIN_W * WK2WE + BIN_WL * PK2WE
    KU0WE_i        = KU0WE + BIN_L * LKU0WE + BIN_W * WKU0WE + BIN_WL * PKU0WE
    AGIDL_i        = AGIDL + BIN_L * LAGIDL + BIN_W * WAGIDL + BIN_WL * PAGIDL
    BGIDL_i        = BGIDL + BIN_L * LBGIDL + BIN_W * WBGIDL + BIN_WL * PBGIDL
    CGIDL_i        = CGIDL + BIN_L * LCGIDL + BIN_W * WCGIDL + BIN_WL * PCGIDL
    EGIDL_i        = EGIDL + BIN_L * LEGIDL + BIN_W * WEGIDL + BIN_WL * PEGIDL
    AGISL_i        = AGISL + BIN_L * LAGISL + BIN_W * WAGISL + BIN_WL * PAGISL
    BGISL_i        = BGISL + BIN_L * LBGISL + BIN_W * WBGISL + BIN_WL * PBGISL
    CGISL_i        = CGISL + BIN_L * LCGISL + BIN_W * WCGISL + BIN_WL * PCGISL
    EGISL_i        = EGISL + BIN_L * LEGISL + BIN_W * WEGISL + BIN_WL * PEGISL
    UTE_i          = UTE + BIN_L * LUTE + BIN_W * WUTE + BIN_WL * PUTE
    UA1_i          = UA1 + BIN_L * LUA1 + BIN_W * WUA1 + BIN_WL * PUA1
    UC1_i          = UC1 + BIN_L * LUC1 + BIN_W * WUC1 + BIN_WL * PUC1
    UD1_i          = UD1 + BIN_L * LUD1 + BIN_W * WUD1 + BIN_WL * PUD1
    EU1_i          = EU1 + BIN_L * LEU1 + BIN_W * WEU1 + BIN_WL * PEU1
    UCSTE_i        = UCSTE + BIN_L * LUCSTE + BIN_W * WUCSTE + BIN_WL * PUCSTE
    PRT_i          = PRT + BIN_L * LPRT + BIN_W * WPRT + BIN_WL * PPRT
    AT_i           = AT + BIN_L * LAT + BIN_W * WAT + BIN_WL * PAT
    PTWGT_i        = PTWGT + BIN_L * LPTWGT + BIN_W * WPTWGT + BIN_WL * PPTWGT
    IIT_i          = IIT + BIN_L * LIIT + BIN_W * WIIT + BIN_WL * PIIT
    TGIDL_i        = TGIDL + BIN_L * LTGIDL + BIN_W * WTGIDL + BIN_WL * PTGIDL
    IGT_i          = IGT + BIN_L * LIGT + BIN_W * WIGT + BIN_WL * PIGT
    AIGBINV_i      = AIGBINV + BIN_L * LAIGBINV + BIN_W * WAIGBINV + BIN_WL * PAIGBINV
    BIGBINV_i      = BIGBINV + BIN_L * LBIGBINV + BIN_W * WBIGBINV + BIN_WL * PBIGBINV
    CIGBINV_i      = CIGBINV + BIN_L * LCIGBINV + BIN_W * WCIGBINV + BIN_WL * PCIGBINV
    EIGBINV_i      = EIGBINV + BIN_L * LEIGBINV + BIN_W * WEIGBINV + BIN_WL * PEIGBINV
    NIGBINV_i      = NIGBINV + BIN_L * LNIGBINV + BIN_W * WNIGBINV + BIN_WL * PNIGBINV
    AIGBACC_i      = AIGBACC + BIN_L * LAIGBACC + BIN_W * WAIGBACC + BIN_WL * PAIGBACC
    BIGBACC_i      = BIGBACC + BIN_L * LBIGBACC + BIN_W * WBIGBACC + BIN_WL * PBIGBACC
    CIGBACC_i      = CIGBACC + BIN_L * LCIGBACC + BIN_W * WCIGBACC + BIN_WL * PCIGBACC
    NIGBACC_i      = NIGBACC + BIN_L * LNIGBACC + BIN_W * WNIGBACC + BIN_WL * PNIGBACC
    AIGC_i         = AIGC + BIN_L * LAIGC + BIN_W * WAIGC + BIN_WL * PAIGC
    BIGC_i         = BIGC + BIN_L * LBIGC + BIN_W * WBIGC + BIN_WL * PBIGC
    CIGC_i         = CIGC + BIN_L * LCIGC + BIN_W * WCIGC + BIN_WL * PCIGC
    AIGS_i         = AIGS + BIN_L * LAIGS + BIN_W * WAIGS + BIN_WL * PAIGS
    BIGS_i         = BIGS + BIN_L * LBIGS + BIN_W * WBIGS + BIN_WL * PBIGS
    CIGS_i         = CIGS + BIN_L * LCIGS + BIN_W * WCIGS + BIN_WL * PCIGS
    AIGD_i         = AIGD + BIN_L * LAIGD + BIN_W * WAIGD + BIN_WL * PAIGD
    BIGD_i         = BIGD + BIN_L * LBIGD + BIN_W * WBIGD + BIN_WL * PBIGD
    CIGD_i         = CIGD + BIN_L * LCIGD + BIN_W * WCIGD + BIN_WL * PCIGD
    POXEDGE_i      = POXEDGE + BIN_L * LPOXEDGE + BIN_W * WPOXEDGE + BIN_WL * PPOXEDGE
    DLCIG_i        = DLCIG + BIN_L * LDLCIG + BIN_W * WDLCIG + BIN_WL * PDLCIG
    DLCIGD_i       = DLCIGD + BIN_L * LDLCIGD + BIN_W * WDLCIGD + BIN_WL * PDLCIGD
    NTOX_i         = NTOX + BIN_L * LNTOX + BIN_W * WNTOX + BIN_WL * PNTOX
    KT1_i          = KT1 + BIN_L * LKT1 + BIN_W * WKT1 + BIN_WL * PKT1
    KT2_i          = KT2 + BIN_L * LKT2 + BIN_W * WKT2 + BIN_WL * PKT2
    PSATB_i        = PSATB + BIN_L * LPSATB + BIN_W * WPSATB + BIN_WL * PPSATB
    A1_i           = A1 + BIN_L * LA1 + BIN_W * WA1 + BIN_WL * PA1
    A11_i          = A11 + BIN_L * LA11 + BIN_W * WA11 + BIN_WL * PA11
    A2_i           = A2 + BIN_L * LA2 + BIN_W * WA2 + BIN_WL * PA2
    A21_i          = A21 + BIN_L * LA21 + BIN_W * WA21 + BIN_WL * PA21
    K0_i           = K0 + BIN_L * LK0 + BIN_W * WK0 + BIN_WL * PK0
    M0_i           = M0 + BIN_L * LM0 + BIN_W * WM0 + BIN_WL * PM0
    K01_i          = K01 + BIN_L * LK01 + BIN_W * WK01 + BIN_WL * PK01
    M01_i          = M01 + BIN_L * LM01 + BIN_W * WM01 + BIN_WL * PM01
    NFACTOREDGE_i  = NFACTOREDGE + BIN_L * LNFACTOREDGE + BIN_W * WNFACTOREDGE + BIN_WL * PNFACTOREDGE
    NDEPEDGE_i     = NDEPEDGE + BIN_L * LNDEPEDGE + BIN_W * WNDEPEDGE + BIN_WL * PNDEPEDGE
    CITEDGE_i      = CITEDGE + BIN_L * LCITEDGE + BIN_W * WCITEDGE + BIN_WL * PCITEDGE
    CDSCDEDGE_i    = CDSCDEDGE + BIN_L * LCDSCDEDGE + BIN_W * WCDSCDEDGE + BIN_WL * PCDSCDEDGE
    CDSCBEDGE_i    = CDSCBEDGE + BIN_L * LCDSCBEDGE + BIN_W * WCDSCBEDGE + BIN_WL * PCDSCBEDGE
    ETA0EDGE_i     = ETA0EDGE + BIN_L * LETA0EDGE + BIN_W * WETA0EDGE + BIN_WL * PETA0EDGE
    ETABEDGE_i     = ETABEDGE + BIN_L * LETABEDGE + BIN_W * WETABEDGE + BIN_WL * PETABEDGE
    KT1EDGE_i      = KT1EDGE + BIN_L * LKT1EDGE + BIN_W * WKT1EDGE + BIN_WL * PKT1EDGE
    KT1LEDGE_i     = KT1LEDGE + BIN_L * LKT1LEDGE + BIN_W * WKT1LEDGE + BIN_WL * PKT1LEDGE
    KT2EDGE_i      = KT2EDGE + BIN_L * LKT2EDGE + BIN_W * WKT2EDGE + BIN_WL * PKT2EDGE
    KT1EXPEDGE_i   = KT1EXPEDGE + BIN_L * LKT1EXPEDGE + BIN_W * WKT1EXPEDGE + BIN_WL * PKT1EXPEDGE
    TNFACTOREDGE_i = TNFACTOREDGE + BIN_L * LTNFACTOREDGE + BIN_W * WTNFACTOREDGE + BIN_WL * PTNFACTOREDGE
    TETA0EDGE_i    = TETA0EDGE + BIN_L * LTETA0EDGE + BIN_W * WTETA0EDGE + BIN_WL * PTETA0EDGE
    K2EDGE_i       = K2EDGE + BIN_L * LK2EDGE + BIN_W * WK2EDGE + BIN_WL * PK2EDGE
    KVTH0EDGE_i    = KVTH0EDGE + BIN_L * LKVTH0EDGE + BIN_W * WKVTH0EDGE + BIN_WL * PKVTH0EDGE
    STK2EDGE_i     = STK2EDGE + BIN_L * LSTK2EDGE + BIN_W * WSTK2EDGE + BIN_WL * PSTK2EDGE
    STETA0EDGE_i   = STETA0EDGE + BIN_L * LSTETA0EDGE + BIN_W * WSTETA0EDGE + BIN_WL * PSTETA0EDGE
    C0_i           = C0 + BIN_L * LC0 + BIN_W * WC0 + BIN_WL * PC0
    C01_i          = C01 + BIN_L * LC01 + BIN_W * WC01 + BIN_WL * PC01
    C0SI_i         = C0SI + BIN_L * LC0SI + BIN_W * WC0SI + BIN_WL * PC0SI
    C0SI1_i        = C0SI1 + BIN_L * LC0SI1 + BIN_W * WC0SI1 + BIN_WL * PC0SI1
    C0SISAT_i      = C0SISAT + BIN_L * LC0SISAT + BIN_W * WC0SISAT + BIN_WL * PC0SISAT
    C0SISAT1_i     = C0SISAT1 + BIN_L * LC0SISAT1 + BIN_W * WC0SISAT1 + BIN_WL * PC0SISAT1

    if (ASYMMOD != 0):
        CDSCDR_i  = CDSCDR + BIN_L * LCDSCDR + BIN_W * WCDSCDR + BIN_WL * PCDSCDR
        ETA0R_i   = ETA0R + BIN_L * LETA0R + BIN_W * WETA0R + BIN_WL * PETA0R
        U0R_i     = U0R + BIN_L * LU0R + BIN_W * WU0R + BIN_WL * PU0R
        UAR_i     = UAR + BIN_L * LUAR + BIN_W * WUAR + BIN_WL * PUAR
        UDR_i     = UDR + BIN_L * LUDR + BIN_W * WUDR + BIN_WL * PUDR
        UCSR_i    = UCSR + BIN_L * LUCSR + BIN_W * WUCSR + BIN_WL * PUCSR
        UCR_i     = UCR + BIN_L * LUCR + BIN_W * WUCR + BIN_WL * PUCR
        PCLMR_i   = PCLMR + BIN_L * LPCLMR + BIN_W * WPCLMR + BIN_WL * PPCLMR
        PDIBLCR_i = PDIBLCR + BIN_L * LPDIBLCR + BIN_W * WPDIBLCR + BIN_WL * PPDIBLCR
        VSATR_i   = VSATR + BIN_L * LVSATR + BIN_W * WVSATR + BIN_WL * PVSATR
        PSATR_i   = PSATR + BIN_L * LPSATR + BIN_W * WPSATR + BIN_WL * PPSATR
        PTWGR_i   = PTWGR + BIN_L * LPTWGR + BIN_W * WPTWGR + BIN_WL * PPTWGR
    else:
        CDSCDR_i  = 0.0
        ETA0R_i   = 0.0
        U0R_i     = 0.0
        UAR_i     = 0.0
        UDR_i     = 0.0
        UCSR_i    = 0.0
        UCR_i     = 0.0
        PCLMR_i   = 0.0
        PDIBLCR_i = 0.0
        VSATR_i   = 0.0
        PSATR_i   = 0.0
        PTWGR_i   = 0.0    

    # Geometrical scaling
    T0        = NDEPL1 * max(Inv_L**NDEPLEXP1 - Inv_Llong**NDEPLEXP1, 0.0) + NDEPL2 * max(Inv_L**NDEPLEXP2 - Inv_Llong**NDEPLEXP2, 0.0)
    T1        = NDEPW * max(Inv_W**NDEPWEXP - Inv_Wwide**NDEPWEXP, 0.0) + NDEPWL * (Inv_W * Inv_L)**NDEPWLEXP
    NDEP_i    = NDEP_i * (1.0 + T0 + T1)
    T0        = NFACTORL * max(Inv_L**NFACTORLEXP - Inv_Llong**NFACTORLEXP, 0.0)
    T1        = NFACTORW * max(Inv_W**NFACTORWEXP - Inv_Wwide**NFACTORWEXP, 0.0) + NFACTORWL * Inv_WL**NFACTORWLEXP
    NFACTOR_i = NFACTOR_i * (1.0 + T0 + T1)
    T0        = (1.0 + CDSCDL * max(Inv_L**CDSCDLEXP - Inv_Llong**CDSCDLEXP, 0.0))
    CDSCD_i   = CDSCD_i * T0
    if (ASYMMOD != 0):
        CDSCDR_i = CDSCDR_i * T0    
    CDSCB_i = CDSCB_i * (1.0 + CDSCBL * max(Inv_L**CDSCBLEXP - Inv_Llong**CDSCBLEXP, 0.0))
    U0_i    = MULU0 * U0_i
    if (MOBSCALE != 1):
        if (U0LEXP > 0.0):
            U0_i = U0_i * (1.0 - U0L * max(Inv_L**U0LEXP - Inv_Llong**U0LEXP, 0.0))
            if (ASYMMOD != 0):
                U0R_i = U0R_i * (1.0 - U0L * max(Inv_L**U0LEXP - Inv_Llong**U0LEXP, 0.0))
        else:
            U0_i = U0_i * (1.0 - U0L)
            if (ASYMMOD != 0):
                U0R_i = U0R_i * (1.0 - U0L)
    else:
        U0_i = U0_i * (1.0 - (UP1 * lexp(-Leff / LP1)) - (UP2 * lexp(-Leff / LP2)))
        if (ASYMMOD != 0):
            U0R_i = U0R_i * (1.0 - (UP1 * lexp(-Leff / LP1)) - (UP2 * lexp(-Leff / LP2)))
    T0   = UAL * max(Inv_L**UALEXP - Inv_Llong**UALEXP, 0.0)
    T1   = UAW * max(Inv_W**UAWEXP - Inv_Wwide**UAWEXP, 0.0) + UAWL * Inv_WL**UAWLEXP
    UA_i = UA_i * (1.0 + T0 + T1)
    if (ASYMMOD != 0):
        UAR_i = UAR_i * (1.0 + T0 + T1)    
    T0   = EUL * max(Inv_L**EULEXP - Inv_Llong**EULEXP, 0.0)
    T1   = EUW * max(Inv_W**EUWEXP - Inv_Wwide**EUWEXP, 0.0) + EUWL * Inv_WL**EUWLEXP
    EU_i = EU_i * (1.0 + T0 + T1)
    T0   = 1.0 + UDL * max(Inv_L**UDLEXP - Inv_Llong**UDLEXP, 0.0)
    UD_i = UD_i * T0
    if (ASYMMOD != 0):
        UDR_i = UDR_i * T0    
    T0   = UCL * max(Inv_L**UCLEXP - Inv_Llong**UCLEXP, 0.0)
    T1   = UCW * max(Inv_W**UCWEXP - Inv_Wwide**UCWEXP, 0.0) + UCWL * Inv_WL**UCWLEXP
    UC_i = UC_i * (1.0 + T0 + T1)
    if (ASYMMOD != 0):
        UCR_i = UCR_i * (1.0 + T0 + T1)    
    T0     = max(Inv_L**DSUB - Inv_Llong**DSUB, 0.0)
    ETA0_i = ETA0_i * T0
    if (ASYMMOD != 0):
        ETA0R_i = ETA0R_i * T0
    ETAB_i   = ETAB_i * max(Inv_L**ETABEXP - Inv_Llong**ETABEXP, 0.0)
    T0       = 1.0 + PDIBLCL * max(Inv_L**PDIBLCLEXP - Inv_Llong**PDIBLCLEXP, 0.0)
    PDIBLC_i = PDIBLC_i * T0
    if (ASYMMOD != 0):
        PDIBLCR_i = PDIBLCR_i * T0
    T0       = DELTA_i * (1.0 + DELTAL * max(Inv_L**DELTALEXP - Inv_Llong**DELTALEXP, 0.0))
    DELTA_i  = min(T0, 0.5)
    FPROUT_i = FPROUT_i * (1.0 + FPROUTL * max(Inv_L**FPROUTLEXP - Inv_Llong**FPROUTLEXP, 0.0))
    T0       = (1.0 + PCLML * max(Inv_L**PCLMLEXP - Inv_Llong**PCLMLEXP, 0.0))
    PCLM_i   = PCLM_i * T0
    PCLM_i   = max(PCLM_i, 0.0)
    if (ASYMMOD != 0):
        PCLMR_i = PCLMR_i * T0
        PCLMR_i = max(PCLMR_i, 0.0)
    T0     = VSATL * max(Inv_L**VSATLEXP - Inv_Llong**VSATLEXP, 0.0)
    T1     = VSATW * max(Inv_W**VSATWEXP - Inv_Wwide**VSATWEXP, 0.0) + VSATWL * Inv_WL**VSATWLEXP
    VSAT_i = VSAT_i * (1.0 + T0 + T1)
    if (ASYMMOD != 0):
        VSATR_i = VSATR_i * (1.0 + T0 + T1)
    PSAT_i = max(PSAT_i * (1.0 + PSATL * max(Inv_L**PSATLEXP - Inv_Llong**PSATLEXP, 0.0)), 0.25)
    if (ASYMMOD != 0):
        PSATR_i = max(PSATR_i * (1.0 + PSATL * max(Inv_L**PSATLEXP - Inv_Llong**PSATLEXP, 0.0)), 0.25)
    T0     = (1.0 + PTWGL * max(Inv_L**PTWGLEXP - Inv_Llong**PTWGLEXP, 0.0))
    PTWG_i = PTWG_i * T0
    if (ASYMMOD != 0):
        PTWGR_i = PTWGR_i * T0
    ALPHA0_i = ALPHA0_i * (1.0 + ALPHA0L * max(Inv_L**ALPHA0LEXP - Inv_Llong**ALPHA0LEXP, 0.0))
    AGIDL_i  = AGIDL_i * (1.0 + AGIDLL * Inv_L + AGIDLW * Inv_W)
    AGISL_i  = AGISL_i * (1.0 + AGISLL * Inv_L + AGISLW * Inv_W)
    AIGC_i   = AIGC_i * (1.0 + AIGCL * Inv_L + AIGCW * Inv_W)
    AIGS_i   = AIGS_i * (1.0 + AIGSL * Inv_L + AIGSW * Inv_W)
    AIGD_i   = AIGD_i * (1.0 + AIGDL * Inv_L + AIGDW * Inv_W)
    PIGCD_i  = PIGCD * (1.0 + PIGCDL * Inv_L)
    T0       = NDEPCVL1 * max(Inv_Lact**NDEPCVLEXP1 - Inv_Llong**NDEPCVLEXP1, 0.0) + NDEPCVL2 * max(Inv_Lact**NDEPCVLEXP2 - Inv_Llong**NDEPCVLEXP2, 0.0)
    T1       = NDEPCVW * max(Inv_Wact**NDEPCVWEXP - Inv_Wwide**NDEPCVWEXP, 0.0) + NDEPCVWL * (Inv_Wact * Inv_Lact)**NDEPCVWLEXP
    NDEPCV_i = NDEPCV_i * (1.0 + T0 + T1)
    T0       = VFBCVL * max(Inv_Lact**VFBCVLEXP - Inv_Llong**VFBCVLEXP, 0.0)
    T1       = VFBCVW * max(Inv_Wact**VFBCVWEXP - Inv_Wwide**VFBCVWEXP, 0.0) + VFBCVWL * Inv_WL**VFBCVWLEXP
    VFBCV_i  = VFBCV_i * (1.0 + T0 + T1)
    T0       = VSATCVL * max(Inv_Lact**VSATCVLEXP - Inv_Llong**VSATCVLEXP, 0.0)
    T1       = VSATCVW * max(Inv_W**VSATCVWEXP - Inv_Wwide**VSATCVWEXP, 0.0) + VSATCVWL * Inv_WL**VSATCVWLEXP
    VSATCV_i = VSATCV_i * (1.0 + T0 + T1)
    PCLMCV_i = PCLMCV_i * (1.0 + PCLMCVL * max(Inv_Lact**PCLMCVLEXP - Inv_Llong**PCLMCVLEXP, 0.0))
    PCLMCV_i = max(PCLMCV_i, 0.0)
    T0       = K1L * max(Inv_L**K1LEXP - Inv_Llong**K1LEXP, 0.0)
    T1       = K1W * max(Inv_W**K1WEXP - Inv_Wwide**K1WEXP, 0.0) + K1WL * Inv_WL**K1WLEXP
    K1_i     = K1_i * (1.0 + T0 + T1)
    T0       = K2L * max(Inv_L**K2LEXP - Inv_Llong**K2LEXP, 0.0)
    T1       = K2W * max(Inv_W**K2WEXP - Inv_Wwide**K2WEXP, 0.0) + K2WL * Inv_WL**K2WLEXP
    K2_i     = K2_i * (1.0 + T0 + T1)
    PRWB_i   = PRWB_i * (1.0 + PRWBL * max(Inv_L**PRWBLEXP - Inv_Llong**PRWBLEXP, 0.0))

    # Global scaling parameters for temperature
    UTE_i   = UTE_i * (1.0 + Inv_L * UTEL)
    UA1_i   = UA1_i * (1.0 + Inv_L * UA1L)
    UD1_i   = UD1_i * (1.0 + Inv_L * UD1L)
    AT_i    = AT_i * (1.0 + Inv_L * ATL)
    PTWGT_i = PTWGT_i * (1.0 + Inv_L * PTWGTL)

    if (RDSMOD == 1):
        RSW_i = RSW_i * (1.0 + RSWL * max(Inv_L**RSWLEXP - Inv_Llong**RSWLEXP, 0.0))
        RDW_i = RDW_i * (1.0 + RDWL * max(Inv_L**RDWLEXP - Inv_Llong**RDWLEXP, 0.0))
    else:
        RDSW_i = RDSW_i * (1.0 + RDSWL * max(Inv_L**RDSWLEXP - Inv_Llong**RDSWLEXP, 0.0))

    # Parameter checking
    if (UCS_i < 1.0):
        UCS_i = 1.0
    elif (UCS_i > 2.0):
        UCS_i = 2.0
    if (ASYMMOD != 0):
        if (UCSR_i < 1.0):
            UCSR_i = 1.0
        elif (UCSR_i > 2.0):
            UCSR_i = 2.0
    if (CGIDL_i < 0.0):
        print("Fatal: CGIDL_i = %e is negative.", CGIDL_i)    
    if (CGISL_i < 0.0):
        print("Fatal: CGISL_i = %e is negative.", CGISL_i)    
    if (CKAPPAD_i <= 0.0):
        print("Fatal: CKAPPAD_i = %e is non-positive.", CKAPPAD_i)    
    if (CKAPPAS_i <= 0.0):
        print("Fatal: CKAPPAS_i = %e is non-positive.", CKAPPAS_i)
    if (PDITS_i < 0.0):
        print("Fatal: PDITS_i = %e is negative.", PDITS_i)
    if (CIT_i < 0.0):
        print("Fatal: CIT_i = %e is negative.", CIT_i)
    if (NFACTOR_i < 0.0):
        print("Fatal: NFACTOR_i = %e is negative.", NFACTOR_i)
    if (K1_i < 0.0):
        print("Fatal: K1_i = %e is negative.", K1_i)
    if (NSD_i <= 0.0):
        print("Fatal: NSD_i = %e is non-positive.", NSD_i)
    if (NDEP_i <= 0.0):
        print("Fatal: NDEP_i = %e is non-positive.", NDEP_i)
    if (NDEPCV_i <= 0.0):
        print("Fatal: NDEPCV_i = %e is non-positive.", NDEPCV_i)
    if (IGBMOD != 0):
        if (NIGBINV_i <= 0.0):
            print("Fatal: NIGBINV_i = %e is non-positive.", NIGBINV_i)
        if (NIGBACC_i <= 0.0):
            print("Fatal: NIGBACC_i = %e is non-positive.", NIGBACC_i)
    if (IGCMOD != 0):
        if (POXEDGE_i <= 0.0):
            print("Fatal: POXEDGE_i = %e is non-positive.", POXEDGE_i)
    if (CDSCD_i < 0.0):
        print("Fatal: CDSCD_i = %e is negative.", CDSCD_i)
    if (ASYMMOD != 0):
        if (CDSCDR_i < 0.0):
            print("Fatal: CDSCDR_i = %e is negative.", CDSCDR_i)
    if (DLCIG_i < 0.0):
        print("Warning: DLCIG = %e is negative, setting it to 0.", DLCIG_i)
        DLCIG_i = 0.0
    if (DLCIGD_i < 0.0):
        print("Warning: DLCIGD = %e is negative, setting it to 0.", DLCIGD_i)
        DLCIGD_i = 0.0
    if (M0_i < 0.0):
        print("Warning: M0_i = %e is negative, setting it to 0.", M0_i)
        M0_i = 0.0
    if (U0_i <= 0.0):
        print("Warning: U0_i = %e is non-positive, setting it to the default value.", U0_i)
        U0_i = 0.067
    if (UA_i < 0.0):
        print("Warning: UA_i = %e is negative, setting it to 0.", UA_i)
        UA_i = 0.0
    if (EU_i < 0.0):
        print("Warning: EU_i = %e is negative, setting it to 0.", EU_i)
        EU_i = 0.0
    if (UD_i < 0.0):
        print("Warning: UD_i = %e is negative, setting it to 0.", UD_i)
        UD_i = 0.0
    if (UCS_i < 0.0):
        print("Warning: UCS_i = %e is negative, setting it to 0.", UCS_i)
        UCS_i = 0.0

    # Process drain series resistance
    DMCGeff = DMCG - DMCGT
    DMCIeff = DMCI
    DMDGeff = DMDG - DMCGT

    # Processing S/D resistances and conductances
    if "NRS" in keys(param):
        RSourceGeo = RSH * NRS
    elif (RGEOMOD > 0 and RSH > 0.0):
        RSourceGeo = BSIMBULKRdseffGeo(NF, GEOMOD, RGEOMOD, MINZ, Weff, RSH, DMCGeff, DMCIeff, DMDGeff, 1)
    else:
        RSourceGeo = 0.0

    if "NRD" in keys(param):
        RDrainGeo = RSH * NRD
    elif (RGEOMOD > 0 and RSH > 0.0):
        RDrainGeo = BSIMBULKRdseffGeo(NF, GEOMOD, RGEOMOD, MINZ, Weff, RSH, DMCGeff, DMCIeff, DMDGeff, 0)
    else:
        RDrainGeo = 0.0

    # Clamping of S/D resistances
    if (RDSMOD == 0):
        if (RSourceGeo < minr):
            RSourceGeo = 0.0
        if (RDrainGeo < minr):
            RDrainGeo = 0.0
    else:
        if (RSourceGeo <= minr):
            RSourceGeo = minr
        if (RDrainGeo <= minr):
            RDrainGeo = minr
    if (RDSMOD == 1):
        if (RSWMIN_i <= 0.0):
            RSWMIN_i = 0.0
        if (RDWMIN_i <= 0.0):
            RDWMIN_i = 0.0
        if (RSW_i <= 0.0):
            RSW_i = 0.0
        if (RDW_i <= 0.0):
            RDW_i = 0.0
    else:
        if (RDSWMIN_i <= 0.0):
            RDSWMIN_i = 0.0
        if (RDSW_i <= 0.0):
            RDSW_i = 0.0

    # Body resistance network
    if (RBODYMOD != 0):
        Lnl  = lln(Leff * 1.0e6)
        Lnw  = lln(Weff * 1.0e6)
        Lnnf = lln(NF)
        Bodymode = 5
        Rbpb = RBPB
        Rbpd = RBPD
        Rbps = RBPS
        Rbdb = RBDB
        Rbsb = RBSB
        if ("RBPS0" not in keys(param)) or ("RBPD0" not in keys(param)):
            Bodymode = 1
        elif ("RBSBX0" not in keys(param)) and ("RBSBY0" not in keys(param)) or ("RBDBX0" not in keys(param)) and ("RBDBY0" not in keys(param)):
            Bodymode = 3
        if (RBODYMOD == 2):
            if (Bodymode == 5):
                Rbsbx = RBSBX0 * lexp(RBSDBXL * Lnl + RBSDBXW * Lnw + RBSDBXNF * Lnnf)
                Rbsby = RBSBY0 * lexp(RBSDBYL * Lnl + RBSDBYW * Lnw + RBSDBYNF * Lnnf)
                Rbsb  = Rbsbx * Rbsby / (Rbsbx + Rbsby)
                Rbdbx = RBDBX0 * lexp(RBSDBXL * Lnl + RBSDBXW * Lnw + RBSDBXNF * Lnnf)
                Rbdby = RBDBY0 * lexp(RBSDBYL * Lnl + RBSDBYW * Lnw + RBSDBYNF * Lnnf)
                Rbdb  = Rbdbx * Rbdby / (Rbdbx + Rbdby)
            if (Bodymode == 3 or Bodymode == 5):
                Rbps = RBPS0 * lexp(RBPSL * Lnl + RBPSW * Lnw + RBPSNF * Lnnf)
                Rbpd = RBPD0 * lexp(RBPDL * Lnl + RBPDW * Lnw + RBPDNF * Lnnf)
            Rbpbx = RBPBX0 * lexp(RBPBXL * Lnl + RBPBXW * Lnw + RBPBXNF * Lnnf)
            Rbpby = RBPBY0 * lexp(RBPBYL * Lnl + RBPBYW * Lnw + RBPBYNF * Lnnf)
            Rbpb  = Rbpbx * Rbpby / (Rbpbx + Rbpby)
        if (RBODYMOD == 1 or (RBODYMOD == 2 and Bodymode == 5)):
            if (Rbdb < 1.0e-3):
                Grbdb = 1.0e3  # in mho
            else:
                Grbdb = GBMIN + 1.0 / Rbdb
            if (Rbpb < 1.0e-3):
                Grbpb = 1.0e3
            else:
                Grbpb = GBMIN + 1.0 / Rbpb
            if (Rbps < 1.0e-3):
                Grbps = 1.0e3
            else:
                Grbps = GBMIN + 1.0 / Rbps
            if (Rbsb < 1.0e-3):
                Grbsb = 1.0e3
            else:
                Grbsb = GBMIN + 1.0 / Rbsb
            if (Rbpd < 1.0e-3):
                Grbpd = 1.0e3
            else:
                Grbpd = GBMIN + 1.0 / Rbpd
        elif (RBODYMOD == 2 and Bodymode == 3):
            Grbdb = GBMIN
            Grbsb = GBMIN
            if (Rbpb < 1.0e-3):
                Grbpb = 1.0e3
            else:
                Grbpb = GBMIN + 1.0 / Rbpb
            if (Rbps < 1.0e-3):
                Grbps = 1.0e3
            else:
                Grbps = GBMIN + 1.0 / Rbps
            if (Rbpd < 1.0e-3):
                Grbpd = 1.0e3
            else:
                Grbpd = GBMIN + 1.0 / Rbpd
        elif (RBODYMOD == 2 and Bodymode == 1):
            Grbdb = GBMIN
            Grbsb = GBMIN
            Grbps = 1.0e3
            Grbpd = 1.0e3
            if (Rbpb < 1.0e-3):
                Grbpb = 1.0e3
            else:
                Grbpb = GBMIN + 1.0 / Rbpb

    # Gate process resistance
    Grgeltd = RSHG * (XGW + Weffcj / 3.0 / NGCON) / (NGCON * NF * (Lnew - XGL))
    if (Grgeltd > 0.0):
        Grgeltd = 1.0 / Grgeltd
    else:
        Grgeltd = 1.0e3
        if (RGATEMOD != 0):
            print("Warning: (instance %M) The gate conductance reset to 1.0e3 mho.")

    T0           = TOXE * TOXE
    T1           = TOXE * POXEDGE_i
    T2           = T1 * T1
    ToxRatio     = lexp(NTOX_i * lln(TOXREF / TOXE)) / T0
    ToxRatioEdge = lexp(NTOX_i * lln(TOXREF / T1)) / T2
    Aechvb       = 4.97232e-7 if (TYPE == ntype) else 3.42537e-7
    Bechvb       = 7.45669e11 if (TYPE == ntype) else 1.16645e12
    AechvbEdge   = Aechvb * Weff * ToxRatioEdge
    BechvbEdge   = -Bechvb * TOXE * POXEDGE_i
    Aechvb       = Aechvb * (Weff * Leff * ToxRatio)
    Bechvb       = -Bechvb * TOXE
    Weff_SH      = WTH0 + Weff

    # Parameters for self-heating effects
    if (SHMOD != 0) and (RTH0 > 0.0) and (Weff_SH > 0.0):
        gth = Weff_SH * NF / RTH0
        cth = CTH0 * Weff_SH * NF
    else:
        # Set gth to some value to prevent a singular G matrix
        gth = 1.0
        cth = 0.0

    # Temperature-dependent calculations
    if (TNOM <= -P_CELSIUS0):
        T0 = REFTEMP - P_CELSIUS0
        print("Warning: TNOM = %e C <= %e C. Setting TNOM to %e C.", TNOM, -P_CELSIUS0, T0)
        Tnom = REFTEMP
    else:
        Tnom = TNOM + P_CELSIUS0
    DevTemp = Temp + P_CELSIUS0 + DTEMP

    Vt         = KboQ * DevTemp
    inv_Vt     = 1.0 / Vt
    TRatio     = DevTemp / Tnom
    delTemp    = DevTemp - Tnom
    Vtm        = KboQ * DevTemp
    Vtm0       = KboQ * Tnom
    Eg         = BG0SUB - TBGASUB * DevTemp * DevTemp / (DevTemp + TBGBSUB)
    Eg0        = BG0SUB - TBGASUB * Tnom * Tnom / (Tnom + TBGBSUB)
    T1         = (DevTemp / Tnom) * sqrt(DevTemp / Tnom)
    ni         = NI0SUB * T1 * lexp(Eg / (2.0 * Vtm0) - Eg / (2.0 * Vtm))
    if ((SHMOD != 0) and (RTH0 > 0.0) and (Weff_SH > 0.0)):
        T0   = lln(NDEP_i / ni)
        phib = sqrt(T0 * T0 + 1.0e-6)
    else:
        phib = lln(NDEP_i / ni)
    if ((SHMOD != 0) and (RTH0 > 0.0) and (Weff_SH > 0.0)):
        T0  = lln(NDEPEDGE_i * NSD_i / (ni * ni))
        Vbi_edge = sqrt(T0 * T0 + 1.0e-6)
    else:
        Vbi_edge = lln(NDEPEDGE_i * NSD_i / (ni * ni))
    if (NGATE_i > 0.0):
        Vfbsdr = -devsign * Vt * lln(NGATE_i / NSD_i) + VFBSDOFF
    else:
        Vfbsdr = 0.0

    # Short channel effects
    Phist     = max(0.4 + Vt * phib + PHIN_i, 0.4)
    sqrtPhist = sqrt(Phist)
    T1DEP     = sqrt(2.0 * epssi / (q * NDEP_i))
    litl      = sqrt((epssi / epsox) * TOXE * XJ_i)
    NFACTOR_t = NFACTOR_i * hypsmooth((1.0 + TNFACTOR * (TRatio - 1.0)), 1e-3)
    ETA0_t    = ETA0_i * (1.0 + TETA0 * (TRatio - 1.0))
    if (ASYMMOD != 0):
        ETA0R_t = ETA0R_i * (1.0 + TETA0 * (TRatio - 1.0))

    # Mobility degradation
    eta_mu = (Oneby3 * ETAMOB) if (TYPE != ntype) else (0.5 * ETAMOB)
    U0_t   = U0_i * TRatio**UTE_i
    UA_t   = UA_i * hypsmooth(1.0 + UA1_i * delTemp - 1.0e-6, 1.0e-3)
    UC_t   = UC_i * hypsmooth(1.0 + UC1_i * delTemp - 1.0e-6, 1.0e-3)
    UD_t   = UD_i * TRatio**UD1_i
    UCS_t  = UCS_i * TRatio**UCSTE_i
    EU_t   = EU_i * hypsmooth((1.0 + EU1_i * (TRatio - 1.0)), 1e-3)
    if (ASYMMOD != 0):
        U0R_t  = U0R_i * TRatio**UTE_i
        UAR_t  = UAR_i * hypsmooth(1.0 + UA1_i * delTemp - 1.0e-6, 1.0e-3)
        UCR_t  = UCR_i * hypsmooth(1.0 + UC1_i * delTemp - 1.0e-6, 1.0e-3)
        UDR_t  = UDR_i * TRatio**UD1_i
        UCSR_t = UCSR_i * TRatio**UCSTE_i
    else:
        U0R_t  = 0.0
        UAR_t  = 0.0
        UCR_t  = 0.0
        UDR_t  = 0.0
        UCSR_t = 0.0
    rdstemp = TRatio**PRT_i
    VSAT_t  = VSAT_i * TRatio**-AT_i
    if (VSAT_t < 100.0):
        print("Warning: VSAT(%f) = %e is less than 100, setting it to 100.", DevTemp, VSAT_t)
        VSAT_t = 100.0
    if (HVMOD == 1):
        rdstemphv = TRatio**PRTHV
        VDRIFT_t  = VDRIFT * TRatio**-ATHV
    if (ASYMMOD != 0):
        VSATR_t = VSATR_i * TRatio**-AT_i
        if(VSATR_t < 100.0):
            print("Warning: VSATR(%f) = %e is less than 100, setting it to 100.", DevTemp, VSATR_t)
            VSATR_t = 100.0

    VSATCV_t = VSATCV_i * TRatio**-AT_i
    if (VSATCV_t < 100.0):
        print("Warning: VSATCV(%f) = %e is less than 100, setting it to 100.", DevTemp, VSATCV_t)
        VSATCV_t = 100.0
    DELTA_t = 1.0 / ( hypsmooth((1.0 / DELTA_i) * (1.0 + TDELTA * delTemp) - 2.0 , 1.0e-3) + 2.0)
    PTWG_t  = PTWG_i * hypsmooth(1.0 - PTWGT_i * delTemp - 1.0e-6, 1.0e-3)
    if (ASYMMOD != 0):
        PTWGR_t = PTWGR_i * hypsmooth(1.0 - PTWGT_i * delTemp - 1.0e-6, 1.0e-3)
    A1_t    = A1_i * hypsmooth(1.0 + A11_i * delTemp - 1.0e-6, 1.0e-3)
    A2_t    = A2_i * hypsmooth(1.0 + A21_i * delTemp - 1.0e-6, 1.0e-3)
    BETA0_t = BETA0_i * TRatio**IIT_i
    BGIDL_t = BGIDL_i * hypsmooth(1.0 + TGIDL_i * delTemp - 1.0e-6, 1.0e-3)
    BGISL_t = BGISL_i * hypsmooth(1.0 + TGIDL_i * delTemp - 1.0e-6, 1.0e-3)
    igtemp  = lexp(IGT_i * lln(TRatio))
    K0_t    = K0_i * hypsmooth(1.0 + K01_i * delTemp - 1.0e-6, 1.0e-3)
    M0_t    = M0_i * hypsmooth(1.0 + M01_i * delTemp - 1.0e-6, 1.0e-3)
    C0_t    = C0_i * hypsmooth(1.0 + C01_i * delTemp - 1.0e-6, 1.0e-3)
    C0SI_t  = C0SI_i * hypsmooth(1.0 + C0SI1_i * delTemp - 1.0e-6, 1.0e-3)
    C0SISAT_t = C0SISAT_i * hypsmooth(1.0 + C0SISAT1_i * delTemp - 1.0e-6, 1.0e-3)

    # Diode model temperature effects
    CJS_t     = CJS * hypsmooth(1.0 + TCJ * delTemp - 1.0e-6, 1.0e-3)
    CJD_t     = CJD * hypsmooth(1.0 + TCJ * delTemp - 1.0e-6, 1.0e-3)
    CJSWS_t   = CJSWS * hypsmooth(1.0 + TCJSW * delTemp - 1.0e-6, 1.0e-3)
    CJSWD_t   = CJSWD * hypsmooth(1.0 + TCJSW * delTemp - 1.0e-6, 1.0e-3)
    CJSWGS_t  = CJSWGS * hypsmooth(1.0 + TCJSWG * delTemp - 1.0e-6, 1.0e-3)
    CJSWGD_t  = CJSWGD * hypsmooth(1.0 + TCJSWG * delTemp - 1.0e-6, 1.0e-3)
    PBS_t     = hypsmooth(PBS - TPB * delTemp - 0.01, 1.0e-3) + 0.01
    PBD_t     = hypsmooth(PBD - TPB * delTemp - 0.01, 1.0e-3) + 0.01
    PBSWS_t   = hypsmooth(PBSWS - TPBSW * delTemp - 0.01, 1.0e-3) + 0.01
    PBSWD_t   = hypsmooth(PBSWD - TPBSW * delTemp - 0.01, 1.0e-3) + 0.01
    PBSWGS_t  = hypsmooth(PBSWGS - TPBSWG * delTemp - 0.01, 1.0e-3) + 0.01
    PBSWGD_t  = hypsmooth(PBSWGD - TPBSWG * delTemp - 0.01, 1.0e-3) + 0.01
    T0        = Eg0 / Vtm0 - Eg / Vtm
    T1        = lln(TRatio)
    T3        = lexp((T0 + XTIS * T1) / NJS)
    JSS_t     = JSS * T3
    JSWS_t    = JSWS * T3
    JSWGS_t   = JSWGS * T3
    T3        = lexp((T0 + XTID * T1) / NJD)
    JSD_t     = JSD * T3
    JSWD_t    = JSWD * T3
    JSWGD_t   = JSWGD * T3
    JTSS_t    = JTSS * lexp(Eg0 * XTSS * (TRatio - 1.0) / Vtm)
    JTSSWS_t  = JTSSWS * lexp(Eg0 * XTSSWS * (TRatio - 1.0) / Vtm)
    JTSSWGS_t = JTSSWGS * (sqrt(JTWEFF / Weffcj) + 1.0) * lexp(Eg0 * XTSSWGS * (TRatio - 1) / Vtm)
    JTSD_t    = JTSD * lexp(Eg0 * XTSD * (TRatio - 1.0) / Vtm)
    JTSSWD_t  = JTSSWD * lexp(Eg0 * XTSSWD * (TRatio - 1.0) / Vtm)
    JTSSWGD_t = JTSSWGD * (sqrt(JTWEFF / Weffcj) + 1.0) * lexp(Eg0 * XTSSWGD * (TRatio - 1) / Vtm)

    # All NJT*'s smoothed to 0.01 to prevent divide by zero/negative values
    NJTS_t     = hypsmooth(NJTS * (1.0 + TNJTS * (TRatio - 1.0)) - 0.01, 1.0e-3) + 0.01
    NJTSSW_t   = hypsmooth(NJTSSW * (1.0 + TNJTSSW * (TRatio - 1.0)) - 0.01, 1.0e-3) + 0.01
    NJTSSWG_t  = hypsmooth(NJTSSWG * (1.0 + TNJTSSWG * (TRatio - 1.0)) - 0.01, 1.0e-3) + 0.01
    NJTSD_t    = hypsmooth(NJTSD * (1.0 + TNJTSD * (TRatio - 1.0)) - 0.01, 1.0e-3) + 0.01
    NJTSSWD_t  = hypsmooth(NJTSSWD * (1.0 + TNJTSSWD * (TRatio - 1.0)) - 0.01, 1.0e-3) + 0.01
    NJTSSWGD_t = hypsmooth(NJTSSWGD * (1.0 + TNJTSSWGD * (TRatio - 1.0)) - 0.01, 1.0e-3) + 0.01

    # Effective S/D junction area and perimeters
    temp_PSeff, temp_PDeff, temp_ASeff, temp_ADeff = BSIMBULKPAeffGeo(NF, GEOMOD, MINZ, Weffcj, DMCGeff, DMCIeff, DMDGeff)
    if "AS" in keys(param):
        ASeff = AS * WMLT * LMLT
    else:
        ASeff = temp_ASeff
    if (ASeff < 0.0):
        print("Warning: (instance %M) ASeff = %e is negative. Set to 0.0.", ASeff)
        ASeff = 0.0
    if "AD" in keys(param):
        ADeff = AD * WMLT * LMLT
    else:
        ADeff = temp_ADeff
    if (ADeff < 0.0):
        print("Warning: (instance %M) ADeff = %e is negative. Set to 0.0.", ADeff)
        ADeff = 0.0
    if "PS" in keys(param):
        if (PERMOD == 0):
            # PS does not include gate-edge perimeters
            PSeff = PS * WMLT
        else:
            # PS includes gate-edge perimeters
            PSeff = max(PS * WMLT - Weffcj * NF, 0.0)
    else:
        PSeff = temp_PSeff
        if (PSeff < 0.0):
            print("Warning: (instance %M) PSeff = %e is negative. Set to 0.0.", PSeff)
            PSeff = 0.0
    if "PD" in keys(param):
        if (PERMOD == 0):
            # PD does not include gate-edge perimeters
            PDeff = PD * WMLT
        else:
            # PD includes gate-edge perimeters
            PDeff = max(PD * WMLT - Weffcj * NF, 0.0)
    else:
        PDeff = temp_PDeff
        if (PDeff < 0.0):
            print("Warning: (instance %M) PDeff = %e is negative. Set to 0.0.", PDeff)
            PDeff = 0.0

    Isbs = ASeff * JSS_t + PSeff * JSWS_t + Weffcj * NF * JSWGS_t
    if (Isbs > 0.0):
        Nvtms    = Vtm * NJS
        XExpBVS  = lexp(-BVS / Nvtms) * XJBVS
        T2       = max(IJTHSFWD / Isbs, 10.0)
        Tb       = 1.0 + T2 - XExpBVS
        VjsmFwd  = Nvtms * lln(0.5 * (Tb + sqrt(Tb * Tb + 4.0 * XExpBVS)))
        T0       = lexp(VjsmFwd / Nvtms)
        IVjsmFwd = Isbs * (T0 - XExpBVS / T0 + XExpBVS - 1.0)
        SslpFwd  = Isbs * (T0 + XExpBVS / T0) / Nvtms
        T2       = hypsmooth(IJTHSREV / Isbs - 10.0, 1.0e-3) + 10.0
        VjsmRev  = -BVS - Nvtms * lln((T2 - 1.0) / XJBVS)
        T1       = XJBVS * lexp(-(BVS + VjsmRev) / Nvtms)
        IVjsmRev = Isbs * (1.0 + T1)
        SslpRev  = -Isbs * T1 / Nvtms
    else:
        Nvtms    = 0.0
        XExpBVS  = 0.0
        VjsmFwd  = 0.0
        IVjsmFwd = 0.0
        SslpFwd  = 0.0
        VjsmRev  = 0.0
        IVjsmRev = 0.0
        SslpRev  = 0.0

    # Drain-side junction currents
    Isbd = ADeff * JSD_t + PDeff * JSWD_t + Weffcj * NF * JSWGD_t
    if (Isbd > 0.0):
        Nvtmd    = Vtm * NJD
        XExpBVD  = lexp(-BVD / Nvtmd) * XJBVD
        T2       = max(IJTHDFWD / Isbd, 10.0)
        Tb       = 1.0 + T2 - XExpBVD
        VjdmFwd  = Nvtmd * lln(0.5 * (Tb + sqrt(Tb * Tb + 4.0 * XExpBVD)))
        T0       = lexp(VjdmFwd / Nvtmd)
        IVjdmFwd = Isbd * (T0 - XExpBVD / T0 + XExpBVD - 1.0)
        DslpFwd  = Isbd * (T0 + XExpBVD / T0) / Nvtmd
        T2       = hypsmooth(IJTHDREV / Isbd - 10.0, 1.0e-3) + 10.0
        VjdmRev  = -BVD - Nvtmd * lln((T2 - 1.0) / XJBVD)
        T1       = XJBVD * lexp(-(BVD + VjdmRev) / Nvtmd)
        IVjdmRev = Isbd * (1.0 + T1)
        DslpRev  = -Isbd * T1 / Nvtmd
    else:
        Nvtmd    = 0.0
        XExpBVD  = 0.0
        VjdmFwd  = 0.0
        IVjdmFwd = 0.0
        DslpFwd  = 0.0
        VjdmRev  = 0.0
        IVjdmRev = 0.0
        DslpRev  = 0.0

    # STI stress equations
    if ((SA > 0.0) and (SB > 0.0) and ((NF == 1.0) or ((NF > 1.0) and (SD > 0.0)))):
        T0              = Lnew**LLODKU0
        W_tmp_stress    = Wnew + WLOD
        T1              = W_tmp_stress**WLODKU0
        tmp1_stress     = LKU0 / T0 + WKU0 / T1 + PKU0 / (T0 * T1)
        kstress_u0      = 1.0 + tmp1_stress
        T0              = Lnew**LLODVTH
        T1              = W_tmp_stress**WLODVTH
        tmp1_stress_vth = LKVTH0 / T0 + WKVTH0 / T1 + PKVTH0 / (T0 * T1)
        kstress_vth0    = 1.0 + tmp1_stress_vth
        T0              = TRatio - 1.0
        ku0_temp        = kstress_u0 * (1.0 + TKU0 * T0) + 1.0e-9
        for i in range(NF):
            T0     = 1.0 / NF / (SA + 0.5 * L_mult + i * (SD + L_mult))
            T1     = 1.0 / NF / (SB + 0.5 * L_mult + i * (SD + L_mult))
            Inv_sa = Inv_sa + T0
            Inv_sb = Inv_sb + T1
        Inv_saref   = 1.0 / (SAREF + 0.5 * L_mult)
        Inv_sbref   = 1.0 / (SBREF + 0.5 * L_mult)
        Inv_odref   = Inv_saref + Inv_sbref
        rho_ref     = (KU0 / ku0_temp) * Inv_odref
        Inv_od      = Inv_sa + Inv_sb
        rho         = (KU0 / ku0_temp) * Inv_od
        mu0_mult    = (1.0 + rho) / (1.0 + rho_ref)
        vsat_mult   = (1.0 + rho * KVSAT) / (1.0 + rho_ref * KVSAT)
        vth0_stress = (KVTH0 / kstress_vth0) * (Inv_od - Inv_odref)
        k2_stress   = (STK2 / kstress_vth0**LODK2) * (Inv_od - Inv_odref)
        eta_stress  = (STETA0 / kstress_vth0**LODETA0) * (Inv_od - Inv_odref)
        U0_t        = U0_t * mu0_mult
        VSAT_t      = VSAT_t * vsat_mult
        K2_i        = K2_i + k2_stress
        ETA0_t      = ETA0_t + eta_stress
        if (EDGEFET == 1):
            vth0_stress_EDGE = (KVTH0EDGE_i / kstress_vth0) * (Inv_od - Inv_odref)
            k2_stress_EDGE   = (STK2EDGE_i / kstress_vth0**LODK2) * (Inv_od - Inv_odref)
            eta_stress_EDGE  = (STETA0EDGE_i / kstress_vth0**LODETA0) * (Inv_od - Inv_odref)
        K2EDGE_i   = K2EDGE_i + k2_stress_EDGE
        ETA0EDGE_i = ETA0EDGE_i + eta_stress_EDGE
    else:
        vth0_stress = 0.0
        vth0_stress_EDGE = 0.0

    # Well proximity effect
    if (WPEMOD == 1):
        Wdrn      = W / NF
        local_sca = SCA
        local_scb = SCB
        local_scc = SCC
        if ("SCA" not in keys(param)) and ("SCB" not in keys(param)) and ("SCC" not in keys(param)):
            if ("SC" in keys(param)) and (SC > 0.0):
                T1        = SC + Wdrn
                T2        = 1.0 / SCREF
                local_sca = SCREF * SCREF / (SC * T1)
                local_scb = ((0.1 * SC + 0.01 * SCREF) * lexp(-10.0 * SC * T2)  - (0.1 * T1 + 0.01 * SCREF) * lexp(-10.0 * T1 * T2)) / Wdrn
                local_scc = ((0.05 * SC + 0.0025 * SCREF) * lexp(-20.0 * SC * T2)  - (0.05 * T1 + 0.0025 * SCREF) * lexp(-20.0 * T1 * T2)) / Wdrn
            else:
                print("Warning: (Instance %M) No WPE as none of SCA, SCB, SCC, SC is given and/or SC not positive.")
    else:
        local_sca = 0.0
        local_scb = 0.0
        local_scc = 0.0

    vth0_well = KVTH0WE_i * (local_sca + WEB * local_scb + WEC * local_scc)
    k2_well   = K2WE_i * (local_sca + WEB * local_scb + WEC * local_scc)
    mu_well   = 1.0 + KU0WE_i * (local_sca + WEB * local_scb + WEC * local_scc)
    U0_t      = U0_t * mu_well
    K2_i      = K2_i + k2_well

    # Load terminal voltages
    Vds           = Vd - Vs
    Vds_noswap    = Vds
    Vsb_noswap    = Vs
    Vdb_noswap    = Vd
    Vbs_jct       = devsign * (Vb - Vs)
    Vbd_jct       = devsign * (Vb - Vd)
    Vgd_noswap    = Vg - Vd
    Vgs_noswap    = Vg - Vs
    Vgd_ov_noswap = devsign * (Vg - Vd)
    Vgs_ov_noswap = devsign * (Vg - Vs)

    # Terminal voltage conditioning
    # Source-drain interchange
    sigvds = 1.0
    if (Vds < 0.0):
        sigvds = -1.0
        Vd = devsign * Vs
        Vs = devsign * Vd
    Vds  = Vd - Vs
    T0   = AVDSX * Vds
    if (T0 > EXPL_THRESHOLD):
       T1 = T0
    else:
       T1 = log(1.0 + exp(T0))
    Vdsx = ((2.0 / AVDSX) * T1) - Vds - ((2.0 / AVDSX) * log(2.0))
    Vbsx = -(Vs + 0.5 * (Vds - Vdsx))

    # Asymmetry model
    T0 = tanh(0.6 * Vds_noswap / Vtm)
    wf = 0.5 + 0.5 * T0
    wr = 1.0 - wf
    if (ASYMMOD != 0):
        CDSCD_a  = CDSCDR_i * wr + CDSCD_i * wf
        ETA0_a   = ETA0R_t * wr + ETA0_t * wf
        PDIBLC_a = PDIBLCR_i * wr + PDIBLC_i * wf
        PCLM_a   = PCLMR_i * wr + PCLM_i * wf
        PSAT_a   = PSATR_i * wr + PSAT_i * wf
        VSAT_a   = VSATR_t * wr + VSAT_t * wf
        PTWG_a   = PTWGR_t * wr + PTWG_t * wf
        U0_a     = U0R_t * wr + U0_t * wf
        UA_a     = UAR_t * wr + UA_t * wf
        UC_a     = UCR_t * wr + UC_t * wf
        UD_a     = UDR_t * wr + UD_t * wf
        UCS_a    = UCSR_t * wr + UCS_t * wf
    else:
        CDSCD_a  = CDSCD_i
        ETA0_a   = ETA0_t
        PDIBLC_a = PDIBLC_i
        PCLM_a   = PCLM_i
        PSAT_a   = PSAT_i
        VSAT_a   = VSAT_t
        PTWG_a   = PTWG_t
        U0_a     = U0_t
        UA_a     = UA_t
        UC_a     = UC_t
        UD_a     = UD_t
        UCS_a    = UCS_t

    # SCE, DIBL, SS degradation effects, Ref: BSIM4
    PhistVbs = Smooth(Phist - Vbsx, 0.05, 0.1)
    sqrtPhistVbs = sqrt(PhistVbs)
    Xdep         = T1DEP * sqrtPhistVbs
    Cdep         = epssi / Xdep
    cdsc         = CIT_i + NFACTOR_t + CDSCD_a * Vdsx - CDSCB_i * Vbsx
    T1           = 1.0 + cdsc/Cox
    n = Smooth(T1, 1.0, 0.05)
    nVt     = n * Vt
    inv_nVt = 1.0 / nVt

    # Vth shift for DIBL
    dVth_dibl = -(ETA0_a + ETAB_i * Vbsx) * Vdsx
    dVth_dibl = Smooth2(dVth_dibl, 0.0, 5.0e-5)

    # Vth shift with temperature
    dvth_temp = (KT1_i + KT1L / Leff + KT2_i * Vbsx) * (TRatio**KT1EXP - 1.0)

    # Vth correction for pocket implants
    if (DVTP0_i > 0.0):
        T0 = -DVTP1_i * Vdsx
        if (T0 < -EXPL_THRESHOLD):
            T2 = MIN_EXPL
        else:
            T2 = lexp(T0)
        T3        = Leff + DVTP0_i * (1.0 + T2)
        dVth_ldop = -nVt * lln(Leff / T3)
    else:
        dVth_ldop = 0.0
    T4        = DVTP5_i + DVTP2_i / Leff**DVTP3_i
    dVth_ldop = dVth_ldop - T4 * tanh(DVTP4_i * Vdsx)

    # Normalization of terminal and flatband voltage by nVt
    VFB_i = VFB_i + DELVTO
    vg    = Vg * inv_nVt
    vs    = Vs * inv_nVt
    vfb   = VFB_i * inv_nVt

    # Compute dVth_VNUD with "first-order" and "second-order" body-bias effect
    dVth_VNUD = K1_i * (sqrtPhistVbs - sqrtPhist) - K2_i * Vbsx
    Vth_shift = dVth_dibl + dVth_ldop + dVth_VNUD - dvth_temp + vth0_stress + vth0_well
    vgfb      = vg - vfb - Vth_shift * inv_nVt

    # Threshold voltage for operating point information
    gam     = sqrt(2.0 * q * epssi * NDEP_i * inv_Vt) / Cox
    q_vth   = 0.5
    T0      = hypsmooth((2.0 * phib + Vs * inv_Vt), 1.0e-3)
    nq      = 1.0 + gam / (2.0 * sqrt(T0))
    psip_th = hypsmooth((Vs * inv_Vt + 2.0 * phib + lln(q_vth) + 2.0 * q_vth + lln(2.0 * nq / gam * (2.0 * q_vth * nq / gam + 2.0 * sqrt(T0)))), 1.0e-3)
    VTH     = devsign * (VFB_i + (psip_th - Vs * inv_Vt) * Vt + Vt * gam * sqrt(psip_th) + Vth_shift)

    # Normalized body factor
    gam     = sqrt(2.0 * q * epssi * NDEP_i * inv_nVt) / Cox
    inv_gam = 1.0 / gam

    # psip: pinch-off voltage
    phib_n = phib / n
    psip = PO_psip(vgfb, gam, 0.0)

    # Normalized inversion charge at source end of channel
    qs = BSIM_q(psip, phib_n, vs, gam)

    # Average charge-surface potential slope, Ref: Charge-based MOS Transistor Modeling by C. Enz & E. Vittoz
    psipclamp = Smooth(psip, 1.0, 2.0)
    sqrtpsip = sqrt(psipclamp)

    # Source side surface potential
    psiavg = psip - 2.0 * qs
    T0 = Smooth(psiavg, 1.0, 2.0)
    nq = 1.0 + gam / (sqrtpsip + sqrt(T0))

    # Drain saturation voltage
    EeffFactor = 1.0e-8 / (epsratio * TOXE)
    T0 = nVt * (vgfb - psip - 2.0 * qs * (nq - 1.0))
    qbs = Smooth(T0, 0.0, 0.1)

    # Source side qi and qb for Vdsat- normalized to Cox
    qis = 2.0 * nq * nVt * qs
    Eeffs = EeffFactor * (qbs + eta_mu * qis)

    # Ref: BSIM4 mobility model
    T2 = (0.5 * (1.0 + (qis / qbs)))**UCS_a
    T3 = (UA_a + UC_a * Vbsx) * Eeffs**EU_t + UD_a / T2
    T4 = 1.0 + T3
    Dmobs = Smooth(T4, 1.0, 0.0015)
    WeffWRFactor = 1.0 / ((Weff * 1.0e6)**WR_i * NF)

    if (RDSMOD == 1):
        Rdss = 0.0
    else:
        T0   = 1.0 + PRWG_i * qis
        T1   = PRWB_i * (sqrtPhistVbs - sqrtPhist)
        T2   = 1.0 / T0 + T1
        T3   = T2 + sqrt(T2 * T2 + 0.01)
        Rdss = (RDSWMIN_i + RDSW_i * T3) * WeffWRFactor * NF * rdstemp
        if (RDSMOD == 2):
            Rdss = (RSourceGeo + (RDSWMIN_i + RDSW_i * T3) * WeffWRFactor * NF + RDrainGeo) * rdstemp

    T0  = Dmobs**(1.0 / PSAT_a)
    T11 = PSATB_i * Vbsx
    T12 = sqrt(0.1 + T11 * T11)
    T1  = 0.5*(1 - T11 + sqrt((1 - T11) * (1 - T11) + T12))
    T2  = 10.0 * PSATX * qs * T1 / (10.0 * PSATX + qs * T1)
    if (PTWG_a < 0.0):
        LambdaC = 2.0 * ((U0_a / T0) * nVt / (VSAT_a * Leff)) * (1.0 / (1.0 - PTWG_a * T2))
    else:
        LambdaC = 2.0 * ((U0_a / T0) * nVt / (VSAT_a * Leff)) * (1.0 + PTWG_a * T2)

    # qdsat for external Rds
    if (Rdss == 0):
        # Accurate qdsat derived from consistent I-V
        T0 = 0.5 * LambdaC * (qs * qs + qs) / (1.0 + 0.5 * LambdaC * (1.0 + qs))
        T1 = 2.0 * LambdaC * (qs - T0)
        T2 = sqrt(1.0 + T1 * T1)
        ln_T1_T2 = asinh(T1)
        if (T1 != 0.0):
            T3 = T2 + (1.0 / T1) * ln_T1_T2
        else:
            T3 = T2 + (1.0 / T2)
        T4 = T0 * T3 - LambdaC * ((qs * qs + qs) - (T0 * T0 + T0))
        if (T1 != 0.0):
            T5 = -2.0 * LambdaC * (T1 * T2 - ln_T1_T2) / (T1 * T1)
        else:
            T5 = -2.0 * LambdaC * (T1/T2) * (T1/T2) *(T1/T2)

        T6 = T0 * T5 + T3 + LambdaC * (2.0 * T0 + 1.0)
        T0 = T0 - (T4 / T6)
        T1 = 2.0 * LambdaC * (qs - T0)
        T2 = sqrt(1.0 + T1 * T1)
        ln_T1_T2 = asinh(T1)
        if (T1 != 0.0):
            T3 = T2 + (1.0 / T1) * ln_T1_T2
        else:
            T3 = T2 + (1.0 / T2)
        T4 = T0 * T3 - LambdaC * ((qs * qs + qs) - (T0 * T0 + T0))
        if (T1 != 0.0):
            T5 = -2.0 * LambdaC * (T1 * T2 - ln_T1_T2) / (T1 * T1)
        else:
            T5 = (T1 / T2) * (T1 / T2) * (T1 / T2)

        T6    = T0 * T5 + T3 + LambdaC * (2.0 * T0 + 1.0)
        qdsat = T0 - (T4/T6)
    # qdsat for internal Rds, Ref: BSIM4
    else:
        # Accurate qdsat derived from consistent I-V
        T11 = Weff * 2.0 * nq * Cox * nVt * VSAT_a
        T12 = T11 * LambdaC * Rdss / (2.0 * nVt)
        T0  = 0.5 * LambdaC * (qs * qs + qs) / (1.0 + 0.5 * LambdaC * (1.0 + qs))
        T1  = 2.0 * LambdaC * (qs - T0)
        T2  = sqrt(1.0 + T1 * T1)
        ln_T1_T2 = asinh(T1)
        if (T1 != 0.0):
            T3 = T2 + (1.0 / T1) * ln_T1_T2
        else:
            T3 = T2 + (1.0 / T2)
        T4 = T0 * T3 + T12 * T0 * (qs + T0 + 1.0) - LambdaC * ((qs * qs + qs) - (T0 * T0 + T0))
        if (T1 != 0.0):
            T5 = -2.0 * LambdaC * (T1 * T2 - ln_T1_T2) / (T1 * T1)
        else:
            T5 = -2.0 * LambdaC * (T1 / T2) * (T1 / T2) * (T1 / T2)
        T6 = T0 * T5 + T3 + T12 * (qs + 2.0 * T0 + 1.0) + LambdaC * (2.0 * T0 + 1.0)
        T0 = T0 - T4 / T6
        T1 = 2.0 * LambdaC * (qs - T0)
        T2 = sqrt(1.0 + T1 * T1)
        ln_T1_T2 = asinh(T1)
        if (T1 != 0):
            T3 = T2 + (1.0 / T1) * ln_T1_T2
        else:
            T3 = T2 + (1.0 / T2)
        T4 = T0 * T3 + T12 * T0 * (qs + T0 + 1.0) - LambdaC * ((qs * qs + qs) - (T0 * T0 + T0))
        if (T1 != 0.0):
            T5 = -2.0 * LambdaC * (T1 * T2 - ln_T1_T2) / (T1 * T1)
        else:
            T5 = -2.0 * LambdaC * (T1 / T2) * (T1 / T2) * (T1 / T2)
        T6    = T0 * T5 + T3 + T12 * (qs + 2.0 * T0 + 1.0) + LambdaC * (2.0 * T0 + 1.0)
        qdsat = T0 - T4 / T6
    vdsat = psip - 2.0 * phib_n - (2.0 * qdsat + lln((qdsat * 2.0 * nq * inv_gam) * ((qdsat * 2.0 * nq * inv_gam) + (gam / (nq - 1.0)))))
    Vdsat = vdsat * nVt

    # Normalized charge qdeff at drain end of channel
    # Vdssat clamped to avoid negative values during transient simulation
    Vdssat = Smooth(Vdsat - Vs, 0.0, 1.0e-3)
    T7      = (Vds / Vdssat)**(1.0 / DELTA_t)
    T8      = (1.0 + T7)**-DELTA_t
    Vdseff  = Vds * T8
    vdeff   = (Vdseff + Vs) * inv_nVt
    qdeff = BSIM_q(psip, phib_n, vdeff, gam)

    # Reevaluation of nq to include qdeff
    psiavg = psip - qs - qdeff -1.0
    T0 = Smooth(psiavg, 1.0, 2.0)
    T2 = sqrt(T0)
    nq = 1.0 + gam / (sqrtpsip + T2)

    # Inversion and bulk charge
    DQSD2 = (qs - qdeff) * (qs - qdeff)
    T0    = 1.0 / (1.0 + qs + qdeff)
    T1    = DQSD2 * T0
    Qb    = vgfb - psip - (nq - 1.0) * (qs + qdeff + Oneby3 * T1)
    T2    = Oneby3 * nq
    T3    = T1 * T0
    Qs    = T2 * (2.0 * qs + qdeff + 0.5 * (1.0 + 0.8 * qs + 1.2 * qdeff) * T3)
    Qd    = T2 * (qs + 2.0 * qdeff + 0.5 * (1.0 + 1.2 * qs + 0.8 * qdeff) * T3)

    # Mobility degradation, Ref: BSIM4
    # Average charges (qba and qia) - normalized to Cox
    qba = Smooth(nVt * Qb, 0.0, 0.1)
    qia   = nVt * (Qs + Qd)

    Eeffm = EeffFactor * (qba + eta_mu * qia)
    T2    = (0.5 * (1.0 + (qia / qba)))**UCS_a
    T3    = (UA_a + UC_a * Vbsx) * Eeffm**EU_t + UD_a / T2
    T4    = 1.0 + T3
    Dmob = Smooth(T4, 1.0, 0.0015)

    # Output conductance
    Esat  = 2.0 * VSAT_a / (U0_a / Dmob)
    EsatL = Esat * Leff
    if (PVAG_i > 0.0):
        PVAGfactor = 1.0 + PVAG_i * qia / EsatL
    else:
        PVAGfactor = 1.0 / (1.0 - PVAG_i * qia / EsatL)

    # Output conductance due to DIBL, Ref: BSIM4
    DIBLfactor = PDIBLC_a
    diffVds    = Vds - Vdseff
    Vgst2Vtm   = qia + 2.0 * nVt
    if (DIBLfactor > 0.0):
        T3     = Vgst2Vtm / (Vdssat + Vgst2Vtm)
        T4     = hypsmooth((1.0 + PDIBLCB_i * Vbsx), 1.0e-3)
        T5     = 1.0 / T4
        VaDIBL = Vgst2Vtm / DIBLfactor * T3 * PVAGfactor * T5
        Moc    = 1.0 + diffVds / VaDIBL
    else:
        Moc = 1.0

    # Degradation factor due to pocket implants, Ref: BSIM4
    if (FPROUT_i <= 0.0):
        Fp = 1.0
    else:
        T9 = FPROUT_i * sqrt(Leff) / Vgst2Vtm
        Fp = 1.0 / (1.0 + T9)

    # Channel length modulation, Ref: BSIM4
    Vasat = Vdssat + EsatL
    if (PCLM_a != 0.0):
        if (PCLMG < 0.0):
            T1 = PCLM_a / (1.0 - PCLMG * qia / EsatL) / Fp
        else:
            T1 = PCLM_a * (1.0 + PCLMG * qia / EsatL) / Fp

        MdL = 1.0 + T1 * lln(1.0 + diffVds / T1 / Vasat)
    else:
        MdL = 1.0
    Moc = Moc * MdL

    # Calculate Va_DITS, Ref: BSIM4
    T1 = lexp(PDITSD_i * Vds)
    if (PDITS_i > 0.0):
        T2      = 1.0 + PDITSL * Leff
        VaDITS  = (1.0 + T2 * T1) / PDITS_i
        VaDITS  = VaDITS * Fp
    else:
        VaDITS  = MAX_EXPL
    T4  = diffVds / VaDITS
    T0  = 1.0 + T4
    Moc = Moc * T0

    # Calculate Va_SCBE, Ref: BSIM4
    if (PSCBE2_i > 0.0):
        if (diffVds > PSCBE1_i * litl / EXPL_THRESHOLD):
            T0     = PSCBE1_i * litl / diffVds
            VaSCBE = Leff * lexp(T0) / PSCBE2_i
        else:
            VaSCBE = MAX_EXPL * Leff/PSCBE2_i
    else:
        VaSCBE = MAX_EXPL
    Mscbe = 1.0 + (diffVds / VaSCBE)
    Moc   = Moc * Mscbe

    # Velocity saturation
    T0  = Dmob**(1.0 / PSAT_a)
    T11 = PSATB_i * Vbsx
    T12 = sqrt(0.1+T11*T11)
    T1  = 0.5*(1-T11+sqrt((1-T11)*(1-T11)+T12))
    T2  = 10.0 * PSATX * qia * T1 / (10.0 * PSATX + qia * T1)
    if (PTWG_a < 0.0):
        LambdaC = 2.0 * ((U0_a / T0) * nVt / (VSAT_a * Leff)) * (1.0 / (1.0 - PTWG_a * T2))
    else:
        LambdaC = 2.0 * ((U0_a / T0) * nVt / (VSAT_a * Leff)) * (1.0 + PTWG_a * T2)
    T1 = 2.0 * LambdaC * (qs - qdeff)
    T2 = sqrt(1.0 + T1 * T1)
    if (T1 != 0.0):
        Dvsat = 0.5 * (T2 + (1.0 / T1) * asinh(T1))
    else:
        Dvsat = 0.5 * (T2 + (1.0 / T2))
    Dptwg = Dvsat

    # S/D series resistances, Ref: BSIM4
    if (RDSMOD == 1):
        Rdsi = 0.0
        Dr   = 1.0
        # Rs (Source side resistance for all fingers)
        T2      = Vgs_noswap - Vfbsdr
        T3      = sqrt(T2 * T2 + 0.01)
        Vgs_eff = 0.5 * (T2 + T3)
        T5      = 1.0 + PRWG_i * Vgs_eff
        T6      = (1.0 / T5) + PRWB_i * Vsb_noswap
        T4      = 0.5 * (T6 + sqrt(T6 * T6 + 0.01))
        Rsource = rdstemp * (RSourceGeo + (RSWMIN_i + RSW_i * T4) * WeffWRFactor)
        # Rd (Drain side resistance for all fingers)
        T2      = Vgd_noswap - Vfbsdr
        T3      = sqrt(T2 * T2 + 0.01)
        Vgd_eff = 0.5 * (T2 + T3)
        T5      = 1.0 + PRWG_i * Vgd_eff
        T6      = (1.0 / T5) + PRWB_i * Vdb_noswap
        T4      = 0.5 * (T6 + sqrt(T6 * T6 + 0.01))
        Rdrain  = rdstemp * (RDrainGeo + (RDWMIN_i + RDW_i * T4) * WeffWRFactor)
    else:
        # Ref: (1) BSIM4 (2) "Operation and Modeling of the MOS Transistor" by Yannis Tsividis
        T0      = 1.0 + PRWG_i * qia
        T1      = PRWB_i * (sqrtPhistVbs - sqrtPhist)
        T2      = 1.0 / T0 + T1
        T3      = 0.5 * (T2 + sqrt(T2 * T2 + 0.01))
        Rdsi    = rdstemp * (RDSWMIN_i + RDSW_i * T3) * WeffWRFactor * NF
        Rdrain  = RDrainGeo
        Rsource = RSourceGeo
        Dr      = 1.0 + U0_a /(Dvsat * Dmob) * Cox * Weff / Leff * qia * Rdsi
        if (RDSMOD == 2):
            Rdsi    = rdstemp * (RSourceGeo + (RDSWMIN_i + RDSW_i * T3) * WeffWRFactor * NF + RDrainGeo)
            Rdrain  = 0.0
            Rsource = 0.0
            Dr      = 1.0 + U0_a /(Dvsat * Dmob) * Cox * Weff / Leff * qia * Rdsi

    # Non-saturation effect
    T0   = A1_t + A2_t / (qia + 2.0 * n * Vtm)
    DQSD = qs - qdeff
    T1   = T0 * DQSD * DQSD
    T2   = T1 + 1.0 - 0.001
    T3   = -1.0 + 0.5 * (T2 + sqrt(T2 * T2 + 0.004))
    Nsat = 0.5 * (1.0 + sqrt(1.0 + T3))

    # MNUD model to enhance Id-Vd fitting flexibility
    T0   = (qs + qdeff)
    T1   = (qs - qdeff)
    T2   = T1 / (T0 + M0_t)
    T3   = K0_t * T2 * T2
    Mnud = 1.0 + T3

    # MNUD1 to enhance the fitting flexiblity for the gm/Id - similar approach used in BSIM-CMG
    T9    = C0_t / (max(0, C0SI_t + C0SISAT_t * T1 * T1) * T0 + 2.0 * n * Vtm)
    Mnud1 = lexp(-T9)
    Dtot  = Dmob * Dvsat * Dr

    # Effective mobility including mobility degradation
    ueff = U0_a / Dtot

    # I-V
    ids  = 2.0 * NF * nq * ueff * Weff / Leff * Cox * nVt * nVt * ((qs - qdeff) * (1.0 + qs + qdeff)) * Moc / Nsat * Mnud * Mnud1
    ids  = ids * IDS0MULT

    # High-voltage model s: Ref. - Harshit Agarwal et.al., IEEE TED vol. 66, issue 10, pp. 4258, 2019
    if (RDSMOD == 1 and HVMOD == 1):
        T4  = 1 + PDRWB * Vbsx
        T0  = ids
        T11 = NF * Weff * q  * VDRIFT_t
        if (RDLCW != 0):
            idrift_sat_d = T11 * NDRIFTD
            delta_hv = ids**(4 - MDRIFT) / (ids**(4 - MDRIFT) + HVFACTOR * idrift_sat_d**(4 - MDRIFT))
            T5  = T0/idrift_sat_d
            if (T5 >= 0.99):
                T5  = 0.5 * ((T5 + 0.99) - sqrt( (T5 - 0.99) * (T5 - 0.99) + 1.0e-6) + 0.001)
            T0D = delta_hv * T5**MDRIFT
            T1D = 1.0 - T0D
            T2D = T1D**(1.0 / MDRIFT)
            rdrift_d = rdstemphv * RDLCW * WeffWRFactor/T2D * T4
            IDRIFTSATD = idrift_sat_d
            if (rdrift_d < 0):
                rdrift_d = 0
        if (RSLCW != 0):
            idrift_sat_s = T11 * NDRIFTS
            delta_hv = ids**(4 - MDRIFT) / (ids**(4 - MDRIFT) + HVFACTOR * idrift_sat_s**(4 - MDRIFT))
            T5  = T0/idrift_sat_s
            if (T5 >= 0.99):
                T5  = 0.5 * ((T5 + 0.99) - sqrt( (T5 - 0.99) * (T5 - 0.99) + 1.0e-6) + 0.001 )
            T0S = delta_hv * T5**MDRIFT
            T1S = 1.0 - T0S
            T2S = T1S**(1.0 / MDRIFT)
            rdrift_s = rdstemphv * RSLCW * WeffWRFactor/T2S * T4
            if (rdrift_s < 0.0):
                rdrift_s = 0.0
        Rdrain  = Rdrain + rdrift_d
        Rsource = Rsource + rdrift_s

    # CV calculations for HVMOD
    if (RDSMOD == 1 and HVCAP == 1 and HVMOD == 1):
        vgfbdrift = -devsign * (Vg - Vd) - VFBOV
        vgfbdrift = vgfbdrift/Vt
        gamhv     = sqrt(2.0 * q * epssi * NDR * inv_Vt) / Cox
        phibHV    = lln(NDR / ni)
        psip_k = PO_psip(vgfbdrift, gamhv, 0.0)
        q_k = BSIM_q(psip_k, phibHV, devsign * (Vd - Vb) / Vt, gamhv)

        # calculate nq for the drift region
        psipclamp_hv = Smooth(psip_k, 1.0, 2.0)
        sqrtpsip_k = sqrt(psipclamp_hv)
        psiavg_hv = psip_k - 2.0 * q_k
        T0 = Smooth(psiavg_hv, 1.0, 2.0)
        nq_hv = 1.0 + gamhv / (sqrtpsip_k + sqrt(T0))
        psi_k = psip_k - 2 * q_k

        # contribution due to accumulation of the overlap region
        QBOV = NF * Wact * LOVER * EPS0 * EPSROX / BSIMBULKTOXP * Vt * (vgfbdrift - psi_k - 2 * nq_hv * q_k)

        # contribution due to inversion of the overlap region
        if (SLHV > 0):
            T1 = 1 + q_k / SLHV1
            T2 = SLHV * 1.9e-9 / T1
            T0 = 3.9 * EPS0 / (BSIMBULKTOXP * 3.9 / EPSROX + T2 / epsratio)
        else:
            T0 = EPS0 * EPSROX / BSIMBULKTOXP

        QIOV = NF * Wact * LOVERACC * 2 * nq_hv * Vt * T0 * q_k

        # For symmetric device, adding contribution of the source side drift region
        if (HVCAPS == 1):
            vgfbdrift = -devsign * (Vg - Vs) - VFBOV
            vgfbdrift = vgfbdrift/Vt
            psip_k = PO_psip(vgfbdrift, gamhv, 0.0)
            q_k = BSIM_q(psip_k, phibHV, devsign * (Vs - Vb) / Vt, gamhv)
            psipclamp_hv = Smooth(psip_k, 1.0, 2.0)
            sqrtpsip_k = sqrt(psipclamp_hv)
            psiavg_hv = psip_k - 2.0 * q_k
            T0 = Smooth(psiavg_hv, 1.0, 2.0)
            nq_hv = 1.0 + gamhv / (sqrtpsip_k + sqrt(T0))
            psi_k = psip_k - 2 * q_k
            QBOVS = NF * Wact * LOVER * EPS0 * EPSROX / BSIMBULKTOXP * Vt * (vgfbdrift - psi_k - 2 * nq_hv * q_k)
            if (SLHV > 0):
                T1 = 1 + q_k / SLHV1
                T2 = SLHV * 1.9e-9 / T1
                T0 = 3.9 * EPS0 / (BSIMBULKTOXP * 3.9 / EPSROX + T2 / epsratio)
            else:
                T0 = EPS0 * EPSROX / BSIMBULKTOXP
            QIOVS = NF * Wact * LOVERACC * 2 * nq_hv * Vt * T0 * q_k
    if (RGATEMOD > 1):
        idsovvds = ueff * Weff / Leff * Cox * qia
        T9       = XRCRG2 * Vt
        T0       = T9 * ueff * Weff / Leff * Cox
        Gcrg     = XRCRG1 * NF * (T0 + idsovvds)
        if (RGATEMOD == 2):
            T11  = Grgeltd + Gcrg
            Gcrg = Grgeltd * Gcrg / T11

    # Impact ionization currents, Ref: BSIM4
    if ((ALPHA0_i <= 0.0) or (BETA0_t <= 0.0)):
        Iii = 0.0
    elif (diffVds > BETA0_t / EXPL_THRESHOLD):
        T1  = -BETA0_t / diffVds
        Iii = ALPHA0_i * diffVds * ids * lexp(T1) / Mscbe
    else:
        Iii = ALPHA0_i * diffVds * ids * MIN_EXPL / Mscbe

    # Secondary impact ionization in the drift region
    if (HVMOD == 1 and IIMOD == 1):
        Ntot = DRII1 * ids/(NF * Weff * q  * VDRIFT_t )
        Nextra = Ntot/NDRIFTD - 1
        Nextra = Smooth(Nextra, 0, DELTAII)
        Nextra = NDRIFTD * Nextra
        T2 = Smooth(devsign * (Vd - Vb) - Vdseff - DRII2, 0, 0.05)
        T3 = 2.0 * q /(EPSRSUB * EPS0) * Nextra
        T3 = T3 * T2
        if (T3 > BETADR / EXPL_THRESHOLD):
            T1  = -BETADR/T3
            IsubDR = ALPHADR * T2 * ids * lexp(T1)
        else:
            IsubDR = ALPHADR * T2 * ids * MIN_EXPL
        Iii = Iii + IsubDR

    # Gate currents, Ref: BSIM4
    if ((IGCMOD != 0) or (IGBMOD != 0)):
        Voxm    = nVt * (vgfb - psip + qs + qdeff)
        T1      = sqrt(Voxm * Voxm + 1.0e-4)
        Voxmacc = 0.5 * (-Voxm + T1)
        Voxminv = 0.5 * (Voxm + T1)
        # Igbinv
        if (IGBMOD != 0):
            T1     = Voxm / NIGBACC_i / Vt
            Vaux_Igbacc = NIGBACC_i * Vt * lln(1.0 + lexp(-T1))
            T2     = AIGBACC_i - BIGBACC_i * Voxmacc
            T3     = 1.0 + CIGBACC_i * Voxmacc
            T4     = -7.45669e11 * TOXE * T2 * T3
            T5     = lexp(T4)
            T6     = 4.97232e-7
            igbacc = NF * Weff * Leff * T6 * ToxRatio * Vg * Vaux_Igbacc * T5
            igbacc = igbacc * igtemp
            T1     = (Voxm - EIGBINV_i) / NIGBINV_i / Vt
            Vaux_Igbinv = NIGBINV_i * Vt * lln(1.0 + lexp(T1))
            T2     = AIGBINV_i - BIGBINV_i * Voxminv
            T3     = 1.0 + CIGBINV_i * Voxminv
            T4     = -9.82222e11 * TOXE * T2 * T3
            T5     = lexp(T4)
            T6     = 3.75956e-7
            igbinv = NF * Weff * Leff * T6 * ToxRatio * Vg * Vaux_Igbinv * T5
            igbinv = igbinv * igtemp
            igb    = igbacc + igbinv
        if (IGCMOD != 0):
            # Igcinv
            T1   = AIGC_i - BIGC_i * Voxminv
            T2   = 1.0 + CIGC_i * Voxminv
            T3   = Bechvb * T1 * T2
            T4   = nq * nVt * (qs + qdeff) * lexp(T3)
            igc0 = NF * Aechvb * T4 * (Vg + 0.5 * Vdsx - 0.5 * (Vs + Vd)) * igtemp
            # Gate-current partitioning
            Vdseffx = sqrt(Vdseff * Vdseff + 0.01) - 0.1
            T1      = PIGCD_i * Vdseffx
            T1_exp  = lexp(-T1)
            T3      = T1 + T1_exp -1.0 + 1.0e-4
            T4      = 1.0 - (T1 + 1.0) * T1_exp + 1.0e-4
            T5      = T1 * T1 + 2.0e-4
            if (sigvds > 0):
                igcd = igc0 * T4 / T5
                igcs = igc0 * T3 / T5
            else:
                igcs = igc0 * T4 / T5
                igcd = igc0 * T3 / T5
            # Igs
            T2      = Vgs_noswap - Vfbsdr
            Vgs_eff = sqrt(T2 * T2 + 1.0e-4)
            if (IGCLAMP == 1):
                T1 = hypsmooth((AIGS_i - BIGS_i * Vgs_eff), 1.0e-6)
                if (CIGS_i < 0.01):
                    CIGS_i = 0.01
            else:
                T1 = AIGS_i - BIGS_i * Vgs_eff
    
            T2       = 1.0 + CIGS_i * Vgs_eff
            T3       = BechvbEdge * T1 * T2
            T4       = lexp(T3)
            igs_mult = igtemp * NF * AechvbEdge * DLCIG_i
            igs      = igs_mult * Vgs_noswap * Vgs_eff * T4
            # Igd
            T2      = Vgd_noswap - Vfbsdr
            Vgd_eff = sqrt(T2 * T2 + 1.0e-4)
            if (IGCLAMP == 1):
                T1 = hypsmooth((AIGD_i - BIGD_i * Vgd_eff), 1.0e-6)
                if (CIGD_i < 0.01):
                    CIGD_i = 0.01
            else:
                T1 = AIGD_i - BIGD_i * Vgd_eff
            T2       = 1.0 + CIGD_i * Vgd_eff
            T3       = BechvbEdge * T1 * T2
            T4       = lexp(T3)
            igd_mult = igtemp * NF * AechvbEdge * DLCIGD_i
            igd      = igd_mult * Vgd_noswap * Vgd_eff * T4

    # GIDL and GISL currents, Ref: BSIM4
    if (GIDLMOD != 0):
        T0 = epsratio * TOXE
        # GIDL
        if ((AGIDL_i <= 0.0) or (BGIDL_t <= 0.0) or (CGIDL_i < 0.0)):
            T6 = 0.0
        else:
            T1 = (-Vgd_noswap - EGIDL_i + Vfbsdr) / T0
            T1 = hypsmooth(T1, 1.0e-2)
            T2 = BGIDL_t / (T1 + 1.0e-3)
            if (CGIDL_i != 0.0):
                T3 = Vdb_noswap * Vdb_noswap * Vdb_noswap
                T4 = CGIDL_i + abs(T3) + 1.0e-4
                T5 = hypsmooth(T3 / T4, 1.0e-6) - 1.0e-6
            else:
                T5 = 1.0
            T6 = AGIDL_i * Weff * T1 * lexp(-T2) * T5

        igidl = T6
        # GISL
        if ((AGISL_i <= 0.0) or (BGISL_t <= 0.0) or (CGISL_i < 0.0)):
            T6 = 0.0
        else:
            T1 = (-Vgs_noswap - EGISL_i + Vfbsdr) / T0
            T1 = hypsmooth(T1, 1.0e-2)
            T2 = BGISL_t / (T1 + 1.0e-3)
            if (CGISL_i != 0.0):
                T3 = Vsb_noswap * Vsb_noswap * Vsb_noswap
                T4 = CGISL_i + abs(T3) + 1.0e-4
                T5 = hypsmooth(T3 / T4, 1.0e-6) - 1.0e-6
            else:
                T5 = 1.0
            T6 = AGISL_i * Weff * T1 * lexp(-T2) * T5
        igisl = T6

    # Junction currents and capacitances
    # Source-side junction currents
    if (Isbs > 0.0):
        if (Vbs_jct < VjsmRev)
            T0  = Vbs_jct / Nvtms
            T1  = lexp(T0) - 1.0
            T2  = IVjsmRev + SslpRev * (Vbs_jct - VjsmRev)
            Ibs = T1 * T2
        elif (Vbs_jct <= VjsmFwd):
            T0  = Vbs_jct / Nvtms
            T1  = (BVS + Vbs_jct) / Nvtms
            T2  = lexp(-T1)
            Ibs = Isbs * (lexp(T0) + XExpBVS - 1.0 - XJBVS * T2)
        else:
            Ibs = IVjsmFwd + SslpFwd * (Vbs_jct - VjsmFwd)
    else:
        Ibs = 0.0

    # Source-side junction tunneling currents
    if (JTSS_t > 0.0):
        if ((VTSS - Vbs_jct) < (VTSS * 1.0e-3))
            T0  = -Vbs_jct / Vtm0 / NJTS_t
            T1  = lexp(T0 * 1.0e3) - 1.0
            Ibs = Ibs - ASeff * JTSS_t * T1
        else:
            T0  = -Vbs_jct / Vtm0 / NJTS_t
            T1  = lexp(T0 * VTSS / (VTSS - Vbs_jct)) - 1.0
            Ibs = Ibs - ASeff * JTSS_t * T1
    if (JTSSWS_t > 0.0):
        if ((VTSSWS - Vbs_jct) < (VTSSWS * 1.0e-3))
            T0  = -Vbs_jct / Vtm0 / NJTSSW_t
            T1  = lexp(T0 * 1.0e3) - 1.0
            Ibs = Ibs - PSeff * JTSSWS_t * T1
        else:
            T0  = -Vbs_jct / Vtm0 / NJTSSW_t
            T1  = lexp(T0 * VTSSWS / (VTSSWS - Vbs_jct)) - 1.0
            Ibs = Ibs - PSeff * JTSSWS_t * T1
    if (JTSSWGS_t > 0.0):
        if ((VTSSWGS - Vbs_jct) < (VTSSWGS * 1.0e-3)):
            T0  = -Vbs_jct / Vtm0 / NJTSSWG_t
            T1  = lexp(T0 * 1.0e3) - 1.0
            Ibs = Ibs - Weffcj * NF * JTSSWGS_t * T1
        else:
            T0  = -Vbs_jct / Vtm0 / NJTSSWG_t
            T1  = lexp(T0 * VTSSWGS / (VTSSWGS - Vbs_jct)) - 1.0
            Ibs = Ibs - Weffcj * NF * JTSSWGS_t * T1

    # Drain-side junction currents
    if (Isbd > 0.0):
        if (Vbd_jct < VjdmRev)
            T0  = Vbd_jct / Nvtmd
            T1  = lexp(T0) - 1.0
            T2  = IVjdmRev + DslpRev * (Vbd_jct - VjdmRev)
            Ibd = T1 * T2
        elif (Vbd_jct <= VjdmFwd):
            T0  = Vbd_jct / Nvtmd
            T1  = (BVD + Vbd_jct) / Nvtmd
            T2  = lexp(-T1)
            Ibd = Isbd * (lexp(T0) + XExpBVD - 1.0 - XJBVD * T2)
        else:
            Ibd = IVjdmFwd + DslpFwd * (Vbd_jct - VjdmFwd)
    else:
        Ibd = 0.0

    # Drain-side junction tunneling currents
    if (JTSD_t > 0.0):
        if ((VTSD - Vbd_jct) < (VTSD * 1.0e-3))
            T0  = -Vbd_jct / Vtm0 / NJTSD_t
            T1  = lexp(T0 * 1.0e3) - 1.0
            Ibd = Ibd - ADeff * JTSD_t * T1
        else:
            T0  = -Vbd_jct / Vtm0 / NJTSD_t
            T1  = lexp(T0 * VTSD/ (VTSD - Vbd_jct)) - 1.0
            Ibd = Ibd - ADeff * JTSD_t * T1
    if (JTSSWD_t > 0.0)
        if ((VTSSWD - Vbd_jct) < (VTSSWD * 1.0e-3))
            T0  = -Vbd_jct / Vtm0 / NJTSSWD_t
            T1  = lexp(T0 * 1.0e3) - 1.0
            Ibd = Ibd - PDeff * JTSSWD_t * T1
        else:
            T0  = -Vbd_jct / Vtm0 / NJTSSWD_t
            T1  = lexp(T0 * VTSSWD / (VTSSWD - Vbd_jct)) - 1.0
            Ibd = Ibd - PDeff * JTSSWD_t * T1

    if (JTSSWGD_t > 0.0)
        if ((VTSSWGD - Vbd_jct) < (VTSSWGD * 1.0e-3))
            T0  = -Vbd_jct / Vtm0 / NJTSSWGD_t
            T1  = lexp(T0 * 1.0e3) - 1.0
            Ibd = Ibd - Weffcj * NF * JTSSWGD_t * T1
        else:
            T0  = -Vbd_jct / Vtm0 / NJTSSWGD_t
            T1  = lexp(T0 * VTSSWGD / (VTSSWGD - Vbd_jct)) - 1.0
            Ibd = Ibd - Weffcj * NF * JTSSWGD_t * T1


    # Junction capacitances (no swapping)
    # Source-to-bulk junction
    Czbs       = CJS_t * ASeff
    Czbssw     = CJSWS_t * PSeff
    Czbsswg    = CJSWGS_t * Weffcj * NF
    czbs_p1    = 0.1**-MJS
    czbs_p2    = 1.0 / (1.0 - MJS) * (1.0 - 0.05 * MJS * (1.0 + MJS) * czbs_p1)
    czbssw_p1  = 0.1**-MJSWS
    czbssw_p2  = 1.0 / (1.0 - MJSWS) * (1.0 - 0.05 * MJSWS * (1.0 + MJSWS) * czbssw_p1)
    czbsswg_p1 = 0.1**-MJSWGS
    czbsswg_p2 = 1.0 / (1.0 - MJSWGS) * (1.0 - 0.05 * MJSWGS * (1.0 + MJSWGS) * czbsswg_p1)
    Qbsj1 = JunCap(Czbs, Vbs_jct, PBS_t, MJS, czbs_p1, czbs_p2)
    Qbsj2 = JunCap(Czbssw, Vbs_jct, PBSWS_t, MJSWS, czbssw_p1, czbssw_p2)
    Qbsj3 = JunCap(Czbsswg, Vbs_jct, PBSWGS_t, MJSWGS, czbsswg_p1, czbsswg_p2)
    Qbsj = Qbsj1 + Qbsj2 + Qbsj3

    # Drain-to-bulk junction
    Czbd       = CJD_t * ADeff
    Czbdsw     = CJSWD_t * PDeff
    Czbdswg    = CJSWGD_t * Weffcj * NF
    czbd_p1    = 0.1**-MJD
    czbd_p2    = 1.0 / (1.0 - MJD) * (1.0 - 0.05 * MJD * (1.0 + MJD) * czbd_p1)
    czbdsw_p1  = 0.1**-MJSWD
    czbdsw_p2  = 1.0 / (1.0 - MJSWD) * (1.0 - 0.05 * MJSWD * (1.0 + MJSWD) * czbdsw_p1)
    czbdswg_p1 = 0.1**-MJSWGD
    czbdswg_p2 = 1.0 / (1.0 - MJSWGD) * (1.0 - 0.05 * MJSWGD * (1.0 + MJSWGD) * czbdswg_p1)
    Qbdj1 = JunCap(Czbd, Vbd_jct, PBD_t, MJD, czbd_p1, czbd_p2)
    Qbdj2 = JunCap(Czbdsw, Vbd_jct, PBSWD_t, MJSWD, czbdsw_p1, czbdsw_p2)
    Qbdj3 = JunCap(Czbdswg, Vbd_jct, PBSWGD_t, MJSWGD, czbdswg_p1, czbdswg_p2)
    Qbdj = Qbdj1 + Qbdj2 + Qbdj3

    #=
    # Sub-surface leakage drain current
    if (SSLMOD != 0)
        T1 = (NDEP_i / 1.0e23)**SSLEXP1
        T2 = (300.0 / DevTemp)**SSLEXP2
        T3 = (devsign * SSL5 * (Vb - Vs)) / Vt
        SSL0_NT  = SSL0 * lexp(-T1 * T2)
        SSL1_NT  = SSL1 * T2 * T1
        PHIB_SSL = SSL3 * tanh(lexp(devsign * SSL4 * ((Vg - Vb) - VTH - (Vs - Vb))))
        Issl     = sigvds * NF * Weff * SSL0_NT * lexp(T3) * lexp(-SSL1_NT * Leff) * lexp(PHIB_SSL / Vt) * (lexp(SSL2 * Vdsx / Vt) - 1.0)

    # Harshit's new flicker noise model. Ref: H. Agarwal et. al., IEEE J-EDS, vol. 3, no. 4, April 2015.
    Nt      = 4.0 * Vt * q
    Esatnoi = 2.0 * VSAT_a / ueff
    if (EM <= 0.0)
       DelClm = 0.0
    else:
        T0     = (diffVds / litl + EM) / Esatnoi
        DelClm = litl * lln(T0)
        if (DelClm < 0.0)
           DelClm = 0.0

    Nstar = Vt / q * (Cox + Cdep + CIT_i)
    Nl    = 2.0 * nq * Cox * Vt * qdeff * Mnud1 * Mnud / q
    T0a   = q * q * q * Vt * abs(ids) * ueff
    T0b   = q * Vt * ids * ids
    T0c   = NOIA + NOIB * Nl + NOIC * Nl * Nl
    T0d   = (Nl + Nstar) * (Nl + Nstar)
    T0e   = NOIA * q * Vt
    if (FNOIMOD == 1)
        LH1 = LH
        if (Leff > LH1)
            T0 = (Leff - LH1)
        else:
            LH1 = Leff
            T0 = LH1

        if(LINTNOI >= T0 / 2.0)
            print("Warning: LINTNOI = %e is too large - Leff for noise is negative. Re-setting LINTNOI = 0.", LINTNOI)
            LINTNOI_i = 0.0
        else:
            LINTNOI_i = LINTNOI

        LeffnoiH = Leff
        vgfbh  = (Vg - VFB_i) / Vt
        gam_h  = sqrt(2.0 * q * epssi * HNDEP / Vt) / Cox
        phib_h = log(HNDEP / ni)

        # Pinch-Off potential for halo region
        psiph = PO_psip(vgfbh, gam_h, 0.0)

        # Normalized inversion charge at source end of halo MOSFET
        qsh = BSIM_q(psiph, phib_h, vs, gam_h)
        nq_h = 1.0 + gam_h / (2.0 * sqrt(psiph))

        # Setting mobility of halo region equal to the mobility of the channel. In general, U0H < ueff
        U0_i_h  = ueff
        beta_h  = U0_i_h * Cox * Weff
        beta_ch = ueff * Cox * Weff

        # Normalized drain current for halo transistor. Eq. (14) of the paper
        i1 = ids * LH1 / (2.0 * nq_h * beta_h * Vt * Vt)

        # Normalized drain current for channel transistor. Eq. (15) of the paper
        i2 = ids * (LeffnoiH - LH1) / (2.0 * nq * beta_ch * nVt * nVt)
        T0 = (1.0 + 4.0 * (qsh * qsh + qsh - i1))
        if (T0 < 1.0)
            qdh = 0.0
        else:
            # Drain charge of halo transistor. Eq. (16) of the paper
            qdh = -0.5 + 0.5 * sqrt(T0)


        # Source charge of channel transistor. Eq. (17) of the paper
        qsch   = -0.5 + 0.5 * sqrt(1.0 + 4.0 * (qdeff * qdeff + qdeff + i2))
        gds_h  = 2.0 * nq_h * beta_h * Vt * qdh
        gds_ch = 2.0 * nq * beta_ch * Vt * qdeff
        gm_ch  = 2.0 * beta_ch * Vt * (qsch - qdeff)
        R_ch   = gds_h * (LeffnoiH - LH1)
        R_h    = gm_ch * LH1 + gds_ch * LH1
        t_tot  = 1.0 / (R_ch + R_h) / (R_ch + R_h)
        CF_ch  = R_ch * R_ch * t_tot
        CF_h   = R_h * R_h * t_tot

        # Local noise source
        if (Leff != LH1)
            Np2       = 2.0 * nq * Cox * Vt * qsch / q
            Leffnoi   = LeffnoiH - 2.0 * LINTNOI_i-LH1
            Leffnoisq = Leffnoi * Leffnoi
            # Channel transistor LNS
            T1     = 1.0e10 * Cox * Leffnoisq
            T2     = NOIA * lln((Np2 + Nstar) / (Nl + Nstar))
            T3     = NOIB * (Np2 - Nl)
            T4     = 0.5 * NOIC * (Np2 * Np2 - Nl * Nl)
            T5     = 1.0e10 * Leffnoisq * Weff * NF
            Ssi_ch = T0a / T1 * (T2 + T3 + T4) + T0b / T5 * DelClm * T0c / T0d
            T6     = Weff * NF * Leffnoi * 1.0e10 * Nstar * Nstar
            Swi_ch = T0e / T6 * ids * ids
            T7 = Swi_ch + Ssi_ch
            if (T7 > 0.0)
                FNPowerAt1Hz_ch = (Ssi_ch * Swi_ch) / T7
            else:
                FNPowerAt1Hz_ch = 0.0
    
        else:
            FNPowerAt1Hz_ch = 0.0


        # Halo transistor LNS
        T8    = NOIA2 * q * Vt
        T9    = Weff * NF * LH1 * 1.0e10 * Nstar * Nstar
        Swi_h = T8 / T9 * ids * ids
        T10   = Swi_h
        if (T10 > 0.0)
            FNPowerAt1Hz_h = Swi_h
        else:
            FNPowerAt1Hz_h = 0.0

        # Overall noise
        FNPowerAt1Hz = FNPowerAt1Hz_ch * CF_ch + FNPowerAt1Hz_h * CF_h
    else:
        # Parameter checking
        if (LINTNOI >= Leff/2.0)
            print("Warning: LINTNOI = %e is too large - Leff for noise is negative. Re-setting LINTNOI = 0.", LINTNOI)
            LINTNOI_i = 0.0
        else:
            LINTNOI_i = LINTNOI

        if (NOIA > 0.0 or NOIB > 0.0 or NOIC > 0.0)
            Leffnoi   = Leff - 2.0 * LINTNOI_i
            Leffnoisq = Leffnoi * Leffnoi
            T0        = 1.0e10 * Cox * Leffnoisq
            N0        = 2.0 * nq * Cox * Vt * qs * Mnud1 * Mnud / q
            T1        = NOIA * lln((N0 + Nstar) / (Nl + Nstar))
            T2        = NOIB * (N0 - Nl)
            T3        = 0.5 * NOIC * (N0 * N0 - Nl * Nl)
            T4        = 1.0e10 * Leffnoisq * Weff * NF
            Ssi       = T0a / T0 * (T1 + T2 + T3) + T0b / T4 * DelClm * T0c / T0d
            T5        = Weff * NF * Leffnoi * 1.0e10 * Nstar * Nstar
            Swi       = T0e / T5 * ids * ids
            T6        = Swi + Ssi
            if (T6 > 0.0)
                FNPowerAt1Hz = (Ssi * Swi) / T6 / (1 + NOIA1 * (qs-qdeff)**NOIAX)
            else:
                FNPowerAt1Hz = 0.0
    
        else:
            FNPowerAt1Hz = 0.0


    T0         = qia / Esatnoi / Leff
    T1         = T0 * T0
    T3         = RNOIA * (1.0 + TNOIA * Leff * T1)
    T4         = RNOIB * (1.0 + TNOIB * Leff * T1)
    T5         = RNOIK * (1.0 + TNOIK * Leff * T1)
    ctnoi      = RNOIC * (1.0 + TNOIC * Leff * T1)
    betanoisq  = 3.0 * T3 * T3
    betanoisq  = (betanoisq - 1.0) * exp(-Leff / LP) + 1.0
    betaLowId  = T5 * T5
    thetanoisq = T4 * T4
    cm_igid    = 0.0
    =#

    # C-V model
    vgfbCV   = vgfb
    gamg2    = (2.0 * q * epssi * NGATE_i) / (Cox * Cox * Vt)
    invgamg2 = 0.0
    if (CVMOD == 1):
        VFBCV_i = VFBCV_i + DELVTO
        vg      = Vg * inv_Vt
        vs      = Vs * inv_Vt
        vfb     = VFBCV_i * inv_Vt
        vgfbCV  = vg - vfb
        phibCV    = lln(NDEPCV_i / ni)
        # Normalized body factor
        gamCV      = sqrt(2.0 * q * epssi * NDEPCV_i * inv_Vt) / Cox
        inv_gam  = 1.0 / gamCV
        gamg2    = (2.0 * q * epssi * NGATE_i) / (Cox * Cox * Vt)
        invgamg2 = (1.0 / gamg2) if (NGATE_i > 0.0) else 0.0
        DPD      = (NDEPCV_i / NGATE_i) if (NGATE_i > 0.0) else 0.0

        # psip: pinch-off voltage
        psip = PO_psip(vgfbCV, gamCV, DPD)

        # Normalized inversion charge at source end of channel
        qs = BSIM_q(psip, phibCV, vs, gamCV)
        psipclamp = Smooth(psip, 1.0, 2.0)
        sqrtpsip = sqrt(psipclamp)

        # Source side surface potential
        psiavg = psip - 2.0 * qs
        T0 = Smooth(psiavg, 1.0, 2.0)
        nq = 1.0 + gamCV / (sqrtpsip + sqrt(T0))

        # Drain saturation voltage
        T0 = Vt * (vgfbCV - psip - 2.0 * qs * (nq - 1.0))
        qbs = Smooth(T0, 0.0, 0.1)

        # Source side qi and qb for Vdsat (normalized to Cox)
        qis = 2.0 * nq * Vt * qs
        Eeffs = EeffFactor * (qbs + eta_mu * qis)

        # Ref: BSIM4 mobility model
        T3 = (UA_a + UC_a * Vbsx) * Eeffs**EU_t
        T4 = 1.0 + T3
        Dmobs = Smooth(T4, 1.0, 0.0015)
        LambdaC_by2 = (U0_a / Dmobs) * Vt / (VSATCV_t * Lact)
        qdsat       = LambdaC_by2 * (qs * qs + qs) / (1.0 + LambdaC_by2 * (1.0 + qs))
        vdsatcv     = psip - 2.0 * phibCV - (2.0 * qdsat + lln((qdsat * 2.0 * nq * inv_gam) * ((qdsat * 2.0 * nq * inv_gam) + (gam / (nq - 1.0)))))
        VdsatCV     = vdsatcv * Vt

        # Normalized charge qdeff at drain end of channel
        VdssatCV = Smooth(VdsatCV - Vs, 0.0, 1e-3)
        VdssatCV     = VdssatCV / ABULK
        T7     = (Vds / VdssatCV)**(1.0 / DELTA_t)
        T8     = (1.0 + T7)**-DELTA_t
        Vdseff = Vds * T8
        vdeff  = (Vdseff + Vs) * inv_Vt
        qdeff = BSIM_q(psip, phibCV, vdeff, gamCV)

        # Reevaluation of nq to include qdeff needed for gummel symmetry
        psiavg = psip - qs - qdeff - 1.0
        T0 = Smooth(psiavg, 1.0, 2.0)
        T2 = sqrt(T0)
        T3 = 1.0 + DPD + gamCV / (sqrtpsip + T2)
        T4 = 0.5 + DPD * T2 * inv_gam
        T5 = sqrt(T4 * T4 + T3 * (qs + qdeff) * invgamg2)
        nq = T3 / (T4 + T5)

        # C-V expressions including velocity saturation and CLM
        # Velocity saturation for C-V
        T0  = Vt * (vgfbCV - psip - 2.0 * qs * (nq - 1.0))
        qbs = Smooth(T0, 0.0, 0.1)
        T1  = Vt * (vgfbCV - psip - 2.0 * qdeff * (nq - 1.0))
        qbd = Smooth(T1, 0.0, 0.1)
        qb  = 0.5 * (qbs + qbd)
        qia = nq * Vt * (qs + qdeff)
        Eeffm = EeffFactor * (qb + eta_mu * qia)
        psip = PO_psip((vgfbCV + DELVFBACC * inv_Vt), gamCV, DPD)
        T3    = (UA_a + UC_a * Vbsx) * Eeffm**EU_t
        T4    = 1.0 + T3
        Dmob = Smooth(T4, 1.0, 0.0015)
        LambdaC = 2.0 * (U0_a / Dmob) * Vt / (VSATCV_t * Lact)
        dps     = qs - qdeff
        T1      = 2.0 * (LambdaC * dps) * (LambdaC * dps)
        zsat    = sqrt(1.0 + T1)
        Dvsat   = 0.5 * (1.0 + zsat)
        # CLM for C-V
        Esat    = 2.0 * VSATCV_t / (U0_a / Dmob)
        EsatL   = Esat * Lact
        Vasat   = VdssatCV + EsatL
        diffVds = Vds - Vdseff
    if (PCLMCV_i != 0.0)
        MdL = 1.0 + PCLMCV_i * lln(1.0 + diffVds / PCLMCV_i / Vasat)
    else:
        MdL = 1.0
    MdL_2       = MdL * MdL
    inv_MdL     = 1.0 / MdL
    inv_MdL_2   = 1.0 / MdL_2
    MdL_less_1  = MdL - 1.0
    vgpqm = vgfbCV - psip
    DQSD  = (qs - qdeff)
    DQSD2 = (qs - qdeff) * (qs - qdeff)
    sis   = vgpqm + 2.0 * qs
    sid   = vgpqm + 2.0 * qdeff
    T1 = Smooth(sis, 0.0, 0.5)
    T2 = Smooth(sid, 0.0, 0.5)
    Temps = sqrt(0.25 + T1 * invgamg2)
    Tempd = sqrt(0.25 + T2 * invgamg2)
    T1 = sis / (1.0 + 2.0 * Temps)
    T2 = sid / (1.0 + 2.0 * Tempd)
    T3 = Temps + Tempd
    T4 = Oneby3 * (DQSD2 / (T3 * T3 * T3))
    T5 = (ABULK*Dvsat * inv_MdL) / (1.0 + qs + qdeff)
    T6 = 0.8 * (T3 * T3 + Temps * Tempd) * T5
    T7 = T6 + (2.0 * invgamg2)
    T8 = Oneby3 * DQSD2 * T5
    dqgeff = sid * (2.0 * Tempd - 1.0) / (2.0 * Tempd + 1.0)
    qbeff  = vgpqm - 2.0 * (nq - 1.0) * qdeff + dqgeff
    Qb  = inv_MdL * (T1 + T2 + (T4 * T7 - nq * (qs + qdeff + T8))) + MdL_less_1 * qbeff
    T9  = qs + qdeff
    T10 = DQSD2 * T5 * T5
    Qi  = nq * inv_MdL * (T9 + Oneby3 * DQSD2 * T5) + 2.0 * nq * MdL_less_1 * qdeff
    Qd1 = nq * inv_MdL_2 * (0.5 * T9 - (DQSD / 6.0) * (1.0 - DQSD * T5 - 0.2 * T10))
    Qd2 = nq * (MdL - inv_MdL) * qdeff
    Qd  = Qd1 + Qd2
    Qs  = Qi - Qd

    # Quantum mechanical effects
    qbaCV = Smooth(Vt * Qb, 0.0, 0.1)
    qiaCV      = Vt * (Qs + Qd)
    T0         = (qiaCV + ETAQM * qbaCV) / QM0
    T1         = 1.0 + T0**(0.7 * BDOS)
    XDCinv     = ADOS * 1.9e-9 / T1
    Coxeffinv  = 3.9 * EPS0 / (BSIMBULKTOXP * 3.9 / EPSROX + XDCinv / epsratio)
    QBi        = -NF * Wact * Lact * (EPS0 * EPSROX / BSIMBULKTOXP) * Vt * Qb
    WLCOXVtinv = NF * Wact * Lact * Coxeffinv * Vt
    QSi        = -WLCOXVtinv * Qs
    QDi        = -WLCOXVtinv * Qd
    QGi        = -(QBi + QSi + QDi)

    # Outer fringing capacitances
    if ("CF" not in keys(param)):
        CF_i = 2.0 * EPSROX * EPS0 / M_PI * lln(CFRCOEFF * (1.0 + 0.4e-6 / TOXE))    
    Cgsof = CGSO + CF_i
    Cgdof = CGDO + CF_i

    # Overlap capacitances
    if (COVMOD == 0):
        Qovs = -Wact * NF * Cgsof * Vgs_ov_noswap
        Qovd = -Wact * NF * Cgdof * Vgd_ov_noswap
    else:
        T0    = sqrt((Vgs_ov_noswap - Vfbsdr + DELTA_1) * (Vgs_ov_noswap - Vfbsdr + DELTA_1) + 4.0 * DELTA_1)
        Vgsov = 0.5 * (Vgs_ov_noswap - Vfbsdr + DELTA_1 - T0)
        T1    = sqrt(1.0 - 4.0 * Vgsov / CKAPPAS_i)
        Qovs  = -Wact * NF * (Cgsof * Vgs_ov_noswap + CGSL_i * (Vgs_ov_noswap - Vfbsdr - Vgsov - 0.5 * CKAPPAS_i * (-1.0 + T1)))
        T0    = sqrt((Vgd_ov_noswap - Vfbsdr + DELTA_1) * (Vgd_ov_noswap - Vfbsdr + DELTA_1) + 4.0 * DELTA_1)
        Vgdov = 0.5 * (Vgd_ov_noswap - Vfbsdr + DELTA_1 - T0)
        T2    = sqrt(1.0 - 4.0 * Vgdov / CKAPPAD_i)
        Qovd  = -Wact * NF * (Cgdof * Vgd_ov_noswap + CGDL_i * (Vgd_ov_noswap - Vfbsdr - Vgdov - 0.5 * CKAPPAD_i * (-1.0 + T2)))
    Qovb = -devsign * NF * Lact * CGBO * (Vg - Vb)
    Qovg = -(Qovs + Qovd + Qovb)

    #=
    # Edge FET model
    if (EDGEFET == 1):
        phib_edge     = lln(NDEPEDGE_i / ni)
        Phist         = max(0.4 + Vt * phib_edge + PHIN_i, 0.4)
        sqrtPhist     = sqrt(Phist)
        T1DEP         = sqrt(2.0 * epssi / (q * NDEPEDGE_i))
        NFACTOREDGE_t = NFACTOREDGE_i * hypsmooth((1.0 + TNFACTOREDGE_i * (TRatio - 1.0)), 1e-3)
        ETA0EDGE_t    = ETA0EDGE_i * (1.0 + TETA0EDGE_i * (TRatio - 1.0))
        PhistVbs = Smooth(Phist - Vbsx, 0.05, 0.1)
        sqrtPhistVbs  = sqrt(PhistVbs)
        Xdep          = T1DEP * sqrtPhistVbs
        Cdep          = epssi / Xdep
        cdsc          = CITEDGE_i + NFACTOREDGE_t + CDSCDEDGE_i * Vdsx - CDSCBEDGE_i * Vbsx
        T1            = 1.0 + cdsc/Cox
        n = Smooth(T1, 1.0, 0.05)
        nVt       = n * Vt
        inv_nVt   = 1.0 / nVt
        vg        = Vg * inv_nVt
        vs        = Vs * inv_nVt
        vfb       = VFB_i * inv_nVt
        dvth_dibl = -(ETA0EDGE_t + ETABEDGE_i * Vbsx) * Vdsx
        dvth_temp = (KT1EDGE_i + KT1LEDGE_i / Leff + KT2EDGE_i * Vbsx) * (TRatio**KT1EXPEDGE_i - 1.0)
        litl_edge = litl * (1.0 + DVT2EDGE * Vbsx)
        T0        = DVT1EDGE * Leff / litl_edge
        if (T0 < 40.0):
            theta_sce_edge = 0.5 * DVT0EDGE / (cosh(T0) - 1.0)
        else:
            theta_sce_edge = DVT0EDGE * lexp(-T0)       
        dvth_sce  = theta_sce_edge * (Vbi_edge - Phist)
        Vth_shift = dvth_dibl - dvth_temp + dvth_sce + DVTEDGE + vth0_stress_EDGE - K2EDGE_i * Vbsx
        vgfb      = vg - vfb - Vth_shift * inv_nVt

        # Normalized body factor
        DGAMMAEDGE_i = DGAMMAEDGE * (1.0 + DGAMMAEDGEL * Leff**-DGAMMAEDGELEXP)
        gam_edge          = sqrt(2.0 * q * epssi * NDEPEDGE_i * inv_nVt) / Cox
        gam_edge          = gam_edge * (1.0 + DGAMMAEDGE_i)
        inv_gam           = 1.0 / gam_edge

        # psip: pinch-off voltage
        phib_n_edge  = phib_edge / n
        psip = PO_psip(vgfb, gam_edge, 0.0)
        qs_edge = BSIM_q(psip, phib_n_edge, vs, gam_edge)

        # Approximate pinch-off voltage
        vdsatedge = 2.0 * nVt * qs_edge + 2.0 * nVt
        Vdsatedge = vdsatedge
        Vdsatedge = Vdsatedge + Vs

        # Vdssat clamped to avoid negative values during transient simulation
        Vdssate = Smooth(Vdsatedge - Vs, 0.0, 1.0e-3)
        T7     = (Vds / Vdssate)**(1.0 / DELTA_t)
        T8     = (1.0 + T7)**-DELTA_t
        Vdseff = Vds * T8
        vdeff  = (Vdseff + Vs) * inv_nVt
        qdeff_edge = BSIM_q(psip, phib_n_edge, vdeff, gam_edge)

        # Nq calculation for Edge FET
        psipclamp = Smooth(psip, 1.0, 2.0)
        sqrtpsip = sqrt(psipclamp)
        psiavg   = psip - qs_edge - qdeff_edge -1.0
        T0 = Smooth(psiavg, 1.0, 2.0)
        T2       = sqrt(T0)
        nq_edge  = 1.0 + gam_edge / (sqrtpsip + T2)
        ids_edge = 2.0 * NF * nq_edge * ueff * WEDGE / Leff * Cox * nVt * nVt * ((qs_edge - qdeff_edge) * (1.0 + qs_edge + qdeff_edge)) * Moc
        ids      = ids_edge + ids    
    =#
    return ids

bsimbulk()
