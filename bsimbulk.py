from math import *
import matplotlib.pyplot as plt
import numpy as np
import re

class bsimbulk:
    """
    BSIM-BULK 107.0.0 model
    """
    ntype = 1
    q = 1.60219e-19
    EPS0 = 8.85418e-12
    KboQ = 8.617087e-5      # Joule/degree
    P_CELSIUS0 = 273.15
    Oneby3 = 0.33333333333333333
    DELTA_1 = 0.02
    REFTEMP = 300.15       # 27 degrees C
    EXPL_THRESHOLD = 80.0
    MAX_EXPL = 5.540622384e34
    MIN_EXPL = 1.804851387e-35
    M_PI = 3.14159265358979323846

    def __repr__(self):
        return f"A bsimbulk class"

    # Set param ungiven first, then call param_update()
    def __init__(self, **kwargs):
        self.VDgiven = False
        self.VGgiven = False
        self.VSgiven = False
        self.VBgiven = False
        self.TEMPgiven = False
        self.Lgiven = False
        self.Wgiven = False
        self.NFgiven = False
        self.NRSgiven = False
        self.NRDgiven = False
        self.VFBSDOFFgiven = False
        self.MINZgiven = False
        self.RGATEMODgiven = False
        self.RBODYMODgiven = False
        self.GEOMODgiven = False
        self.RGEOMODgiven = False
        self.RBPBgiven = False
        self.RBPDgiven = False
        self.RBPSgiven = False
        self.RBDBgiven = False
        self.RBSBgiven = False
        self.SAgiven = False
        self.SBgiven = False
        self.SDgiven = False
        self.SCAgiven = False
        self.SCBgiven = False
        self.SCCgiven = False
        self.SCgiven = False
        self.ASgiven = False
        self.ADgiven = False
        self.PSgiven = False
        self.PDgiven = False
        self.XGWgiven = False
        self.NGCONgiven = False
        self.DTEMPgiven = False
        self.MULU0given = False
        self.DELVTOgiven = False
        self.IDS0MULTgiven = False
        self.EDGEFETgiven = False
        self.SSLMODgiven = False
        self.TYPEgiven = False
        self.CVMODgiven = False
        self.COVMODgiven = False
        self.RDSMODgiven = False
        self.WPEMODgiven = False
        self.ASYMMODgiven = False
        self.GIDLMODgiven = False
        self.IGCMODgiven = False
        self.IGBMODgiven = False
        self.TNOIMODgiven = False
        self.SHMODgiven = False
        self.MOBSCALEgiven = False
        self.LLONGgiven = False
        self.LMLTgiven = False
        self.WMLTgiven = False
        self.XLgiven = False
        self.WWIDEgiven = False
        self.XWgiven = False
        self.LINTgiven = False
        self.LLgiven = False
        self.LWgiven = False
        self.LWLgiven = False
        self.LLNgiven = False
        self.LWNgiven = False
        self.WINTgiven = False
        self.WLgiven = False
        self.WWgiven = False
        self.WWLgiven = False
        self.WLNgiven = False
        self.WWNgiven = False
        self.DLCgiven = False
        self.LLCgiven = False
        self.LWCgiven = False
        self.LWLCgiven = False
        self.DWCgiven = False
        self.WLCgiven = False
        self.WWCgiven = False
        self.WWLCgiven = False
        self.TOXEgiven = False
        self.TOXPgiven = False
        self.DTOXgiven = False
        self.NDEPgiven = False
        self.NDEPL1given = False
        self.NDEPLEXP1given = False
        self.NDEPL2given = False
        self.NDEPLEXP2given = False
        self.NDEPWgiven = False
        self.NDEPWEXPgiven = False
        self.NDEPWLgiven = False
        self.NDEPWLEXPgiven = False
        self.LNDEPgiven = False
        self.WNDEPgiven = False
        self.PNDEPgiven = False
        self.NDEPCVgiven = False
        self.NDEPCVL1given = False
        self.NDEPCVLEXP1given = False
        self.NDEPCVL2given = False
        self.NDEPCVLEXP2given = False
        self.NDEPCVWgiven = False
        self.NDEPCVWEXPgiven = False
        self.NDEPCVWLgiven = False
        self.NDEPCVWLEXPgiven = False
        self.LNDEPCVgiven = False
        self.WNDEPCVgiven = False
        self.PNDEPCVgiven = False
        self.NGATEgiven = False
        self.LNGATEgiven = False
        self.WNGATEgiven = False
        self.PNGATEgiven = False
        self.EASUBgiven = False
        self.NI0SUBgiven = False
        self.BG0SUBgiven = False
        self.EPSRSUBgiven = False
        self.EPSROXgiven = False
        self.XJgiven = False
        self.LXJgiven = False
        self.WXJgiven = False
        self.PXJgiven = False
        self.VFBgiven = False
        self.LVFBgiven = False
        self.WVFBgiven = False
        self.PVFBgiven = False
        self.VFBCVgiven = False
        self.LVFBCVgiven = False
        self.WVFBCVgiven = False
        self.PVFBCVgiven = False
        self.VFBCVLgiven = False
        self.VFBCVLEXPgiven = False
        self.VFBCVWgiven = False
        self.VFBCVWEXPgiven = False
        self.VFBCVWLgiven = False
        self.VFBCVWLEXPgiven = False
        self.DELVFBACCgiven = False
        self.PERMODgiven = False
        self.DWJgiven = False
        self.NSDgiven = False
        self.LNSDgiven = False
        self.WNSDgiven = False
        self.PNSDgiven = False
        self.DVTP0given = False
        self.LDVTP0given = False
        self.WDVTP0given = False
        self.PDVTP0given = False
        self.DVTP1given = False
        self.LDVTP1given = False
        self.WDVTP1given = False
        self.PDVTP1given = False
        self.DVTP2given = False
        self.LDVTP2given = False
        self.WDVTP2given = False
        self.PDVTP2given = False
        self.DVTP3given = False
        self.LDVTP3given = False
        self.WDVTP3given = False
        self.PDVTP3given = False
        self.DVTP4given = False
        self.LDVTP4given = False
        self.WDVTP4given = False
        self.PDVTP4given = False
        self.DVTP5given = False
        self.LDVTP5given = False
        self.WDVTP5given = False
        self.PDVTP5given = False
        self.PHINgiven = False
        self.LPHINgiven = False
        self.WPHINgiven = False
        self.PPHINgiven = False
        self.ETA0given = False
        self.LETA0given = False
        self.WETA0given = False
        self.PETA0given = False
        self.ETA0Rgiven = False
        self.LETA0Rgiven = False
        self.WETA0Rgiven = False
        self.PETA0Rgiven = False
        self.DSUBgiven = False
        self.ETABgiven = False
        self.ETABEXPgiven = False
        self.LETABgiven = False
        self.WETABgiven = False
        self.PETABgiven = False
        self.K1given = False
        self.K1Lgiven = False
        self.K1LEXPgiven = False
        self.K1Wgiven = False
        self.K1WEXPgiven = False
        self.K1WLgiven = False
        self.K1WLEXPgiven = False
        self.LK1given = False
        self.WK1given = False
        self.PK1given = False
        self.K2given = False
        self.K2Lgiven = False
        self.K2LEXPgiven = False
        self.K2Wgiven = False
        self.K2WEXPgiven = False
        self.K2WLgiven = False
        self.K2WLEXPgiven = False
        self.LK2given = False
        self.WK2given = False
        self.PK2given = False
        self.ADOSgiven = False
        self.BDOSgiven = False
        self.QM0given = False
        self.ETAQMgiven = False
        self.CITgiven = False
        self.LCITgiven = False
        self.WCITgiven = False
        self.PCITgiven = False
        self.NFACTORgiven = False
        self.NFACTORLgiven = False
        self.NFACTORLEXPgiven = False
        self.NFACTORWgiven = False
        self.NFACTORWEXPgiven = False
        self.NFACTORWLgiven = False
        self.NFACTORWLEXPgiven = False
        self.LNFACTORgiven = False
        self.WNFACTORgiven = False
        self.PNFACTORgiven = False
        self.CDSCDgiven = False
        self.CDSCDLgiven = False
        self.CDSCDLEXPgiven = False
        self.LCDSCDgiven = False
        self.WCDSCDgiven = False
        self.PCDSCDgiven = False
        self.CDSCDRgiven = False
        self.CDSCDLRgiven = False
        self.LCDSCDRgiven = False
        self.WCDSCDRgiven = False
        self.PCDSCDRgiven = False
        self.CDSCBgiven = False
        self.CDSCBLgiven = False
        self.CDSCBLEXPgiven = False
        self.LCDSCBgiven = False
        self.WCDSCBgiven = False
        self.PCDSCBgiven = False
        self.VSATgiven = False
        self.LVSATgiven = False
        self.WVSATgiven = False
        self.PVSATgiven = False
        self.VSATLgiven = False
        self.VSATLEXPgiven = False
        self.VSATWgiven = False
        self.VSATWEXPgiven = False
        self.VSATWLgiven = False
        self.VSATWLEXPgiven = False
        self.VSATRgiven = False
        self.LVSATRgiven = False
        self.WVSATRgiven = False
        self.PVSATRgiven = False
        self.DELTAgiven = False
        self.LDELTAgiven = False
        self.WDELTAgiven = False
        self.PDELTAgiven = False
        self.DELTALgiven = False
        self.DELTALEXPgiven = False
        self.VSATCVgiven = False
        self.LVSATCVgiven = False
        self.WVSATCVgiven = False
        self.PVSATCVgiven = False
        self.VSATCVLgiven = False
        self.VSATCVLEXPgiven = False
        self.VSATCVWgiven = False
        self.VSATCVWEXPgiven = False
        self.VSATCVWLgiven = False
        self.VSATCVWLEXPgiven = False
        self.UP1given = False
        self.LP1given = False
        self.UP2given = False
        self.LP2given = False
        self.U0given = False
        self.U0Lgiven = False
        self.U0LEXPgiven = False
        self.LU0given = False
        self.WU0given = False
        self.PU0given = False
        self.U0Rgiven = False
        self.LU0Rgiven = False
        self.WU0Rgiven = False
        self.PU0Rgiven = False
        self.ETAMOBgiven = False
        self.UAgiven = False
        self.UALgiven = False
        self.UALEXPgiven = False
        self.UAWgiven = False
        self.UAWEXPgiven = False
        self.UAWLgiven = False
        self.UAWLEXPgiven = False
        self.LUAgiven = False
        self.WUAgiven = False
        self.PUAgiven = False
        self.UARgiven = False
        self.LUARgiven = False
        self.WUARgiven = False
        self.PUARgiven = False
        self.EUgiven = False
        self.LEUgiven = False
        self.WEUgiven = False
        self.PEUgiven = False
        self.EULgiven = False
        self.EULEXPgiven = False
        self.EUWgiven = False
        self.EUWEXPgiven = False
        self.EUWLgiven = False
        self.EUWLEXPgiven = False
        self.UDgiven = False
        self.UDLgiven = False
        self.UDLEXPgiven = False
        self.LUDgiven = False
        self.WUDgiven = False
        self.PUDgiven = False
        self.UDRgiven = False
        self.LUDRgiven = False
        self.WUDRgiven = False
        self.PUDRgiven = False
        self.UCSgiven = False
        self.LUCSgiven = False
        self.WUCSgiven = False
        self.PUCSgiven = False
        self.UCSRgiven = False
        self.LUCSRgiven = False
        self.WUCSRgiven = False
        self.PUCSRgiven = False
        self.UCgiven = False
        self.UCLgiven = False
        self.UCLEXPgiven = False
        self.UCWgiven = False
        self.UCWEXPgiven = False
        self.UCWLgiven = False
        self.UCWLEXPgiven = False
        self.LUCgiven = False
        self.WUCgiven = False
        self.PUCgiven = False
        self.UCRgiven = False
        self.LUCRgiven = False
        self.WUCRgiven = False
        self.PUCRgiven = False
        self.PCLMgiven = False
        self.PCLMLgiven = False
        self.PCLMLEXPgiven = False
        self.LPCLMgiven = False
        self.WPCLMgiven = False
        self.PPCLMgiven = False
        self.PCLMRgiven = False
        self.LPCLMRgiven = False
        self.WPCLMRgiven = False
        self.PPCLMRgiven = False
        self.PCLMGgiven = False
        self.PCLMCVgiven = False
        self.PCLMCVLgiven = False
        self.PCLMCVLEXPgiven = False
        self.LPCLMCVgiven = False
        self.WPCLMCVgiven = False
        self.PPCLMCVgiven = False
        self.PSCBE1given = False
        self.LPSCBE1given = False
        self.WPSCBE1given = False
        self.PPSCBE1given = False
        self.PSCBE2given = False
        self.LPSCBE2given = False
        self.WPSCBE2given = False
        self.PPSCBE2given = False
        self.PDITSgiven = False
        self.LPDITSgiven = False
        self.WPDITSgiven = False
        self.PPDITSgiven = False
        self.PDITSLgiven = False
        self.PDITSDgiven = False
        self.LPDITSDgiven = False
        self.WPDITSDgiven = False
        self.PPDITSDgiven = False
        self.RSHgiven = False
        self.PRWGgiven = False
        self.LPRWGgiven = False
        self.WPRWGgiven = False
        self.PPRWGgiven = False
        self.PRWBgiven = False
        self.LPRWBgiven = False
        self.WPRWBgiven = False
        self.PPRWBgiven = False
        self.PRWBLgiven = False
        self.PRWBLEXPgiven = False
        self.WRgiven = False
        self.LWRgiven = False
        self.WWRgiven = False
        self.PWRgiven = False
        self.RSWMINgiven = False
        self.LRSWMINgiven = False
        self.WRSWMINgiven = False
        self.PRSWMINgiven = False
        self.RSWgiven = False
        self.LRSWgiven = False
        self.WRSWgiven = False
        self.PRSWgiven = False
        self.RSWLgiven = False
        self.RSWLEXPgiven = False
        self.RDWMINgiven = False
        self.LRDWMINgiven = False
        self.WRDWMINgiven = False
        self.PRDWMINgiven = False
        self.RDWgiven = False
        self.LRDWgiven = False
        self.WRDWgiven = False
        self.PRDWgiven = False
        self.RDWLgiven = False
        self.RDWLEXPgiven = False
        self.RDSWMINgiven = False
        self.LRDSWMINgiven = False
        self.WRDSWMINgiven = False
        self.PRDSWMINgiven = False
        self.RDSWgiven = False
        self.RDSWLgiven = False
        self.RDSWLEXPgiven = False
        self.LRDSWgiven = False
        self.WRDSWgiven = False
        self.PRDSWgiven = False
        self.PSATgiven = False
        self.LPSATgiven = False
        self.WPSATgiven = False
        self.PPSATgiven = False
        self.PSATLgiven = False
        self.PSATLEXPgiven = False
        self.PSATBgiven = False
        self.PSATRgiven = False
        self.LPSATRgiven = False
        self.WPSATRgiven = False
        self.PPSATRgiven = False
        self.LPSATBgiven = False
        self.WPSATBgiven = False
        self.PPSATBgiven = False
        self.PSATXgiven = False
        self.PTWGgiven = False
        self.LPTWGgiven = False
        self.WPTWGgiven = False
        self.PPTWGgiven = False
        self.PTWGLgiven = False
        self.PTWGLEXPgiven = False
        self.PTWGRgiven = False
        self.LPTWGRgiven = False
        self.WPTWGRgiven = False
        self.PPTWGRgiven = False
        self.PTWGLRgiven = False
        self.PTWGLEXPRgiven = False
        self.A1given = False
        self.LA1given = False
        self.WA1given = False
        self.PA1given = False
        self.A11given = False
        self.LA11given = False
        self.WA11given = False
        self.PA11given = False
        self.A2given = False
        self.LA2given = False
        self.WA2given = False
        self.PA2given = False
        self.A21given = False
        self.LA21given = False
        self.WA21given = False
        self.PA21given = False
        self.PDIBLCgiven = False
        self.PDIBLCLgiven = False
        self.PDIBLCLEXPgiven = False
        self.LPDIBLCgiven = False
        self.WPDIBLCgiven = False
        self.PPDIBLCgiven = False
        self.PDIBLCRgiven = False
        self.PDIBLCLRgiven = False
        self.PDIBLCLEXPRgiven = False
        self.LPDIBLCRgiven = False
        self.WPDIBLCRgiven = False
        self.PPDIBLCRgiven = False
        self.PDIBLCBgiven = False
        self.LPDIBLCBgiven = False
        self.WPDIBLCBgiven = False
        self.PPDIBLCBgiven = False
        self.PVAGgiven = False
        self.LPVAGgiven = False
        self.WPVAGgiven = False
        self.PPVAGgiven = False
        self.FPROUTgiven = False
        self.FPROUTLgiven = False
        self.FPROUTLEXPgiven = False
        self.LFPROUTgiven = False
        self.WFPROUTgiven = False
        self.PFPROUTgiven = False
        self.ALPHA0given = False
        self.ALPHA0Lgiven = False
        self.ALPHA0LEXPgiven = False
        self.LALPHA0given = False
        self.WALPHA0given = False
        self.PALPHA0given = False
        self.BETA0given = False
        self.LBETA0given = False
        self.WBETA0given = False
        self.PBETA0given = False
        self.AIGBACCgiven = False
        self.BIGBACCgiven = False
        self.CIGBACCgiven = False
        self.NIGBACCgiven = False
        self.AIGBINVgiven = False
        self.BIGBINVgiven = False
        self.CIGBINVgiven = False
        self.EIGBINVgiven = False
        self.NIGBINVgiven = False
        self.AIGCgiven = False
        self.BIGCgiven = False
        self.CIGCgiven = False
        self.AIGSgiven = False
        self.BIGSgiven = False
        self.CIGSgiven = False
        self.AIGDgiven = False
        self.BIGDgiven = False
        self.CIGDgiven = False
        self.DLCIGgiven = False
        self.DLCIGDgiven = False
        self.POXEDGEgiven = False
        self.NTOXgiven = False
        self.TOXREFgiven = False
        self.PIGCDgiven = False
        self.AIGCLgiven = False
        self.AIGCWgiven = False
        self.AIGSLgiven = False
        self.AIGSWgiven = False
        self.AIGDLgiven = False
        self.AIGDWgiven = False
        self.PIGCDLgiven = False
        self.LAIGBINVgiven = False
        self.WAIGBINVgiven = False
        self.PAIGBINVgiven = False
        self.LBIGBINVgiven = False
        self.WBIGBINVgiven = False
        self.PBIGBINVgiven = False
        self.LCIGBINVgiven = False
        self.WCIGBINVgiven = False
        self.PCIGBINVgiven = False
        self.LEIGBINVgiven = False
        self.WEIGBINVgiven = False
        self.PEIGBINVgiven = False
        self.LNIGBINVgiven = False
        self.WNIGBINVgiven = False
        self.PNIGBINVgiven = False
        self.LAIGBACCgiven = False
        self.WAIGBACCgiven = False
        self.PAIGBACCgiven = False
        self.LBIGBACCgiven = False
        self.WBIGBACCgiven = False
        self.PBIGBACCgiven = False
        self.LCIGBACCgiven = False
        self.WCIGBACCgiven = False
        self.PCIGBACCgiven = False
        self.LNIGBACCgiven = False
        self.WNIGBACCgiven = False
        self.PNIGBACCgiven = False
        self.LAIGCgiven = False
        self.WAIGCgiven = False
        self.PAIGCgiven = False
        self.LBIGCgiven = False
        self.WBIGCgiven = False
        self.PBIGCgiven = False
        self.LCIGCgiven = False
        self.WCIGCgiven = False
        self.PCIGCgiven = False
        self.LAIGSgiven = False
        self.WAIGSgiven = False
        self.PAIGSgiven = False
        self.LBIGSgiven = False
        self.WBIGSgiven = False
        self.PBIGSgiven = False
        self.LCIGSgiven = False
        self.WCIGSgiven = False
        self.PCIGSgiven = False
        self.LAIGDgiven = False
        self.WAIGDgiven = False
        self.PAIGDgiven = False
        self.LBIGDgiven = False
        self.WBIGDgiven = False
        self.PBIGDgiven = False
        self.LCIGDgiven = False
        self.WCIGDgiven = False
        self.PCIGDgiven = False
        self.LPOXEDGEgiven = False
        self.WPOXEDGEgiven = False
        self.PPOXEDGEgiven = False
        self.LDLCIGgiven = False
        self.WDLCIGgiven = False
        self.PDLCIGgiven = False
        self.LDLCIGDgiven = False
        self.WDLCIGDgiven = False
        self.PDLCIGDgiven = False
        self.LNTOXgiven = False
        self.WNTOXgiven = False
        self.PNTOXgiven = False
        self.AGIDLgiven = False
        self.AGIDLLgiven = False
        self.AGIDLWgiven = False
        self.LAGIDLgiven = False
        self.WAGIDLgiven = False
        self.PAGIDLgiven = False
        self.BGIDLgiven = False
        self.LBGIDLgiven = False
        self.WBGIDLgiven = False
        self.PBGIDLgiven = False
        self.CGIDLgiven = False
        self.LCGIDLgiven = False
        self.WCGIDLgiven = False
        self.PCGIDLgiven = False
        self.EGIDLgiven = False
        self.LEGIDLgiven = False
        self.WEGIDLgiven = False
        self.PEGIDLgiven = False
        self.AGISLgiven = False
        self.AGISLLgiven = False
        self.AGISLWgiven = False
        self.LAGISLgiven = False
        self.WAGISLgiven = False
        self.PAGISLgiven = False
        self.BGISLgiven = False
        self.LBGISLgiven = False
        self.WBGISLgiven = False
        self.PBGISLgiven = False
        self.CGISLgiven = False
        self.LCGISLgiven = False
        self.WCGISLgiven = False
        self.PCGISLgiven = False
        self.EGISLgiven = False
        self.LEGISLgiven = False
        self.WEGISLgiven = False
        self.PEGISLgiven = False
        self.CFgiven = False
        self.LCFgiven = False
        self.WCFgiven = False
        self.PCFgiven = False
        self.CFRCOEFFgiven = False
        self.CGSOgiven = False
        self.CGDOgiven = False
        self.CGBOgiven = False
        self.CGSLgiven = False
        self.LCGSLgiven = False
        self.WCGSLgiven = False
        self.PCGSLgiven = False
        self.CGDLgiven = False
        self.LCGDLgiven = False
        self.WCGDLgiven = False
        self.PCGDLgiven = False
        self.CKAPPASgiven = False
        self.LCKAPPASgiven = False
        self.WCKAPPASgiven = False
        self.PCKAPPASgiven = False
        self.CKAPPADgiven = False
        self.LCKAPPADgiven = False
        self.WCKAPPADgiven = False
        self.PCKAPPADgiven = False
        self.DMCGgiven = False
        self.DMCIgiven = False
        self.DMDGgiven = False
        self.DMCGTgiven = False
        self.XGLgiven = False
        self.RSHGgiven = False
        self.CJSgiven = False
        self.CJDgiven = False
        self.CJSWSgiven = False
        self.CJSWDgiven = False
        self.CJSWGSgiven = False
        self.CJSWGDgiven = False
        self.PBSgiven = False
        self.PBDgiven = False
        self.PBSWSgiven = False
        self.PBSWDgiven = False
        self.PBSWGSgiven = False
        self.PBSWGDgiven = False
        self.MJSgiven = False
        self.MJDgiven = False
        self.MJSWSgiven = False
        self.MJSWDgiven = False
        self.MJSWGSgiven = False
        self.MJSWGDgiven = False
        self.JSSgiven = False
        self.JSDgiven = False
        self.JSWSgiven = False
        self.JSWDgiven = False
        self.JSWGSgiven = False
        self.JSWGDgiven = False
        self.NJSgiven = False
        self.NJDgiven = False
        self.IJTHSFWDgiven = False
        self.IJTHDFWDgiven = False
        self.IJTHSREVgiven = False
        self.IJTHDREVgiven = False
        self.BVSgiven = False
        self.BVDgiven = False
        self.XJBVSgiven = False
        self.XJBVDgiven = False
        self.JTSSgiven = False
        self.JTSDgiven = False
        self.JTSSWSgiven = False
        self.JTSSWDgiven = False
        self.JTSSWGSgiven = False
        self.JTSSWGDgiven = False
        self.JTWEFFgiven = False
        self.NJTSgiven = False
        self.NJTSDgiven = False
        self.NJTSSWgiven = False
        self.NJTSSWDgiven = False
        self.NJTSSWGgiven = False
        self.NJTSSWGDgiven = False
        self.VTSSgiven = False
        self.VTSDgiven = False
        self.VTSSWSgiven = False
        self.VTSSWDgiven = False
        self.VTSSWGSgiven = False
        self.VTSSWGDgiven = False
        self.XRCRG1given = False
        self.XRCRG2given = False
        self.GBMINgiven = False
        self.RBPS0given = False
        self.RBPSLgiven = False
        self.RBPSWgiven = False
        self.RBPSNFgiven = False
        self.RBPD0given = False
        self.RBPDLgiven = False
        self.RBPDWgiven = False
        self.RBPDNFgiven = False
        self.RBPBX0given = False
        self.RBPBXLgiven = False
        self.RBPBXWgiven = False
        self.RBPBXNFgiven = False
        self.RBPBY0given = False
        self.RBPBYLgiven = False
        self.RBPBYWgiven = False
        self.RBPBYNFgiven = False
        self.RBSBX0given = False
        self.RBSBY0given = False
        self.RBDBX0given = False
        self.RBDBY0given = False
        self.RBSDBXLgiven = False
        self.RBSDBXWgiven = False
        self.RBSDBXNFgiven = False
        self.RBSDBYLgiven = False
        self.RBSDBYWgiven = False
        self.RBSDBYNFgiven = False
        self.EFgiven = False
        self.EMgiven = False
        self.NOIAgiven = False
        self.NOIBgiven = False
        self.NOICgiven = False
        self.LINTNOIgiven = False
        self.NOIA1given = False
        self.NOIAXgiven = False
        self.NTNOIgiven = False
        self.RNOIAgiven = False
        self.RNOIBgiven = False
        self.RNOICgiven = False
        self.TNOIAgiven = False
        self.TNOIBgiven = False
        self.TNOICgiven = False
        self.BINUNITgiven = False
        self.DLBINgiven = False
        self.DWBINgiven = False
        self.TNOMgiven = False
        self.TBGASUBgiven = False
        self.TBGBSUBgiven = False
        self.TNFACTORgiven = False
        self.UTEgiven = False
        self.LUTEgiven = False
        self.WUTEgiven = False
        self.PUTEgiven = False
        self.UTELgiven = False
        self.UA1given = False
        self.LUA1given = False
        self.WUA1given = False
        self.PUA1given = False
        self.UA1Lgiven = False
        self.UC1given = False
        self.LUC1given = False
        self.WUC1given = False
        self.PUC1given = False
        self.UD1given = False
        self.LUD1given = False
        self.WUD1given = False
        self.PUD1given = False
        self.UD1Lgiven = False
        self.EU1given = False
        self.LEU1given = False
        self.WEU1given = False
        self.PEU1given = False
        self.UCSTEgiven = False
        self.LUCSTEgiven = False
        self.WUCSTEgiven = False
        self.PUCSTEgiven = False
        self.TETA0given = False
        self.PRTgiven = False
        self.LPRTgiven = False
        self.WPRTgiven = False
        self.PPRTgiven = False
        self.ATgiven = False
        self.LATgiven = False
        self.WATgiven = False
        self.PATgiven = False
        self.ATLgiven = False
        self.TDELTAgiven = False
        self.PTWGTgiven = False
        self.LPTWGTgiven = False
        self.WPTWGTgiven = False
        self.PPTWGTgiven = False
        self.PTWGTLgiven = False
        self.KT1given = False
        self.KT1EXPgiven = False
        self.KT1Lgiven = False
        self.LKT1given = False
        self.WKT1given = False
        self.PKT1given = False
        self.KT2given = False
        self.LKT2given = False
        self.WKT2given = False
        self.PKT2given = False
        self.IITgiven = False
        self.LIITgiven = False
        self.WIITgiven = False
        self.PIITgiven = False
        self.IGTgiven = False
        self.LIGTgiven = False
        self.WIGTgiven = False
        self.PIGTgiven = False
        self.TGIDLgiven = False
        self.LTGIDLgiven = False
        self.WTGIDLgiven = False
        self.PTGIDLgiven = False
        self.TCJgiven = False
        self.TCJSWgiven = False
        self.TCJSWGgiven = False
        self.TPBgiven = False
        self.TPBSWgiven = False
        self.TPBSWGgiven = False
        self.XTISgiven = False
        self.XTIDgiven = False
        self.XTSSgiven = False
        self.XTSDgiven = False
        self.XTSSWSgiven = False
        self.XTSSWDgiven = False
        self.XTSSWGSgiven = False
        self.XTSSWGDgiven = False
        self.TNJTSgiven = False
        self.TNJTSDgiven = False
        self.TNJTSSWgiven = False
        self.TNJTSSWDgiven = False
        self.TNJTSSWGgiven = False
        self.TNJTSSWGDgiven = False
        self.RTH0given = False
        self.CTH0given = False
        self.WTH0given = False
        self.SAREFgiven = False
        self.SBREFgiven = False
        self.WLODgiven = False
        self.KU0given = False
        self.KVSATgiven = False
        self.TKU0given = False
        self.LKU0given = False
        self.WKU0given = False
        self.PKU0given = False
        self.LLODKU0given = False
        self.WLODKU0given = False
        self.KVTH0given = False
        self.LKVTH0given = False
        self.WKVTH0given = False
        self.PKVTH0given = False
        self.LLODVTHgiven = False
        self.WLODVTHgiven = False
        self.STK2given = False
        self.LODK2given = False
        self.STETA0given = False
        self.LODETA0given = False
        self.WEBgiven = False
        self.WECgiven = False
        self.KVTH0WEgiven = False
        self.LKVTH0WEgiven = False
        self.WKVTH0WEgiven = False
        self.PKVTH0WEgiven = False
        self.K2WEgiven = False
        self.LK2WEgiven = False
        self.WK2WEgiven = False
        self.PK2WEgiven = False
        self.KU0WEgiven = False
        self.LKU0WEgiven = False
        self.WKU0WEgiven = False
        self.PKU0WEgiven = False
        self.SCREFgiven = False
        self.SSL0given = False
        self.SSL1given = False
        self.SSL2given = False
        self.SSL3given = False
        self.SSL4given = False
        self.SSL5given = False
        self.SSLEXP1given = False
        self.SSLEXP2given = False
        self.AVDSXgiven = False
        self.WEDGEgiven = False
        self.DGAMMAEDGEgiven = False
        self.DGAMMAEDGELgiven = False
        self.DGAMMAEDGELEXPgiven = False
        self.DVTEDGEgiven = False
        self.NDEPEDGEgiven = False
        self.LNDEPEDGEgiven = False
        self.WNDEPEDGEgiven = False
        self.PNDEPEDGEgiven = False
        self.NFACTOREDGEgiven = False
        self.LNFACTOREDGEgiven = False
        self.WNFACTOREDGEgiven = False
        self.PNFACTOREDGEgiven = False
        self.CITEDGEgiven = False
        self.LCITEDGEgiven = False
        self.WCITEDGEgiven = False
        self.PCITEDGEgiven = False
        self.CDSCDEDGEgiven = False
        self.LCDSCDEDGEgiven = False
        self.WCDSCDEDGEgiven = False
        self.PCDSCDEDGEgiven = False
        self.CDSCBEDGEgiven = False
        self.LCDSCBEDGEgiven = False
        self.WCDSCBEDGEgiven = False
        self.PCDSCBEDGEgiven = False
        self.ETA0EDGEgiven = False
        self.LETA0EDGEgiven = False
        self.WETA0EDGEgiven = False
        self.PETA0EDGEgiven = False
        self.ETABEDGEgiven = False
        self.LETABEDGEgiven = False
        self.WETABEDGEgiven = False
        self.PETABEDGEgiven = False
        self.KT1EDGEgiven = False
        self.LKT1EDGEgiven = False
        self.WKT1EDGEgiven = False
        self.PKT1EDGEgiven = False
        self.KT1LEDGEgiven = False
        self.LKT1LEDGEgiven = False
        self.WKT1LEDGEgiven = False
        self.PKT1LEDGEgiven = False
        self.KT2EDGEgiven = False
        self.LKT2EDGEgiven = False
        self.WKT2EDGEgiven = False
        self.PKT2EDGEgiven = False
        self.KT1EXPEDGEgiven = False
        self.LKT1EXPEDGEgiven = False
        self.WKT1EXPEDGEgiven = False
        self.PKT1EXPEDGEgiven = False
        self.TNFACTOREDGEgiven = False
        self.LTNFACTOREDGEgiven = False
        self.WTNFACTOREDGEgiven = False
        self.PTNFACTOREDGEgiven = False
        self.TETA0EDGEgiven = False
        self.LTETA0EDGEgiven = False
        self.WTETA0EDGEgiven = False
        self.PTETA0EDGEgiven = False
        self.DVT0EDGEgiven = False
        self.DVT1EDGEgiven = False
        self.DVT2EDGEgiven = False
        self.K2EDGEgiven = False
        self.LK2EDGEgiven = False
        self.WK2EDGEgiven = False
        self.PK2EDGEgiven = False
        self.KVTH0EDGEgiven = False
        self.LKVTH0EDGEgiven = False
        self.WKVTH0EDGEgiven = False
        self.PKVTH0EDGEgiven = False
        self.STK2EDGEgiven = False
        self.LSTK2EDGEgiven = False
        self.WSTK2EDGEgiven = False
        self.PSTK2EDGEgiven = False
        self.STETA0EDGEgiven = False
        self.LSTETA0EDGEgiven = False
        self.WSTETA0EDGEgiven = False
        self.PSTETA0EDGEgiven = False
        self.IGCLAMPgiven = False
        self.LPgiven = False
        self.RNOIKgiven = False
        self.TNOIKgiven = False
        self.TNOIK2given = False
        self.K0given = False
        self.LK0given = False
        self.WK0given = False
        self.PK0given = False
        self.K01given = False
        self.LK01given = False
        self.WK01given = False
        self.PK01given = False
        self.M0given = False
        self.LM0given = False
        self.WM0given = False
        self.PM0given = False
        self.M01given = False
        self.LM01given = False
        self.WM01given = False
        self.PM01given = False
        self.NEDGEgiven = False
        self.NOIA1_EDGEgiven = False
        self.NOIAX_EDGEgiven = False
        self.FNOIMODgiven = False
        self.LHgiven = False
        self.NOIA2given = False
        self.HNDEPgiven = False
        self.ABULKgiven = False
        self.C0given = False
        self.LC0given = False
        self.WC0given = False
        self.PC0given = False
        self.C01given = False
        self.LC01given = False
        self.WC01given = False
        self.PC01given = False
        self.C0SIgiven = False
        self.LC0SIgiven = False
        self.WC0SIgiven = False
        self.PC0SIgiven = False
        self.C0SI1given = False
        self.LC0SI1given = False
        self.WC0SI1given = False
        self.PC0SI1given = False
        self.C0SISATgiven = False
        self.LC0SISATgiven = False
        self.WC0SISATgiven = False
        self.PC0SISATgiven = False
        self.C0SISAT1given = False
        self.LC0SISAT1given = False
        self.WC0SISAT1given = False
        self.PC0SISAT1given = False
        self.minrgiven = False
        self.HVMODgiven = False
        self.HVCAPgiven = False
        self.HVCAPSgiven = False
        self.IIMODgiven = False
        self.NDRIFTDgiven = False
        self.VDRIFTgiven = False
        self.MDRIFTgiven = False
        self.NDRIFTSgiven = False
        self.RDLCWgiven = False
        self.RSLCWgiven = False
        self.PDRWBgiven = False
        self.VFBDRIFTgiven = False
        self.VFBOVgiven = False
        self.LOVERgiven = False
        self.LOVERACCgiven = False
        self.NDRgiven = False
        self.SLHVgiven = False
        self.SLHV1given = False
        self.ALPHADRgiven = False
        self.BETADRgiven = False
        self.PRTHVgiven = False
        self.ATHVgiven = False
        self.HVFACTORgiven = False
        self.DRII1given = False
        self.DRII2given = False
        self.DELTAIIgiven = False
        self.param_update(**kwargs)

    # Param initialization and later update
    def param_update(self, **param):
        if 'VD' in param:
            self.VD = param['VD']
            self.VDgiven = True
        else:
            if self.VDgiven == False:
                self.VD = 1.0
        if 'VG' in param:
            self.VG = param['VG']
            self.VGgiven = True
        else:
            if self.VGgiven == False:
                self.VG = 1.0
        if 'VS' in param:
            self.VS = param['VS']
            self.VSgiven = True
        else:
            if self.VSgiven == False:
                self.VS = 0.0
        if 'VB' in param:
            self.VB = param['VB']
            self.VBgiven = True
        else:
            if self.VBgiven == False:
                self.VB = 0.0
        if 'TEMP' in param:
            self.TEMP = param['TEMP']
            self.TEMPgiven = True
        else:
            if self.TEMPgiven == False:
                self.TEMP = 25.0
        if 'L' in param:
            self.L = param['L']
            self.Lgiven = True
        elif 'L'.swapcase() in param:
            self.L = param['L'.swapcase()]
            self.Lgiven = True
        else:
            if self.Lgiven == False:
                self.L = 1e-05
        if 'W' in param:
            self.W = param['W']
            self.Wgiven = True
        elif 'W'.swapcase() in param:
            self.W = param['W'.swapcase()]
            self.Wgiven = True
        else:
            if self.Wgiven == False:
                self.W = 1e-05
        if 'NF' in param:
            self.NF = param['NF']
            self.NFgiven = True
        elif 'NF'.swapcase() in param:
            self.NF = param['NF'.swapcase()]
            self.NFgiven = True
        else:
            if self.NFgiven == False:
                self.NF = 1.0
        if 'NRS' in param:
            self.NRS = param['NRS']
            self.NRSgiven = True
        elif 'NRS'.swapcase() in param:
            self.NRS = param['NRS'.swapcase()]
            self.NRSgiven = True
        else:
            if self.NRSgiven == False:
                self.NRS = 1.0
        if 'NRD' in param:
            self.NRD = param['NRD']
            self.NRDgiven = True
        elif 'NRD'.swapcase() in param:
            self.NRD = param['NRD'.swapcase()]
            self.NRDgiven = True
        else:
            if self.NRDgiven == False:
                self.NRD = 1.0
        if 'VFBSDOFF' in param:
            self.VFBSDOFF = param['VFBSDOFF']
            self.VFBSDOFFgiven = True
        elif 'VFBSDOFF'.swapcase() in param:
            self.VFBSDOFF = param['VFBSDOFF'.swapcase()]
            self.VFBSDOFFgiven = True
        else:
            if self.VFBSDOFFgiven == False:
                self.VFBSDOFF = 0.0
        if 'MINZ' in param:
            self.MINZ = param['MINZ']
            self.MINZgiven = True
        elif 'MINZ'.swapcase() in param:
            self.MINZ = param['MINZ'.swapcase()]
            self.MINZgiven = True
        else:
            if self.MINZgiven == False:
                self.MINZ = 0.0
        if 'RGATEMOD' in param:
            self.RGATEMOD = param['RGATEMOD']
            self.RGATEMODgiven = True
        elif 'RGATEMOD'.swapcase() in param:
            self.RGATEMOD = param['RGATEMOD'.swapcase()]
            self.RGATEMODgiven = True
        else:
            if self.RGATEMODgiven == False:
                self.RGATEMOD = 0.0
        if 'RBODYMOD' in param:
            self.RBODYMOD = param['RBODYMOD']
            self.RBODYMODgiven = True
        elif 'RBODYMOD'.swapcase() in param:
            self.RBODYMOD = param['RBODYMOD'.swapcase()]
            self.RBODYMODgiven = True
        else:
            if self.RBODYMODgiven == False:
                self.RBODYMOD = 0.0
        if 'GEOMOD' in param:
            self.GEOMOD = param['GEOMOD']
            self.GEOMODgiven = True
        elif 'GEOMOD'.swapcase() in param:
            self.GEOMOD = param['GEOMOD'.swapcase()]
            self.GEOMODgiven = True
        else:
            if self.GEOMODgiven == False:
                self.GEOMOD = 0.0
        if 'RGEOMOD' in param:
            self.RGEOMOD = param['RGEOMOD']
            self.RGEOMODgiven = True
        elif 'RGEOMOD'.swapcase() in param:
            self.RGEOMOD = param['RGEOMOD'.swapcase()]
            self.RGEOMODgiven = True
        else:
            if self.RGEOMODgiven == False:
                self.RGEOMOD = 0.0
        if 'RBPB' in param:
            self.RBPB = param['RBPB']
            self.RBPBgiven = True
        elif 'RBPB'.swapcase() in param:
            self.RBPB = param['RBPB'.swapcase()]
            self.RBPBgiven = True
        else:
            if self.RBPBgiven == False:
                self.RBPB = 50.0
        if 'RBPD' in param:
            self.RBPD = param['RBPD']
            self.RBPDgiven = True
        elif 'RBPD'.swapcase() in param:
            self.RBPD = param['RBPD'.swapcase()]
            self.RBPDgiven = True
        else:
            if self.RBPDgiven == False:
                self.RBPD = 50.0
        if 'RBPS' in param:
            self.RBPS = param['RBPS']
            self.RBPSgiven = True
        elif 'RBPS'.swapcase() in param:
            self.RBPS = param['RBPS'.swapcase()]
            self.RBPSgiven = True
        else:
            if self.RBPSgiven == False:
                self.RBPS = 50.0
        if 'RBDB' in param:
            self.RBDB = param['RBDB']
            self.RBDBgiven = True
        elif 'RBDB'.swapcase() in param:
            self.RBDB = param['RBDB'.swapcase()]
            self.RBDBgiven = True
        else:
            if self.RBDBgiven == False:
                self.RBDB = 50.0
        if 'RBSB' in param:
            self.RBSB = param['RBSB']
            self.RBSBgiven = True
        elif 'RBSB'.swapcase() in param:
            self.RBSB = param['RBSB'.swapcase()]
            self.RBSBgiven = True
        else:
            if self.RBSBgiven == False:
                self.RBSB = 50.0
        if 'SA' in param:
            self.SA = param['SA']
            self.SAgiven = True
        elif 'SA'.swapcase() in param:
            self.SA = param['SA'.swapcase()]
            self.SAgiven = True
        else:
            if self.SAgiven == False:
                self.SA = 0.0
        if 'SB' in param:
            self.SB = param['SB']
            self.SBgiven = True
        elif 'SB'.swapcase() in param:
            self.SB = param['SB'.swapcase()]
            self.SBgiven = True
        else:
            if self.SBgiven == False:
                self.SB = 0.0
        if 'SD' in param:
            self.SD = param['SD']
            self.SDgiven = True
        elif 'SD'.swapcase() in param:
            self.SD = param['SD'.swapcase()]
            self.SDgiven = True
        else:
            if self.SDgiven == False:
                self.SD = 0.0
        if 'SCA' in param:
            self.SCA = param['SCA']
            self.SCAgiven = True
        elif 'SCA'.swapcase() in param:
            self.SCA = param['SCA'.swapcase()]
            self.SCAgiven = True
        else:
            if self.SCAgiven == False:
                self.SCA = 0.0
        if 'SCB' in param:
            self.SCB = param['SCB']
            self.SCBgiven = True
        elif 'SCB'.swapcase() in param:
            self.SCB = param['SCB'.swapcase()]
            self.SCBgiven = True
        else:
            if self.SCBgiven == False:
                self.SCB = 0.0
        if 'SCC' in param:
            self.SCC = param['SCC']
            self.SCCgiven = True
        elif 'SCC'.swapcase() in param:
            self.SCC = param['SCC'.swapcase()]
            self.SCCgiven = True
        else:
            if self.SCCgiven == False:
                self.SCC = 0.0
        if 'SC' in param:
            self.SC = param['SC']
            self.SCgiven = True
        elif 'SC'.swapcase() in param:
            self.SC = param['SC'.swapcase()]
            self.SCgiven = True
        else:
            if self.SCgiven == False:
                self.SC = 0.0
        if 'AS' in param:
            self.AS = param['AS']
            self.ASgiven = True
        elif 'AS'.swapcase() in param:
            self.AS = param['AS'.swapcase()]
            self.ASgiven = True
        else:
            if self.ASgiven == False:
                self.AS = 0.0
        if 'AD' in param:
            self.AD = param['AD']
            self.ADgiven = True
        elif 'AD'.swapcase() in param:
            self.AD = param['AD'.swapcase()]
            self.ADgiven = True
        else:
            if self.ADgiven == False:
                self.AD = 0.0
        if 'PS' in param:
            self.PS = param['PS']
            self.PSgiven = True
        elif 'PS'.swapcase() in param:
            self.PS = param['PS'.swapcase()]
            self.PSgiven = True
        else:
            if self.PSgiven == False:
                self.PS = 0.0
        if 'PD' in param:
            self.PD = param['PD']
            self.PDgiven = True
        elif 'PD'.swapcase() in param:
            self.PD = param['PD'.swapcase()]
            self.PDgiven = True
        else:
            if self.PDgiven == False:
                self.PD = 0.0
        if 'XGW' in param:
            self.XGW = param['XGW']
            self.XGWgiven = True
        elif 'XGW'.swapcase() in param:
            self.XGW = param['XGW'.swapcase()]
            self.XGWgiven = True
        else:
            if self.XGWgiven == False:
                self.XGW = 0.0
        if 'NGCON' in param:
            self.NGCON = param['NGCON']
            self.NGCONgiven = True
        elif 'NGCON'.swapcase() in param:
            self.NGCON = param['NGCON'.swapcase()]
            self.NGCONgiven = True
        else:
            if self.NGCONgiven == False:
                self.NGCON = 1.0
        if 'DTEMP' in param:
            self.DTEMP = param['DTEMP']
            self.DTEMPgiven = True
        elif 'DTEMP'.swapcase() in param:
            self.DTEMP = param['DTEMP'.swapcase()]
            self.DTEMPgiven = True
        else:
            if self.DTEMPgiven == False:
                self.DTEMP = 0.0
        if 'MULU0' in param:
            self.MULU0 = param['MULU0']
            self.MULU0given = True
        elif 'MULU0'.swapcase() in param:
            self.MULU0 = param['MULU0'.swapcase()]
            self.MULU0given = True
        else:
            if self.MULU0given == False:
                self.MULU0 = 1.0
        if 'DELVTO' in param:
            self.DELVTO = param['DELVTO']
            self.DELVTOgiven = True
        elif 'DELVTO'.swapcase() in param:
            self.DELVTO = param['DELVTO'.swapcase()]
            self.DELVTOgiven = True
        else:
            if self.DELVTOgiven == False:
                self.DELVTO = 0.0
        if 'IDS0MULT' in param:
            self.IDS0MULT = param['IDS0MULT']
            self.IDS0MULTgiven = True
        elif 'IDS0MULT'.swapcase() in param:
            self.IDS0MULT = param['IDS0MULT'.swapcase()]
            self.IDS0MULTgiven = True
        else:
            if self.IDS0MULTgiven == False:
                self.IDS0MULT = 1.0
        if 'EDGEFET' in param:
            self.EDGEFET = param['EDGEFET']
            self.EDGEFETgiven = True
        elif 'EDGEFET'.swapcase() in param:
            self.EDGEFET = param['EDGEFET'.swapcase()]
            self.EDGEFETgiven = True
        else:
            if self.EDGEFETgiven == False:
                self.EDGEFET = 0.0
        if 'SSLMOD' in param:
            self.SSLMOD = param['SSLMOD']
            self.SSLMODgiven = True
        elif 'SSLMOD'.swapcase() in param:
            self.SSLMOD = param['SSLMOD'.swapcase()]
            self.SSLMODgiven = True
        else:
            if self.SSLMODgiven == False:
                self.SSLMOD = 0.0
        if 'TYPE' in param:
            self.TYPE = param['TYPE']
            self.TYPEgiven = True
        elif 'TYPE'.swapcase() in param:
            self.TYPE = param['TYPE'.swapcase()]
            self.TYPEgiven = True
        else:
            if self.TYPEgiven == False:
                self.TYPE = self.ntype
        if 'CVMOD' in param:
            self.CVMOD = param['CVMOD']
            self.CVMODgiven = True
        elif 'CVMOD'.swapcase() in param:
            self.CVMOD = param['CVMOD'.swapcase()]
            self.CVMODgiven = True
        else:
            if self.CVMODgiven == False:
                self.CVMOD = 0.0
        if 'COVMOD' in param:
            self.COVMOD = param['COVMOD']
            self.COVMODgiven = True
        elif 'COVMOD'.swapcase() in param:
            self.COVMOD = param['COVMOD'.swapcase()]
            self.COVMODgiven = True
        else:
            if self.COVMODgiven == False:
                self.COVMOD = 0.0
        if 'RDSMOD' in param:
            self.RDSMOD = param['RDSMOD']
            self.RDSMODgiven = True
        elif 'RDSMOD'.swapcase() in param:
            self.RDSMOD = param['RDSMOD'.swapcase()]
            self.RDSMODgiven = True
        else:
            if self.RDSMODgiven == False:
                self.RDSMOD = 0.0
        if 'WPEMOD' in param:
            self.WPEMOD = param['WPEMOD']
            self.WPEMODgiven = True
        elif 'WPEMOD'.swapcase() in param:
            self.WPEMOD = param['WPEMOD'.swapcase()]
            self.WPEMODgiven = True
        else:
            if self.WPEMODgiven == False:
                self.WPEMOD = 0.0
        if 'ASYMMOD' in param:
            self.ASYMMOD = param['ASYMMOD']
            self.ASYMMODgiven = True
        elif 'ASYMMOD'.swapcase() in param:
            self.ASYMMOD = param['ASYMMOD'.swapcase()]
            self.ASYMMODgiven = True
        else:
            if self.ASYMMODgiven == False:
                self.ASYMMOD = 0.0
        if 'GIDLMOD' in param:
            self.GIDLMOD = param['GIDLMOD']
            self.GIDLMODgiven = True
        elif 'GIDLMOD'.swapcase() in param:
            self.GIDLMOD = param['GIDLMOD'.swapcase()]
            self.GIDLMODgiven = True
        else:
            if self.GIDLMODgiven == False:
                self.GIDLMOD = 0.0
        if 'IGCMOD' in param:
            self.IGCMOD = param['IGCMOD']
            self.IGCMODgiven = True
        elif 'IGCMOD'.swapcase() in param:
            self.IGCMOD = param['IGCMOD'.swapcase()]
            self.IGCMODgiven = True
        else:
            if self.IGCMODgiven == False:
                self.IGCMOD = 0.0
        if 'IGBMOD' in param:
            self.IGBMOD = param['IGBMOD']
            self.IGBMODgiven = True
        elif 'IGBMOD'.swapcase() in param:
            self.IGBMOD = param['IGBMOD'.swapcase()]
            self.IGBMODgiven = True
        else:
            if self.IGBMODgiven == False:
                self.IGBMOD = 0.0
        if 'TNOIMOD' in param:
            self.TNOIMOD = param['TNOIMOD']
            self.TNOIMODgiven = True
        elif 'TNOIMOD'.swapcase() in param:
            self.TNOIMOD = param['TNOIMOD'.swapcase()]
            self.TNOIMODgiven = True
        else:
            if self.TNOIMODgiven == False:
                self.TNOIMOD = 0.0
        if 'SHMOD' in param:
            self.SHMOD = param['SHMOD']
            self.SHMODgiven = True
        elif 'SHMOD'.swapcase() in param:
            self.SHMOD = param['SHMOD'.swapcase()]
            self.SHMODgiven = True
        else:
            if self.SHMODgiven == False:
                self.SHMOD = 0.0
        if 'MOBSCALE' in param:
            self.MOBSCALE = param['MOBSCALE']
            self.MOBSCALEgiven = True
        elif 'MOBSCALE'.swapcase() in param:
            self.MOBSCALE = param['MOBSCALE'.swapcase()]
            self.MOBSCALEgiven = True
        else:
            if self.MOBSCALEgiven == False:
                self.MOBSCALE = 0.0
        if 'LLONG' in param:
            self.LLONG = param['LLONG']
            self.LLONGgiven = True
        elif 'LLONG'.swapcase() in param:
            self.LLONG = param['LLONG'.swapcase()]
            self.LLONGgiven = True
        else:
            if self.LLONGgiven == False:
                self.LLONG = 1e-05
        if 'LMLT' in param:
            self.LMLT = param['LMLT']
            self.LMLTgiven = True
        elif 'LMLT'.swapcase() in param:
            self.LMLT = param['LMLT'.swapcase()]
            self.LMLTgiven = True
        else:
            if self.LMLTgiven == False:
                self.LMLT = 1.0
        if 'WMLT' in param:
            self.WMLT = param['WMLT']
            self.WMLTgiven = True
        elif 'WMLT'.swapcase() in param:
            self.WMLT = param['WMLT'.swapcase()]
            self.WMLTgiven = True
        else:
            if self.WMLTgiven == False:
                self.WMLT = 1.0
        if 'XL' in param:
            self.XL = param['XL']
            self.XLgiven = True
        elif 'XL'.swapcase() in param:
            self.XL = param['XL'.swapcase()]
            self.XLgiven = True
        else:
            if self.XLgiven == False:
                self.XL = 0.0
        if 'WWIDE' in param:
            self.WWIDE = param['WWIDE']
            self.WWIDEgiven = True
        elif 'WWIDE'.swapcase() in param:
            self.WWIDE = param['WWIDE'.swapcase()]
            self.WWIDEgiven = True
        else:
            if self.WWIDEgiven == False:
                self.WWIDE = 1e-05
        if 'XW' in param:
            self.XW = param['XW']
            self.XWgiven = True
        elif 'XW'.swapcase() in param:
            self.XW = param['XW'.swapcase()]
            self.XWgiven = True
        else:
            if self.XWgiven == False:
                self.XW = 0.0
        if 'LINT' in param:
            self.LINT = param['LINT']
            self.LINTgiven = True
        elif 'LINT'.swapcase() in param:
            self.LINT = param['LINT'.swapcase()]
            self.LINTgiven = True
        else:
            if self.LINTgiven == False:
                self.LINT = 0.0
        if 'LL' in param:
            self.LL = param['LL']
            self.LLgiven = True
        elif 'LL'.swapcase() in param:
            self.LL = param['LL'.swapcase()]
            self.LLgiven = True
        else:
            if self.LLgiven == False:
                self.LL = 0.0
        if 'LW' in param:
            self.LW = param['LW']
            self.LWgiven = True
        elif 'LW'.swapcase() in param:
            self.LW = param['LW'.swapcase()]
            self.LWgiven = True
        else:
            if self.LWgiven == False:
                self.LW = 0.0
        if 'LWL' in param:
            self.LWL = param['LWL']
            self.LWLgiven = True
        elif 'LWL'.swapcase() in param:
            self.LWL = param['LWL'.swapcase()]
            self.LWLgiven = True
        else:
            if self.LWLgiven == False:
                self.LWL = 0.0
        if 'LLN' in param:
            self.LLN = param['LLN']
            self.LLNgiven = True
        elif 'LLN'.swapcase() in param:
            self.LLN = param['LLN'.swapcase()]
            self.LLNgiven = True
        else:
            if self.LLNgiven == False:
                self.LLN = 1.0
        if 'LWN' in param:
            self.LWN = param['LWN']
            self.LWNgiven = True
        elif 'LWN'.swapcase() in param:
            self.LWN = param['LWN'.swapcase()]
            self.LWNgiven = True
        else:
            if self.LWNgiven == False:
                self.LWN = 1.0
        if 'WINT' in param:
            self.WINT = param['WINT']
            self.WINTgiven = True
        elif 'WINT'.swapcase() in param:
            self.WINT = param['WINT'.swapcase()]
            self.WINTgiven = True
        else:
            if self.WINTgiven == False:
                self.WINT = 0.0
        if 'WL' in param:
            self.WL = param['WL']
            self.WLgiven = True
        elif 'WL'.swapcase() in param:
            self.WL = param['WL'.swapcase()]
            self.WLgiven = True
        else:
            if self.WLgiven == False:
                self.WL = 0.0
        if 'WW' in param:
            self.WW = param['WW']
            self.WWgiven = True
        elif 'WW'.swapcase() in param:
            self.WW = param['WW'.swapcase()]
            self.WWgiven = True
        else:
            if self.WWgiven == False:
                self.WW = 0.0
        if 'WWL' in param:
            self.WWL = param['WWL']
            self.WWLgiven = True
        elif 'WWL'.swapcase() in param:
            self.WWL = param['WWL'.swapcase()]
            self.WWLgiven = True
        else:
            if self.WWLgiven == False:
                self.WWL = 0.0
        if 'WLN' in param:
            self.WLN = param['WLN']
            self.WLNgiven = True
        elif 'WLN'.swapcase() in param:
            self.WLN = param['WLN'.swapcase()]
            self.WLNgiven = True
        else:
            if self.WLNgiven == False:
                self.WLN = 1.0
        if 'WWN' in param:
            self.WWN = param['WWN']
            self.WWNgiven = True
        elif 'WWN'.swapcase() in param:
            self.WWN = param['WWN'.swapcase()]
            self.WWNgiven = True
        else:
            if self.WWNgiven == False:
                self.WWN = 1.0
        if 'DLC' in param:
            self.DLC = param['DLC']
            self.DLCgiven = True
        elif 'DLC'.swapcase() in param:
            self.DLC = param['DLC'.swapcase()]
            self.DLCgiven = True
        else:
            if self.DLCgiven == False:
                self.DLC = 0.0
        if 'LLC' in param:
            self.LLC = param['LLC']
            self.LLCgiven = True
        elif 'LLC'.swapcase() in param:
            self.LLC = param['LLC'.swapcase()]
            self.LLCgiven = True
        else:
            if self.LLCgiven == False:
                self.LLC = 0.0
        if 'LWC' in param:
            self.LWC = param['LWC']
            self.LWCgiven = True
        elif 'LWC'.swapcase() in param:
            self.LWC = param['LWC'.swapcase()]
            self.LWCgiven = True
        else:
            if self.LWCgiven == False:
                self.LWC = 0.0
        if 'LWLC' in param:
            self.LWLC = param['LWLC']
            self.LWLCgiven = True
        elif 'LWLC'.swapcase() in param:
            self.LWLC = param['LWLC'.swapcase()]
            self.LWLCgiven = True
        else:
            if self.LWLCgiven == False:
                self.LWLC = 0.0
        if 'DWC' in param:
            self.DWC = param['DWC']
            self.DWCgiven = True
        elif 'DWC'.swapcase() in param:
            self.DWC = param['DWC'.swapcase()]
            self.DWCgiven = True
        else:
            if self.DWCgiven == False:
                self.DWC = 0.0
        if 'WLC' in param:
            self.WLC = param['WLC']
            self.WLCgiven = True
        elif 'WLC'.swapcase() in param:
            self.WLC = param['WLC'.swapcase()]
            self.WLCgiven = True
        else:
            if self.WLCgiven == False:
                self.WLC = 0.0
        if 'WWC' in param:
            self.WWC = param['WWC']
            self.WWCgiven = True
        elif 'WWC'.swapcase() in param:
            self.WWC = param['WWC'.swapcase()]
            self.WWCgiven = True
        else:
            if self.WWCgiven == False:
                self.WWC = 0.0
        if 'WWLC' in param:
            self.WWLC = param['WWLC']
            self.WWLCgiven = True
        elif 'WWLC'.swapcase() in param:
            self.WWLC = param['WWLC'.swapcase()]
            self.WWLCgiven = True
        else:
            if self.WWLCgiven == False:
                self.WWLC = 0.0
        if 'TOXE' in param:
            self.TOXE = param['TOXE']
            self.TOXEgiven = True
        elif 'TOXE'.swapcase() in param:
            self.TOXE = param['TOXE'.swapcase()]
            self.TOXEgiven = True
        else:
            if self.TOXEgiven == False:
                self.TOXE = 3e-09
        if 'TOXP' in param:
            self.TOXP = param['TOXP']
            self.TOXPgiven = True
        elif 'TOXP'.swapcase() in param:
            self.TOXP = param['TOXP'.swapcase()]
            self.TOXPgiven = True
        else:
            if self.TOXPgiven == False:
                self.TOXP = self.TOXE
        if 'DTOX' in param:
            self.DTOX = param['DTOX']
            self.DTOXgiven = True
        elif 'DTOX'.swapcase() in param:
            self.DTOX = param['DTOX'.swapcase()]
            self.DTOXgiven = True
        else:
            if self.DTOXgiven == False:
                self.DTOX = 0.0
        if 'NDEP' in param:
            self.NDEP = param['NDEP']
            self.NDEPgiven = True
        elif 'NDEP'.swapcase() in param:
            self.NDEP = param['NDEP'.swapcase()]
            self.NDEPgiven = True
        else:
            if self.NDEPgiven == False:
                self.NDEP = 1e+24
        if 'NDEPL1' in param:
            self.NDEPL1 = param['NDEPL1']
            self.NDEPL1given = True
        elif 'NDEPL1'.swapcase() in param:
            self.NDEPL1 = param['NDEPL1'.swapcase()]
            self.NDEPL1given = True
        else:
            if self.NDEPL1given == False:
                self.NDEPL1 = 0.0
        if 'NDEPLEXP1' in param:
            self.NDEPLEXP1 = param['NDEPLEXP1']
            self.NDEPLEXP1given = True
        elif 'NDEPLEXP1'.swapcase() in param:
            self.NDEPLEXP1 = param['NDEPLEXP1'.swapcase()]
            self.NDEPLEXP1given = True
        else:
            if self.NDEPLEXP1given == False:
                self.NDEPLEXP1 = 1.0
        if 'NDEPL2' in param:
            self.NDEPL2 = param['NDEPL2']
            self.NDEPL2given = True
        elif 'NDEPL2'.swapcase() in param:
            self.NDEPL2 = param['NDEPL2'.swapcase()]
            self.NDEPL2given = True
        else:
            if self.NDEPL2given == False:
                self.NDEPL2 = 0.0
        if 'NDEPLEXP2' in param:
            self.NDEPLEXP2 = param['NDEPLEXP2']
            self.NDEPLEXP2given = True
        elif 'NDEPLEXP2'.swapcase() in param:
            self.NDEPLEXP2 = param['NDEPLEXP2'.swapcase()]
            self.NDEPLEXP2given = True
        else:
            if self.NDEPLEXP2given == False:
                self.NDEPLEXP2 = 2.0
        if 'NDEPW' in param:
            self.NDEPW = param['NDEPW']
            self.NDEPWgiven = True
        elif 'NDEPW'.swapcase() in param:
            self.NDEPW = param['NDEPW'.swapcase()]
            self.NDEPWgiven = True
        else:
            if self.NDEPWgiven == False:
                self.NDEPW = 0.0
        if 'NDEPWEXP' in param:
            self.NDEPWEXP = param['NDEPWEXP']
            self.NDEPWEXPgiven = True
        elif 'NDEPWEXP'.swapcase() in param:
            self.NDEPWEXP = param['NDEPWEXP'.swapcase()]
            self.NDEPWEXPgiven = True
        else:
            if self.NDEPWEXPgiven == False:
                self.NDEPWEXP = 1.0
        if 'NDEPWL' in param:
            self.NDEPWL = param['NDEPWL']
            self.NDEPWLgiven = True
        elif 'NDEPWL'.swapcase() in param:
            self.NDEPWL = param['NDEPWL'.swapcase()]
            self.NDEPWLgiven = True
        else:
            if self.NDEPWLgiven == False:
                self.NDEPWL = 0.0
        if 'NDEPWLEXP' in param:
            self.NDEPWLEXP = param['NDEPWLEXP']
            self.NDEPWLEXPgiven = True
        elif 'NDEPWLEXP'.swapcase() in param:
            self.NDEPWLEXP = param['NDEPWLEXP'.swapcase()]
            self.NDEPWLEXPgiven = True
        else:
            if self.NDEPWLEXPgiven == False:
                self.NDEPWLEXP = 1.0
        if 'LNDEP' in param:
            self.LNDEP = param['LNDEP']
            self.LNDEPgiven = True
        elif 'LNDEP'.swapcase() in param:
            self.LNDEP = param['LNDEP'.swapcase()]
            self.LNDEPgiven = True
        else:
            if self.LNDEPgiven == False:
                self.LNDEP = 0.0
        if 'WNDEP' in param:
            self.WNDEP = param['WNDEP']
            self.WNDEPgiven = True
        elif 'WNDEP'.swapcase() in param:
            self.WNDEP = param['WNDEP'.swapcase()]
            self.WNDEPgiven = True
        else:
            if self.WNDEPgiven == False:
                self.WNDEP = 0.0
        if 'PNDEP' in param:
            self.PNDEP = param['PNDEP']
            self.PNDEPgiven = True
        elif 'PNDEP'.swapcase() in param:
            self.PNDEP = param['PNDEP'.swapcase()]
            self.PNDEPgiven = True
        else:
            if self.PNDEPgiven == False:
                self.PNDEP = 0.0
        if 'NDEPCV' in param:
            self.NDEPCV = param['NDEPCV']
            self.NDEPCVgiven = True
        elif 'NDEPCV'.swapcase() in param:
            self.NDEPCV = param['NDEPCV'.swapcase()]
            self.NDEPCVgiven = True
        else:
            if self.NDEPCVgiven == False:
                self.NDEPCV = 1e+24
        if 'NDEPCVL1' in param:
            self.NDEPCVL1 = param['NDEPCVL1']
            self.NDEPCVL1given = True
        elif 'NDEPCVL1'.swapcase() in param:
            self.NDEPCVL1 = param['NDEPCVL1'.swapcase()]
            self.NDEPCVL1given = True
        else:
            if self.NDEPCVL1given == False:
                self.NDEPCVL1 = 0.0
        if 'NDEPCVLEXP1' in param:
            self.NDEPCVLEXP1 = param['NDEPCVLEXP1']
            self.NDEPCVLEXP1given = True
        elif 'NDEPCVLEXP1'.swapcase() in param:
            self.NDEPCVLEXP1 = param['NDEPCVLEXP1'.swapcase()]
            self.NDEPCVLEXP1given = True
        else:
            if self.NDEPCVLEXP1given == False:
                self.NDEPCVLEXP1 = 1.0
        if 'NDEPCVL2' in param:
            self.NDEPCVL2 = param['NDEPCVL2']
            self.NDEPCVL2given = True
        elif 'NDEPCVL2'.swapcase() in param:
            self.NDEPCVL2 = param['NDEPCVL2'.swapcase()]
            self.NDEPCVL2given = True
        else:
            if self.NDEPCVL2given == False:
                self.NDEPCVL2 = 0.0
        if 'NDEPCVLEXP2' in param:
            self.NDEPCVLEXP2 = param['NDEPCVLEXP2']
            self.NDEPCVLEXP2given = True
        elif 'NDEPCVLEXP2'.swapcase() in param:
            self.NDEPCVLEXP2 = param['NDEPCVLEXP2'.swapcase()]
            self.NDEPCVLEXP2given = True
        else:
            if self.NDEPCVLEXP2given == False:
                self.NDEPCVLEXP2 = 2.0
        if 'NDEPCVW' in param:
            self.NDEPCVW = param['NDEPCVW']
            self.NDEPCVWgiven = True
        elif 'NDEPCVW'.swapcase() in param:
            self.NDEPCVW = param['NDEPCVW'.swapcase()]
            self.NDEPCVWgiven = True
        else:
            if self.NDEPCVWgiven == False:
                self.NDEPCVW = 0.0
        if 'NDEPCVWEXP' in param:
            self.NDEPCVWEXP = param['NDEPCVWEXP']
            self.NDEPCVWEXPgiven = True
        elif 'NDEPCVWEXP'.swapcase() in param:
            self.NDEPCVWEXP = param['NDEPCVWEXP'.swapcase()]
            self.NDEPCVWEXPgiven = True
        else:
            if self.NDEPCVWEXPgiven == False:
                self.NDEPCVWEXP = 1.0
        if 'NDEPCVWL' in param:
            self.NDEPCVWL = param['NDEPCVWL']
            self.NDEPCVWLgiven = True
        elif 'NDEPCVWL'.swapcase() in param:
            self.NDEPCVWL = param['NDEPCVWL'.swapcase()]
            self.NDEPCVWLgiven = True
        else:
            if self.NDEPCVWLgiven == False:
                self.NDEPCVWL = 0.0
        if 'NDEPCVWLEXP' in param:
            self.NDEPCVWLEXP = param['NDEPCVWLEXP']
            self.NDEPCVWLEXPgiven = True
        elif 'NDEPCVWLEXP'.swapcase() in param:
            self.NDEPCVWLEXP = param['NDEPCVWLEXP'.swapcase()]
            self.NDEPCVWLEXPgiven = True
        else:
            if self.NDEPCVWLEXPgiven == False:
                self.NDEPCVWLEXP = 1.0
        if 'LNDEPCV' in param:
            self.LNDEPCV = param['LNDEPCV']
            self.LNDEPCVgiven = True
        elif 'LNDEPCV'.swapcase() in param:
            self.LNDEPCV = param['LNDEPCV'.swapcase()]
            self.LNDEPCVgiven = True
        else:
            if self.LNDEPCVgiven == False:
                self.LNDEPCV = 0.0
        if 'WNDEPCV' in param:
            self.WNDEPCV = param['WNDEPCV']
            self.WNDEPCVgiven = True
        elif 'WNDEPCV'.swapcase() in param:
            self.WNDEPCV = param['WNDEPCV'.swapcase()]
            self.WNDEPCVgiven = True
        else:
            if self.WNDEPCVgiven == False:
                self.WNDEPCV = 0.0
        if 'PNDEPCV' in param:
            self.PNDEPCV = param['PNDEPCV']
            self.PNDEPCVgiven = True
        elif 'PNDEPCV'.swapcase() in param:
            self.PNDEPCV = param['PNDEPCV'.swapcase()]
            self.PNDEPCVgiven = True
        else:
            if self.PNDEPCVgiven == False:
                self.PNDEPCV = 0.0
        if 'NGATE' in param:
            self.NGATE = param['NGATE']
            self.NGATEgiven = True
        elif 'NGATE'.swapcase() in param:
            self.NGATE = param['NGATE'.swapcase()]
            self.NGATEgiven = True
        else:
            if self.NGATEgiven == False:
                self.NGATE = 5e+25
        if 'LNGATE' in param:
            self.LNGATE = param['LNGATE']
            self.LNGATEgiven = True
        elif 'LNGATE'.swapcase() in param:
            self.LNGATE = param['LNGATE'.swapcase()]
            self.LNGATEgiven = True
        else:
            if self.LNGATEgiven == False:
                self.LNGATE = 0.0
        if 'WNGATE' in param:
            self.WNGATE = param['WNGATE']
            self.WNGATEgiven = True
        elif 'WNGATE'.swapcase() in param:
            self.WNGATE = param['WNGATE'.swapcase()]
            self.WNGATEgiven = True
        else:
            if self.WNGATEgiven == False:
                self.WNGATE = 0.0
        if 'PNGATE' in param:
            self.PNGATE = param['PNGATE']
            self.PNGATEgiven = True
        elif 'PNGATE'.swapcase() in param:
            self.PNGATE = param['PNGATE'.swapcase()]
            self.PNGATEgiven = True
        else:
            if self.PNGATEgiven == False:
                self.PNGATE = 0.0
        if 'EASUB' in param:
            self.EASUB = param['EASUB']
            self.EASUBgiven = True
        elif 'EASUB'.swapcase() in param:
            self.EASUB = param['EASUB'.swapcase()]
            self.EASUBgiven = True
        else:
            if self.EASUBgiven == False:
                self.EASUB = 4.05
        if 'NI0SUB' in param:
            self.NI0SUB = param['NI0SUB']
            self.NI0SUBgiven = True
        elif 'NI0SUB'.swapcase() in param:
            self.NI0SUB = param['NI0SUB'.swapcase()]
            self.NI0SUBgiven = True
        else:
            if self.NI0SUBgiven == False:
                self.NI0SUB = 1.1e+16
        if 'BG0SUB' in param:
            self.BG0SUB = param['BG0SUB']
            self.BG0SUBgiven = True
        elif 'BG0SUB'.swapcase() in param:
            self.BG0SUB = param['BG0SUB'.swapcase()]
            self.BG0SUBgiven = True
        else:
            if self.BG0SUBgiven == False:
                self.BG0SUB = 1.17
        if 'EPSRSUB' in param:
            self.EPSRSUB = param['EPSRSUB']
            self.EPSRSUBgiven = True
        elif 'EPSRSUB'.swapcase() in param:
            self.EPSRSUB = param['EPSRSUB'.swapcase()]
            self.EPSRSUBgiven = True
        else:
            if self.EPSRSUBgiven == False:
                self.EPSRSUB = 11.9
        if 'EPSROX' in param:
            self.EPSROX = param['EPSROX']
            self.EPSROXgiven = True
        elif 'EPSROX'.swapcase() in param:
            self.EPSROX = param['EPSROX'.swapcase()]
            self.EPSROXgiven = True
        else:
            if self.EPSROXgiven == False:
                self.EPSROX = 3.9
        if 'XJ' in param:
            self.XJ = param['XJ']
            self.XJgiven = True
        elif 'XJ'.swapcase() in param:
            self.XJ = param['XJ'.swapcase()]
            self.XJgiven = True
        else:
            if self.XJgiven == False:
                self.XJ = 1.5e-07
        if 'LXJ' in param:
            self.LXJ = param['LXJ']
            self.LXJgiven = True
        elif 'LXJ'.swapcase() in param:
            self.LXJ = param['LXJ'.swapcase()]
            self.LXJgiven = True
        else:
            if self.LXJgiven == False:
                self.LXJ = 0.0
        if 'WXJ' in param:
            self.WXJ = param['WXJ']
            self.WXJgiven = True
        elif 'WXJ'.swapcase() in param:
            self.WXJ = param['WXJ'.swapcase()]
            self.WXJgiven = True
        else:
            if self.WXJgiven == False:
                self.WXJ = 0.0
        if 'PXJ' in param:
            self.PXJ = param['PXJ']
            self.PXJgiven = True
        elif 'PXJ'.swapcase() in param:
            self.PXJ = param['PXJ'.swapcase()]
            self.PXJgiven = True
        else:
            if self.PXJgiven == False:
                self.PXJ = 0.0
        if 'VFB' in param:
            self.VFB = param['VFB']
            self.VFBgiven = True
        elif 'VFB'.swapcase() in param:
            self.VFB = param['VFB'.swapcase()]
            self.VFBgiven = True
        else:
            if self.VFBgiven == False:
                self.VFB = -0.5
        if 'LVFB' in param:
            self.LVFB = param['LVFB']
            self.LVFBgiven = True
        elif 'LVFB'.swapcase() in param:
            self.LVFB = param['LVFB'.swapcase()]
            self.LVFBgiven = True
        else:
            if self.LVFBgiven == False:
                self.LVFB = 0.0
        if 'WVFB' in param:
            self.WVFB = param['WVFB']
            self.WVFBgiven = True
        elif 'WVFB'.swapcase() in param:
            self.WVFB = param['WVFB'.swapcase()]
            self.WVFBgiven = True
        else:
            if self.WVFBgiven == False:
                self.WVFB = 0.0
        if 'PVFB' in param:
            self.PVFB = param['PVFB']
            self.PVFBgiven = True
        elif 'PVFB'.swapcase() in param:
            self.PVFB = param['PVFB'.swapcase()]
            self.PVFBgiven = True
        else:
            if self.PVFBgiven == False:
                self.PVFB = 0.0
        if 'VFBCV' in param:
            self.VFBCV = param['VFBCV']
            self.VFBCVgiven = True
        elif 'VFBCV'.swapcase() in param:
            self.VFBCV = param['VFBCV'.swapcase()]
            self.VFBCVgiven = True
        else:
            if self.VFBCVgiven == False:
                self.VFBCV = -0.5
        if 'LVFBCV' in param:
            self.LVFBCV = param['LVFBCV']
            self.LVFBCVgiven = True
        elif 'LVFBCV'.swapcase() in param:
            self.LVFBCV = param['LVFBCV'.swapcase()]
            self.LVFBCVgiven = True
        else:
            if self.LVFBCVgiven == False:
                self.LVFBCV = 0.0
        if 'WVFBCV' in param:
            self.WVFBCV = param['WVFBCV']
            self.WVFBCVgiven = True
        elif 'WVFBCV'.swapcase() in param:
            self.WVFBCV = param['WVFBCV'.swapcase()]
            self.WVFBCVgiven = True
        else:
            if self.WVFBCVgiven == False:
                self.WVFBCV = 0.0
        if 'PVFBCV' in param:
            self.PVFBCV = param['PVFBCV']
            self.PVFBCVgiven = True
        elif 'PVFBCV'.swapcase() in param:
            self.PVFBCV = param['PVFBCV'.swapcase()]
            self.PVFBCVgiven = True
        else:
            if self.PVFBCVgiven == False:
                self.PVFBCV = 0.0
        if 'VFBCVL' in param:
            self.VFBCVL = param['VFBCVL']
            self.VFBCVLgiven = True
        elif 'VFBCVL'.swapcase() in param:
            self.VFBCVL = param['VFBCVL'.swapcase()]
            self.VFBCVLgiven = True
        else:
            if self.VFBCVLgiven == False:
                self.VFBCVL = 0.0
        if 'VFBCVLEXP' in param:
            self.VFBCVLEXP = param['VFBCVLEXP']
            self.VFBCVLEXPgiven = True
        elif 'VFBCVLEXP'.swapcase() in param:
            self.VFBCVLEXP = param['VFBCVLEXP'.swapcase()]
            self.VFBCVLEXPgiven = True
        else:
            if self.VFBCVLEXPgiven == False:
                self.VFBCVLEXP = 1.0
        if 'VFBCVW' in param:
            self.VFBCVW = param['VFBCVW']
            self.VFBCVWgiven = True
        elif 'VFBCVW'.swapcase() in param:
            self.VFBCVW = param['VFBCVW'.swapcase()]
            self.VFBCVWgiven = True
        else:
            if self.VFBCVWgiven == False:
                self.VFBCVW = 0.0
        if 'VFBCVWEXP' in param:
            self.VFBCVWEXP = param['VFBCVWEXP']
            self.VFBCVWEXPgiven = True
        elif 'VFBCVWEXP'.swapcase() in param:
            self.VFBCVWEXP = param['VFBCVWEXP'.swapcase()]
            self.VFBCVWEXPgiven = True
        else:
            if self.VFBCVWEXPgiven == False:
                self.VFBCVWEXP = 1.0
        if 'VFBCVWL' in param:
            self.VFBCVWL = param['VFBCVWL']
            self.VFBCVWLgiven = True
        elif 'VFBCVWL'.swapcase() in param:
            self.VFBCVWL = param['VFBCVWL'.swapcase()]
            self.VFBCVWLgiven = True
        else:
            if self.VFBCVWLgiven == False:
                self.VFBCVWL = 0.0
        if 'VFBCVWLEXP' in param:
            self.VFBCVWLEXP = param['VFBCVWLEXP']
            self.VFBCVWLEXPgiven = True
        elif 'VFBCVWLEXP'.swapcase() in param:
            self.VFBCVWLEXP = param['VFBCVWLEXP'.swapcase()]
            self.VFBCVWLEXPgiven = True
        else:
            if self.VFBCVWLEXPgiven == False:
                self.VFBCVWLEXP = 1.0
        if 'DELVFBACC' in param:
            self.DELVFBACC = param['DELVFBACC']
            self.DELVFBACCgiven = True
        elif 'DELVFBACC'.swapcase() in param:
            self.DELVFBACC = param['DELVFBACC'.swapcase()]
            self.DELVFBACCgiven = True
        else:
            if self.DELVFBACCgiven == False:
                self.DELVFBACC = 0.0
        if 'PERMOD' in param:
            self.PERMOD = param['PERMOD']
            self.PERMODgiven = True
        elif 'PERMOD'.swapcase() in param:
            self.PERMOD = param['PERMOD'.swapcase()]
            self.PERMODgiven = True
        else:
            if self.PERMODgiven == False:
                self.PERMOD = 1.0
        if 'DWJ' in param:
            self.DWJ = param['DWJ']
            self.DWJgiven = True
        elif 'DWJ'.swapcase() in param:
            self.DWJ = param['DWJ'.swapcase()]
            self.DWJgiven = True
        else:
            if self.DWJgiven == False:
                self.DWJ = self.DWC
        if 'NSD' in param:
            self.NSD = param['NSD']
            self.NSDgiven = True
        elif 'NSD'.swapcase() in param:
            self.NSD = param['NSD'.swapcase()]
            self.NSDgiven = True
        else:
            if self.NSDgiven == False:
                self.NSD = 1e+26
        if 'LNSD' in param:
            self.LNSD = param['LNSD']
            self.LNSDgiven = True
        elif 'LNSD'.swapcase() in param:
            self.LNSD = param['LNSD'.swapcase()]
            self.LNSDgiven = True
        else:
            if self.LNSDgiven == False:
                self.LNSD = 0.0
        if 'WNSD' in param:
            self.WNSD = param['WNSD']
            self.WNSDgiven = True
        elif 'WNSD'.swapcase() in param:
            self.WNSD = param['WNSD'.swapcase()]
            self.WNSDgiven = True
        else:
            if self.WNSDgiven == False:
                self.WNSD = 0.0
        if 'PNSD' in param:
            self.PNSD = param['PNSD']
            self.PNSDgiven = True
        elif 'PNSD'.swapcase() in param:
            self.PNSD = param['PNSD'.swapcase()]
            self.PNSDgiven = True
        else:
            if self.PNSDgiven == False:
                self.PNSD = 0.0
        if 'DVTP0' in param:
            self.DVTP0 = param['DVTP0']
            self.DVTP0given = True
        elif 'DVTP0'.swapcase() in param:
            self.DVTP0 = param['DVTP0'.swapcase()]
            self.DVTP0given = True
        else:
            if self.DVTP0given == False:
                self.DVTP0 = 0.0
        if 'LDVTP0' in param:
            self.LDVTP0 = param['LDVTP0']
            self.LDVTP0given = True
        elif 'LDVTP0'.swapcase() in param:
            self.LDVTP0 = param['LDVTP0'.swapcase()]
            self.LDVTP0given = True
        else:
            if self.LDVTP0given == False:
                self.LDVTP0 = 0.0
        if 'WDVTP0' in param:
            self.WDVTP0 = param['WDVTP0']
            self.WDVTP0given = True
        elif 'WDVTP0'.swapcase() in param:
            self.WDVTP0 = param['WDVTP0'.swapcase()]
            self.WDVTP0given = True
        else:
            if self.WDVTP0given == False:
                self.WDVTP0 = 0.0
        if 'PDVTP0' in param:
            self.PDVTP0 = param['PDVTP0']
            self.PDVTP0given = True
        elif 'PDVTP0'.swapcase() in param:
            self.PDVTP0 = param['PDVTP0'.swapcase()]
            self.PDVTP0given = True
        else:
            if self.PDVTP0given == False:
                self.PDVTP0 = 0.0
        if 'DVTP1' in param:
            self.DVTP1 = param['DVTP1']
            self.DVTP1given = True
        elif 'DVTP1'.swapcase() in param:
            self.DVTP1 = param['DVTP1'.swapcase()]
            self.DVTP1given = True
        else:
            if self.DVTP1given == False:
                self.DVTP1 = 0.0
        if 'LDVTP1' in param:
            self.LDVTP1 = param['LDVTP1']
            self.LDVTP1given = True
        elif 'LDVTP1'.swapcase() in param:
            self.LDVTP1 = param['LDVTP1'.swapcase()]
            self.LDVTP1given = True
        else:
            if self.LDVTP1given == False:
                self.LDVTP1 = 0.0
        if 'WDVTP1' in param:
            self.WDVTP1 = param['WDVTP1']
            self.WDVTP1given = True
        elif 'WDVTP1'.swapcase() in param:
            self.WDVTP1 = param['WDVTP1'.swapcase()]
            self.WDVTP1given = True
        else:
            if self.WDVTP1given == False:
                self.WDVTP1 = 0.0
        if 'PDVTP1' in param:
            self.PDVTP1 = param['PDVTP1']
            self.PDVTP1given = True
        elif 'PDVTP1'.swapcase() in param:
            self.PDVTP1 = param['PDVTP1'.swapcase()]
            self.PDVTP1given = True
        else:
            if self.PDVTP1given == False:
                self.PDVTP1 = 0.0
        if 'DVTP2' in param:
            self.DVTP2 = param['DVTP2']
            self.DVTP2given = True
        elif 'DVTP2'.swapcase() in param:
            self.DVTP2 = param['DVTP2'.swapcase()]
            self.DVTP2given = True
        else:
            if self.DVTP2given == False:
                self.DVTP2 = 0.0
        if 'LDVTP2' in param:
            self.LDVTP2 = param['LDVTP2']
            self.LDVTP2given = True
        elif 'LDVTP2'.swapcase() in param:
            self.LDVTP2 = param['LDVTP2'.swapcase()]
            self.LDVTP2given = True
        else:
            if self.LDVTP2given == False:
                self.LDVTP2 = 0.0
        if 'WDVTP2' in param:
            self.WDVTP2 = param['WDVTP2']
            self.WDVTP2given = True
        elif 'WDVTP2'.swapcase() in param:
            self.WDVTP2 = param['WDVTP2'.swapcase()]
            self.WDVTP2given = True
        else:
            if self.WDVTP2given == False:
                self.WDVTP2 = 0.0
        if 'PDVTP2' in param:
            self.PDVTP2 = param['PDVTP2']
            self.PDVTP2given = True
        elif 'PDVTP2'.swapcase() in param:
            self.PDVTP2 = param['PDVTP2'.swapcase()]
            self.PDVTP2given = True
        else:
            if self.PDVTP2given == False:
                self.PDVTP2 = 0.0
        if 'DVTP3' in param:
            self.DVTP3 = param['DVTP3']
            self.DVTP3given = True
        elif 'DVTP3'.swapcase() in param:
            self.DVTP3 = param['DVTP3'.swapcase()]
            self.DVTP3given = True
        else:
            if self.DVTP3given == False:
                self.DVTP3 = 0.0
        if 'LDVTP3' in param:
            self.LDVTP3 = param['LDVTP3']
            self.LDVTP3given = True
        elif 'LDVTP3'.swapcase() in param:
            self.LDVTP3 = param['LDVTP3'.swapcase()]
            self.LDVTP3given = True
        else:
            if self.LDVTP3given == False:
                self.LDVTP3 = 0.0
        if 'WDVTP3' in param:
            self.WDVTP3 = param['WDVTP3']
            self.WDVTP3given = True
        elif 'WDVTP3'.swapcase() in param:
            self.WDVTP3 = param['WDVTP3'.swapcase()]
            self.WDVTP3given = True
        else:
            if self.WDVTP3given == False:
                self.WDVTP3 = 0.0
        if 'PDVTP3' in param:
            self.PDVTP3 = param['PDVTP3']
            self.PDVTP3given = True
        elif 'PDVTP3'.swapcase() in param:
            self.PDVTP3 = param['PDVTP3'.swapcase()]
            self.PDVTP3given = True
        else:
            if self.PDVTP3given == False:
                self.PDVTP3 = 0.0
        if 'DVTP4' in param:
            self.DVTP4 = param['DVTP4']
            self.DVTP4given = True
        elif 'DVTP4'.swapcase() in param:
            self.DVTP4 = param['DVTP4'.swapcase()]
            self.DVTP4given = True
        else:
            if self.DVTP4given == False:
                self.DVTP4 = 0.0
        if 'LDVTP4' in param:
            self.LDVTP4 = param['LDVTP4']
            self.LDVTP4given = True
        elif 'LDVTP4'.swapcase() in param:
            self.LDVTP4 = param['LDVTP4'.swapcase()]
            self.LDVTP4given = True
        else:
            if self.LDVTP4given == False:
                self.LDVTP4 = 0.0
        if 'WDVTP4' in param:
            self.WDVTP4 = param['WDVTP4']
            self.WDVTP4given = True
        elif 'WDVTP4'.swapcase() in param:
            self.WDVTP4 = param['WDVTP4'.swapcase()]
            self.WDVTP4given = True
        else:
            if self.WDVTP4given == False:
                self.WDVTP4 = 0.0
        if 'PDVTP4' in param:
            self.PDVTP4 = param['PDVTP4']
            self.PDVTP4given = True
        elif 'PDVTP4'.swapcase() in param:
            self.PDVTP4 = param['PDVTP4'.swapcase()]
            self.PDVTP4given = True
        else:
            if self.PDVTP4given == False:
                self.PDVTP4 = 0.0
        if 'DVTP5' in param:
            self.DVTP5 = param['DVTP5']
            self.DVTP5given = True
        elif 'DVTP5'.swapcase() in param:
            self.DVTP5 = param['DVTP5'.swapcase()]
            self.DVTP5given = True
        else:
            if self.DVTP5given == False:
                self.DVTP5 = 0.0
        if 'LDVTP5' in param:
            self.LDVTP5 = param['LDVTP5']
            self.LDVTP5given = True
        elif 'LDVTP5'.swapcase() in param:
            self.LDVTP5 = param['LDVTP5'.swapcase()]
            self.LDVTP5given = True
        else:
            if self.LDVTP5given == False:
                self.LDVTP5 = 0.0
        if 'WDVTP5' in param:
            self.WDVTP5 = param['WDVTP5']
            self.WDVTP5given = True
        elif 'WDVTP5'.swapcase() in param:
            self.WDVTP5 = param['WDVTP5'.swapcase()]
            self.WDVTP5given = True
        else:
            if self.WDVTP5given == False:
                self.WDVTP5 = 0.0
        if 'PDVTP5' in param:
            self.PDVTP5 = param['PDVTP5']
            self.PDVTP5given = True
        elif 'PDVTP5'.swapcase() in param:
            self.PDVTP5 = param['PDVTP5'.swapcase()]
            self.PDVTP5given = True
        else:
            if self.PDVTP5given == False:
                self.PDVTP5 = 0.0
        if 'PHIN' in param:
            self.PHIN = param['PHIN']
            self.PHINgiven = True
        elif 'PHIN'.swapcase() in param:
            self.PHIN = param['PHIN'.swapcase()]
            self.PHINgiven = True
        else:
            if self.PHINgiven == False:
                self.PHIN = 0.045
        if 'LPHIN' in param:
            self.LPHIN = param['LPHIN']
            self.LPHINgiven = True
        elif 'LPHIN'.swapcase() in param:
            self.LPHIN = param['LPHIN'.swapcase()]
            self.LPHINgiven = True
        else:
            if self.LPHINgiven == False:
                self.LPHIN = 0.0
        if 'WPHIN' in param:
            self.WPHIN = param['WPHIN']
            self.WPHINgiven = True
        elif 'WPHIN'.swapcase() in param:
            self.WPHIN = param['WPHIN'.swapcase()]
            self.WPHINgiven = True
        else:
            if self.WPHINgiven == False:
                self.WPHIN = 0.0
        if 'PPHIN' in param:
            self.PPHIN = param['PPHIN']
            self.PPHINgiven = True
        elif 'PPHIN'.swapcase() in param:
            self.PPHIN = param['PPHIN'.swapcase()]
            self.PPHINgiven = True
        else:
            if self.PPHINgiven == False:
                self.PPHIN = 0.0
        if 'ETA0' in param:
            self.ETA0 = param['ETA0']
            self.ETA0given = True
        elif 'ETA0'.swapcase() in param:
            self.ETA0 = param['ETA0'.swapcase()]
            self.ETA0given = True
        else:
            if self.ETA0given == False:
                self.ETA0 = 0.08
        if 'LETA0' in param:
            self.LETA0 = param['LETA0']
            self.LETA0given = True
        elif 'LETA0'.swapcase() in param:
            self.LETA0 = param['LETA0'.swapcase()]
            self.LETA0given = True
        else:
            if self.LETA0given == False:
                self.LETA0 = 0.0
        if 'WETA0' in param:
            self.WETA0 = param['WETA0']
            self.WETA0given = True
        elif 'WETA0'.swapcase() in param:
            self.WETA0 = param['WETA0'.swapcase()]
            self.WETA0given = True
        else:
            if self.WETA0given == False:
                self.WETA0 = 0.0
        if 'PETA0' in param:
            self.PETA0 = param['PETA0']
            self.PETA0given = True
        elif 'PETA0'.swapcase() in param:
            self.PETA0 = param['PETA0'.swapcase()]
            self.PETA0given = True
        else:
            if self.PETA0given == False:
                self.PETA0 = 0.0
        if 'ETA0R' in param:
            self.ETA0R = param['ETA0R']
            self.ETA0Rgiven = True
        elif 'ETA0R'.swapcase() in param:
            self.ETA0R = param['ETA0R'.swapcase()]
            self.ETA0Rgiven = True
        else:
            if self.ETA0Rgiven == False:
                self.ETA0R = self.ETA0
        if 'LETA0R' in param:
            self.LETA0R = param['LETA0R']
            self.LETA0Rgiven = True
        elif 'LETA0R'.swapcase() in param:
            self.LETA0R = param['LETA0R'.swapcase()]
            self.LETA0Rgiven = True
        else:
            if self.LETA0Rgiven == False:
                self.LETA0R = self.LETA0
        if 'WETA0R' in param:
            self.WETA0R = param['WETA0R']
            self.WETA0Rgiven = True
        elif 'WETA0R'.swapcase() in param:
            self.WETA0R = param['WETA0R'.swapcase()]
            self.WETA0Rgiven = True
        else:
            if self.WETA0Rgiven == False:
                self.WETA0R = self.WETA0
        if 'PETA0R' in param:
            self.PETA0R = param['PETA0R']
            self.PETA0Rgiven = True
        elif 'PETA0R'.swapcase() in param:
            self.PETA0R = param['PETA0R'.swapcase()]
            self.PETA0Rgiven = True
        else:
            if self.PETA0Rgiven == False:
                self.PETA0R = self.PETA0
        if 'DSUB' in param:
            self.DSUB = param['DSUB']
            self.DSUBgiven = True
        elif 'DSUB'.swapcase() in param:
            self.DSUB = param['DSUB'.swapcase()]
            self.DSUBgiven = True
        else:
            if self.DSUBgiven == False:
                self.DSUB = 1.0
        if 'ETAB' in param:
            self.ETAB = param['ETAB']
            self.ETABgiven = True
        elif 'ETAB'.swapcase() in param:
            self.ETAB = param['ETAB'.swapcase()]
            self.ETABgiven = True
        else:
            if self.ETABgiven == False:
                self.ETAB = -0.07
        if 'ETABEXP' in param:
            self.ETABEXP = param['ETABEXP']
            self.ETABEXPgiven = True
        elif 'ETABEXP'.swapcase() in param:
            self.ETABEXP = param['ETABEXP'.swapcase()]
            self.ETABEXPgiven = True
        else:
            if self.ETABEXPgiven == False:
                self.ETABEXP = 1.0
        if 'LETAB' in param:
            self.LETAB = param['LETAB']
            self.LETABgiven = True
        elif 'LETAB'.swapcase() in param:
            self.LETAB = param['LETAB'.swapcase()]
            self.LETABgiven = True
        else:
            if self.LETABgiven == False:
                self.LETAB = 0.0
        if 'WETAB' in param:
            self.WETAB = param['WETAB']
            self.WETABgiven = True
        elif 'WETAB'.swapcase() in param:
            self.WETAB = param['WETAB'.swapcase()]
            self.WETABgiven = True
        else:
            if self.WETABgiven == False:
                self.WETAB = 0.0
        if 'PETAB' in param:
            self.PETAB = param['PETAB']
            self.PETABgiven = True
        elif 'PETAB'.swapcase() in param:
            self.PETAB = param['PETAB'.swapcase()]
            self.PETABgiven = True
        else:
            if self.PETABgiven == False:
                self.PETAB = 0.0
        if 'K1' in param:
            self.K1 = param['K1']
            self.K1given = True
        elif 'K1'.swapcase() in param:
            self.K1 = param['K1'.swapcase()]
            self.K1given = True
        else:
            if self.K1given == False:
                self.K1 = 0.0
        if 'K1L' in param:
            self.K1L = param['K1L']
            self.K1Lgiven = True
        elif 'K1L'.swapcase() in param:
            self.K1L = param['K1L'.swapcase()]
            self.K1Lgiven = True
        else:
            if self.K1Lgiven == False:
                self.K1L = 0.0
        if 'K1LEXP' in param:
            self.K1LEXP = param['K1LEXP']
            self.K1LEXPgiven = True
        elif 'K1LEXP'.swapcase() in param:
            self.K1LEXP = param['K1LEXP'.swapcase()]
            self.K1LEXPgiven = True
        else:
            if self.K1LEXPgiven == False:
                self.K1LEXP = 1.0
        if 'K1W' in param:
            self.K1W = param['K1W']
            self.K1Wgiven = True
        elif 'K1W'.swapcase() in param:
            self.K1W = param['K1W'.swapcase()]
            self.K1Wgiven = True
        else:
            if self.K1Wgiven == False:
                self.K1W = 0.0
        if 'K1WEXP' in param:
            self.K1WEXP = param['K1WEXP']
            self.K1WEXPgiven = True
        elif 'K1WEXP'.swapcase() in param:
            self.K1WEXP = param['K1WEXP'.swapcase()]
            self.K1WEXPgiven = True
        else:
            if self.K1WEXPgiven == False:
                self.K1WEXP = 1.0
        if 'K1WL' in param:
            self.K1WL = param['K1WL']
            self.K1WLgiven = True
        elif 'K1WL'.swapcase() in param:
            self.K1WL = param['K1WL'.swapcase()]
            self.K1WLgiven = True
        else:
            if self.K1WLgiven == False:
                self.K1WL = 0.0
        if 'K1WLEXP' in param:
            self.K1WLEXP = param['K1WLEXP']
            self.K1WLEXPgiven = True
        elif 'K1WLEXP'.swapcase() in param:
            self.K1WLEXP = param['K1WLEXP'.swapcase()]
            self.K1WLEXPgiven = True
        else:
            if self.K1WLEXPgiven == False:
                self.K1WLEXP = 1.0
        if 'LK1' in param:
            self.LK1 = param['LK1']
            self.LK1given = True
        elif 'LK1'.swapcase() in param:
            self.LK1 = param['LK1'.swapcase()]
            self.LK1given = True
        else:
            if self.LK1given == False:
                self.LK1 = 0.0
        if 'WK1' in param:
            self.WK1 = param['WK1']
            self.WK1given = True
        elif 'WK1'.swapcase() in param:
            self.WK1 = param['WK1'.swapcase()]
            self.WK1given = True
        else:
            if self.WK1given == False:
                self.WK1 = 0.0
        if 'PK1' in param:
            self.PK1 = param['PK1']
            self.PK1given = True
        elif 'PK1'.swapcase() in param:
            self.PK1 = param['PK1'.swapcase()]
            self.PK1given = True
        else:
            if self.PK1given == False:
                self.PK1 = 0.0
        if 'K2' in param:
            self.K2 = param['K2']
            self.K2given = True
        elif 'K2'.swapcase() in param:
            self.K2 = param['K2'.swapcase()]
            self.K2given = True
        else:
            if self.K2given == False:
                self.K2 = 0.0
        if 'K2L' in param:
            self.K2L = param['K2L']
            self.K2Lgiven = True
        elif 'K2L'.swapcase() in param:
            self.K2L = param['K2L'.swapcase()]
            self.K2Lgiven = True
        else:
            if self.K2Lgiven == False:
                self.K2L = 0.0
        if 'K2LEXP' in param:
            self.K2LEXP = param['K2LEXP']
            self.K2LEXPgiven = True
        elif 'K2LEXP'.swapcase() in param:
            self.K2LEXP = param['K2LEXP'.swapcase()]
            self.K2LEXPgiven = True
        else:
            if self.K2LEXPgiven == False:
                self.K2LEXP = 1.0
        if 'K2W' in param:
            self.K2W = param['K2W']
            self.K2Wgiven = True
        elif 'K2W'.swapcase() in param:
            self.K2W = param['K2W'.swapcase()]
            self.K2Wgiven = True
        else:
            if self.K2Wgiven == False:
                self.K2W = 0.0
        if 'K2WEXP' in param:
            self.K2WEXP = param['K2WEXP']
            self.K2WEXPgiven = True
        elif 'K2WEXP'.swapcase() in param:
            self.K2WEXP = param['K2WEXP'.swapcase()]
            self.K2WEXPgiven = True
        else:
            if self.K2WEXPgiven == False:
                self.K2WEXP = 1.0
        if 'K2WL' in param:
            self.K2WL = param['K2WL']
            self.K2WLgiven = True
        elif 'K2WL'.swapcase() in param:
            self.K2WL = param['K2WL'.swapcase()]
            self.K2WLgiven = True
        else:
            if self.K2WLgiven == False:
                self.K2WL = 0.0
        if 'K2WLEXP' in param:
            self.K2WLEXP = param['K2WLEXP']
            self.K2WLEXPgiven = True
        elif 'K2WLEXP'.swapcase() in param:
            self.K2WLEXP = param['K2WLEXP'.swapcase()]
            self.K2WLEXPgiven = True
        else:
            if self.K2WLEXPgiven == False:
                self.K2WLEXP = 1.0
        if 'LK2' in param:
            self.LK2 = param['LK2']
            self.LK2given = True
        elif 'LK2'.swapcase() in param:
            self.LK2 = param['LK2'.swapcase()]
            self.LK2given = True
        else:
            if self.LK2given == False:
                self.LK2 = 0.0
        if 'WK2' in param:
            self.WK2 = param['WK2']
            self.WK2given = True
        elif 'WK2'.swapcase() in param:
            self.WK2 = param['WK2'.swapcase()]
            self.WK2given = True
        else:
            if self.WK2given == False:
                self.WK2 = 0.0
        if 'PK2' in param:
            self.PK2 = param['PK2']
            self.PK2given = True
        elif 'PK2'.swapcase() in param:
            self.PK2 = param['PK2'.swapcase()]
            self.PK2given = True
        else:
            if self.PK2given == False:
                self.PK2 = 0.0
        if 'ADOS' in param:
            self.ADOS = param['ADOS']
            self.ADOSgiven = True
        elif 'ADOS'.swapcase() in param:
            self.ADOS = param['ADOS'.swapcase()]
            self.ADOSgiven = True
        else:
            if self.ADOSgiven == False:
                self.ADOS = 0.0
        if 'BDOS' in param:
            self.BDOS = param['BDOS']
            self.BDOSgiven = True
        elif 'BDOS'.swapcase() in param:
            self.BDOS = param['BDOS'.swapcase()]
            self.BDOSgiven = True
        else:
            if self.BDOSgiven == False:
                self.BDOS = 1.0
        if 'QM0' in param:
            self.QM0 = param['QM0']
            self.QM0given = True
        elif 'QM0'.swapcase() in param:
            self.QM0 = param['QM0'.swapcase()]
            self.QM0given = True
        else:
            if self.QM0given == False:
                self.QM0 = 0.001
        if 'ETAQM' in param:
            self.ETAQM = param['ETAQM']
            self.ETAQMgiven = True
        elif 'ETAQM'.swapcase() in param:
            self.ETAQM = param['ETAQM'.swapcase()]
            self.ETAQMgiven = True
        else:
            if self.ETAQMgiven == False:
                self.ETAQM = 0.54
        if 'CIT' in param:
            self.CIT = param['CIT']
            self.CITgiven = True
        elif 'CIT'.swapcase() in param:
            self.CIT = param['CIT'.swapcase()]
            self.CITgiven = True
        else:
            if self.CITgiven == False:
                self.CIT = 0.0
        if 'LCIT' in param:
            self.LCIT = param['LCIT']
            self.LCITgiven = True
        elif 'LCIT'.swapcase() in param:
            self.LCIT = param['LCIT'.swapcase()]
            self.LCITgiven = True
        else:
            if self.LCITgiven == False:
                self.LCIT = 0.0
        if 'WCIT' in param:
            self.WCIT = param['WCIT']
            self.WCITgiven = True
        elif 'WCIT'.swapcase() in param:
            self.WCIT = param['WCIT'.swapcase()]
            self.WCITgiven = True
        else:
            if self.WCITgiven == False:
                self.WCIT = 0.0
        if 'PCIT' in param:
            self.PCIT = param['PCIT']
            self.PCITgiven = True
        elif 'PCIT'.swapcase() in param:
            self.PCIT = param['PCIT'.swapcase()]
            self.PCITgiven = True
        else:
            if self.PCITgiven == False:
                self.PCIT = 0.0
        if 'NFACTOR' in param:
            self.NFACTOR = param['NFACTOR']
            self.NFACTORgiven = True
        elif 'NFACTOR'.swapcase() in param:
            self.NFACTOR = param['NFACTOR'.swapcase()]
            self.NFACTORgiven = True
        else:
            if self.NFACTORgiven == False:
                self.NFACTOR = 0.0
        if 'NFACTORL' in param:
            self.NFACTORL = param['NFACTORL']
            self.NFACTORLgiven = True
        elif 'NFACTORL'.swapcase() in param:
            self.NFACTORL = param['NFACTORL'.swapcase()]
            self.NFACTORLgiven = True
        else:
            if self.NFACTORLgiven == False:
                self.NFACTORL = 0.0
        if 'NFACTORLEXP' in param:
            self.NFACTORLEXP = param['NFACTORLEXP']
            self.NFACTORLEXPgiven = True
        elif 'NFACTORLEXP'.swapcase() in param:
            self.NFACTORLEXP = param['NFACTORLEXP'.swapcase()]
            self.NFACTORLEXPgiven = True
        else:
            if self.NFACTORLEXPgiven == False:
                self.NFACTORLEXP = 1.0
        if 'NFACTORW' in param:
            self.NFACTORW = param['NFACTORW']
            self.NFACTORWgiven = True
        elif 'NFACTORW'.swapcase() in param:
            self.NFACTORW = param['NFACTORW'.swapcase()]
            self.NFACTORWgiven = True
        else:
            if self.NFACTORWgiven == False:
                self.NFACTORW = 0.0
        if 'NFACTORWEXP' in param:
            self.NFACTORWEXP = param['NFACTORWEXP']
            self.NFACTORWEXPgiven = True
        elif 'NFACTORWEXP'.swapcase() in param:
            self.NFACTORWEXP = param['NFACTORWEXP'.swapcase()]
            self.NFACTORWEXPgiven = True
        else:
            if self.NFACTORWEXPgiven == False:
                self.NFACTORWEXP = 1.0
        if 'NFACTORWL' in param:
            self.NFACTORWL = param['NFACTORWL']
            self.NFACTORWLgiven = True
        elif 'NFACTORWL'.swapcase() in param:
            self.NFACTORWL = param['NFACTORWL'.swapcase()]
            self.NFACTORWLgiven = True
        else:
            if self.NFACTORWLgiven == False:
                self.NFACTORWL = 0.0
        if 'NFACTORWLEXP' in param:
            self.NFACTORWLEXP = param['NFACTORWLEXP']
            self.NFACTORWLEXPgiven = True
        elif 'NFACTORWLEXP'.swapcase() in param:
            self.NFACTORWLEXP = param['NFACTORWLEXP'.swapcase()]
            self.NFACTORWLEXPgiven = True
        else:
            if self.NFACTORWLEXPgiven == False:
                self.NFACTORWLEXP = 1.0
        if 'LNFACTOR' in param:
            self.LNFACTOR = param['LNFACTOR']
            self.LNFACTORgiven = True
        elif 'LNFACTOR'.swapcase() in param:
            self.LNFACTOR = param['LNFACTOR'.swapcase()]
            self.LNFACTORgiven = True
        else:
            if self.LNFACTORgiven == False:
                self.LNFACTOR = 0.0
        if 'WNFACTOR' in param:
            self.WNFACTOR = param['WNFACTOR']
            self.WNFACTORgiven = True
        elif 'WNFACTOR'.swapcase() in param:
            self.WNFACTOR = param['WNFACTOR'.swapcase()]
            self.WNFACTORgiven = True
        else:
            if self.WNFACTORgiven == False:
                self.WNFACTOR = 0.0
        if 'PNFACTOR' in param:
            self.PNFACTOR = param['PNFACTOR']
            self.PNFACTORgiven = True
        elif 'PNFACTOR'.swapcase() in param:
            self.PNFACTOR = param['PNFACTOR'.swapcase()]
            self.PNFACTORgiven = True
        else:
            if self.PNFACTORgiven == False:
                self.PNFACTOR = 0.0
        if 'CDSCD' in param:
            self.CDSCD = param['CDSCD']
            self.CDSCDgiven = True
        elif 'CDSCD'.swapcase() in param:
            self.CDSCD = param['CDSCD'.swapcase()]
            self.CDSCDgiven = True
        else:
            if self.CDSCDgiven == False:
                self.CDSCD = 1e-09
        if 'CDSCDL' in param:
            self.CDSCDL = param['CDSCDL']
            self.CDSCDLgiven = True
        elif 'CDSCDL'.swapcase() in param:
            self.CDSCDL = param['CDSCDL'.swapcase()]
            self.CDSCDLgiven = True
        else:
            if self.CDSCDLgiven == False:
                self.CDSCDL = 0.0
        if 'CDSCDLEXP' in param:
            self.CDSCDLEXP = param['CDSCDLEXP']
            self.CDSCDLEXPgiven = True
        elif 'CDSCDLEXP'.swapcase() in param:
            self.CDSCDLEXP = param['CDSCDLEXP'.swapcase()]
            self.CDSCDLEXPgiven = True
        else:
            if self.CDSCDLEXPgiven == False:
                self.CDSCDLEXP = 1.0
        if 'LCDSCD' in param:
            self.LCDSCD = param['LCDSCD']
            self.LCDSCDgiven = True
        elif 'LCDSCD'.swapcase() in param:
            self.LCDSCD = param['LCDSCD'.swapcase()]
            self.LCDSCDgiven = True
        else:
            if self.LCDSCDgiven == False:
                self.LCDSCD = 0.0
        if 'WCDSCD' in param:
            self.WCDSCD = param['WCDSCD']
            self.WCDSCDgiven = True
        elif 'WCDSCD'.swapcase() in param:
            self.WCDSCD = param['WCDSCD'.swapcase()]
            self.WCDSCDgiven = True
        else:
            if self.WCDSCDgiven == False:
                self.WCDSCD = 0.0
        if 'PCDSCD' in param:
            self.PCDSCD = param['PCDSCD']
            self.PCDSCDgiven = True
        elif 'PCDSCD'.swapcase() in param:
            self.PCDSCD = param['PCDSCD'.swapcase()]
            self.PCDSCDgiven = True
        else:
            if self.PCDSCDgiven == False:
                self.PCDSCD = 0.0
        if 'CDSCDR' in param:
            self.CDSCDR = param['CDSCDR']
            self.CDSCDRgiven = True
        elif 'CDSCDR'.swapcase() in param:
            self.CDSCDR = param['CDSCDR'.swapcase()]
            self.CDSCDRgiven = True
        else:
            if self.CDSCDRgiven == False:
                self.CDSCDR = self.CDSCD
        if 'CDSCDLR' in param:
            self.CDSCDLR = param['CDSCDLR']
            self.CDSCDLRgiven = True
        elif 'CDSCDLR'.swapcase() in param:
            self.CDSCDLR = param['CDSCDLR'.swapcase()]
            self.CDSCDLRgiven = True
        else:
            if self.CDSCDLRgiven == False:
                self.CDSCDLR = self.CDSCDL
        if 'LCDSCDR' in param:
            self.LCDSCDR = param['LCDSCDR']
            self.LCDSCDRgiven = True
        elif 'LCDSCDR'.swapcase() in param:
            self.LCDSCDR = param['LCDSCDR'.swapcase()]
            self.LCDSCDRgiven = True
        else:
            if self.LCDSCDRgiven == False:
                self.LCDSCDR = self.LCDSCD
        if 'WCDSCDR' in param:
            self.WCDSCDR = param['WCDSCDR']
            self.WCDSCDRgiven = True
        elif 'WCDSCDR'.swapcase() in param:
            self.WCDSCDR = param['WCDSCDR'.swapcase()]
            self.WCDSCDRgiven = True
        else:
            if self.WCDSCDRgiven == False:
                self.WCDSCDR = self.WCDSCD
        if 'PCDSCDR' in param:
            self.PCDSCDR = param['PCDSCDR']
            self.PCDSCDRgiven = True
        elif 'PCDSCDR'.swapcase() in param:
            self.PCDSCDR = param['PCDSCDR'.swapcase()]
            self.PCDSCDRgiven = True
        else:
            if self.PCDSCDRgiven == False:
                self.PCDSCDR = self.PCDSCD
        if 'CDSCB' in param:
            self.CDSCB = param['CDSCB']
            self.CDSCBgiven = True
        elif 'CDSCB'.swapcase() in param:
            self.CDSCB = param['CDSCB'.swapcase()]
            self.CDSCBgiven = True
        else:
            if self.CDSCBgiven == False:
                self.CDSCB = 0.0
        if 'CDSCBL' in param:
            self.CDSCBL = param['CDSCBL']
            self.CDSCBLgiven = True
        elif 'CDSCBL'.swapcase() in param:
            self.CDSCBL = param['CDSCBL'.swapcase()]
            self.CDSCBLgiven = True
        else:
            if self.CDSCBLgiven == False:
                self.CDSCBL = 0.0
        if 'CDSCBLEXP' in param:
            self.CDSCBLEXP = param['CDSCBLEXP']
            self.CDSCBLEXPgiven = True
        elif 'CDSCBLEXP'.swapcase() in param:
            self.CDSCBLEXP = param['CDSCBLEXP'.swapcase()]
            self.CDSCBLEXPgiven = True
        else:
            if self.CDSCBLEXPgiven == False:
                self.CDSCBLEXP = 1.0
        if 'LCDSCB' in param:
            self.LCDSCB = param['LCDSCB']
            self.LCDSCBgiven = True
        elif 'LCDSCB'.swapcase() in param:
            self.LCDSCB = param['LCDSCB'.swapcase()]
            self.LCDSCBgiven = True
        else:
            if self.LCDSCBgiven == False:
                self.LCDSCB = 0.0
        if 'WCDSCB' in param:
            self.WCDSCB = param['WCDSCB']
            self.WCDSCBgiven = True
        elif 'WCDSCB'.swapcase() in param:
            self.WCDSCB = param['WCDSCB'.swapcase()]
            self.WCDSCBgiven = True
        else:
            if self.WCDSCBgiven == False:
                self.WCDSCB = 0.0
        if 'PCDSCB' in param:
            self.PCDSCB = param['PCDSCB']
            self.PCDSCBgiven = True
        elif 'PCDSCB'.swapcase() in param:
            self.PCDSCB = param['PCDSCB'.swapcase()]
            self.PCDSCBgiven = True
        else:
            if self.PCDSCBgiven == False:
                self.PCDSCB = 0.0
        if 'VSAT' in param:
            self.VSAT = param['VSAT']
            self.VSATgiven = True
        elif 'VSAT'.swapcase() in param:
            self.VSAT = param['VSAT'.swapcase()]
            self.VSATgiven = True
        else:
            if self.VSATgiven == False:
                self.VSAT = 100000.0
        if 'LVSAT' in param:
            self.LVSAT = param['LVSAT']
            self.LVSATgiven = True
        elif 'LVSAT'.swapcase() in param:
            self.LVSAT = param['LVSAT'.swapcase()]
            self.LVSATgiven = True
        else:
            if self.LVSATgiven == False:
                self.LVSAT = 0.0
        if 'WVSAT' in param:
            self.WVSAT = param['WVSAT']
            self.WVSATgiven = True
        elif 'WVSAT'.swapcase() in param:
            self.WVSAT = param['WVSAT'.swapcase()]
            self.WVSATgiven = True
        else:
            if self.WVSATgiven == False:
                self.WVSAT = 0.0
        if 'PVSAT' in param:
            self.PVSAT = param['PVSAT']
            self.PVSATgiven = True
        elif 'PVSAT'.swapcase() in param:
            self.PVSAT = param['PVSAT'.swapcase()]
            self.PVSATgiven = True
        else:
            if self.PVSATgiven == False:
                self.PVSAT = 0.0
        if 'VSATL' in param:
            self.VSATL = param['VSATL']
            self.VSATLgiven = True
        elif 'VSATL'.swapcase() in param:
            self.VSATL = param['VSATL'.swapcase()]
            self.VSATLgiven = True
        else:
            if self.VSATLgiven == False:
                self.VSATL = 0.0
        if 'VSATLEXP' in param:
            self.VSATLEXP = param['VSATLEXP']
            self.VSATLEXPgiven = True
        elif 'VSATLEXP'.swapcase() in param:
            self.VSATLEXP = param['VSATLEXP'.swapcase()]
            self.VSATLEXPgiven = True
        else:
            if self.VSATLEXPgiven == False:
                self.VSATLEXP = 1.0
        if 'VSATW' in param:
            self.VSATW = param['VSATW']
            self.VSATWgiven = True
        elif 'VSATW'.swapcase() in param:
            self.VSATW = param['VSATW'.swapcase()]
            self.VSATWgiven = True
        else:
            if self.VSATWgiven == False:
                self.VSATW = 0.0
        if 'VSATWEXP' in param:
            self.VSATWEXP = param['VSATWEXP']
            self.VSATWEXPgiven = True
        elif 'VSATWEXP'.swapcase() in param:
            self.VSATWEXP = param['VSATWEXP'.swapcase()]
            self.VSATWEXPgiven = True
        else:
            if self.VSATWEXPgiven == False:
                self.VSATWEXP = 1.0
        if 'VSATWL' in param:
            self.VSATWL = param['VSATWL']
            self.VSATWLgiven = True
        elif 'VSATWL'.swapcase() in param:
            self.VSATWL = param['VSATWL'.swapcase()]
            self.VSATWLgiven = True
        else:
            if self.VSATWLgiven == False:
                self.VSATWL = 0.0
        if 'VSATWLEXP' in param:
            self.VSATWLEXP = param['VSATWLEXP']
            self.VSATWLEXPgiven = True
        elif 'VSATWLEXP'.swapcase() in param:
            self.VSATWLEXP = param['VSATWLEXP'.swapcase()]
            self.VSATWLEXPgiven = True
        else:
            if self.VSATWLEXPgiven == False:
                self.VSATWLEXP = 1.0
        if 'VSATR' in param:
            self.VSATR = param['VSATR']
            self.VSATRgiven = True
        elif 'VSATR'.swapcase() in param:
            self.VSATR = param['VSATR'.swapcase()]
            self.VSATRgiven = True
        else:
            if self.VSATRgiven == False:
                self.VSATR = self.VSAT
        if 'LVSATR' in param:
            self.LVSATR = param['LVSATR']
            self.LVSATRgiven = True
        elif 'LVSATR'.swapcase() in param:
            self.LVSATR = param['LVSATR'.swapcase()]
            self.LVSATRgiven = True
        else:
            if self.LVSATRgiven == False:
                self.LVSATR = self.LVSAT
        if 'WVSATR' in param:
            self.WVSATR = param['WVSATR']
            self.WVSATRgiven = True
        elif 'WVSATR'.swapcase() in param:
            self.WVSATR = param['WVSATR'.swapcase()]
            self.WVSATRgiven = True
        else:
            if self.WVSATRgiven == False:
                self.WVSATR = self.WVSAT
        if 'PVSATR' in param:
            self.PVSATR = param['PVSATR']
            self.PVSATRgiven = True
        elif 'PVSATR'.swapcase() in param:
            self.PVSATR = param['PVSATR'.swapcase()]
            self.PVSATRgiven = True
        else:
            if self.PVSATRgiven == False:
                self.PVSATR = self.PVSAT
        if 'DELTA' in param:
            self.DELTA = param['DELTA']
            self.DELTAgiven = True
        elif 'DELTA'.swapcase() in param:
            self.DELTA = param['DELTA'.swapcase()]
            self.DELTAgiven = True
        else:
            if self.DELTAgiven == False:
                self.DELTA = 0.125
        if 'LDELTA' in param:
            self.LDELTA = param['LDELTA']
            self.LDELTAgiven = True
        elif 'LDELTA'.swapcase() in param:
            self.LDELTA = param['LDELTA'.swapcase()]
            self.LDELTAgiven = True
        else:
            if self.LDELTAgiven == False:
                self.LDELTA = 0.0
        if 'WDELTA' in param:
            self.WDELTA = param['WDELTA']
            self.WDELTAgiven = True
        elif 'WDELTA'.swapcase() in param:
            self.WDELTA = param['WDELTA'.swapcase()]
            self.WDELTAgiven = True
        else:
            if self.WDELTAgiven == False:
                self.WDELTA = 0.0
        if 'PDELTA' in param:
            self.PDELTA = param['PDELTA']
            self.PDELTAgiven = True
        elif 'PDELTA'.swapcase() in param:
            self.PDELTA = param['PDELTA'.swapcase()]
            self.PDELTAgiven = True
        else:
            if self.PDELTAgiven == False:
                self.PDELTA = 0.0
        if 'DELTAL' in param:
            self.DELTAL = param['DELTAL']
            self.DELTALgiven = True
        elif 'DELTAL'.swapcase() in param:
            self.DELTAL = param['DELTAL'.swapcase()]
            self.DELTALgiven = True
        else:
            if self.DELTALgiven == False:
                self.DELTAL = 0.0
        if 'DELTALEXP' in param:
            self.DELTALEXP = param['DELTALEXP']
            self.DELTALEXPgiven = True
        elif 'DELTALEXP'.swapcase() in param:
            self.DELTALEXP = param['DELTALEXP'.swapcase()]
            self.DELTALEXPgiven = True
        else:
            if self.DELTALEXPgiven == False:
                self.DELTALEXP = 1.0
        if 'VSATCV' in param:
            self.VSATCV = param['VSATCV']
            self.VSATCVgiven = True
        elif 'VSATCV'.swapcase() in param:
            self.VSATCV = param['VSATCV'.swapcase()]
            self.VSATCVgiven = True
        else:
            if self.VSATCVgiven == False:
                self.VSATCV = 100000.0
        if 'LVSATCV' in param:
            self.LVSATCV = param['LVSATCV']
            self.LVSATCVgiven = True
        elif 'LVSATCV'.swapcase() in param:
            self.LVSATCV = param['LVSATCV'.swapcase()]
            self.LVSATCVgiven = True
        else:
            if self.LVSATCVgiven == False:
                self.LVSATCV = 0.0
        if 'WVSATCV' in param:
            self.WVSATCV = param['WVSATCV']
            self.WVSATCVgiven = True
        elif 'WVSATCV'.swapcase() in param:
            self.WVSATCV = param['WVSATCV'.swapcase()]
            self.WVSATCVgiven = True
        else:
            if self.WVSATCVgiven == False:
                self.WVSATCV = 0.0
        if 'PVSATCV' in param:
            self.PVSATCV = param['PVSATCV']
            self.PVSATCVgiven = True
        elif 'PVSATCV'.swapcase() in param:
            self.PVSATCV = param['PVSATCV'.swapcase()]
            self.PVSATCVgiven = True
        else:
            if self.PVSATCVgiven == False:
                self.PVSATCV = 0.0
        if 'VSATCVL' in param:
            self.VSATCVL = param['VSATCVL']
            self.VSATCVLgiven = True
        elif 'VSATCVL'.swapcase() in param:
            self.VSATCVL = param['VSATCVL'.swapcase()]
            self.VSATCVLgiven = True
        else:
            if self.VSATCVLgiven == False:
                self.VSATCVL = 0.0
        if 'VSATCVLEXP' in param:
            self.VSATCVLEXP = param['VSATCVLEXP']
            self.VSATCVLEXPgiven = True
        elif 'VSATCVLEXP'.swapcase() in param:
            self.VSATCVLEXP = param['VSATCVLEXP'.swapcase()]
            self.VSATCVLEXPgiven = True
        else:
            if self.VSATCVLEXPgiven == False:
                self.VSATCVLEXP = 1.0
        if 'VSATCVW' in param:
            self.VSATCVW = param['VSATCVW']
            self.VSATCVWgiven = True
        elif 'VSATCVW'.swapcase() in param:
            self.VSATCVW = param['VSATCVW'.swapcase()]
            self.VSATCVWgiven = True
        else:
            if self.VSATCVWgiven == False:
                self.VSATCVW = 0.0
        if 'VSATCVWEXP' in param:
            self.VSATCVWEXP = param['VSATCVWEXP']
            self.VSATCVWEXPgiven = True
        elif 'VSATCVWEXP'.swapcase() in param:
            self.VSATCVWEXP = param['VSATCVWEXP'.swapcase()]
            self.VSATCVWEXPgiven = True
        else:
            if self.VSATCVWEXPgiven == False:
                self.VSATCVWEXP = 1.0
        if 'VSATCVWL' in param:
            self.VSATCVWL = param['VSATCVWL']
            self.VSATCVWLgiven = True
        elif 'VSATCVWL'.swapcase() in param:
            self.VSATCVWL = param['VSATCVWL'.swapcase()]
            self.VSATCVWLgiven = True
        else:
            if self.VSATCVWLgiven == False:
                self.VSATCVWL = 0.0
        if 'VSATCVWLEXP' in param:
            self.VSATCVWLEXP = param['VSATCVWLEXP']
            self.VSATCVWLEXPgiven = True
        elif 'VSATCVWLEXP'.swapcase() in param:
            self.VSATCVWLEXP = param['VSATCVWLEXP'.swapcase()]
            self.VSATCVWLEXPgiven = True
        else:
            if self.VSATCVWLEXPgiven == False:
                self.VSATCVWLEXP = 1.0
        if 'UP1' in param:
            self.UP1 = param['UP1']
            self.UP1given = True
        elif 'UP1'.swapcase() in param:
            self.UP1 = param['UP1'.swapcase()]
            self.UP1given = True
        else:
            if self.UP1given == False:
                self.UP1 = 0.0
        if 'LP1' in param:
            self.LP1 = param['LP1']
            self.LP1given = True
        elif 'LP1'.swapcase() in param:
            self.LP1 = param['LP1'.swapcase()]
            self.LP1given = True
        else:
            if self.LP1given == False:
                self.LP1 = 1e-08
        if 'UP2' in param:
            self.UP2 = param['UP2']
            self.UP2given = True
        elif 'UP2'.swapcase() in param:
            self.UP2 = param['UP2'.swapcase()]
            self.UP2given = True
        else:
            if self.UP2given == False:
                self.UP2 = 0.0
        if 'LP2' in param:
            self.LP2 = param['LP2']
            self.LP2given = True
        elif 'LP2'.swapcase() in param:
            self.LP2 = param['LP2'.swapcase()]
            self.LP2given = True
        else:
            if self.LP2given == False:
                self.LP2 = 1e-08
        if 'U0' in param:
            self.U0 = param['U0']
            self.U0given = True
        elif 'U0'.swapcase() in param:
            self.U0 = param['U0'.swapcase()]
            self.U0given = True
        else:
            if self.U0given == False:
                self.U0 = 0.067
        if 'U0L' in param:
            self.U0L = param['U0L']
            self.U0Lgiven = True
        elif 'U0L'.swapcase() in param:
            self.U0L = param['U0L'.swapcase()]
            self.U0Lgiven = True
        else:
            if self.U0Lgiven == False:
                self.U0L = 0.0
        if 'U0LEXP' in param:
            self.U0LEXP = param['U0LEXP']
            self.U0LEXPgiven = True
        elif 'U0LEXP'.swapcase() in param:
            self.U0LEXP = param['U0LEXP'.swapcase()]
            self.U0LEXPgiven = True
        else:
            if self.U0LEXPgiven == False:
                self.U0LEXP = 1.0
        if 'LU0' in param:
            self.LU0 = param['LU0']
            self.LU0given = True
        elif 'LU0'.swapcase() in param:
            self.LU0 = param['LU0'.swapcase()]
            self.LU0given = True
        else:
            if self.LU0given == False:
                self.LU0 = 0.0
        if 'WU0' in param:
            self.WU0 = param['WU0']
            self.WU0given = True
        elif 'WU0'.swapcase() in param:
            self.WU0 = param['WU0'.swapcase()]
            self.WU0given = True
        else:
            if self.WU0given == False:
                self.WU0 = 0.0
        if 'PU0' in param:
            self.PU0 = param['PU0']
            self.PU0given = True
        elif 'PU0'.swapcase() in param:
            self.PU0 = param['PU0'.swapcase()]
            self.PU0given = True
        else:
            if self.PU0given == False:
                self.PU0 = 0.0
        if 'U0R' in param:
            self.U0R = param['U0R']
            self.U0Rgiven = True
        elif 'U0R'.swapcase() in param:
            self.U0R = param['U0R'.swapcase()]
            self.U0Rgiven = True
        else:
            if self.U0Rgiven == False:
                self.U0R = self.U0
        if 'LU0R' in param:
            self.LU0R = param['LU0R']
            self.LU0Rgiven = True
        elif 'LU0R'.swapcase() in param:
            self.LU0R = param['LU0R'.swapcase()]
            self.LU0Rgiven = True
        else:
            if self.LU0Rgiven == False:
                self.LU0R = self.LU0
        if 'WU0R' in param:
            self.WU0R = param['WU0R']
            self.WU0Rgiven = True
        elif 'WU0R'.swapcase() in param:
            self.WU0R = param['WU0R'.swapcase()]
            self.WU0Rgiven = True
        else:
            if self.WU0Rgiven == False:
                self.WU0R = self.WU0
        if 'PU0R' in param:
            self.PU0R = param['PU0R']
            self.PU0Rgiven = True
        elif 'PU0R'.swapcase() in param:
            self.PU0R = param['PU0R'.swapcase()]
            self.PU0Rgiven = True
        else:
            if self.PU0Rgiven == False:
                self.PU0R = self.PU0
        if 'ETAMOB' in param:
            self.ETAMOB = param['ETAMOB']
            self.ETAMOBgiven = True
        elif 'ETAMOB'.swapcase() in param:
            self.ETAMOB = param['ETAMOB'.swapcase()]
            self.ETAMOBgiven = True
        else:
            if self.ETAMOBgiven == False:
                self.ETAMOB = 1.0
        if 'UA' in param:
            self.UA = param['UA']
            self.UAgiven = True
        elif 'UA'.swapcase() in param:
            self.UA = param['UA'.swapcase()]
            self.UAgiven = True
        else:
            if self.UAgiven == False:
                self.UA = 0.001
        if 'UAL' in param:
            self.UAL = param['UAL']
            self.UALgiven = True
        elif 'UAL'.swapcase() in param:
            self.UAL = param['UAL'.swapcase()]
            self.UALgiven = True
        else:
            if self.UALgiven == False:
                self.UAL = 0.0
        if 'UALEXP' in param:
            self.UALEXP = param['UALEXP']
            self.UALEXPgiven = True
        elif 'UALEXP'.swapcase() in param:
            self.UALEXP = param['UALEXP'.swapcase()]
            self.UALEXPgiven = True
        else:
            if self.UALEXPgiven == False:
                self.UALEXP = 1.0
        if 'UAW' in param:
            self.UAW = param['UAW']
            self.UAWgiven = True
        elif 'UAW'.swapcase() in param:
            self.UAW = param['UAW'.swapcase()]
            self.UAWgiven = True
        else:
            if self.UAWgiven == False:
                self.UAW = 0.0
        if 'UAWEXP' in param:
            self.UAWEXP = param['UAWEXP']
            self.UAWEXPgiven = True
        elif 'UAWEXP'.swapcase() in param:
            self.UAWEXP = param['UAWEXP'.swapcase()]
            self.UAWEXPgiven = True
        else:
            if self.UAWEXPgiven == False:
                self.UAWEXP = 1.0
        if 'UAWL' in param:
            self.UAWL = param['UAWL']
            self.UAWLgiven = True
        elif 'UAWL'.swapcase() in param:
            self.UAWL = param['UAWL'.swapcase()]
            self.UAWLgiven = True
        else:
            if self.UAWLgiven == False:
                self.UAWL = 0.0
        if 'UAWLEXP' in param:
            self.UAWLEXP = param['UAWLEXP']
            self.UAWLEXPgiven = True
        elif 'UAWLEXP'.swapcase() in param:
            self.UAWLEXP = param['UAWLEXP'.swapcase()]
            self.UAWLEXPgiven = True
        else:
            if self.UAWLEXPgiven == False:
                self.UAWLEXP = 1.0
        if 'LUA' in param:
            self.LUA = param['LUA']
            self.LUAgiven = True
        elif 'LUA'.swapcase() in param:
            self.LUA = param['LUA'.swapcase()]
            self.LUAgiven = True
        else:
            if self.LUAgiven == False:
                self.LUA = 0.0
        if 'WUA' in param:
            self.WUA = param['WUA']
            self.WUAgiven = True
        elif 'WUA'.swapcase() in param:
            self.WUA = param['WUA'.swapcase()]
            self.WUAgiven = True
        else:
            if self.WUAgiven == False:
                self.WUA = 0.0
        if 'PUA' in param:
            self.PUA = param['PUA']
            self.PUAgiven = True
        elif 'PUA'.swapcase() in param:
            self.PUA = param['PUA'.swapcase()]
            self.PUAgiven = True
        else:
            if self.PUAgiven == False:
                self.PUA = 0.0
        if 'UAR' in param:
            self.UAR = param['UAR']
            self.UARgiven = True
        elif 'UAR'.swapcase() in param:
            self.UAR = param['UAR'.swapcase()]
            self.UARgiven = True
        else:
            if self.UARgiven == False:
                self.UAR = self.UA
        if 'LUAR' in param:
            self.LUAR = param['LUAR']
            self.LUARgiven = True
        elif 'LUAR'.swapcase() in param:
            self.LUAR = param['LUAR'.swapcase()]
            self.LUARgiven = True
        else:
            if self.LUARgiven == False:
                self.LUAR = self.LUA
        if 'WUAR' in param:
            self.WUAR = param['WUAR']
            self.WUARgiven = True
        elif 'WUAR'.swapcase() in param:
            self.WUAR = param['WUAR'.swapcase()]
            self.WUARgiven = True
        else:
            if self.WUARgiven == False:
                self.WUAR = self.WUA
        if 'PUAR' in param:
            self.PUAR = param['PUAR']
            self.PUARgiven = True
        elif 'PUAR'.swapcase() in param:
            self.PUAR = param['PUAR'.swapcase()]
            self.PUARgiven = True
        else:
            if self.PUARgiven == False:
                self.PUAR = self.PUA
        if 'EU' in param:
            self.EU = param['EU']
            self.EUgiven = True
        elif 'EU'.swapcase() in param:
            self.EU = param['EU'.swapcase()]
            self.EUgiven = True
        else:
            if self.EUgiven == False:
                self.EU = 1.5
        if 'LEU' in param:
            self.LEU = param['LEU']
            self.LEUgiven = True
        elif 'LEU'.swapcase() in param:
            self.LEU = param['LEU'.swapcase()]
            self.LEUgiven = True
        else:
            if self.LEUgiven == False:
                self.LEU = 0.0
        if 'WEU' in param:
            self.WEU = param['WEU']
            self.WEUgiven = True
        elif 'WEU'.swapcase() in param:
            self.WEU = param['WEU'.swapcase()]
            self.WEUgiven = True
        else:
            if self.WEUgiven == False:
                self.WEU = 0.0
        if 'PEU' in param:
            self.PEU = param['PEU']
            self.PEUgiven = True
        elif 'PEU'.swapcase() in param:
            self.PEU = param['PEU'.swapcase()]
            self.PEUgiven = True
        else:
            if self.PEUgiven == False:
                self.PEU = 0.0
        if 'EUL' in param:
            self.EUL = param['EUL']
            self.EULgiven = True
        elif 'EUL'.swapcase() in param:
            self.EUL = param['EUL'.swapcase()]
            self.EULgiven = True
        else:
            if self.EULgiven == False:
                self.EUL = 0.0
        if 'EULEXP' in param:
            self.EULEXP = param['EULEXP']
            self.EULEXPgiven = True
        elif 'EULEXP'.swapcase() in param:
            self.EULEXP = param['EULEXP'.swapcase()]
            self.EULEXPgiven = True
        else:
            if self.EULEXPgiven == False:
                self.EULEXP = 1.0
        if 'EUW' in param:
            self.EUW = param['EUW']
            self.EUWgiven = True
        elif 'EUW'.swapcase() in param:
            self.EUW = param['EUW'.swapcase()]
            self.EUWgiven = True
        else:
            if self.EUWgiven == False:
                self.EUW = 0.0
        if 'EUWEXP' in param:
            self.EUWEXP = param['EUWEXP']
            self.EUWEXPgiven = True
        elif 'EUWEXP'.swapcase() in param:
            self.EUWEXP = param['EUWEXP'.swapcase()]
            self.EUWEXPgiven = True
        else:
            if self.EUWEXPgiven == False:
                self.EUWEXP = 1.0
        if 'EUWL' in param:
            self.EUWL = param['EUWL']
            self.EUWLgiven = True
        elif 'EUWL'.swapcase() in param:
            self.EUWL = param['EUWL'.swapcase()]
            self.EUWLgiven = True
        else:
            if self.EUWLgiven == False:
                self.EUWL = 0.0
        if 'EUWLEXP' in param:
            self.EUWLEXP = param['EUWLEXP']
            self.EUWLEXPgiven = True
        elif 'EUWLEXP'.swapcase() in param:
            self.EUWLEXP = param['EUWLEXP'.swapcase()]
            self.EUWLEXPgiven = True
        else:
            if self.EUWLEXPgiven == False:
                self.EUWLEXP = 1.0
        if 'UD' in param:
            self.UD = param['UD']
            self.UDgiven = True
        elif 'UD'.swapcase() in param:
            self.UD = param['UD'.swapcase()]
            self.UDgiven = True
        else:
            if self.UDgiven == False:
                self.UD = 0.001
        if 'UDL' in param:
            self.UDL = param['UDL']
            self.UDLgiven = True
        elif 'UDL'.swapcase() in param:
            self.UDL = param['UDL'.swapcase()]
            self.UDLgiven = True
        else:
            if self.UDLgiven == False:
                self.UDL = 0.0
        if 'UDLEXP' in param:
            self.UDLEXP = param['UDLEXP']
            self.UDLEXPgiven = True
        elif 'UDLEXP'.swapcase() in param:
            self.UDLEXP = param['UDLEXP'.swapcase()]
            self.UDLEXPgiven = True
        else:
            if self.UDLEXPgiven == False:
                self.UDLEXP = 1.0
        if 'LUD' in param:
            self.LUD = param['LUD']
            self.LUDgiven = True
        elif 'LUD'.swapcase() in param:
            self.LUD = param['LUD'.swapcase()]
            self.LUDgiven = True
        else:
            if self.LUDgiven == False:
                self.LUD = 0.0
        if 'WUD' in param:
            self.WUD = param['WUD']
            self.WUDgiven = True
        elif 'WUD'.swapcase() in param:
            self.WUD = param['WUD'.swapcase()]
            self.WUDgiven = True
        else:
            if self.WUDgiven == False:
                self.WUD = 0.0
        if 'PUD' in param:
            self.PUD = param['PUD']
            self.PUDgiven = True
        elif 'PUD'.swapcase() in param:
            self.PUD = param['PUD'.swapcase()]
            self.PUDgiven = True
        else:
            if self.PUDgiven == False:
                self.PUD = 0.0
        if 'UDR' in param:
            self.UDR = param['UDR']
            self.UDRgiven = True
        elif 'UDR'.swapcase() in param:
            self.UDR = param['UDR'.swapcase()]
            self.UDRgiven = True
        else:
            if self.UDRgiven == False:
                self.UDR = self.UD
        if 'LUDR' in param:
            self.LUDR = param['LUDR']
            self.LUDRgiven = True
        elif 'LUDR'.swapcase() in param:
            self.LUDR = param['LUDR'.swapcase()]
            self.LUDRgiven = True
        else:
            if self.LUDRgiven == False:
                self.LUDR = self.LUD
        if 'WUDR' in param:
            self.WUDR = param['WUDR']
            self.WUDRgiven = True
        elif 'WUDR'.swapcase() in param:
            self.WUDR = param['WUDR'.swapcase()]
            self.WUDRgiven = True
        else:
            if self.WUDRgiven == False:
                self.WUDR = self.WUD
        if 'PUDR' in param:
            self.PUDR = param['PUDR']
            self.PUDRgiven = True
        elif 'PUDR'.swapcase() in param:
            self.PUDR = param['PUDR'.swapcase()]
            self.PUDRgiven = True
        else:
            if self.PUDRgiven == False:
                self.PUDR = self.PUD
        if 'UCS' in param:
            self.UCS = param['UCS']
            self.UCSgiven = True
        elif 'UCS'.swapcase() in param:
            self.UCS = param['UCS'.swapcase()]
            self.UCSgiven = True
        else:
            if self.UCSgiven == False:
                self.UCS = 2.0
        if 'LUCS' in param:
            self.LUCS = param['LUCS']
            self.LUCSgiven = True
        elif 'LUCS'.swapcase() in param:
            self.LUCS = param['LUCS'.swapcase()]
            self.LUCSgiven = True
        else:
            if self.LUCSgiven == False:
                self.LUCS = 0.0
        if 'WUCS' in param:
            self.WUCS = param['WUCS']
            self.WUCSgiven = True
        elif 'WUCS'.swapcase() in param:
            self.WUCS = param['WUCS'.swapcase()]
            self.WUCSgiven = True
        else:
            if self.WUCSgiven == False:
                self.WUCS = 0.0
        if 'PUCS' in param:
            self.PUCS = param['PUCS']
            self.PUCSgiven = True
        elif 'PUCS'.swapcase() in param:
            self.PUCS = param['PUCS'.swapcase()]
            self.PUCSgiven = True
        else:
            if self.PUCSgiven == False:
                self.PUCS = 0.0
        if 'UCSR' in param:
            self.UCSR = param['UCSR']
            self.UCSRgiven = True
        elif 'UCSR'.swapcase() in param:
            self.UCSR = param['UCSR'.swapcase()]
            self.UCSRgiven = True
        else:
            if self.UCSRgiven == False:
                self.UCSR = self.UCS
        if 'LUCSR' in param:
            self.LUCSR = param['LUCSR']
            self.LUCSRgiven = True
        elif 'LUCSR'.swapcase() in param:
            self.LUCSR = param['LUCSR'.swapcase()]
            self.LUCSRgiven = True
        else:
            if self.LUCSRgiven == False:
                self.LUCSR = self.LUCS
        if 'WUCSR' in param:
            self.WUCSR = param['WUCSR']
            self.WUCSRgiven = True
        elif 'WUCSR'.swapcase() in param:
            self.WUCSR = param['WUCSR'.swapcase()]
            self.WUCSRgiven = True
        else:
            if self.WUCSRgiven == False:
                self.WUCSR = self.WUCS
        if 'PUCSR' in param:
            self.PUCSR = param['PUCSR']
            self.PUCSRgiven = True
        elif 'PUCSR'.swapcase() in param:
            self.PUCSR = param['PUCSR'.swapcase()]
            self.PUCSRgiven = True
        else:
            if self.PUCSRgiven == False:
                self.PUCSR = self.PUCS
        if 'UC' in param:
            self.UC = param['UC']
            self.UCgiven = True
        elif 'UC'.swapcase() in param:
            self.UC = param['UC'.swapcase()]
            self.UCgiven = True
        else:
            if self.UCgiven == False:
                self.UC = 0.0
        if 'UCL' in param:
            self.UCL = param['UCL']
            self.UCLgiven = True
        elif 'UCL'.swapcase() in param:
            self.UCL = param['UCL'.swapcase()]
            self.UCLgiven = True
        else:
            if self.UCLgiven == False:
                self.UCL = 0.0
        if 'UCLEXP' in param:
            self.UCLEXP = param['UCLEXP']
            self.UCLEXPgiven = True
        elif 'UCLEXP'.swapcase() in param:
            self.UCLEXP = param['UCLEXP'.swapcase()]
            self.UCLEXPgiven = True
        else:
            if self.UCLEXPgiven == False:
                self.UCLEXP = 1.0
        if 'UCW' in param:
            self.UCW = param['UCW']
            self.UCWgiven = True
        elif 'UCW'.swapcase() in param:
            self.UCW = param['UCW'.swapcase()]
            self.UCWgiven = True
        else:
            if self.UCWgiven == False:
                self.UCW = 0.0
        if 'UCWEXP' in param:
            self.UCWEXP = param['UCWEXP']
            self.UCWEXPgiven = True
        elif 'UCWEXP'.swapcase() in param:
            self.UCWEXP = param['UCWEXP'.swapcase()]
            self.UCWEXPgiven = True
        else:
            if self.UCWEXPgiven == False:
                self.UCWEXP = 1.0
        if 'UCWL' in param:
            self.UCWL = param['UCWL']
            self.UCWLgiven = True
        elif 'UCWL'.swapcase() in param:
            self.UCWL = param['UCWL'.swapcase()]
            self.UCWLgiven = True
        else:
            if self.UCWLgiven == False:
                self.UCWL = 0.0
        if 'UCWLEXP' in param:
            self.UCWLEXP = param['UCWLEXP']
            self.UCWLEXPgiven = True
        elif 'UCWLEXP'.swapcase() in param:
            self.UCWLEXP = param['UCWLEXP'.swapcase()]
            self.UCWLEXPgiven = True
        else:
            if self.UCWLEXPgiven == False:
                self.UCWLEXP = 1.0
        if 'LUC' in param:
            self.LUC = param['LUC']
            self.LUCgiven = True
        elif 'LUC'.swapcase() in param:
            self.LUC = param['LUC'.swapcase()]
            self.LUCgiven = True
        else:
            if self.LUCgiven == False:
                self.LUC = 0.0
        if 'WUC' in param:
            self.WUC = param['WUC']
            self.WUCgiven = True
        elif 'WUC'.swapcase() in param:
            self.WUC = param['WUC'.swapcase()]
            self.WUCgiven = True
        else:
            if self.WUCgiven == False:
                self.WUC = 0.0
        if 'PUC' in param:
            self.PUC = param['PUC']
            self.PUCgiven = True
        elif 'PUC'.swapcase() in param:
            self.PUC = param['PUC'.swapcase()]
            self.PUCgiven = True
        else:
            if self.PUCgiven == False:
                self.PUC = 0.0
        if 'UCR' in param:
            self.UCR = param['UCR']
            self.UCRgiven = True
        elif 'UCR'.swapcase() in param:
            self.UCR = param['UCR'.swapcase()]
            self.UCRgiven = True
        else:
            if self.UCRgiven == False:
                self.UCR = self.UC
        if 'LUCR' in param:
            self.LUCR = param['LUCR']
            self.LUCRgiven = True
        elif 'LUCR'.swapcase() in param:
            self.LUCR = param['LUCR'.swapcase()]
            self.LUCRgiven = True
        else:
            if self.LUCRgiven == False:
                self.LUCR = self.LUC
        if 'WUCR' in param:
            self.WUCR = param['WUCR']
            self.WUCRgiven = True
        elif 'WUCR'.swapcase() in param:
            self.WUCR = param['WUCR'.swapcase()]
            self.WUCRgiven = True
        else:
            if self.WUCRgiven == False:
                self.WUCR = self.WUC
        if 'PUCR' in param:
            self.PUCR = param['PUCR']
            self.PUCRgiven = True
        elif 'PUCR'.swapcase() in param:
            self.PUCR = param['PUCR'.swapcase()]
            self.PUCRgiven = True
        else:
            if self.PUCRgiven == False:
                self.PUCR = self.PUC
        if 'PCLM' in param:
            self.PCLM = param['PCLM']
            self.PCLMgiven = True
        elif 'PCLM'.swapcase() in param:
            self.PCLM = param['PCLM'.swapcase()]
            self.PCLMgiven = True
        else:
            if self.PCLMgiven == False:
                self.PCLM = 0.0
        if 'PCLML' in param:
            self.PCLML = param['PCLML']
            self.PCLMLgiven = True
        elif 'PCLML'.swapcase() in param:
            self.PCLML = param['PCLML'.swapcase()]
            self.PCLMLgiven = True
        else:
            if self.PCLMLgiven == False:
                self.PCLML = 0.0
        if 'PCLMLEXP' in param:
            self.PCLMLEXP = param['PCLMLEXP']
            self.PCLMLEXPgiven = True
        elif 'PCLMLEXP'.swapcase() in param:
            self.PCLMLEXP = param['PCLMLEXP'.swapcase()]
            self.PCLMLEXPgiven = True
        else:
            if self.PCLMLEXPgiven == False:
                self.PCLMLEXP = 1.0
        if 'LPCLM' in param:
            self.LPCLM = param['LPCLM']
            self.LPCLMgiven = True
        elif 'LPCLM'.swapcase() in param:
            self.LPCLM = param['LPCLM'.swapcase()]
            self.LPCLMgiven = True
        else:
            if self.LPCLMgiven == False:
                self.LPCLM = 0.0
        if 'WPCLM' in param:
            self.WPCLM = param['WPCLM']
            self.WPCLMgiven = True
        elif 'WPCLM'.swapcase() in param:
            self.WPCLM = param['WPCLM'.swapcase()]
            self.WPCLMgiven = True
        else:
            if self.WPCLMgiven == False:
                self.WPCLM = 0.0
        if 'PPCLM' in param:
            self.PPCLM = param['PPCLM']
            self.PPCLMgiven = True
        elif 'PPCLM'.swapcase() in param:
            self.PPCLM = param['PPCLM'.swapcase()]
            self.PPCLMgiven = True
        else:
            if self.PPCLMgiven == False:
                self.PPCLM = 0.0
        if 'PCLMR' in param:
            self.PCLMR = param['PCLMR']
            self.PCLMRgiven = True
        elif 'PCLMR'.swapcase() in param:
            self.PCLMR = param['PCLMR'.swapcase()]
            self.PCLMRgiven = True
        else:
            if self.PCLMRgiven == False:
                self.PCLMR = self.PCLM
        if 'LPCLMR' in param:
            self.LPCLMR = param['LPCLMR']
            self.LPCLMRgiven = True
        elif 'LPCLMR'.swapcase() in param:
            self.LPCLMR = param['LPCLMR'.swapcase()]
            self.LPCLMRgiven = True
        else:
            if self.LPCLMRgiven == False:
                self.LPCLMR = self.LPCLM
        if 'WPCLMR' in param:
            self.WPCLMR = param['WPCLMR']
            self.WPCLMRgiven = True
        elif 'WPCLMR'.swapcase() in param:
            self.WPCLMR = param['WPCLMR'.swapcase()]
            self.WPCLMRgiven = True
        else:
            if self.WPCLMRgiven == False:
                self.WPCLMR = self.WPCLM
        if 'PPCLMR' in param:
            self.PPCLMR = param['PPCLMR']
            self.PPCLMRgiven = True
        elif 'PPCLMR'.swapcase() in param:
            self.PPCLMR = param['PPCLMR'.swapcase()]
            self.PPCLMRgiven = True
        else:
            if self.PPCLMRgiven == False:
                self.PPCLMR = self.PPCLM
        if 'PCLMG' in param:
            self.PCLMG = param['PCLMG']
            self.PCLMGgiven = True
        elif 'PCLMG'.swapcase() in param:
            self.PCLMG = param['PCLMG'.swapcase()]
            self.PCLMGgiven = True
        else:
            if self.PCLMGgiven == False:
                self.PCLMG = 0.0
        if 'PCLMCV' in param:
            self.PCLMCV = param['PCLMCV']
            self.PCLMCVgiven = True
        elif 'PCLMCV'.swapcase() in param:
            self.PCLMCV = param['PCLMCV'.swapcase()]
            self.PCLMCVgiven = True
        else:
            if self.PCLMCVgiven == False:
                self.PCLMCV = self.PCLM
        if 'PCLMCVL' in param:
            self.PCLMCVL = param['PCLMCVL']
            self.PCLMCVLgiven = True
        elif 'PCLMCVL'.swapcase() in param:
            self.PCLMCVL = param['PCLMCVL'.swapcase()]
            self.PCLMCVLgiven = True
        else:
            if self.PCLMCVLgiven == False:
                self.PCLMCVL = self.PCLML
        if 'PCLMCVLEXP' in param:
            self.PCLMCVLEXP = param['PCLMCVLEXP']
            self.PCLMCVLEXPgiven = True
        elif 'PCLMCVLEXP'.swapcase() in param:
            self.PCLMCVLEXP = param['PCLMCVLEXP'.swapcase()]
            self.PCLMCVLEXPgiven = True
        else:
            if self.PCLMCVLEXPgiven == False:
                self.PCLMCVLEXP = self.PCLMLEXP
        if 'LPCLMCV' in param:
            self.LPCLMCV = param['LPCLMCV']
            self.LPCLMCVgiven = True
        elif 'LPCLMCV'.swapcase() in param:
            self.LPCLMCV = param['LPCLMCV'.swapcase()]
            self.LPCLMCVgiven = True
        else:
            if self.LPCLMCVgiven == False:
                self.LPCLMCV = self.LPCLM
        if 'WPCLMCV' in param:
            self.WPCLMCV = param['WPCLMCV']
            self.WPCLMCVgiven = True
        elif 'WPCLMCV'.swapcase() in param:
            self.WPCLMCV = param['WPCLMCV'.swapcase()]
            self.WPCLMCVgiven = True
        else:
            if self.WPCLMCVgiven == False:
                self.WPCLMCV = self.WPCLM
        if 'PPCLMCV' in param:
            self.PPCLMCV = param['PPCLMCV']
            self.PPCLMCVgiven = True
        elif 'PPCLMCV'.swapcase() in param:
            self.PPCLMCV = param['PPCLMCV'.swapcase()]
            self.PPCLMCVgiven = True
        else:
            if self.PPCLMCVgiven == False:
                self.PPCLMCV = self.PPCLM
        if 'PSCBE1' in param:
            self.PSCBE1 = param['PSCBE1']
            self.PSCBE1given = True
        elif 'PSCBE1'.swapcase() in param:
            self.PSCBE1 = param['PSCBE1'.swapcase()]
            self.PSCBE1given = True
        else:
            if self.PSCBE1given == False:
                self.PSCBE1 = 424000000.0
        if 'LPSCBE1' in param:
            self.LPSCBE1 = param['LPSCBE1']
            self.LPSCBE1given = True
        elif 'LPSCBE1'.swapcase() in param:
            self.LPSCBE1 = param['LPSCBE1'.swapcase()]
            self.LPSCBE1given = True
        else:
            if self.LPSCBE1given == False:
                self.LPSCBE1 = 0.0
        if 'WPSCBE1' in param:
            self.WPSCBE1 = param['WPSCBE1']
            self.WPSCBE1given = True
        elif 'WPSCBE1'.swapcase() in param:
            self.WPSCBE1 = param['WPSCBE1'.swapcase()]
            self.WPSCBE1given = True
        else:
            if self.WPSCBE1given == False:
                self.WPSCBE1 = 0.0
        if 'PPSCBE1' in param:
            self.PPSCBE1 = param['PPSCBE1']
            self.PPSCBE1given = True
        elif 'PPSCBE1'.swapcase() in param:
            self.PPSCBE1 = param['PPSCBE1'.swapcase()]
            self.PPSCBE1given = True
        else:
            if self.PPSCBE1given == False:
                self.PPSCBE1 = 0.0
        if 'PSCBE2' in param:
            self.PSCBE2 = param['PSCBE2']
            self.PSCBE2given = True
        elif 'PSCBE2'.swapcase() in param:
            self.PSCBE2 = param['PSCBE2'.swapcase()]
            self.PSCBE2given = True
        else:
            if self.PSCBE2given == False:
                self.PSCBE2 = 1e-08
        if 'LPSCBE2' in param:
            self.LPSCBE2 = param['LPSCBE2']
            self.LPSCBE2given = True
        elif 'LPSCBE2'.swapcase() in param:
            self.LPSCBE2 = param['LPSCBE2'.swapcase()]
            self.LPSCBE2given = True
        else:
            if self.LPSCBE2given == False:
                self.LPSCBE2 = 0.0
        if 'WPSCBE2' in param:
            self.WPSCBE2 = param['WPSCBE2']
            self.WPSCBE2given = True
        elif 'WPSCBE2'.swapcase() in param:
            self.WPSCBE2 = param['WPSCBE2'.swapcase()]
            self.WPSCBE2given = True
        else:
            if self.WPSCBE2given == False:
                self.WPSCBE2 = 0.0
        if 'PPSCBE2' in param:
            self.PPSCBE2 = param['PPSCBE2']
            self.PPSCBE2given = True
        elif 'PPSCBE2'.swapcase() in param:
            self.PPSCBE2 = param['PPSCBE2'.swapcase()]
            self.PPSCBE2given = True
        else:
            if self.PPSCBE2given == False:
                self.PPSCBE2 = 0.0
        if 'PDITS' in param:
            self.PDITS = param['PDITS']
            self.PDITSgiven = True
        elif 'PDITS'.swapcase() in param:
            self.PDITS = param['PDITS'.swapcase()]
            self.PDITSgiven = True
        else:
            if self.PDITSgiven == False:
                self.PDITS = 0.0
        if 'LPDITS' in param:
            self.LPDITS = param['LPDITS']
            self.LPDITSgiven = True
        elif 'LPDITS'.swapcase() in param:
            self.LPDITS = param['LPDITS'.swapcase()]
            self.LPDITSgiven = True
        else:
            if self.LPDITSgiven == False:
                self.LPDITS = 0.0
        if 'WPDITS' in param:
            self.WPDITS = param['WPDITS']
            self.WPDITSgiven = True
        elif 'WPDITS'.swapcase() in param:
            self.WPDITS = param['WPDITS'.swapcase()]
            self.WPDITSgiven = True
        else:
            if self.WPDITSgiven == False:
                self.WPDITS = 0.0
        if 'PPDITS' in param:
            self.PPDITS = param['PPDITS']
            self.PPDITSgiven = True
        elif 'PPDITS'.swapcase() in param:
            self.PPDITS = param['PPDITS'.swapcase()]
            self.PPDITSgiven = True
        else:
            if self.PPDITSgiven == False:
                self.PPDITS = 0.0
        if 'PDITSL' in param:
            self.PDITSL = param['PDITSL']
            self.PDITSLgiven = True
        elif 'PDITSL'.swapcase() in param:
            self.PDITSL = param['PDITSL'.swapcase()]
            self.PDITSLgiven = True
        else:
            if self.PDITSLgiven == False:
                self.PDITSL = 0.0
        if 'PDITSD' in param:
            self.PDITSD = param['PDITSD']
            self.PDITSDgiven = True
        elif 'PDITSD'.swapcase() in param:
            self.PDITSD = param['PDITSD'.swapcase()]
            self.PDITSDgiven = True
        else:
            if self.PDITSDgiven == False:
                self.PDITSD = 0.0
        if 'LPDITSD' in param:
            self.LPDITSD = param['LPDITSD']
            self.LPDITSDgiven = True
        elif 'LPDITSD'.swapcase() in param:
            self.LPDITSD = param['LPDITSD'.swapcase()]
            self.LPDITSDgiven = True
        else:
            if self.LPDITSDgiven == False:
                self.LPDITSD = 0.0
        if 'WPDITSD' in param:
            self.WPDITSD = param['WPDITSD']
            self.WPDITSDgiven = True
        elif 'WPDITSD'.swapcase() in param:
            self.WPDITSD = param['WPDITSD'.swapcase()]
            self.WPDITSDgiven = True
        else:
            if self.WPDITSDgiven == False:
                self.WPDITSD = 0.0
        if 'PPDITSD' in param:
            self.PPDITSD = param['PPDITSD']
            self.PPDITSDgiven = True
        elif 'PPDITSD'.swapcase() in param:
            self.PPDITSD = param['PPDITSD'.swapcase()]
            self.PPDITSDgiven = True
        else:
            if self.PPDITSDgiven == False:
                self.PPDITSD = 0.0
        if 'RSH' in param:
            self.RSH = param['RSH']
            self.RSHgiven = True
        elif 'RSH'.swapcase() in param:
            self.RSH = param['RSH'.swapcase()]
            self.RSHgiven = True
        else:
            if self.RSHgiven == False:
                self.RSH = 0.0
        if 'PRWG' in param:
            self.PRWG = param['PRWG']
            self.PRWGgiven = True
        elif 'PRWG'.swapcase() in param:
            self.PRWG = param['PRWG'.swapcase()]
            self.PRWGgiven = True
        else:
            if self.PRWGgiven == False:
                self.PRWG = 1.0
        if 'LPRWG' in param:
            self.LPRWG = param['LPRWG']
            self.LPRWGgiven = True
        elif 'LPRWG'.swapcase() in param:
            self.LPRWG = param['LPRWG'.swapcase()]
            self.LPRWGgiven = True
        else:
            if self.LPRWGgiven == False:
                self.LPRWG = 0.0
        if 'WPRWG' in param:
            self.WPRWG = param['WPRWG']
            self.WPRWGgiven = True
        elif 'WPRWG'.swapcase() in param:
            self.WPRWG = param['WPRWG'.swapcase()]
            self.WPRWGgiven = True
        else:
            if self.WPRWGgiven == False:
                self.WPRWG = 0.0
        if 'PPRWG' in param:
            self.PPRWG = param['PPRWG']
            self.PPRWGgiven = True
        elif 'PPRWG'.swapcase() in param:
            self.PPRWG = param['PPRWG'.swapcase()]
            self.PPRWGgiven = True
        else:
            if self.PPRWGgiven == False:
                self.PPRWG = 0.0
        if 'PRWB' in param:
            self.PRWB = param['PRWB']
            self.PRWBgiven = True
        elif 'PRWB'.swapcase() in param:
            self.PRWB = param['PRWB'.swapcase()]
            self.PRWBgiven = True
        else:
            if self.PRWBgiven == False:
                self.PRWB = 0.0
        if 'LPRWB' in param:
            self.LPRWB = param['LPRWB']
            self.LPRWBgiven = True
        elif 'LPRWB'.swapcase() in param:
            self.LPRWB = param['LPRWB'.swapcase()]
            self.LPRWBgiven = True
        else:
            if self.LPRWBgiven == False:
                self.LPRWB = 0.0
        if 'WPRWB' in param:
            self.WPRWB = param['WPRWB']
            self.WPRWBgiven = True
        elif 'WPRWB'.swapcase() in param:
            self.WPRWB = param['WPRWB'.swapcase()]
            self.WPRWBgiven = True
        else:
            if self.WPRWBgiven == False:
                self.WPRWB = 0.0
        if 'PPRWB' in param:
            self.PPRWB = param['PPRWB']
            self.PPRWBgiven = True
        elif 'PPRWB'.swapcase() in param:
            self.PPRWB = param['PPRWB'.swapcase()]
            self.PPRWBgiven = True
        else:
            if self.PPRWBgiven == False:
                self.PPRWB = 0.0
        if 'PRWBL' in param:
            self.PRWBL = param['PRWBL']
            self.PRWBLgiven = True
        elif 'PRWBL'.swapcase() in param:
            self.PRWBL = param['PRWBL'.swapcase()]
            self.PRWBLgiven = True
        else:
            if self.PRWBLgiven == False:
                self.PRWBL = 0.0
        if 'PRWBLEXP' in param:
            self.PRWBLEXP = param['PRWBLEXP']
            self.PRWBLEXPgiven = True
        elif 'PRWBLEXP'.swapcase() in param:
            self.PRWBLEXP = param['PRWBLEXP'.swapcase()]
            self.PRWBLEXPgiven = True
        else:
            if self.PRWBLEXPgiven == False:
                self.PRWBLEXP = 1.0
        if 'WR' in param:
            self.WR = param['WR']
            self.WRgiven = True
        elif 'WR'.swapcase() in param:
            self.WR = param['WR'.swapcase()]
            self.WRgiven = True
        else:
            if self.WRgiven == False:
                self.WR = 1.0
        if 'LWR' in param:
            self.LWR = param['LWR']
            self.LWRgiven = True
        elif 'LWR'.swapcase() in param:
            self.LWR = param['LWR'.swapcase()]
            self.LWRgiven = True
        else:
            if self.LWRgiven == False:
                self.LWR = 0.0
        if 'WWR' in param:
            self.WWR = param['WWR']
            self.WWRgiven = True
        elif 'WWR'.swapcase() in param:
            self.WWR = param['WWR'.swapcase()]
            self.WWRgiven = True
        else:
            if self.WWRgiven == False:
                self.WWR = 0.0
        if 'PWR' in param:
            self.PWR = param['PWR']
            self.PWRgiven = True
        elif 'PWR'.swapcase() in param:
            self.PWR = param['PWR'.swapcase()]
            self.PWRgiven = True
        else:
            if self.PWRgiven == False:
                self.PWR = 0.0
        if 'RSWMIN' in param:
            self.RSWMIN = param['RSWMIN']
            self.RSWMINgiven = True
        elif 'RSWMIN'.swapcase() in param:
            self.RSWMIN = param['RSWMIN'.swapcase()]
            self.RSWMINgiven = True
        else:
            if self.RSWMINgiven == False:
                self.RSWMIN = 0.0
        if 'LRSWMIN' in param:
            self.LRSWMIN = param['LRSWMIN']
            self.LRSWMINgiven = True
        elif 'LRSWMIN'.swapcase() in param:
            self.LRSWMIN = param['LRSWMIN'.swapcase()]
            self.LRSWMINgiven = True
        else:
            if self.LRSWMINgiven == False:
                self.LRSWMIN = 0.0
        if 'WRSWMIN' in param:
            self.WRSWMIN = param['WRSWMIN']
            self.WRSWMINgiven = True
        elif 'WRSWMIN'.swapcase() in param:
            self.WRSWMIN = param['WRSWMIN'.swapcase()]
            self.WRSWMINgiven = True
        else:
            if self.WRSWMINgiven == False:
                self.WRSWMIN = 0.0
        if 'PRSWMIN' in param:
            self.PRSWMIN = param['PRSWMIN']
            self.PRSWMINgiven = True
        elif 'PRSWMIN'.swapcase() in param:
            self.PRSWMIN = param['PRSWMIN'.swapcase()]
            self.PRSWMINgiven = True
        else:
            if self.PRSWMINgiven == False:
                self.PRSWMIN = 0.0
        if 'RSW' in param:
            self.RSW = param['RSW']
            self.RSWgiven = True
        elif 'RSW'.swapcase() in param:
            self.RSW = param['RSW'.swapcase()]
            self.RSWgiven = True
        else:
            if self.RSWgiven == False:
                self.RSW = 10.0
        if 'LRSW' in param:
            self.LRSW = param['LRSW']
            self.LRSWgiven = True
        elif 'LRSW'.swapcase() in param:
            self.LRSW = param['LRSW'.swapcase()]
            self.LRSWgiven = True
        else:
            if self.LRSWgiven == False:
                self.LRSW = 0.0
        if 'WRSW' in param:
            self.WRSW = param['WRSW']
            self.WRSWgiven = True
        elif 'WRSW'.swapcase() in param:
            self.WRSW = param['WRSW'.swapcase()]
            self.WRSWgiven = True
        else:
            if self.WRSWgiven == False:
                self.WRSW = 0.0
        if 'PRSW' in param:
            self.PRSW = param['PRSW']
            self.PRSWgiven = True
        elif 'PRSW'.swapcase() in param:
            self.PRSW = param['PRSW'.swapcase()]
            self.PRSWgiven = True
        else:
            if self.PRSWgiven == False:
                self.PRSW = 0.0
        if 'RSWL' in param:
            self.RSWL = param['RSWL']
            self.RSWLgiven = True
        elif 'RSWL'.swapcase() in param:
            self.RSWL = param['RSWL'.swapcase()]
            self.RSWLgiven = True
        else:
            if self.RSWLgiven == False:
                self.RSWL = 0.0
        if 'RSWLEXP' in param:
            self.RSWLEXP = param['RSWLEXP']
            self.RSWLEXPgiven = True
        elif 'RSWLEXP'.swapcase() in param:
            self.RSWLEXP = param['RSWLEXP'.swapcase()]
            self.RSWLEXPgiven = True
        else:
            if self.RSWLEXPgiven == False:
                self.RSWLEXP = 1.0
        if 'RDWMIN' in param:
            self.RDWMIN = param['RDWMIN']
            self.RDWMINgiven = True
        elif 'RDWMIN'.swapcase() in param:
            self.RDWMIN = param['RDWMIN'.swapcase()]
            self.RDWMINgiven = True
        else:
            if self.RDWMINgiven == False:
                self.RDWMIN = self.RSWMIN
        if 'LRDWMIN' in param:
            self.LRDWMIN = param['LRDWMIN']
            self.LRDWMINgiven = True
        elif 'LRDWMIN'.swapcase() in param:
            self.LRDWMIN = param['LRDWMIN'.swapcase()]
            self.LRDWMINgiven = True
        else:
            if self.LRDWMINgiven == False:
                self.LRDWMIN = self.LRSWMIN
        if 'WRDWMIN' in param:
            self.WRDWMIN = param['WRDWMIN']
            self.WRDWMINgiven = True
        elif 'WRDWMIN'.swapcase() in param:
            self.WRDWMIN = param['WRDWMIN'.swapcase()]
            self.WRDWMINgiven = True
        else:
            if self.WRDWMINgiven == False:
                self.WRDWMIN = self.WRSWMIN
        if 'PRDWMIN' in param:
            self.PRDWMIN = param['PRDWMIN']
            self.PRDWMINgiven = True
        elif 'PRDWMIN'.swapcase() in param:
            self.PRDWMIN = param['PRDWMIN'.swapcase()]
            self.PRDWMINgiven = True
        else:
            if self.PRDWMINgiven == False:
                self.PRDWMIN = self.PRSWMIN
        if 'RDW' in param:
            self.RDW = param['RDW']
            self.RDWgiven = True
        elif 'RDW'.swapcase() in param:
            self.RDW = param['RDW'.swapcase()]
            self.RDWgiven = True
        else:
            if self.RDWgiven == False:
                self.RDW = self.RSW
        if 'LRDW' in param:
            self.LRDW = param['LRDW']
            self.LRDWgiven = True
        elif 'LRDW'.swapcase() in param:
            self.LRDW = param['LRDW'.swapcase()]
            self.LRDWgiven = True
        else:
            if self.LRDWgiven == False:
                self.LRDW = self.LRSW
        if 'WRDW' in param:
            self.WRDW = param['WRDW']
            self.WRDWgiven = True
        elif 'WRDW'.swapcase() in param:
            self.WRDW = param['WRDW'.swapcase()]
            self.WRDWgiven = True
        else:
            if self.WRDWgiven == False:
                self.WRDW = self.WRSW
        if 'PRDW' in param:
            self.PRDW = param['PRDW']
            self.PRDWgiven = True
        elif 'PRDW'.swapcase() in param:
            self.PRDW = param['PRDW'.swapcase()]
            self.PRDWgiven = True
        else:
            if self.PRDWgiven == False:
                self.PRDW = self.PRSW
        if 'RDWL' in param:
            self.RDWL = param['RDWL']
            self.RDWLgiven = True
        elif 'RDWL'.swapcase() in param:
            self.RDWL = param['RDWL'.swapcase()]
            self.RDWLgiven = True
        else:
            if self.RDWLgiven == False:
                self.RDWL = self.RSWL
        if 'RDWLEXP' in param:
            self.RDWLEXP = param['RDWLEXP']
            self.RDWLEXPgiven = True
        elif 'RDWLEXP'.swapcase() in param:
            self.RDWLEXP = param['RDWLEXP'.swapcase()]
            self.RDWLEXPgiven = True
        else:
            if self.RDWLEXPgiven == False:
                self.RDWLEXP = self.RSWLEXP
        if 'RDSWMIN' in param:
            self.RDSWMIN = param['RDSWMIN']
            self.RDSWMINgiven = True
        elif 'RDSWMIN'.swapcase() in param:
            self.RDSWMIN = param['RDSWMIN'.swapcase()]
            self.RDSWMINgiven = True
        else:
            if self.RDSWMINgiven == False:
                self.RDSWMIN = 0.0
        if 'LRDSWMIN' in param:
            self.LRDSWMIN = param['LRDSWMIN']
            self.LRDSWMINgiven = True
        elif 'LRDSWMIN'.swapcase() in param:
            self.LRDSWMIN = param['LRDSWMIN'.swapcase()]
            self.LRDSWMINgiven = True
        else:
            if self.LRDSWMINgiven == False:
                self.LRDSWMIN = 0.0
        if 'WRDSWMIN' in param:
            self.WRDSWMIN = param['WRDSWMIN']
            self.WRDSWMINgiven = True
        elif 'WRDSWMIN'.swapcase() in param:
            self.WRDSWMIN = param['WRDSWMIN'.swapcase()]
            self.WRDSWMINgiven = True
        else:
            if self.WRDSWMINgiven == False:
                self.WRDSWMIN = 0.0
        if 'PRDSWMIN' in param:
            self.PRDSWMIN = param['PRDSWMIN']
            self.PRDSWMINgiven = True
        elif 'PRDSWMIN'.swapcase() in param:
            self.PRDSWMIN = param['PRDSWMIN'.swapcase()]
            self.PRDSWMINgiven = True
        else:
            if self.PRDSWMINgiven == False:
                self.PRDSWMIN = 0.0
        if 'RDSW' in param:
            self.RDSW = param['RDSW']
            self.RDSWgiven = True
        elif 'RDSW'.swapcase() in param:
            self.RDSW = param['RDSW'.swapcase()]
            self.RDSWgiven = True
        else:
            if self.RDSWgiven == False:
                self.RDSW = 20.0
        if 'RDSWL' in param:
            self.RDSWL = param['RDSWL']
            self.RDSWLgiven = True
        elif 'RDSWL'.swapcase() in param:
            self.RDSWL = param['RDSWL'.swapcase()]
            self.RDSWLgiven = True
        else:
            if self.RDSWLgiven == False:
                self.RDSWL = 0.0
        if 'RDSWLEXP' in param:
            self.RDSWLEXP = param['RDSWLEXP']
            self.RDSWLEXPgiven = True
        elif 'RDSWLEXP'.swapcase() in param:
            self.RDSWLEXP = param['RDSWLEXP'.swapcase()]
            self.RDSWLEXPgiven = True
        else:
            if self.RDSWLEXPgiven == False:
                self.RDSWLEXP = 1.0
        if 'LRDSW' in param:
            self.LRDSW = param['LRDSW']
            self.LRDSWgiven = True
        elif 'LRDSW'.swapcase() in param:
            self.LRDSW = param['LRDSW'.swapcase()]
            self.LRDSWgiven = True
        else:
            if self.LRDSWgiven == False:
                self.LRDSW = 0.0
        if 'WRDSW' in param:
            self.WRDSW = param['WRDSW']
            self.WRDSWgiven = True
        elif 'WRDSW'.swapcase() in param:
            self.WRDSW = param['WRDSW'.swapcase()]
            self.WRDSWgiven = True
        else:
            if self.WRDSWgiven == False:
                self.WRDSW = 0.0
        if 'PRDSW' in param:
            self.PRDSW = param['PRDSW']
            self.PRDSWgiven = True
        elif 'PRDSW'.swapcase() in param:
            self.PRDSW = param['PRDSW'.swapcase()]
            self.PRDSWgiven = True
        else:
            if self.PRDSWgiven == False:
                self.PRDSW = 0.0
        if 'PSAT' in param:
            self.PSAT = param['PSAT']
            self.PSATgiven = True
        elif 'PSAT'.swapcase() in param:
            self.PSAT = param['PSAT'.swapcase()]
            self.PSATgiven = True
        else:
            if self.PSATgiven == False:
                self.PSAT = 1.0
        if 'LPSAT' in param:
            self.LPSAT = param['LPSAT']
            self.LPSATgiven = True
        elif 'LPSAT'.swapcase() in param:
            self.LPSAT = param['LPSAT'.swapcase()]
            self.LPSATgiven = True
        else:
            if self.LPSATgiven == False:
                self.LPSAT = 0.0
        if 'WPSAT' in param:
            self.WPSAT = param['WPSAT']
            self.WPSATgiven = True
        elif 'WPSAT'.swapcase() in param:
            self.WPSAT = param['WPSAT'.swapcase()]
            self.WPSATgiven = True
        else:
            if self.WPSATgiven == False:
                self.WPSAT = 0.0
        if 'PPSAT' in param:
            self.PPSAT = param['PPSAT']
            self.PPSATgiven = True
        elif 'PPSAT'.swapcase() in param:
            self.PPSAT = param['PPSAT'.swapcase()]
            self.PPSATgiven = True
        else:
            if self.PPSATgiven == False:
                self.PPSAT = 0.0
        if 'PSATL' in param:
            self.PSATL = param['PSATL']
            self.PSATLgiven = True
        elif 'PSATL'.swapcase() in param:
            self.PSATL = param['PSATL'.swapcase()]
            self.PSATLgiven = True
        else:
            if self.PSATLgiven == False:
                self.PSATL = 0.0
        if 'PSATLEXP' in param:
            self.PSATLEXP = param['PSATLEXP']
            self.PSATLEXPgiven = True
        elif 'PSATLEXP'.swapcase() in param:
            self.PSATLEXP = param['PSATLEXP'.swapcase()]
            self.PSATLEXPgiven = True
        else:
            if self.PSATLEXPgiven == False:
                self.PSATLEXP = 1.0
        if 'PSATB' in param:
            self.PSATB = param['PSATB']
            self.PSATBgiven = True
        elif 'PSATB'.swapcase() in param:
            self.PSATB = param['PSATB'.swapcase()]
            self.PSATBgiven = True
        else:
            if self.PSATBgiven == False:
                self.PSATB = 0.0
        if 'PSATR' in param:
            self.PSATR = param['PSATR']
            self.PSATRgiven = True
        elif 'PSATR'.swapcase() in param:
            self.PSATR = param['PSATR'.swapcase()]
            self.PSATRgiven = True
        else:
            if self.PSATRgiven == False:
                self.PSATR = self.PSAT
        if 'LPSATR' in param:
            self.LPSATR = param['LPSATR']
            self.LPSATRgiven = True
        elif 'LPSATR'.swapcase() in param:
            self.LPSATR = param['LPSATR'.swapcase()]
            self.LPSATRgiven = True
        else:
            if self.LPSATRgiven == False:
                self.LPSATR = self.LPSAT
        if 'WPSATR' in param:
            self.WPSATR = param['WPSATR']
            self.WPSATRgiven = True
        elif 'WPSATR'.swapcase() in param:
            self.WPSATR = param['WPSATR'.swapcase()]
            self.WPSATRgiven = True
        else:
            if self.WPSATRgiven == False:
                self.WPSATR = self.WPSAT
        if 'PPSATR' in param:
            self.PPSATR = param['PPSATR']
            self.PPSATRgiven = True
        elif 'PPSATR'.swapcase() in param:
            self.PPSATR = param['PPSATR'.swapcase()]
            self.PPSATRgiven = True
        else:
            if self.PPSATRgiven == False:
                self.PPSATR = self.PPSAT
        if 'LPSATB' in param:
            self.LPSATB = param['LPSATB']
            self.LPSATBgiven = True
        elif 'LPSATB'.swapcase() in param:
            self.LPSATB = param['LPSATB'.swapcase()]
            self.LPSATBgiven = True
        else:
            if self.LPSATBgiven == False:
                self.LPSATB = 0.0
        if 'WPSATB' in param:
            self.WPSATB = param['WPSATB']
            self.WPSATBgiven = True
        elif 'WPSATB'.swapcase() in param:
            self.WPSATB = param['WPSATB'.swapcase()]
            self.WPSATBgiven = True
        else:
            if self.WPSATBgiven == False:
                self.WPSATB = 0.0
        if 'PPSATB' in param:
            self.PPSATB = param['PPSATB']
            self.PPSATBgiven = True
        elif 'PPSATB'.swapcase() in param:
            self.PPSATB = param['PPSATB'.swapcase()]
            self.PPSATBgiven = True
        else:
            if self.PPSATBgiven == False:
                self.PPSATB = 0.0
        if 'PSATX' in param:
            self.PSATX = param['PSATX']
            self.PSATXgiven = True
        elif 'PSATX'.swapcase() in param:
            self.PSATX = param['PSATX'.swapcase()]
            self.PSATXgiven = True
        else:
            if self.PSATXgiven == False:
                self.PSATX = 1.0
        if 'PTWG' in param:
            self.PTWG = param['PTWG']
            self.PTWGgiven = True
        elif 'PTWG'.swapcase() in param:
            self.PTWG = param['PTWG'.swapcase()]
            self.PTWGgiven = True
        else:
            if self.PTWGgiven == False:
                self.PTWG = 0.0
        if 'LPTWG' in param:
            self.LPTWG = param['LPTWG']
            self.LPTWGgiven = True
        elif 'LPTWG'.swapcase() in param:
            self.LPTWG = param['LPTWG'.swapcase()]
            self.LPTWGgiven = True
        else:
            if self.LPTWGgiven == False:
                self.LPTWG = 0.0
        if 'WPTWG' in param:
            self.WPTWG = param['WPTWG']
            self.WPTWGgiven = True
        elif 'WPTWG'.swapcase() in param:
            self.WPTWG = param['WPTWG'.swapcase()]
            self.WPTWGgiven = True
        else:
            if self.WPTWGgiven == False:
                self.WPTWG = 0.0
        if 'PPTWG' in param:
            self.PPTWG = param['PPTWG']
            self.PPTWGgiven = True
        elif 'PPTWG'.swapcase() in param:
            self.PPTWG = param['PPTWG'.swapcase()]
            self.PPTWGgiven = True
        else:
            if self.PPTWGgiven == False:
                self.PPTWG = 0.0
        if 'PTWGL' in param:
            self.PTWGL = param['PTWGL']
            self.PTWGLgiven = True
        elif 'PTWGL'.swapcase() in param:
            self.PTWGL = param['PTWGL'.swapcase()]
            self.PTWGLgiven = True
        else:
            if self.PTWGLgiven == False:
                self.PTWGL = 0.0
        if 'PTWGLEXP' in param:
            self.PTWGLEXP = param['PTWGLEXP']
            self.PTWGLEXPgiven = True
        elif 'PTWGLEXP'.swapcase() in param:
            self.PTWGLEXP = param['PTWGLEXP'.swapcase()]
            self.PTWGLEXPgiven = True
        else:
            if self.PTWGLEXPgiven == False:
                self.PTWGLEXP = 1.0
        if 'PTWGR' in param:
            self.PTWGR = param['PTWGR']
            self.PTWGRgiven = True
        elif 'PTWGR'.swapcase() in param:
            self.PTWGR = param['PTWGR'.swapcase()]
            self.PTWGRgiven = True
        else:
            if self.PTWGRgiven == False:
                self.PTWGR = self.PTWG
        if 'LPTWGR' in param:
            self.LPTWGR = param['LPTWGR']
            self.LPTWGRgiven = True
        elif 'LPTWGR'.swapcase() in param:
            self.LPTWGR = param['LPTWGR'.swapcase()]
            self.LPTWGRgiven = True
        else:
            if self.LPTWGRgiven == False:
                self.LPTWGR = self.LPTWG
        if 'WPTWGR' in param:
            self.WPTWGR = param['WPTWGR']
            self.WPTWGRgiven = True
        elif 'WPTWGR'.swapcase() in param:
            self.WPTWGR = param['WPTWGR'.swapcase()]
            self.WPTWGRgiven = True
        else:
            if self.WPTWGRgiven == False:
                self.WPTWGR = self.WPTWG
        if 'PPTWGR' in param:
            self.PPTWGR = param['PPTWGR']
            self.PPTWGRgiven = True
        elif 'PPTWGR'.swapcase() in param:
            self.PPTWGR = param['PPTWGR'.swapcase()]
            self.PPTWGRgiven = True
        else:
            if self.PPTWGRgiven == False:
                self.PPTWGR = self.PPTWG
        if 'PTWGLR' in param:
            self.PTWGLR = param['PTWGLR']
            self.PTWGLRgiven = True
        elif 'PTWGLR'.swapcase() in param:
            self.PTWGLR = param['PTWGLR'.swapcase()]
            self.PTWGLRgiven = True
        else:
            if self.PTWGLRgiven == False:
                self.PTWGLR = self.PTWGL
        if 'PTWGLEXPR' in param:
            self.PTWGLEXPR = param['PTWGLEXPR']
            self.PTWGLEXPRgiven = True
        elif 'PTWGLEXPR'.swapcase() in param:
            self.PTWGLEXPR = param['PTWGLEXPR'.swapcase()]
            self.PTWGLEXPRgiven = True
        else:
            if self.PTWGLEXPRgiven == False:
                self.PTWGLEXPR = self.PTWGLEXP
        if 'A1' in param:
            self.A1 = param['A1']
            self.A1given = True
        elif 'A1'.swapcase() in param:
            self.A1 = param['A1'.swapcase()]
            self.A1given = True
        else:
            if self.A1given == False:
                self.A1 = 0.0
        if 'LA1' in param:
            self.LA1 = param['LA1']
            self.LA1given = True
        elif 'LA1'.swapcase() in param:
            self.LA1 = param['LA1'.swapcase()]
            self.LA1given = True
        else:
            if self.LA1given == False:
                self.LA1 = 0.0
        if 'WA1' in param:
            self.WA1 = param['WA1']
            self.WA1given = True
        elif 'WA1'.swapcase() in param:
            self.WA1 = param['WA1'.swapcase()]
            self.WA1given = True
        else:
            if self.WA1given == False:
                self.WA1 = 0.0
        if 'PA1' in param:
            self.PA1 = param['PA1']
            self.PA1given = True
        elif 'PA1'.swapcase() in param:
            self.PA1 = param['PA1'.swapcase()]
            self.PA1given = True
        else:
            if self.PA1given == False:
                self.PA1 = 0.0
        if 'A11' in param:
            self.A11 = param['A11']
            self.A11given = True
        elif 'A11'.swapcase() in param:
            self.A11 = param['A11'.swapcase()]
            self.A11given = True
        else:
            if self.A11given == False:
                self.A11 = 0.0
        if 'LA11' in param:
            self.LA11 = param['LA11']
            self.LA11given = True
        elif 'LA11'.swapcase() in param:
            self.LA11 = param['LA11'.swapcase()]
            self.LA11given = True
        else:
            if self.LA11given == False:
                self.LA11 = 0.0
        if 'WA11' in param:
            self.WA11 = param['WA11']
            self.WA11given = True
        elif 'WA11'.swapcase() in param:
            self.WA11 = param['WA11'.swapcase()]
            self.WA11given = True
        else:
            if self.WA11given == False:
                self.WA11 = 0.0
        if 'PA11' in param:
            self.PA11 = param['PA11']
            self.PA11given = True
        elif 'PA11'.swapcase() in param:
            self.PA11 = param['PA11'.swapcase()]
            self.PA11given = True
        else:
            if self.PA11given == False:
                self.PA11 = 0.0
        if 'A2' in param:
            self.A2 = param['A2']
            self.A2given = True
        elif 'A2'.swapcase() in param:
            self.A2 = param['A2'.swapcase()]
            self.A2given = True
        else:
            if self.A2given == False:
                self.A2 = 0.0
        if 'LA2' in param:
            self.LA2 = param['LA2']
            self.LA2given = True
        elif 'LA2'.swapcase() in param:
            self.LA2 = param['LA2'.swapcase()]
            self.LA2given = True
        else:
            if self.LA2given == False:
                self.LA2 = 0.0
        if 'WA2' in param:
            self.WA2 = param['WA2']
            self.WA2given = True
        elif 'WA2'.swapcase() in param:
            self.WA2 = param['WA2'.swapcase()]
            self.WA2given = True
        else:
            if self.WA2given == False:
                self.WA2 = 0.0
        if 'PA2' in param:
            self.PA2 = param['PA2']
            self.PA2given = True
        elif 'PA2'.swapcase() in param:
            self.PA2 = param['PA2'.swapcase()]
            self.PA2given = True
        else:
            if self.PA2given == False:
                self.PA2 = 0.0
        if 'A21' in param:
            self.A21 = param['A21']
            self.A21given = True
        elif 'A21'.swapcase() in param:
            self.A21 = param['A21'.swapcase()]
            self.A21given = True
        else:
            if self.A21given == False:
                self.A21 = 0.0
        if 'LA21' in param:
            self.LA21 = param['LA21']
            self.LA21given = True
        elif 'LA21'.swapcase() in param:
            self.LA21 = param['LA21'.swapcase()]
            self.LA21given = True
        else:
            if self.LA21given == False:
                self.LA21 = 0.0
        if 'WA21' in param:
            self.WA21 = param['WA21']
            self.WA21given = True
        elif 'WA21'.swapcase() in param:
            self.WA21 = param['WA21'.swapcase()]
            self.WA21given = True
        else:
            if self.WA21given == False:
                self.WA21 = 0.0
        if 'PA21' in param:
            self.PA21 = param['PA21']
            self.PA21given = True
        elif 'PA21'.swapcase() in param:
            self.PA21 = param['PA21'.swapcase()]
            self.PA21given = True
        else:
            if self.PA21given == False:
                self.PA21 = 0.0
        if 'PDIBLC' in param:
            self.PDIBLC = param['PDIBLC']
            self.PDIBLCgiven = True
        elif 'PDIBLC'.swapcase() in param:
            self.PDIBLC = param['PDIBLC'.swapcase()]
            self.PDIBLCgiven = True
        else:
            if self.PDIBLCgiven == False:
                self.PDIBLC = 0.0
        if 'PDIBLCL' in param:
            self.PDIBLCL = param['PDIBLCL']
            self.PDIBLCLgiven = True
        elif 'PDIBLCL'.swapcase() in param:
            self.PDIBLCL = param['PDIBLCL'.swapcase()]
            self.PDIBLCLgiven = True
        else:
            if self.PDIBLCLgiven == False:
                self.PDIBLCL = 0.0
        if 'PDIBLCLEXP' in param:
            self.PDIBLCLEXP = param['PDIBLCLEXP']
            self.PDIBLCLEXPgiven = True
        elif 'PDIBLCLEXP'.swapcase() in param:
            self.PDIBLCLEXP = param['PDIBLCLEXP'.swapcase()]
            self.PDIBLCLEXPgiven = True
        else:
            if self.PDIBLCLEXPgiven == False:
                self.PDIBLCLEXP = 1.0
        if 'LPDIBLC' in param:
            self.LPDIBLC = param['LPDIBLC']
            self.LPDIBLCgiven = True
        elif 'LPDIBLC'.swapcase() in param:
            self.LPDIBLC = param['LPDIBLC'.swapcase()]
            self.LPDIBLCgiven = True
        else:
            if self.LPDIBLCgiven == False:
                self.LPDIBLC = 0.0
        if 'WPDIBLC' in param:
            self.WPDIBLC = param['WPDIBLC']
            self.WPDIBLCgiven = True
        elif 'WPDIBLC'.swapcase() in param:
            self.WPDIBLC = param['WPDIBLC'.swapcase()]
            self.WPDIBLCgiven = True
        else:
            if self.WPDIBLCgiven == False:
                self.WPDIBLC = 0.0
        if 'PPDIBLC' in param:
            self.PPDIBLC = param['PPDIBLC']
            self.PPDIBLCgiven = True
        elif 'PPDIBLC'.swapcase() in param:
            self.PPDIBLC = param['PPDIBLC'.swapcase()]
            self.PPDIBLCgiven = True
        else:
            if self.PPDIBLCgiven == False:
                self.PPDIBLC = 0.0
        if 'PDIBLCR' in param:
            self.PDIBLCR = param['PDIBLCR']
            self.PDIBLCRgiven = True
        elif 'PDIBLCR'.swapcase() in param:
            self.PDIBLCR = param['PDIBLCR'.swapcase()]
            self.PDIBLCRgiven = True
        else:
            if self.PDIBLCRgiven == False:
                self.PDIBLCR = self.PDIBLC
        if 'PDIBLCLR' in param:
            self.PDIBLCLR = param['PDIBLCLR']
            self.PDIBLCLRgiven = True
        elif 'PDIBLCLR'.swapcase() in param:
            self.PDIBLCLR = param['PDIBLCLR'.swapcase()]
            self.PDIBLCLRgiven = True
        else:
            if self.PDIBLCLRgiven == False:
                self.PDIBLCLR = self.PDIBLCL
        if 'PDIBLCLEXPR' in param:
            self.PDIBLCLEXPR = param['PDIBLCLEXPR']
            self.PDIBLCLEXPRgiven = True
        elif 'PDIBLCLEXPR'.swapcase() in param:
            self.PDIBLCLEXPR = param['PDIBLCLEXPR'.swapcase()]
            self.PDIBLCLEXPRgiven = True
        else:
            if self.PDIBLCLEXPRgiven == False:
                self.PDIBLCLEXPR = self.PDIBLCLEXP
        if 'LPDIBLCR' in param:
            self.LPDIBLCR = param['LPDIBLCR']
            self.LPDIBLCRgiven = True
        elif 'LPDIBLCR'.swapcase() in param:
            self.LPDIBLCR = param['LPDIBLCR'.swapcase()]
            self.LPDIBLCRgiven = True
        else:
            if self.LPDIBLCRgiven == False:
                self.LPDIBLCR = self.LPDIBLC
        if 'WPDIBLCR' in param:
            self.WPDIBLCR = param['WPDIBLCR']
            self.WPDIBLCRgiven = True
        elif 'WPDIBLCR'.swapcase() in param:
            self.WPDIBLCR = param['WPDIBLCR'.swapcase()]
            self.WPDIBLCRgiven = True
        else:
            if self.WPDIBLCRgiven == False:
                self.WPDIBLCR = self.WPDIBLC
        if 'PPDIBLCR' in param:
            self.PPDIBLCR = param['PPDIBLCR']
            self.PPDIBLCRgiven = True
        elif 'PPDIBLCR'.swapcase() in param:
            self.PPDIBLCR = param['PPDIBLCR'.swapcase()]
            self.PPDIBLCRgiven = True
        else:
            if self.PPDIBLCRgiven == False:
                self.PPDIBLCR = self.PPDIBLC
        if 'PDIBLCB' in param:
            self.PDIBLCB = param['PDIBLCB']
            self.PDIBLCBgiven = True
        elif 'PDIBLCB'.swapcase() in param:
            self.PDIBLCB = param['PDIBLCB'.swapcase()]
            self.PDIBLCBgiven = True
        else:
            if self.PDIBLCBgiven == False:
                self.PDIBLCB = 0.0
        if 'LPDIBLCB' in param:
            self.LPDIBLCB = param['LPDIBLCB']
            self.LPDIBLCBgiven = True
        elif 'LPDIBLCB'.swapcase() in param:
            self.LPDIBLCB = param['LPDIBLCB'.swapcase()]
            self.LPDIBLCBgiven = True
        else:
            if self.LPDIBLCBgiven == False:
                self.LPDIBLCB = 0.0
        if 'WPDIBLCB' in param:
            self.WPDIBLCB = param['WPDIBLCB']
            self.WPDIBLCBgiven = True
        elif 'WPDIBLCB'.swapcase() in param:
            self.WPDIBLCB = param['WPDIBLCB'.swapcase()]
            self.WPDIBLCBgiven = True
        else:
            if self.WPDIBLCBgiven == False:
                self.WPDIBLCB = 0.0
        if 'PPDIBLCB' in param:
            self.PPDIBLCB = param['PPDIBLCB']
            self.PPDIBLCBgiven = True
        elif 'PPDIBLCB'.swapcase() in param:
            self.PPDIBLCB = param['PPDIBLCB'.swapcase()]
            self.PPDIBLCBgiven = True
        else:
            if self.PPDIBLCBgiven == False:
                self.PPDIBLCB = 0.0
        if 'PVAG' in param:
            self.PVAG = param['PVAG']
            self.PVAGgiven = True
        elif 'PVAG'.swapcase() in param:
            self.PVAG = param['PVAG'.swapcase()]
            self.PVAGgiven = True
        else:
            if self.PVAGgiven == False:
                self.PVAG = 1.0
        if 'LPVAG' in param:
            self.LPVAG = param['LPVAG']
            self.LPVAGgiven = True
        elif 'LPVAG'.swapcase() in param:
            self.LPVAG = param['LPVAG'.swapcase()]
            self.LPVAGgiven = True
        else:
            if self.LPVAGgiven == False:
                self.LPVAG = 0.0
        if 'WPVAG' in param:
            self.WPVAG = param['WPVAG']
            self.WPVAGgiven = True
        elif 'WPVAG'.swapcase() in param:
            self.WPVAG = param['WPVAG'.swapcase()]
            self.WPVAGgiven = True
        else:
            if self.WPVAGgiven == False:
                self.WPVAG = 0.0
        if 'PPVAG' in param:
            self.PPVAG = param['PPVAG']
            self.PPVAGgiven = True
        elif 'PPVAG'.swapcase() in param:
            self.PPVAG = param['PPVAG'.swapcase()]
            self.PPVAGgiven = True
        else:
            if self.PPVAGgiven == False:
                self.PPVAG = 0.0
        if 'FPROUT' in param:
            self.FPROUT = param['FPROUT']
            self.FPROUTgiven = True
        elif 'FPROUT'.swapcase() in param:
            self.FPROUT = param['FPROUT'.swapcase()]
            self.FPROUTgiven = True
        else:
            if self.FPROUTgiven == False:
                self.FPROUT = 0.0
        if 'FPROUTL' in param:
            self.FPROUTL = param['FPROUTL']
            self.FPROUTLgiven = True
        elif 'FPROUTL'.swapcase() in param:
            self.FPROUTL = param['FPROUTL'.swapcase()]
            self.FPROUTLgiven = True
        else:
            if self.FPROUTLgiven == False:
                self.FPROUTL = 0.0
        if 'FPROUTLEXP' in param:
            self.FPROUTLEXP = param['FPROUTLEXP']
            self.FPROUTLEXPgiven = True
        elif 'FPROUTLEXP'.swapcase() in param:
            self.FPROUTLEXP = param['FPROUTLEXP'.swapcase()]
            self.FPROUTLEXPgiven = True
        else:
            if self.FPROUTLEXPgiven == False:
                self.FPROUTLEXP = 1.0
        if 'LFPROUT' in param:
            self.LFPROUT = param['LFPROUT']
            self.LFPROUTgiven = True
        elif 'LFPROUT'.swapcase() in param:
            self.LFPROUT = param['LFPROUT'.swapcase()]
            self.LFPROUTgiven = True
        else:
            if self.LFPROUTgiven == False:
                self.LFPROUT = 0.0
        if 'WFPROUT' in param:
            self.WFPROUT = param['WFPROUT']
            self.WFPROUTgiven = True
        elif 'WFPROUT'.swapcase() in param:
            self.WFPROUT = param['WFPROUT'.swapcase()]
            self.WFPROUTgiven = True
        else:
            if self.WFPROUTgiven == False:
                self.WFPROUT = 0.0
        if 'PFPROUT' in param:
            self.PFPROUT = param['PFPROUT']
            self.PFPROUTgiven = True
        elif 'PFPROUT'.swapcase() in param:
            self.PFPROUT = param['PFPROUT'.swapcase()]
            self.PFPROUTgiven = True
        else:
            if self.PFPROUTgiven == False:
                self.PFPROUT = 0.0
        if 'ALPHA0' in param:
            self.ALPHA0 = param['ALPHA0']
            self.ALPHA0given = True
        elif 'ALPHA0'.swapcase() in param:
            self.ALPHA0 = param['ALPHA0'.swapcase()]
            self.ALPHA0given = True
        else:
            if self.ALPHA0given == False:
                self.ALPHA0 = 0.0
        if 'ALPHA0L' in param:
            self.ALPHA0L = param['ALPHA0L']
            self.ALPHA0Lgiven = True
        elif 'ALPHA0L'.swapcase() in param:
            self.ALPHA0L = param['ALPHA0L'.swapcase()]
            self.ALPHA0Lgiven = True
        else:
            if self.ALPHA0Lgiven == False:
                self.ALPHA0L = 0.0
        if 'ALPHA0LEXP' in param:
            self.ALPHA0LEXP = param['ALPHA0LEXP']
            self.ALPHA0LEXPgiven = True
        elif 'ALPHA0LEXP'.swapcase() in param:
            self.ALPHA0LEXP = param['ALPHA0LEXP'.swapcase()]
            self.ALPHA0LEXPgiven = True
        else:
            if self.ALPHA0LEXPgiven == False:
                self.ALPHA0LEXP = 1.0
        if 'LALPHA0' in param:
            self.LALPHA0 = param['LALPHA0']
            self.LALPHA0given = True
        elif 'LALPHA0'.swapcase() in param:
            self.LALPHA0 = param['LALPHA0'.swapcase()]
            self.LALPHA0given = True
        else:
            if self.LALPHA0given == False:
                self.LALPHA0 = 0.0
        if 'WALPHA0' in param:
            self.WALPHA0 = param['WALPHA0']
            self.WALPHA0given = True
        elif 'WALPHA0'.swapcase() in param:
            self.WALPHA0 = param['WALPHA0'.swapcase()]
            self.WALPHA0given = True
        else:
            if self.WALPHA0given == False:
                self.WALPHA0 = 0.0
        if 'PALPHA0' in param:
            self.PALPHA0 = param['PALPHA0']
            self.PALPHA0given = True
        elif 'PALPHA0'.swapcase() in param:
            self.PALPHA0 = param['PALPHA0'.swapcase()]
            self.PALPHA0given = True
        else:
            if self.PALPHA0given == False:
                self.PALPHA0 = 0.0
        if 'BETA0' in param:
            self.BETA0 = param['BETA0']
            self.BETA0given = True
        elif 'BETA0'.swapcase() in param:
            self.BETA0 = param['BETA0'.swapcase()]
            self.BETA0given = True
        else:
            if self.BETA0given == False:
                self.BETA0 = 0.0
        if 'LBETA0' in param:
            self.LBETA0 = param['LBETA0']
            self.LBETA0given = True
        elif 'LBETA0'.swapcase() in param:
            self.LBETA0 = param['LBETA0'.swapcase()]
            self.LBETA0given = True
        else:
            if self.LBETA0given == False:
                self.LBETA0 = 0.0
        if 'WBETA0' in param:
            self.WBETA0 = param['WBETA0']
            self.WBETA0given = True
        elif 'WBETA0'.swapcase() in param:
            self.WBETA0 = param['WBETA0'.swapcase()]
            self.WBETA0given = True
        else:
            if self.WBETA0given == False:
                self.WBETA0 = 0.0
        if 'PBETA0' in param:
            self.PBETA0 = param['PBETA0']
            self.PBETA0given = True
        elif 'PBETA0'.swapcase() in param:
            self.PBETA0 = param['PBETA0'.swapcase()]
            self.PBETA0given = True
        else:
            if self.PBETA0given == False:
                self.PBETA0 = 0.0
        if 'AIGBACC' in param:
            self.AIGBACC = param['AIGBACC']
            self.AIGBACCgiven = True
        elif 'AIGBACC'.swapcase() in param:
            self.AIGBACC = param['AIGBACC'.swapcase()]
            self.AIGBACCgiven = True
        else:
            if self.AIGBACCgiven == False:
                self.AIGBACC = 0.0136
        if 'BIGBACC' in param:
            self.BIGBACC = param['BIGBACC']
            self.BIGBACCgiven = True
        elif 'BIGBACC'.swapcase() in param:
            self.BIGBACC = param['BIGBACC'.swapcase()]
            self.BIGBACCgiven = True
        else:
            if self.BIGBACCgiven == False:
                self.BIGBACC = 0.00171
        if 'CIGBACC' in param:
            self.CIGBACC = param['CIGBACC']
            self.CIGBACCgiven = True
        elif 'CIGBACC'.swapcase() in param:
            self.CIGBACC = param['CIGBACC'.swapcase()]
            self.CIGBACCgiven = True
        else:
            if self.CIGBACCgiven == False:
                self.CIGBACC = 0.075
        if 'NIGBACC' in param:
            self.NIGBACC = param['NIGBACC']
            self.NIGBACCgiven = True
        elif 'NIGBACC'.swapcase() in param:
            self.NIGBACC = param['NIGBACC'.swapcase()]
            self.NIGBACCgiven = True
        else:
            if self.NIGBACCgiven == False:
                self.NIGBACC = 1.0
        if 'AIGBINV' in param:
            self.AIGBINV = param['AIGBINV']
            self.AIGBINVgiven = True
        elif 'AIGBINV'.swapcase() in param:
            self.AIGBINV = param['AIGBINV'.swapcase()]
            self.AIGBINVgiven = True
        else:
            if self.AIGBINVgiven == False:
                self.AIGBINV = 0.0111
        if 'BIGBINV' in param:
            self.BIGBINV = param['BIGBINV']
            self.BIGBINVgiven = True
        elif 'BIGBINV'.swapcase() in param:
            self.BIGBINV = param['BIGBINV'.swapcase()]
            self.BIGBINVgiven = True
        else:
            if self.BIGBINVgiven == False:
                self.BIGBINV = 0.000949
        if 'CIGBINV' in param:
            self.CIGBINV = param['CIGBINV']
            self.CIGBINVgiven = True
        elif 'CIGBINV'.swapcase() in param:
            self.CIGBINV = param['CIGBINV'.swapcase()]
            self.CIGBINVgiven = True
        else:
            if self.CIGBINVgiven == False:
                self.CIGBINV = 0.006
        if 'EIGBINV' in param:
            self.EIGBINV = param['EIGBINV']
            self.EIGBINVgiven = True
        elif 'EIGBINV'.swapcase() in param:
            self.EIGBINV = param['EIGBINV'.swapcase()]
            self.EIGBINVgiven = True
        else:
            if self.EIGBINVgiven == False:
                self.EIGBINV = 1.1
        if 'NIGBINV' in param:
            self.NIGBINV = param['NIGBINV']
            self.NIGBINVgiven = True
        elif 'NIGBINV'.swapcase() in param:
            self.NIGBINV = param['NIGBINV'.swapcase()]
            self.NIGBINVgiven = True
        else:
            if self.NIGBINVgiven == False:
                self.NIGBINV = 3.0
        if 'AIGC' in param:
            self.AIGC = param['AIGC']
            self.AIGCgiven = True
        elif 'AIGC'.swapcase() in param:
            self.AIGC = param['AIGC'.swapcase()]
            self.AIGCgiven = True
        else:
            if self.AIGCgiven == False:
                self.AIGC = 1.36e-2 if (self.TYPE == self.ntype) else 9.8e-3
        if 'BIGC' in param:
            self.BIGC = param['BIGC']
            self.BIGCgiven = True
        elif 'BIGC'.swapcase() in param:
            self.BIGC = param['BIGC'.swapcase()]
            self.BIGCgiven = True
        else:
            if self.BIGCgiven == False:
                self.BIGC = 1.71e-3 if (self.TYPE == self.ntype) else 7.59e-4
        if 'CIGC' in param:
            self.CIGC = param['CIGC']
            self.CIGCgiven = True
        elif 'CIGC'.swapcase() in param:
            self.CIGC = param['CIGC'.swapcase()]
            self.CIGCgiven = True
        else:
            if self.CIGCgiven == False:
                self.CIGC = 0.075 if (self.TYPE == self.ntype) else 0.03
        if 'AIGS' in param:
            self.AIGS = param['AIGS']
            self.AIGSgiven = True
        elif 'AIGS'.swapcase() in param:
            self.AIGS = param['AIGS'.swapcase()]
            self.AIGSgiven = True
        else:
            if self.AIGSgiven == False:
                self.AIGS = 1.36e-2 if (self.TYPE == self.ntype) else 9.8e-3
        if 'BIGS' in param:
            self.BIGS = param['BIGS']
            self.BIGSgiven = True
        elif 'BIGS'.swapcase() in param:
            self.BIGS = param['BIGS'.swapcase()]
            self.BIGSgiven = True
        else:
            if self.BIGSgiven == False:
                self.BIGS = 1.71e-3 if (self.TYPE == self.ntype) else 7.59e-4
        if 'CIGS' in param:
            self.CIGS = param['CIGS']
            self.CIGSgiven = True
        elif 'CIGS'.swapcase() in param:
            self.CIGS = param['CIGS'.swapcase()]
            self.CIGSgiven = True
        else:
            if self.CIGSgiven == False:
                self.CIGS = 0.075 if (self.TYPE == self.ntype) else 0.03
        if 'AIGD' in param:
            self.AIGD = param['AIGD']
            self.AIGDgiven = True
        elif 'AIGD'.swapcase() in param:
            self.AIGD = param['AIGD'.swapcase()]
            self.AIGDgiven = True
        else:
            if self.AIGDgiven == False:
                self.AIGD = 1.36e-2 if (self.TYPE == self.ntype) else 9.8e-3
        if 'BIGD' in param:
            self.BIGD = param['BIGD']
            self.BIGDgiven = True
        elif 'BIGD'.swapcase() in param:
            self.BIGD = param['BIGD'.swapcase()]
            self.BIGDgiven = True
        else:
            if self.BIGDgiven == False:
                self.BIGD = 1.71e-3 if (self.TYPE == self.ntype) else 7.59e-4
        if 'CIGD' in param:
            self.CIGD = param['CIGD']
            self.CIGDgiven = True
        elif 'CIGD'.swapcase() in param:
            self.CIGD = param['CIGD'.swapcase()]
            self.CIGDgiven = True
        else:
            if self.CIGDgiven == False:
                self.CIGD = 0.075 if (self.TYPE == self.ntype) else 0.03
        if 'DLCIG' in param:
            self.DLCIG = param['DLCIG']
            self.DLCIGgiven = True
        elif 'DLCIG'.swapcase() in param:
            self.DLCIG = param['DLCIG'.swapcase()]
            self.DLCIGgiven = True
        else:
            if self.DLCIGgiven == False:
                self.DLCIG = self.LINT
        if 'DLCIGD' in param:
            self.DLCIGD = param['DLCIGD']
            self.DLCIGDgiven = True
        elif 'DLCIGD'.swapcase() in param:
            self.DLCIGD = param['DLCIGD'.swapcase()]
            self.DLCIGDgiven = True
        else:
            if self.DLCIGDgiven == False:
                self.DLCIGD = self.DLCIG
        if 'POXEDGE' in param:
            self.POXEDGE = param['POXEDGE']
            self.POXEDGEgiven = True
        elif 'POXEDGE'.swapcase() in param:
            self.POXEDGE = param['POXEDGE'.swapcase()]
            self.POXEDGEgiven = True
        else:
            if self.POXEDGEgiven == False:
                self.POXEDGE = 1.0
        if 'NTOX' in param:
            self.NTOX = param['NTOX']
            self.NTOXgiven = True
        elif 'NTOX'.swapcase() in param:
            self.NTOX = param['NTOX'.swapcase()]
            self.NTOXgiven = True
        else:
            if self.NTOXgiven == False:
                self.NTOX = 1.0
        if 'TOXREF' in param:
            self.TOXREF = param['TOXREF']
            self.TOXREFgiven = True
        elif 'TOXREF'.swapcase() in param:
            self.TOXREF = param['TOXREF'.swapcase()]
            self.TOXREFgiven = True
        else:
            if self.TOXREFgiven == False:
                self.TOXREF = 3e-09
        if 'PIGCD' in param:
            self.PIGCD = param['PIGCD']
            self.PIGCDgiven = True
        elif 'PIGCD'.swapcase() in param:
            self.PIGCD = param['PIGCD'.swapcase()]
            self.PIGCDgiven = True
        else:
            if self.PIGCDgiven == False:
                self.PIGCD = 1.0
        if 'AIGCL' in param:
            self.AIGCL = param['AIGCL']
            self.AIGCLgiven = True
        elif 'AIGCL'.swapcase() in param:
            self.AIGCL = param['AIGCL'.swapcase()]
            self.AIGCLgiven = True
        else:
            if self.AIGCLgiven == False:
                self.AIGCL = 0.0
        if 'AIGCW' in param:
            self.AIGCW = param['AIGCW']
            self.AIGCWgiven = True
        elif 'AIGCW'.swapcase() in param:
            self.AIGCW = param['AIGCW'.swapcase()]
            self.AIGCWgiven = True
        else:
            if self.AIGCWgiven == False:
                self.AIGCW = 0.0
        if 'AIGSL' in param:
            self.AIGSL = param['AIGSL']
            self.AIGSLgiven = True
        elif 'AIGSL'.swapcase() in param:
            self.AIGSL = param['AIGSL'.swapcase()]
            self.AIGSLgiven = True
        else:
            if self.AIGSLgiven == False:
                self.AIGSL = 0.0
        if 'AIGSW' in param:
            self.AIGSW = param['AIGSW']
            self.AIGSWgiven = True
        elif 'AIGSW'.swapcase() in param:
            self.AIGSW = param['AIGSW'.swapcase()]
            self.AIGSWgiven = True
        else:
            if self.AIGSWgiven == False:
                self.AIGSW = 0.0
        if 'AIGDL' in param:
            self.AIGDL = param['AIGDL']
            self.AIGDLgiven = True
        elif 'AIGDL'.swapcase() in param:
            self.AIGDL = param['AIGDL'.swapcase()]
            self.AIGDLgiven = True
        else:
            if self.AIGDLgiven == False:
                self.AIGDL = 0.0
        if 'AIGDW' in param:
            self.AIGDW = param['AIGDW']
            self.AIGDWgiven = True
        elif 'AIGDW'.swapcase() in param:
            self.AIGDW = param['AIGDW'.swapcase()]
            self.AIGDWgiven = True
        else:
            if self.AIGDWgiven == False:
                self.AIGDW = 0.0
        if 'PIGCDL' in param:
            self.PIGCDL = param['PIGCDL']
            self.PIGCDLgiven = True
        elif 'PIGCDL'.swapcase() in param:
            self.PIGCDL = param['PIGCDL'.swapcase()]
            self.PIGCDLgiven = True
        else:
            if self.PIGCDLgiven == False:
                self.PIGCDL = 0.0
        if 'LAIGBINV' in param:
            self.LAIGBINV = param['LAIGBINV']
            self.LAIGBINVgiven = True
        elif 'LAIGBINV'.swapcase() in param:
            self.LAIGBINV = param['LAIGBINV'.swapcase()]
            self.LAIGBINVgiven = True
        else:
            if self.LAIGBINVgiven == False:
                self.LAIGBINV = 0.0
        if 'WAIGBINV' in param:
            self.WAIGBINV = param['WAIGBINV']
            self.WAIGBINVgiven = True
        elif 'WAIGBINV'.swapcase() in param:
            self.WAIGBINV = param['WAIGBINV'.swapcase()]
            self.WAIGBINVgiven = True
        else:
            if self.WAIGBINVgiven == False:
                self.WAIGBINV = 0.0
        if 'PAIGBINV' in param:
            self.PAIGBINV = param['PAIGBINV']
            self.PAIGBINVgiven = True
        elif 'PAIGBINV'.swapcase() in param:
            self.PAIGBINV = param['PAIGBINV'.swapcase()]
            self.PAIGBINVgiven = True
        else:
            if self.PAIGBINVgiven == False:
                self.PAIGBINV = 0.0
        if 'LBIGBINV' in param:
            self.LBIGBINV = param['LBIGBINV']
            self.LBIGBINVgiven = True
        elif 'LBIGBINV'.swapcase() in param:
            self.LBIGBINV = param['LBIGBINV'.swapcase()]
            self.LBIGBINVgiven = True
        else:
            if self.LBIGBINVgiven == False:
                self.LBIGBINV = 0.0
        if 'WBIGBINV' in param:
            self.WBIGBINV = param['WBIGBINV']
            self.WBIGBINVgiven = True
        elif 'WBIGBINV'.swapcase() in param:
            self.WBIGBINV = param['WBIGBINV'.swapcase()]
            self.WBIGBINVgiven = True
        else:
            if self.WBIGBINVgiven == False:
                self.WBIGBINV = 0.0
        if 'PBIGBINV' in param:
            self.PBIGBINV = param['PBIGBINV']
            self.PBIGBINVgiven = True
        elif 'PBIGBINV'.swapcase() in param:
            self.PBIGBINV = param['PBIGBINV'.swapcase()]
            self.PBIGBINVgiven = True
        else:
            if self.PBIGBINVgiven == False:
                self.PBIGBINV = 0.0
        if 'LCIGBINV' in param:
            self.LCIGBINV = param['LCIGBINV']
            self.LCIGBINVgiven = True
        elif 'LCIGBINV'.swapcase() in param:
            self.LCIGBINV = param['LCIGBINV'.swapcase()]
            self.LCIGBINVgiven = True
        else:
            if self.LCIGBINVgiven == False:
                self.LCIGBINV = 0.0
        if 'WCIGBINV' in param:
            self.WCIGBINV = param['WCIGBINV']
            self.WCIGBINVgiven = True
        elif 'WCIGBINV'.swapcase() in param:
            self.WCIGBINV = param['WCIGBINV'.swapcase()]
            self.WCIGBINVgiven = True
        else:
            if self.WCIGBINVgiven == False:
                self.WCIGBINV = 0.0
        if 'PCIGBINV' in param:
            self.PCIGBINV = param['PCIGBINV']
            self.PCIGBINVgiven = True
        elif 'PCIGBINV'.swapcase() in param:
            self.PCIGBINV = param['PCIGBINV'.swapcase()]
            self.PCIGBINVgiven = True
        else:
            if self.PCIGBINVgiven == False:
                self.PCIGBINV = 0.0
        if 'LEIGBINV' in param:
            self.LEIGBINV = param['LEIGBINV']
            self.LEIGBINVgiven = True
        elif 'LEIGBINV'.swapcase() in param:
            self.LEIGBINV = param['LEIGBINV'.swapcase()]
            self.LEIGBINVgiven = True
        else:
            if self.LEIGBINVgiven == False:
                self.LEIGBINV = 0.0
        if 'WEIGBINV' in param:
            self.WEIGBINV = param['WEIGBINV']
            self.WEIGBINVgiven = True
        elif 'WEIGBINV'.swapcase() in param:
            self.WEIGBINV = param['WEIGBINV'.swapcase()]
            self.WEIGBINVgiven = True
        else:
            if self.WEIGBINVgiven == False:
                self.WEIGBINV = 0.0
        if 'PEIGBINV' in param:
            self.PEIGBINV = param['PEIGBINV']
            self.PEIGBINVgiven = True
        elif 'PEIGBINV'.swapcase() in param:
            self.PEIGBINV = param['PEIGBINV'.swapcase()]
            self.PEIGBINVgiven = True
        else:
            if self.PEIGBINVgiven == False:
                self.PEIGBINV = 0.0
        if 'LNIGBINV' in param:
            self.LNIGBINV = param['LNIGBINV']
            self.LNIGBINVgiven = True
        elif 'LNIGBINV'.swapcase() in param:
            self.LNIGBINV = param['LNIGBINV'.swapcase()]
            self.LNIGBINVgiven = True
        else:
            if self.LNIGBINVgiven == False:
                self.LNIGBINV = 0.0
        if 'WNIGBINV' in param:
            self.WNIGBINV = param['WNIGBINV']
            self.WNIGBINVgiven = True
        elif 'WNIGBINV'.swapcase() in param:
            self.WNIGBINV = param['WNIGBINV'.swapcase()]
            self.WNIGBINVgiven = True
        else:
            if self.WNIGBINVgiven == False:
                self.WNIGBINV = 0.0
        if 'PNIGBINV' in param:
            self.PNIGBINV = param['PNIGBINV']
            self.PNIGBINVgiven = True
        elif 'PNIGBINV'.swapcase() in param:
            self.PNIGBINV = param['PNIGBINV'.swapcase()]
            self.PNIGBINVgiven = True
        else:
            if self.PNIGBINVgiven == False:
                self.PNIGBINV = 0.0
        if 'LAIGBACC' in param:
            self.LAIGBACC = param['LAIGBACC']
            self.LAIGBACCgiven = True
        elif 'LAIGBACC'.swapcase() in param:
            self.LAIGBACC = param['LAIGBACC'.swapcase()]
            self.LAIGBACCgiven = True
        else:
            if self.LAIGBACCgiven == False:
                self.LAIGBACC = 0.0
        if 'WAIGBACC' in param:
            self.WAIGBACC = param['WAIGBACC']
            self.WAIGBACCgiven = True
        elif 'WAIGBACC'.swapcase() in param:
            self.WAIGBACC = param['WAIGBACC'.swapcase()]
            self.WAIGBACCgiven = True
        else:
            if self.WAIGBACCgiven == False:
                self.WAIGBACC = 0.0
        if 'PAIGBACC' in param:
            self.PAIGBACC = param['PAIGBACC']
            self.PAIGBACCgiven = True
        elif 'PAIGBACC'.swapcase() in param:
            self.PAIGBACC = param['PAIGBACC'.swapcase()]
            self.PAIGBACCgiven = True
        else:
            if self.PAIGBACCgiven == False:
                self.PAIGBACC = 0.0
        if 'LBIGBACC' in param:
            self.LBIGBACC = param['LBIGBACC']
            self.LBIGBACCgiven = True
        elif 'LBIGBACC'.swapcase() in param:
            self.LBIGBACC = param['LBIGBACC'.swapcase()]
            self.LBIGBACCgiven = True
        else:
            if self.LBIGBACCgiven == False:
                self.LBIGBACC = 0.0
        if 'WBIGBACC' in param:
            self.WBIGBACC = param['WBIGBACC']
            self.WBIGBACCgiven = True
        elif 'WBIGBACC'.swapcase() in param:
            self.WBIGBACC = param['WBIGBACC'.swapcase()]
            self.WBIGBACCgiven = True
        else:
            if self.WBIGBACCgiven == False:
                self.WBIGBACC = 0.0
        if 'PBIGBACC' in param:
            self.PBIGBACC = param['PBIGBACC']
            self.PBIGBACCgiven = True
        elif 'PBIGBACC'.swapcase() in param:
            self.PBIGBACC = param['PBIGBACC'.swapcase()]
            self.PBIGBACCgiven = True
        else:
            if self.PBIGBACCgiven == False:
                self.PBIGBACC = 0.0
        if 'LCIGBACC' in param:
            self.LCIGBACC = param['LCIGBACC']
            self.LCIGBACCgiven = True
        elif 'LCIGBACC'.swapcase() in param:
            self.LCIGBACC = param['LCIGBACC'.swapcase()]
            self.LCIGBACCgiven = True
        else:
            if self.LCIGBACCgiven == False:
                self.LCIGBACC = 0.0
        if 'WCIGBACC' in param:
            self.WCIGBACC = param['WCIGBACC']
            self.WCIGBACCgiven = True
        elif 'WCIGBACC'.swapcase() in param:
            self.WCIGBACC = param['WCIGBACC'.swapcase()]
            self.WCIGBACCgiven = True
        else:
            if self.WCIGBACCgiven == False:
                self.WCIGBACC = 0.0
        if 'PCIGBACC' in param:
            self.PCIGBACC = param['PCIGBACC']
            self.PCIGBACCgiven = True
        elif 'PCIGBACC'.swapcase() in param:
            self.PCIGBACC = param['PCIGBACC'.swapcase()]
            self.PCIGBACCgiven = True
        else:
            if self.PCIGBACCgiven == False:
                self.PCIGBACC = 0.0
        if 'LNIGBACC' in param:
            self.LNIGBACC = param['LNIGBACC']
            self.LNIGBACCgiven = True
        elif 'LNIGBACC'.swapcase() in param:
            self.LNIGBACC = param['LNIGBACC'.swapcase()]
            self.LNIGBACCgiven = True
        else:
            if self.LNIGBACCgiven == False:
                self.LNIGBACC = 0.0
        if 'WNIGBACC' in param:
            self.WNIGBACC = param['WNIGBACC']
            self.WNIGBACCgiven = True
        elif 'WNIGBACC'.swapcase() in param:
            self.WNIGBACC = param['WNIGBACC'.swapcase()]
            self.WNIGBACCgiven = True
        else:
            if self.WNIGBACCgiven == False:
                self.WNIGBACC = 0.0
        if 'PNIGBACC' in param:
            self.PNIGBACC = param['PNIGBACC']
            self.PNIGBACCgiven = True
        elif 'PNIGBACC'.swapcase() in param:
            self.PNIGBACC = param['PNIGBACC'.swapcase()]
            self.PNIGBACCgiven = True
        else:
            if self.PNIGBACCgiven == False:
                self.PNIGBACC = 0.0
        if 'LAIGC' in param:
            self.LAIGC = param['LAIGC']
            self.LAIGCgiven = True
        elif 'LAIGC'.swapcase() in param:
            self.LAIGC = param['LAIGC'.swapcase()]
            self.LAIGCgiven = True
        else:
            if self.LAIGCgiven == False:
                self.LAIGC = 0.0
        if 'WAIGC' in param:
            self.WAIGC = param['WAIGC']
            self.WAIGCgiven = True
        elif 'WAIGC'.swapcase() in param:
            self.WAIGC = param['WAIGC'.swapcase()]
            self.WAIGCgiven = True
        else:
            if self.WAIGCgiven == False:
                self.WAIGC = 0.0
        if 'PAIGC' in param:
            self.PAIGC = param['PAIGC']
            self.PAIGCgiven = True
        elif 'PAIGC'.swapcase() in param:
            self.PAIGC = param['PAIGC'.swapcase()]
            self.PAIGCgiven = True
        else:
            if self.PAIGCgiven == False:
                self.PAIGC = 0.0
        if 'LBIGC' in param:
            self.LBIGC = param['LBIGC']
            self.LBIGCgiven = True
        elif 'LBIGC'.swapcase() in param:
            self.LBIGC = param['LBIGC'.swapcase()]
            self.LBIGCgiven = True
        else:
            if self.LBIGCgiven == False:
                self.LBIGC = 0.0
        if 'WBIGC' in param:
            self.WBIGC = param['WBIGC']
            self.WBIGCgiven = True
        elif 'WBIGC'.swapcase() in param:
            self.WBIGC = param['WBIGC'.swapcase()]
            self.WBIGCgiven = True
        else:
            if self.WBIGCgiven == False:
                self.WBIGC = 0.0
        if 'PBIGC' in param:
            self.PBIGC = param['PBIGC']
            self.PBIGCgiven = True
        elif 'PBIGC'.swapcase() in param:
            self.PBIGC = param['PBIGC'.swapcase()]
            self.PBIGCgiven = True
        else:
            if self.PBIGCgiven == False:
                self.PBIGC = 0.0
        if 'LCIGC' in param:
            self.LCIGC = param['LCIGC']
            self.LCIGCgiven = True
        elif 'LCIGC'.swapcase() in param:
            self.LCIGC = param['LCIGC'.swapcase()]
            self.LCIGCgiven = True
        else:
            if self.LCIGCgiven == False:
                self.LCIGC = 0.0
        if 'WCIGC' in param:
            self.WCIGC = param['WCIGC']
            self.WCIGCgiven = True
        elif 'WCIGC'.swapcase() in param:
            self.WCIGC = param['WCIGC'.swapcase()]
            self.WCIGCgiven = True
        else:
            if self.WCIGCgiven == False:
                self.WCIGC = 0.0
        if 'PCIGC' in param:
            self.PCIGC = param['PCIGC']
            self.PCIGCgiven = True
        elif 'PCIGC'.swapcase() in param:
            self.PCIGC = param['PCIGC'.swapcase()]
            self.PCIGCgiven = True
        else:
            if self.PCIGCgiven == False:
                self.PCIGC = 0.0
        if 'LAIGS' in param:
            self.LAIGS = param['LAIGS']
            self.LAIGSgiven = True
        elif 'LAIGS'.swapcase() in param:
            self.LAIGS = param['LAIGS'.swapcase()]
            self.LAIGSgiven = True
        else:
            if self.LAIGSgiven == False:
                self.LAIGS = 0.0
        if 'WAIGS' in param:
            self.WAIGS = param['WAIGS']
            self.WAIGSgiven = True
        elif 'WAIGS'.swapcase() in param:
            self.WAIGS = param['WAIGS'.swapcase()]
            self.WAIGSgiven = True
        else:
            if self.WAIGSgiven == False:
                self.WAIGS = 0.0
        if 'PAIGS' in param:
            self.PAIGS = param['PAIGS']
            self.PAIGSgiven = True
        elif 'PAIGS'.swapcase() in param:
            self.PAIGS = param['PAIGS'.swapcase()]
            self.PAIGSgiven = True
        else:
            if self.PAIGSgiven == False:
                self.PAIGS = 0.0
        if 'LBIGS' in param:
            self.LBIGS = param['LBIGS']
            self.LBIGSgiven = True
        elif 'LBIGS'.swapcase() in param:
            self.LBIGS = param['LBIGS'.swapcase()]
            self.LBIGSgiven = True
        else:
            if self.LBIGSgiven == False:
                self.LBIGS = 0.0
        if 'WBIGS' in param:
            self.WBIGS = param['WBIGS']
            self.WBIGSgiven = True
        elif 'WBIGS'.swapcase() in param:
            self.WBIGS = param['WBIGS'.swapcase()]
            self.WBIGSgiven = True
        else:
            if self.WBIGSgiven == False:
                self.WBIGS = 0.0
        if 'PBIGS' in param:
            self.PBIGS = param['PBIGS']
            self.PBIGSgiven = True
        elif 'PBIGS'.swapcase() in param:
            self.PBIGS = param['PBIGS'.swapcase()]
            self.PBIGSgiven = True
        else:
            if self.PBIGSgiven == False:
                self.PBIGS = 0.0
        if 'LCIGS' in param:
            self.LCIGS = param['LCIGS']
            self.LCIGSgiven = True
        elif 'LCIGS'.swapcase() in param:
            self.LCIGS = param['LCIGS'.swapcase()]
            self.LCIGSgiven = True
        else:
            if self.LCIGSgiven == False:
                self.LCIGS = 0.0
        if 'WCIGS' in param:
            self.WCIGS = param['WCIGS']
            self.WCIGSgiven = True
        elif 'WCIGS'.swapcase() in param:
            self.WCIGS = param['WCIGS'.swapcase()]
            self.WCIGSgiven = True
        else:
            if self.WCIGSgiven == False:
                self.WCIGS = 0.0
        if 'PCIGS' in param:
            self.PCIGS = param['PCIGS']
            self.PCIGSgiven = True
        elif 'PCIGS'.swapcase() in param:
            self.PCIGS = param['PCIGS'.swapcase()]
            self.PCIGSgiven = True
        else:
            if self.PCIGSgiven == False:
                self.PCIGS = 0.0
        if 'LAIGD' in param:
            self.LAIGD = param['LAIGD']
            self.LAIGDgiven = True
        elif 'LAIGD'.swapcase() in param:
            self.LAIGD = param['LAIGD'.swapcase()]
            self.LAIGDgiven = True
        else:
            if self.LAIGDgiven == False:
                self.LAIGD = 0.0
        if 'WAIGD' in param:
            self.WAIGD = param['WAIGD']
            self.WAIGDgiven = True
        elif 'WAIGD'.swapcase() in param:
            self.WAIGD = param['WAIGD'.swapcase()]
            self.WAIGDgiven = True
        else:
            if self.WAIGDgiven == False:
                self.WAIGD = 0.0
        if 'PAIGD' in param:
            self.PAIGD = param['PAIGD']
            self.PAIGDgiven = True
        elif 'PAIGD'.swapcase() in param:
            self.PAIGD = param['PAIGD'.swapcase()]
            self.PAIGDgiven = True
        else:
            if self.PAIGDgiven == False:
                self.PAIGD = 0.0
        if 'LBIGD' in param:
            self.LBIGD = param['LBIGD']
            self.LBIGDgiven = True
        elif 'LBIGD'.swapcase() in param:
            self.LBIGD = param['LBIGD'.swapcase()]
            self.LBIGDgiven = True
        else:
            if self.LBIGDgiven == False:
                self.LBIGD = 0.0
        if 'WBIGD' in param:
            self.WBIGD = param['WBIGD']
            self.WBIGDgiven = True
        elif 'WBIGD'.swapcase() in param:
            self.WBIGD = param['WBIGD'.swapcase()]
            self.WBIGDgiven = True
        else:
            if self.WBIGDgiven == False:
                self.WBIGD = 0.0
        if 'PBIGD' in param:
            self.PBIGD = param['PBIGD']
            self.PBIGDgiven = True
        elif 'PBIGD'.swapcase() in param:
            self.PBIGD = param['PBIGD'.swapcase()]
            self.PBIGDgiven = True
        else:
            if self.PBIGDgiven == False:
                self.PBIGD = 0.0
        if 'LCIGD' in param:
            self.LCIGD = param['LCIGD']
            self.LCIGDgiven = True
        elif 'LCIGD'.swapcase() in param:
            self.LCIGD = param['LCIGD'.swapcase()]
            self.LCIGDgiven = True
        else:
            if self.LCIGDgiven == False:
                self.LCIGD = 0.0
        if 'WCIGD' in param:
            self.WCIGD = param['WCIGD']
            self.WCIGDgiven = True
        elif 'WCIGD'.swapcase() in param:
            self.WCIGD = param['WCIGD'.swapcase()]
            self.WCIGDgiven = True
        else:
            if self.WCIGDgiven == False:
                self.WCIGD = 0.0
        if 'PCIGD' in param:
            self.PCIGD = param['PCIGD']
            self.PCIGDgiven = True
        elif 'PCIGD'.swapcase() in param:
            self.PCIGD = param['PCIGD'.swapcase()]
            self.PCIGDgiven = True
        else:
            if self.PCIGDgiven == False:
                self.PCIGD = 0.0
        if 'LPOXEDGE' in param:
            self.LPOXEDGE = param['LPOXEDGE']
            self.LPOXEDGEgiven = True
        elif 'LPOXEDGE'.swapcase() in param:
            self.LPOXEDGE = param['LPOXEDGE'.swapcase()]
            self.LPOXEDGEgiven = True
        else:
            if self.LPOXEDGEgiven == False:
                self.LPOXEDGE = 0.0
        if 'WPOXEDGE' in param:
            self.WPOXEDGE = param['WPOXEDGE']
            self.WPOXEDGEgiven = True
        elif 'WPOXEDGE'.swapcase() in param:
            self.WPOXEDGE = param['WPOXEDGE'.swapcase()]
            self.WPOXEDGEgiven = True
        else:
            if self.WPOXEDGEgiven == False:
                self.WPOXEDGE = 0.0
        if 'PPOXEDGE' in param:
            self.PPOXEDGE = param['PPOXEDGE']
            self.PPOXEDGEgiven = True
        elif 'PPOXEDGE'.swapcase() in param:
            self.PPOXEDGE = param['PPOXEDGE'.swapcase()]
            self.PPOXEDGEgiven = True
        else:
            if self.PPOXEDGEgiven == False:
                self.PPOXEDGE = 0.0
        if 'LDLCIG' in param:
            self.LDLCIG = param['LDLCIG']
            self.LDLCIGgiven = True
        elif 'LDLCIG'.swapcase() in param:
            self.LDLCIG = param['LDLCIG'.swapcase()]
            self.LDLCIGgiven = True
        else:
            if self.LDLCIGgiven == False:
                self.LDLCIG = 0.0
        if 'WDLCIG' in param:
            self.WDLCIG = param['WDLCIG']
            self.WDLCIGgiven = True
        elif 'WDLCIG'.swapcase() in param:
            self.WDLCIG = param['WDLCIG'.swapcase()]
            self.WDLCIGgiven = True
        else:
            if self.WDLCIGgiven == False:
                self.WDLCIG = 0.0
        if 'PDLCIG' in param:
            self.PDLCIG = param['PDLCIG']
            self.PDLCIGgiven = True
        elif 'PDLCIG'.swapcase() in param:
            self.PDLCIG = param['PDLCIG'.swapcase()]
            self.PDLCIGgiven = True
        else:
            if self.PDLCIGgiven == False:
                self.PDLCIG = 0.0
        if 'LDLCIGD' in param:
            self.LDLCIGD = param['LDLCIGD']
            self.LDLCIGDgiven = True
        elif 'LDLCIGD'.swapcase() in param:
            self.LDLCIGD = param['LDLCIGD'.swapcase()]
            self.LDLCIGDgiven = True
        else:
            if self.LDLCIGDgiven == False:
                self.LDLCIGD = 0.0
        if 'WDLCIGD' in param:
            self.WDLCIGD = param['WDLCIGD']
            self.WDLCIGDgiven = True
        elif 'WDLCIGD'.swapcase() in param:
            self.WDLCIGD = param['WDLCIGD'.swapcase()]
            self.WDLCIGDgiven = True
        else:
            if self.WDLCIGDgiven == False:
                self.WDLCIGD = 0.0
        if 'PDLCIGD' in param:
            self.PDLCIGD = param['PDLCIGD']
            self.PDLCIGDgiven = True
        elif 'PDLCIGD'.swapcase() in param:
            self.PDLCIGD = param['PDLCIGD'.swapcase()]
            self.PDLCIGDgiven = True
        else:
            if self.PDLCIGDgiven == False:
                self.PDLCIGD = 0.0
        if 'LNTOX' in param:
            self.LNTOX = param['LNTOX']
            self.LNTOXgiven = True
        elif 'LNTOX'.swapcase() in param:
            self.LNTOX = param['LNTOX'.swapcase()]
            self.LNTOXgiven = True
        else:
            if self.LNTOXgiven == False:
                self.LNTOX = 0.0
        if 'WNTOX' in param:
            self.WNTOX = param['WNTOX']
            self.WNTOXgiven = True
        elif 'WNTOX'.swapcase() in param:
            self.WNTOX = param['WNTOX'.swapcase()]
            self.WNTOXgiven = True
        else:
            if self.WNTOXgiven == False:
                self.WNTOX = 0.0
        if 'PNTOX' in param:
            self.PNTOX = param['PNTOX']
            self.PNTOXgiven = True
        elif 'PNTOX'.swapcase() in param:
            self.PNTOX = param['PNTOX'.swapcase()]
            self.PNTOXgiven = True
        else:
            if self.PNTOXgiven == False:
                self.PNTOX = 0.0
        if 'AGIDL' in param:
            self.AGIDL = param['AGIDL']
            self.AGIDLgiven = True
        elif 'AGIDL'.swapcase() in param:
            self.AGIDL = param['AGIDL'.swapcase()]
            self.AGIDLgiven = True
        else:
            if self.AGIDLgiven == False:
                self.AGIDL = 0.0
        if 'AGIDLL' in param:
            self.AGIDLL = param['AGIDLL']
            self.AGIDLLgiven = True
        elif 'AGIDLL'.swapcase() in param:
            self.AGIDLL = param['AGIDLL'.swapcase()]
            self.AGIDLLgiven = True
        else:
            if self.AGIDLLgiven == False:
                self.AGIDLL = 0.0
        if 'AGIDLW' in param:
            self.AGIDLW = param['AGIDLW']
            self.AGIDLWgiven = True
        elif 'AGIDLW'.swapcase() in param:
            self.AGIDLW = param['AGIDLW'.swapcase()]
            self.AGIDLWgiven = True
        else:
            if self.AGIDLWgiven == False:
                self.AGIDLW = 0.0
        if 'LAGIDL' in param:
            self.LAGIDL = param['LAGIDL']
            self.LAGIDLgiven = True
        elif 'LAGIDL'.swapcase() in param:
            self.LAGIDL = param['LAGIDL'.swapcase()]
            self.LAGIDLgiven = True
        else:
            if self.LAGIDLgiven == False:
                self.LAGIDL = 0.0
        if 'WAGIDL' in param:
            self.WAGIDL = param['WAGIDL']
            self.WAGIDLgiven = True
        elif 'WAGIDL'.swapcase() in param:
            self.WAGIDL = param['WAGIDL'.swapcase()]
            self.WAGIDLgiven = True
        else:
            if self.WAGIDLgiven == False:
                self.WAGIDL = 0.0
        if 'PAGIDL' in param:
            self.PAGIDL = param['PAGIDL']
            self.PAGIDLgiven = True
        elif 'PAGIDL'.swapcase() in param:
            self.PAGIDL = param['PAGIDL'.swapcase()]
            self.PAGIDLgiven = True
        else:
            if self.PAGIDLgiven == False:
                self.PAGIDL = 0.0
        if 'BGIDL' in param:
            self.BGIDL = param['BGIDL']
            self.BGIDLgiven = True
        elif 'BGIDL'.swapcase() in param:
            self.BGIDL = param['BGIDL'.swapcase()]
            self.BGIDLgiven = True
        else:
            if self.BGIDLgiven == False:
                self.BGIDL = 2300000000.0
        if 'LBGIDL' in param:
            self.LBGIDL = param['LBGIDL']
            self.LBGIDLgiven = True
        elif 'LBGIDL'.swapcase() in param:
            self.LBGIDL = param['LBGIDL'.swapcase()]
            self.LBGIDLgiven = True
        else:
            if self.LBGIDLgiven == False:
                self.LBGIDL = 0.0
        if 'WBGIDL' in param:
            self.WBGIDL = param['WBGIDL']
            self.WBGIDLgiven = True
        elif 'WBGIDL'.swapcase() in param:
            self.WBGIDL = param['WBGIDL'.swapcase()]
            self.WBGIDLgiven = True
        else:
            if self.WBGIDLgiven == False:
                self.WBGIDL = 0.0
        if 'PBGIDL' in param:
            self.PBGIDL = param['PBGIDL']
            self.PBGIDLgiven = True
        elif 'PBGIDL'.swapcase() in param:
            self.PBGIDL = param['PBGIDL'.swapcase()]
            self.PBGIDLgiven = True
        else:
            if self.PBGIDLgiven == False:
                self.PBGIDL = 0.0
        if 'CGIDL' in param:
            self.CGIDL = param['CGIDL']
            self.CGIDLgiven = True
        elif 'CGIDL'.swapcase() in param:
            self.CGIDL = param['CGIDL'.swapcase()]
            self.CGIDLgiven = True
        else:
            if self.CGIDLgiven == False:
                self.CGIDL = 0.5
        if 'LCGIDL' in param:
            self.LCGIDL = param['LCGIDL']
            self.LCGIDLgiven = True
        elif 'LCGIDL'.swapcase() in param:
            self.LCGIDL = param['LCGIDL'.swapcase()]
            self.LCGIDLgiven = True
        else:
            if self.LCGIDLgiven == False:
                self.LCGIDL = 0.0
        if 'WCGIDL' in param:
            self.WCGIDL = param['WCGIDL']
            self.WCGIDLgiven = True
        elif 'WCGIDL'.swapcase() in param:
            self.WCGIDL = param['WCGIDL'.swapcase()]
            self.WCGIDLgiven = True
        else:
            if self.WCGIDLgiven == False:
                self.WCGIDL = 0.0
        if 'PCGIDL' in param:
            self.PCGIDL = param['PCGIDL']
            self.PCGIDLgiven = True
        elif 'PCGIDL'.swapcase() in param:
            self.PCGIDL = param['PCGIDL'.swapcase()]
            self.PCGIDLgiven = True
        else:
            if self.PCGIDLgiven == False:
                self.PCGIDL = 0.0
        if 'EGIDL' in param:
            self.EGIDL = param['EGIDL']
            self.EGIDLgiven = True
        elif 'EGIDL'.swapcase() in param:
            self.EGIDL = param['EGIDL'.swapcase()]
            self.EGIDLgiven = True
        else:
            if self.EGIDLgiven == False:
                self.EGIDL = 0.8
        if 'LEGIDL' in param:
            self.LEGIDL = param['LEGIDL']
            self.LEGIDLgiven = True
        elif 'LEGIDL'.swapcase() in param:
            self.LEGIDL = param['LEGIDL'.swapcase()]
            self.LEGIDLgiven = True
        else:
            if self.LEGIDLgiven == False:
                self.LEGIDL = 0.0
        if 'WEGIDL' in param:
            self.WEGIDL = param['WEGIDL']
            self.WEGIDLgiven = True
        elif 'WEGIDL'.swapcase() in param:
            self.WEGIDL = param['WEGIDL'.swapcase()]
            self.WEGIDLgiven = True
        else:
            if self.WEGIDLgiven == False:
                self.WEGIDL = 0.0
        if 'PEGIDL' in param:
            self.PEGIDL = param['PEGIDL']
            self.PEGIDLgiven = True
        elif 'PEGIDL'.swapcase() in param:
            self.PEGIDL = param['PEGIDL'.swapcase()]
            self.PEGIDLgiven = True
        else:
            if self.PEGIDLgiven == False:
                self.PEGIDL = 0.0
        if 'AGISL' in param:
            self.AGISL = param['AGISL']
            self.AGISLgiven = True
        elif 'AGISL'.swapcase() in param:
            self.AGISL = param['AGISL'.swapcase()]
            self.AGISLgiven = True
        else:
            if self.AGISLgiven == False:
                self.AGISL = self.AGIDL
        if 'AGISLL' in param:
            self.AGISLL = param['AGISLL']
            self.AGISLLgiven = True
        elif 'AGISLL'.swapcase() in param:
            self.AGISLL = param['AGISLL'.swapcase()]
            self.AGISLLgiven = True
        else:
            if self.AGISLLgiven == False:
                self.AGISLL = self.AGIDLL
        if 'AGISLW' in param:
            self.AGISLW = param['AGISLW']
            self.AGISLWgiven = True
        elif 'AGISLW'.swapcase() in param:
            self.AGISLW = param['AGISLW'.swapcase()]
            self.AGISLWgiven = True
        else:
            if self.AGISLWgiven == False:
                self.AGISLW = self.AGIDLW
        if 'LAGISL' in param:
            self.LAGISL = param['LAGISL']
            self.LAGISLgiven = True
        elif 'LAGISL'.swapcase() in param:
            self.LAGISL = param['LAGISL'.swapcase()]
            self.LAGISLgiven = True
        else:
            if self.LAGISLgiven == False:
                self.LAGISL = self.LAGIDL
        if 'WAGISL' in param:
            self.WAGISL = param['WAGISL']
            self.WAGISLgiven = True
        elif 'WAGISL'.swapcase() in param:
            self.WAGISL = param['WAGISL'.swapcase()]
            self.WAGISLgiven = True
        else:
            if self.WAGISLgiven == False:
                self.WAGISL = self.WAGIDL
        if 'PAGISL' in param:
            self.PAGISL = param['PAGISL']
            self.PAGISLgiven = True
        elif 'PAGISL'.swapcase() in param:
            self.PAGISL = param['PAGISL'.swapcase()]
            self.PAGISLgiven = True
        else:
            if self.PAGISLgiven == False:
                self.PAGISL = self.PAGIDL
        if 'BGISL' in param:
            self.BGISL = param['BGISL']
            self.BGISLgiven = True
        elif 'BGISL'.swapcase() in param:
            self.BGISL = param['BGISL'.swapcase()]
            self.BGISLgiven = True
        else:
            if self.BGISLgiven == False:
                self.BGISL = self.BGIDL
        if 'LBGISL' in param:
            self.LBGISL = param['LBGISL']
            self.LBGISLgiven = True
        elif 'LBGISL'.swapcase() in param:
            self.LBGISL = param['LBGISL'.swapcase()]
            self.LBGISLgiven = True
        else:
            if self.LBGISLgiven == False:
                self.LBGISL = self.LBGIDL
        if 'WBGISL' in param:
            self.WBGISL = param['WBGISL']
            self.WBGISLgiven = True
        elif 'WBGISL'.swapcase() in param:
            self.WBGISL = param['WBGISL'.swapcase()]
            self.WBGISLgiven = True
        else:
            if self.WBGISLgiven == False:
                self.WBGISL = self.WBGIDL
        if 'PBGISL' in param:
            self.PBGISL = param['PBGISL']
            self.PBGISLgiven = True
        elif 'PBGISL'.swapcase() in param:
            self.PBGISL = param['PBGISL'.swapcase()]
            self.PBGISLgiven = True
        else:
            if self.PBGISLgiven == False:
                self.PBGISL = self.PBGIDL
        if 'CGISL' in param:
            self.CGISL = param['CGISL']
            self.CGISLgiven = True
        elif 'CGISL'.swapcase() in param:
            self.CGISL = param['CGISL'.swapcase()]
            self.CGISLgiven = True
        else:
            if self.CGISLgiven == False:
                self.CGISL = self.CGIDL
        if 'LCGISL' in param:
            self.LCGISL = param['LCGISL']
            self.LCGISLgiven = True
        elif 'LCGISL'.swapcase() in param:
            self.LCGISL = param['LCGISL'.swapcase()]
            self.LCGISLgiven = True
        else:
            if self.LCGISLgiven == False:
                self.LCGISL = self.LCGIDL
        if 'WCGISL' in param:
            self.WCGISL = param['WCGISL']
            self.WCGISLgiven = True
        elif 'WCGISL'.swapcase() in param:
            self.WCGISL = param['WCGISL'.swapcase()]
            self.WCGISLgiven = True
        else:
            if self.WCGISLgiven == False:
                self.WCGISL = self.WCGIDL
        if 'PCGISL' in param:
            self.PCGISL = param['PCGISL']
            self.PCGISLgiven = True
        elif 'PCGISL'.swapcase() in param:
            self.PCGISL = param['PCGISL'.swapcase()]
            self.PCGISLgiven = True
        else:
            if self.PCGISLgiven == False:
                self.PCGISL = self.PCGIDL
        if 'EGISL' in param:
            self.EGISL = param['EGISL']
            self.EGISLgiven = True
        elif 'EGISL'.swapcase() in param:
            self.EGISL = param['EGISL'.swapcase()]
            self.EGISLgiven = True
        else:
            if self.EGISLgiven == False:
                self.EGISL = self.EGIDL
        if 'LEGISL' in param:
            self.LEGISL = param['LEGISL']
            self.LEGISLgiven = True
        elif 'LEGISL'.swapcase() in param:
            self.LEGISL = param['LEGISL'.swapcase()]
            self.LEGISLgiven = True
        else:
            if self.LEGISLgiven == False:
                self.LEGISL = self.LEGIDL
        if 'WEGISL' in param:
            self.WEGISL = param['WEGISL']
            self.WEGISLgiven = True
        elif 'WEGISL'.swapcase() in param:
            self.WEGISL = param['WEGISL'.swapcase()]
            self.WEGISLgiven = True
        else:
            if self.WEGISLgiven == False:
                self.WEGISL = self.WEGIDL
        if 'PEGISL' in param:
            self.PEGISL = param['PEGISL']
            self.PEGISLgiven = True
        elif 'PEGISL'.swapcase() in param:
            self.PEGISL = param['PEGISL'.swapcase()]
            self.PEGISLgiven = True
        else:
            if self.PEGISLgiven == False:
                self.PEGISL = self.PEGIDL
        if 'CF' in param:
            self.CF = param['CF']
            self.CFgiven = True
        elif 'CF'.swapcase() in param:
            self.CF = param['CF'.swapcase()]
            self.CFgiven = True
        else:
            if self.CFgiven == False:
                self.CF = 0.0
        if 'LCF' in param:
            self.LCF = param['LCF']
            self.LCFgiven = True
        elif 'LCF'.swapcase() in param:
            self.LCF = param['LCF'.swapcase()]
            self.LCFgiven = True
        else:
            if self.LCFgiven == False:
                self.LCF = 0.0
        if 'WCF' in param:
            self.WCF = param['WCF']
            self.WCFgiven = True
        elif 'WCF'.swapcase() in param:
            self.WCF = param['WCF'.swapcase()]
            self.WCFgiven = True
        else:
            if self.WCFgiven == False:
                self.WCF = 0.0
        if 'PCF' in param:
            self.PCF = param['PCF']
            self.PCFgiven = True
        elif 'PCF'.swapcase() in param:
            self.PCF = param['PCF'.swapcase()]
            self.PCFgiven = True
        else:
            if self.PCFgiven == False:
                self.PCF = 0.0
        if 'CFRCOEFF' in param:
            self.CFRCOEFF = param['CFRCOEFF']
            self.CFRCOEFFgiven = True
        elif 'CFRCOEFF'.swapcase() in param:
            self.CFRCOEFF = param['CFRCOEFF'.swapcase()]
            self.CFRCOEFFgiven = True
        else:
            if self.CFRCOEFFgiven == False:
                self.CFRCOEFF = 1.0
        if 'CGSO' in param:
            self.CGSO = param['CGSO']
            self.CGSOgiven = True
        elif 'CGSO'.swapcase() in param:
            self.CGSO = param['CGSO'.swapcase()]
            self.CGSOgiven = True
        else:
            if self.CGSOgiven == False:
                self.CGSO = 0.0
        if 'CGDO' in param:
            self.CGDO = param['CGDO']
            self.CGDOgiven = True
        elif 'CGDO'.swapcase() in param:
            self.CGDO = param['CGDO'.swapcase()]
            self.CGDOgiven = True
        else:
            if self.CGDOgiven == False:
                self.CGDO = 0.0
        if 'CGBO' in param:
            self.CGBO = param['CGBO']
            self.CGBOgiven = True
        elif 'CGBO'.swapcase() in param:
            self.CGBO = param['CGBO'.swapcase()]
            self.CGBOgiven = True
        else:
            if self.CGBOgiven == False:
                self.CGBO = 0.0
        if 'CGSL' in param:
            self.CGSL = param['CGSL']
            self.CGSLgiven = True
        elif 'CGSL'.swapcase() in param:
            self.CGSL = param['CGSL'.swapcase()]
            self.CGSLgiven = True
        else:
            if self.CGSLgiven == False:
                self.CGSL = 0.0
        if 'LCGSL' in param:
            self.LCGSL = param['LCGSL']
            self.LCGSLgiven = True
        elif 'LCGSL'.swapcase() in param:
            self.LCGSL = param['LCGSL'.swapcase()]
            self.LCGSLgiven = True
        else:
            if self.LCGSLgiven == False:
                self.LCGSL = 0.0
        if 'WCGSL' in param:
            self.WCGSL = param['WCGSL']
            self.WCGSLgiven = True
        elif 'WCGSL'.swapcase() in param:
            self.WCGSL = param['WCGSL'.swapcase()]
            self.WCGSLgiven = True
        else:
            if self.WCGSLgiven == False:
                self.WCGSL = 0.0
        if 'PCGSL' in param:
            self.PCGSL = param['PCGSL']
            self.PCGSLgiven = True
        elif 'PCGSL'.swapcase() in param:
            self.PCGSL = param['PCGSL'.swapcase()]
            self.PCGSLgiven = True
        else:
            if self.PCGSLgiven == False:
                self.PCGSL = 0.0
        if 'CGDL' in param:
            self.CGDL = param['CGDL']
            self.CGDLgiven = True
        elif 'CGDL'.swapcase() in param:
            self.CGDL = param['CGDL'.swapcase()]
            self.CGDLgiven = True
        else:
            if self.CGDLgiven == False:
                self.CGDL = 0.0
        if 'LCGDL' in param:
            self.LCGDL = param['LCGDL']
            self.LCGDLgiven = True
        elif 'LCGDL'.swapcase() in param:
            self.LCGDL = param['LCGDL'.swapcase()]
            self.LCGDLgiven = True
        else:
            if self.LCGDLgiven == False:
                self.LCGDL = 0.0
        if 'WCGDL' in param:
            self.WCGDL = param['WCGDL']
            self.WCGDLgiven = True
        elif 'WCGDL'.swapcase() in param:
            self.WCGDL = param['WCGDL'.swapcase()]
            self.WCGDLgiven = True
        else:
            if self.WCGDLgiven == False:
                self.WCGDL = 0.0
        if 'PCGDL' in param:
            self.PCGDL = param['PCGDL']
            self.PCGDLgiven = True
        elif 'PCGDL'.swapcase() in param:
            self.PCGDL = param['PCGDL'.swapcase()]
            self.PCGDLgiven = True
        else:
            if self.PCGDLgiven == False:
                self.PCGDL = 0.0
        if 'CKAPPAS' in param:
            self.CKAPPAS = param['CKAPPAS']
            self.CKAPPASgiven = True
        elif 'CKAPPAS'.swapcase() in param:
            self.CKAPPAS = param['CKAPPAS'.swapcase()]
            self.CKAPPASgiven = True
        else:
            if self.CKAPPASgiven == False:
                self.CKAPPAS = 0.6
        if 'LCKAPPAS' in param:
            self.LCKAPPAS = param['LCKAPPAS']
            self.LCKAPPASgiven = True
        elif 'LCKAPPAS'.swapcase() in param:
            self.LCKAPPAS = param['LCKAPPAS'.swapcase()]
            self.LCKAPPASgiven = True
        else:
            if self.LCKAPPASgiven == False:
                self.LCKAPPAS = 0.0
        if 'WCKAPPAS' in param:
            self.WCKAPPAS = param['WCKAPPAS']
            self.WCKAPPASgiven = True
        elif 'WCKAPPAS'.swapcase() in param:
            self.WCKAPPAS = param['WCKAPPAS'.swapcase()]
            self.WCKAPPASgiven = True
        else:
            if self.WCKAPPASgiven == False:
                self.WCKAPPAS = 0.0
        if 'PCKAPPAS' in param:
            self.PCKAPPAS = param['PCKAPPAS']
            self.PCKAPPASgiven = True
        elif 'PCKAPPAS'.swapcase() in param:
            self.PCKAPPAS = param['PCKAPPAS'.swapcase()]
            self.PCKAPPASgiven = True
        else:
            if self.PCKAPPASgiven == False:
                self.PCKAPPAS = 0.0
        if 'CKAPPAD' in param:
            self.CKAPPAD = param['CKAPPAD']
            self.CKAPPADgiven = True
        elif 'CKAPPAD'.swapcase() in param:
            self.CKAPPAD = param['CKAPPAD'.swapcase()]
            self.CKAPPADgiven = True
        else:
            if self.CKAPPADgiven == False:
                self.CKAPPAD = 0.6
        if 'LCKAPPAD' in param:
            self.LCKAPPAD = param['LCKAPPAD']
            self.LCKAPPADgiven = True
        elif 'LCKAPPAD'.swapcase() in param:
            self.LCKAPPAD = param['LCKAPPAD'.swapcase()]
            self.LCKAPPADgiven = True
        else:
            if self.LCKAPPADgiven == False:
                self.LCKAPPAD = 0.0
        if 'WCKAPPAD' in param:
            self.WCKAPPAD = param['WCKAPPAD']
            self.WCKAPPADgiven = True
        elif 'WCKAPPAD'.swapcase() in param:
            self.WCKAPPAD = param['WCKAPPAD'.swapcase()]
            self.WCKAPPADgiven = True
        else:
            if self.WCKAPPADgiven == False:
                self.WCKAPPAD = 0.0
        if 'PCKAPPAD' in param:
            self.PCKAPPAD = param['PCKAPPAD']
            self.PCKAPPADgiven = True
        elif 'PCKAPPAD'.swapcase() in param:
            self.PCKAPPAD = param['PCKAPPAD'.swapcase()]
            self.PCKAPPADgiven = True
        else:
            if self.PCKAPPADgiven == False:
                self.PCKAPPAD = 0.0
        if 'DMCG' in param:
            self.DMCG = param['DMCG']
            self.DMCGgiven = True
        elif 'DMCG'.swapcase() in param:
            self.DMCG = param['DMCG'.swapcase()]
            self.DMCGgiven = True
        else:
            if self.DMCGgiven == False:
                self.DMCG = 0.0
        if 'DMCI' in param:
            self.DMCI = param['DMCI']
            self.DMCIgiven = True
        elif 'DMCI'.swapcase() in param:
            self.DMCI = param['DMCI'.swapcase()]
            self.DMCIgiven = True
        else:
            if self.DMCIgiven == False:
                self.DMCI = self.DMCG
        if 'DMDG' in param:
            self.DMDG = param['DMDG']
            self.DMDGgiven = True
        elif 'DMDG'.swapcase() in param:
            self.DMDG = param['DMDG'.swapcase()]
            self.DMDGgiven = True
        else:
            if self.DMDGgiven == False:
                self.DMDG = 0.0
        if 'DMCGT' in param:
            self.DMCGT = param['DMCGT']
            self.DMCGTgiven = True
        elif 'DMCGT'.swapcase() in param:
            self.DMCGT = param['DMCGT'.swapcase()]
            self.DMCGTgiven = True
        else:
            if self.DMCGTgiven == False:
                self.DMCGT = 0.0
        if 'XGL' in param:
            self.XGL = param['XGL']
            self.XGLgiven = True
        elif 'XGL'.swapcase() in param:
            self.XGL = param['XGL'.swapcase()]
            self.XGLgiven = True
        else:
            if self.XGLgiven == False:
                self.XGL = 0.0
        if 'RSHG' in param:
            self.RSHG = param['RSHG']
            self.RSHGgiven = True
        elif 'RSHG'.swapcase() in param:
            self.RSHG = param['RSHG'.swapcase()]
            self.RSHGgiven = True
        else:
            if self.RSHGgiven == False:
                self.RSHG = 0.1
        if 'CJS' in param:
            self.CJS = param['CJS']
            self.CJSgiven = True
        elif 'CJS'.swapcase() in param:
            self.CJS = param['CJS'.swapcase()]
            self.CJSgiven = True
        else:
            if self.CJSgiven == False:
                self.CJS = 0.0005
        if 'CJD' in param:
            self.CJD = param['CJD']
            self.CJDgiven = True
        elif 'CJD'.swapcase() in param:
            self.CJD = param['CJD'.swapcase()]
            self.CJDgiven = True
        else:
            if self.CJDgiven == False:
                self.CJD = self.CJS
        if 'CJSWS' in param:
            self.CJSWS = param['CJSWS']
            self.CJSWSgiven = True
        elif 'CJSWS'.swapcase() in param:
            self.CJSWS = param['CJSWS'.swapcase()]
            self.CJSWSgiven = True
        else:
            if self.CJSWSgiven == False:
                self.CJSWS = 5e-10
        if 'CJSWD' in param:
            self.CJSWD = param['CJSWD']
            self.CJSWDgiven = True
        elif 'CJSWD'.swapcase() in param:
            self.CJSWD = param['CJSWD'.swapcase()]
            self.CJSWDgiven = True
        else:
            if self.CJSWDgiven == False:
                self.CJSWD = self.CJSWS
        if 'CJSWGS' in param:
            self.CJSWGS = param['CJSWGS']
            self.CJSWGSgiven = True
        elif 'CJSWGS'.swapcase() in param:
            self.CJSWGS = param['CJSWGS'.swapcase()]
            self.CJSWGSgiven = True
        else:
            if self.CJSWGSgiven == False:
                self.CJSWGS = 0.0
        if 'CJSWGD' in param:
            self.CJSWGD = param['CJSWGD']
            self.CJSWGDgiven = True
        elif 'CJSWGD'.swapcase() in param:
            self.CJSWGD = param['CJSWGD'.swapcase()]
            self.CJSWGDgiven = True
        else:
            if self.CJSWGDgiven == False:
                self.CJSWGD = self.CJSWGS
        if 'PBS' in param:
            self.PBS = param['PBS']
            self.PBSgiven = True
        elif 'PBS'.swapcase() in param:
            self.PBS = param['PBS'.swapcase()]
            self.PBSgiven = True
        else:
            if self.PBSgiven == False:
                self.PBS = 1.0
        if 'PBD' in param:
            self.PBD = param['PBD']
            self.PBDgiven = True
        elif 'PBD'.swapcase() in param:
            self.PBD = param['PBD'.swapcase()]
            self.PBDgiven = True
        else:
            if self.PBDgiven == False:
                self.PBD = self.PBS
        if 'PBSWS' in param:
            self.PBSWS = param['PBSWS']
            self.PBSWSgiven = True
        elif 'PBSWS'.swapcase() in param:
            self.PBSWS = param['PBSWS'.swapcase()]
            self.PBSWSgiven = True
        else:
            if self.PBSWSgiven == False:
                self.PBSWS = 1.0
        if 'PBSWD' in param:
            self.PBSWD = param['PBSWD']
            self.PBSWDgiven = True
        elif 'PBSWD'.swapcase() in param:
            self.PBSWD = param['PBSWD'.swapcase()]
            self.PBSWDgiven = True
        else:
            if self.PBSWDgiven == False:
                self.PBSWD = self.PBSWS
        if 'PBSWGS' in param:
            self.PBSWGS = param['PBSWGS']
            self.PBSWGSgiven = True
        elif 'PBSWGS'.swapcase() in param:
            self.PBSWGS = param['PBSWGS'.swapcase()]
            self.PBSWGSgiven = True
        else:
            if self.PBSWGSgiven == False:
                self.PBSWGS = self.PBSWS
        if 'PBSWGD' in param:
            self.PBSWGD = param['PBSWGD']
            self.PBSWGDgiven = True
        elif 'PBSWGD'.swapcase() in param:
            self.PBSWGD = param['PBSWGD'.swapcase()]
            self.PBSWGDgiven = True
        else:
            if self.PBSWGDgiven == False:
                self.PBSWGD = self.PBSWGS
        if 'MJS' in param:
            self.MJS = param['MJS']
            self.MJSgiven = True
        elif 'MJS'.swapcase() in param:
            self.MJS = param['MJS'.swapcase()]
            self.MJSgiven = True
        else:
            if self.MJSgiven == False:
                self.MJS = 0.5
        if 'MJD' in param:
            self.MJD = param['MJD']
            self.MJDgiven = True
        elif 'MJD'.swapcase() in param:
            self.MJD = param['MJD'.swapcase()]
            self.MJDgiven = True
        else:
            if self.MJDgiven == False:
                self.MJD = self.MJS
        if 'MJSWS' in param:
            self.MJSWS = param['MJSWS']
            self.MJSWSgiven = True
        elif 'MJSWS'.swapcase() in param:
            self.MJSWS = param['MJSWS'.swapcase()]
            self.MJSWSgiven = True
        else:
            if self.MJSWSgiven == False:
                self.MJSWS = 0.33
        if 'MJSWD' in param:
            self.MJSWD = param['MJSWD']
            self.MJSWDgiven = True
        elif 'MJSWD'.swapcase() in param:
            self.MJSWD = param['MJSWD'.swapcase()]
            self.MJSWDgiven = True
        else:
            if self.MJSWDgiven == False:
                self.MJSWD = self.MJSWS
        if 'MJSWGS' in param:
            self.MJSWGS = param['MJSWGS']
            self.MJSWGSgiven = True
        elif 'MJSWGS'.swapcase() in param:
            self.MJSWGS = param['MJSWGS'.swapcase()]
            self.MJSWGSgiven = True
        else:
            if self.MJSWGSgiven == False:
                self.MJSWGS = self.MJSWS
        if 'MJSWGD' in param:
            self.MJSWGD = param['MJSWGD']
            self.MJSWGDgiven = True
        elif 'MJSWGD'.swapcase() in param:
            self.MJSWGD = param['MJSWGD'.swapcase()]
            self.MJSWGDgiven = True
        else:
            if self.MJSWGDgiven == False:
                self.MJSWGD = self.MJSWGS
        if 'JSS' in param:
            self.JSS = param['JSS']
            self.JSSgiven = True
        elif 'JSS'.swapcase() in param:
            self.JSS = param['JSS'.swapcase()]
            self.JSSgiven = True
        else:
            if self.JSSgiven == False:
                self.JSS = 0.0001
        if 'JSD' in param:
            self.JSD = param['JSD']
            self.JSDgiven = True
        elif 'JSD'.swapcase() in param:
            self.JSD = param['JSD'.swapcase()]
            self.JSDgiven = True
        else:
            if self.JSDgiven == False:
                self.JSD = self.JSS
        if 'JSWS' in param:
            self.JSWS = param['JSWS']
            self.JSWSgiven = True
        elif 'JSWS'.swapcase() in param:
            self.JSWS = param['JSWS'.swapcase()]
            self.JSWSgiven = True
        else:
            if self.JSWSgiven == False:
                self.JSWS = 0.0
        if 'JSWD' in param:
            self.JSWD = param['JSWD']
            self.JSWDgiven = True
        elif 'JSWD'.swapcase() in param:
            self.JSWD = param['JSWD'.swapcase()]
            self.JSWDgiven = True
        else:
            if self.JSWDgiven == False:
                self.JSWD = self.JSWS
        if 'JSWGS' in param:
            self.JSWGS = param['JSWGS']
            self.JSWGSgiven = True
        elif 'JSWGS'.swapcase() in param:
            self.JSWGS = param['JSWGS'.swapcase()]
            self.JSWGSgiven = True
        else:
            if self.JSWGSgiven == False:
                self.JSWGS = 0.0
        if 'JSWGD' in param:
            self.JSWGD = param['JSWGD']
            self.JSWGDgiven = True
        elif 'JSWGD'.swapcase() in param:
            self.JSWGD = param['JSWGD'.swapcase()]
            self.JSWGDgiven = True
        else:
            if self.JSWGDgiven == False:
                self.JSWGD = self.JSWGS
        if 'NJS' in param:
            self.NJS = param['NJS']
            self.NJSgiven = True
        elif 'NJS'.swapcase() in param:
            self.NJS = param['NJS'.swapcase()]
            self.NJSgiven = True
        else:
            if self.NJSgiven == False:
                self.NJS = 1.0
        if 'NJD' in param:
            self.NJD = param['NJD']
            self.NJDgiven = True
        elif 'NJD'.swapcase() in param:
            self.NJD = param['NJD'.swapcase()]
            self.NJDgiven = True
        else:
            if self.NJDgiven == False:
                self.NJD = self.NJS
        if 'IJTHSFWD' in param:
            self.IJTHSFWD = param['IJTHSFWD']
            self.IJTHSFWDgiven = True
        elif 'IJTHSFWD'.swapcase() in param:
            self.IJTHSFWD = param['IJTHSFWD'.swapcase()]
            self.IJTHSFWDgiven = True
        else:
            if self.IJTHSFWDgiven == False:
                self.IJTHSFWD = 0.1
        if 'IJTHDFWD' in param:
            self.IJTHDFWD = param['IJTHDFWD']
            self.IJTHDFWDgiven = True
        elif 'IJTHDFWD'.swapcase() in param:
            self.IJTHDFWD = param['IJTHDFWD'.swapcase()]
            self.IJTHDFWDgiven = True
        else:
            if self.IJTHDFWDgiven == False:
                self.IJTHDFWD = self.IJTHSFWD
        if 'IJTHSREV' in param:
            self.IJTHSREV = param['IJTHSREV']
            self.IJTHSREVgiven = True
        elif 'IJTHSREV'.swapcase() in param:
            self.IJTHSREV = param['IJTHSREV'.swapcase()]
            self.IJTHSREVgiven = True
        else:
            if self.IJTHSREVgiven == False:
                self.IJTHSREV = 0.1
        if 'IJTHDREV' in param:
            self.IJTHDREV = param['IJTHDREV']
            self.IJTHDREVgiven = True
        elif 'IJTHDREV'.swapcase() in param:
            self.IJTHDREV = param['IJTHDREV'.swapcase()]
            self.IJTHDREVgiven = True
        else:
            if self.IJTHDREVgiven == False:
                self.IJTHDREV = self.IJTHSREV
        if 'BVS' in param:
            self.BVS = param['BVS']
            self.BVSgiven = True
        elif 'BVS'.swapcase() in param:
            self.BVS = param['BVS'.swapcase()]
            self.BVSgiven = True
        else:
            if self.BVSgiven == False:
                self.BVS = 10.0
        if 'BVD' in param:
            self.BVD = param['BVD']
            self.BVDgiven = True
        elif 'BVD'.swapcase() in param:
            self.BVD = param['BVD'.swapcase()]
            self.BVDgiven = True
        else:
            if self.BVDgiven == False:
                self.BVD = self.BVS
        if 'XJBVS' in param:
            self.XJBVS = param['XJBVS']
            self.XJBVSgiven = True
        elif 'XJBVS'.swapcase() in param:
            self.XJBVS = param['XJBVS'.swapcase()]
            self.XJBVSgiven = True
        else:
            if self.XJBVSgiven == False:
                self.XJBVS = 1.0
        if 'XJBVD' in param:
            self.XJBVD = param['XJBVD']
            self.XJBVDgiven = True
        elif 'XJBVD'.swapcase() in param:
            self.XJBVD = param['XJBVD'.swapcase()]
            self.XJBVDgiven = True
        else:
            if self.XJBVDgiven == False:
                self.XJBVD = self.XJBVS
        if 'JTSS' in param:
            self.JTSS = param['JTSS']
            self.JTSSgiven = True
        elif 'JTSS'.swapcase() in param:
            self.JTSS = param['JTSS'.swapcase()]
            self.JTSSgiven = True
        else:
            if self.JTSSgiven == False:
                self.JTSS = 0.0
        if 'JTSD' in param:
            self.JTSD = param['JTSD']
            self.JTSDgiven = True
        elif 'JTSD'.swapcase() in param:
            self.JTSD = param['JTSD'.swapcase()]
            self.JTSDgiven = True
        else:
            if self.JTSDgiven == False:
                self.JTSD = self.JTSS
        if 'JTSSWS' in param:
            self.JTSSWS = param['JTSSWS']
            self.JTSSWSgiven = True
        elif 'JTSSWS'.swapcase() in param:
            self.JTSSWS = param['JTSSWS'.swapcase()]
            self.JTSSWSgiven = True
        else:
            if self.JTSSWSgiven == False:
                self.JTSSWS = 0.0
        if 'JTSSWD' in param:
            self.JTSSWD = param['JTSSWD']
            self.JTSSWDgiven = True
        elif 'JTSSWD'.swapcase() in param:
            self.JTSSWD = param['JTSSWD'.swapcase()]
            self.JTSSWDgiven = True
        else:
            if self.JTSSWDgiven == False:
                self.JTSSWD = self.JTSSWS
        if 'JTSSWGS' in param:
            self.JTSSWGS = param['JTSSWGS']
            self.JTSSWGSgiven = True
        elif 'JTSSWGS'.swapcase() in param:
            self.JTSSWGS = param['JTSSWGS'.swapcase()]
            self.JTSSWGSgiven = True
        else:
            if self.JTSSWGSgiven == False:
                self.JTSSWGS = 0.0
        if 'JTSSWGD' in param:
            self.JTSSWGD = param['JTSSWGD']
            self.JTSSWGDgiven = True
        elif 'JTSSWGD'.swapcase() in param:
            self.JTSSWGD = param['JTSSWGD'.swapcase()]
            self.JTSSWGDgiven = True
        else:
            if self.JTSSWGDgiven == False:
                self.JTSSWGD = self.JTSSWGS
        if 'JTWEFF' in param:
            self.JTWEFF = param['JTWEFF']
            self.JTWEFFgiven = True
        elif 'JTWEFF'.swapcase() in param:
            self.JTWEFF = param['JTWEFF'.swapcase()]
            self.JTWEFFgiven = True
        else:
            if self.JTWEFFgiven == False:
                self.JTWEFF = 0.0
        if 'NJTS' in param:
            self.NJTS = param['NJTS']
            self.NJTSgiven = True
        elif 'NJTS'.swapcase() in param:
            self.NJTS = param['NJTS'.swapcase()]
            self.NJTSgiven = True
        else:
            if self.NJTSgiven == False:
                self.NJTS = 20.0
        if 'NJTSD' in param:
            self.NJTSD = param['NJTSD']
            self.NJTSDgiven = True
        elif 'NJTSD'.swapcase() in param:
            self.NJTSD = param['NJTSD'.swapcase()]
            self.NJTSDgiven = True
        else:
            if self.NJTSDgiven == False:
                self.NJTSD = self.NJTS
        if 'NJTSSW' in param:
            self.NJTSSW = param['NJTSSW']
            self.NJTSSWgiven = True
        elif 'NJTSSW'.swapcase() in param:
            self.NJTSSW = param['NJTSSW'.swapcase()]
            self.NJTSSWgiven = True
        else:
            if self.NJTSSWgiven == False:
                self.NJTSSW = 20.0
        if 'NJTSSWD' in param:
            self.NJTSSWD = param['NJTSSWD']
            self.NJTSSWDgiven = True
        elif 'NJTSSWD'.swapcase() in param:
            self.NJTSSWD = param['NJTSSWD'.swapcase()]
            self.NJTSSWDgiven = True
        else:
            if self.NJTSSWDgiven == False:
                self.NJTSSWD = self.NJTSSW
        if 'NJTSSWG' in param:
            self.NJTSSWG = param['NJTSSWG']
            self.NJTSSWGgiven = True
        elif 'NJTSSWG'.swapcase() in param:
            self.NJTSSWG = param['NJTSSWG'.swapcase()]
            self.NJTSSWGgiven = True
        else:
            if self.NJTSSWGgiven == False:
                self.NJTSSWG = 20.0
        if 'NJTSSWGD' in param:
            self.NJTSSWGD = param['NJTSSWGD']
            self.NJTSSWGDgiven = True
        elif 'NJTSSWGD'.swapcase() in param:
            self.NJTSSWGD = param['NJTSSWGD'.swapcase()]
            self.NJTSSWGDgiven = True
        else:
            if self.NJTSSWGDgiven == False:
                self.NJTSSWGD = self.NJTSSWG
        if 'VTSS' in param:
            self.VTSS = param['VTSS']
            self.VTSSgiven = True
        elif 'VTSS'.swapcase() in param:
            self.VTSS = param['VTSS'.swapcase()]
            self.VTSSgiven = True
        else:
            if self.VTSSgiven == False:
                self.VTSS = 10.0
        if 'VTSD' in param:
            self.VTSD = param['VTSD']
            self.VTSDgiven = True
        elif 'VTSD'.swapcase() in param:
            self.VTSD = param['VTSD'.swapcase()]
            self.VTSDgiven = True
        else:
            if self.VTSDgiven == False:
                self.VTSD = self.VTSS
        if 'VTSSWS' in param:
            self.VTSSWS = param['VTSSWS']
            self.VTSSWSgiven = True
        elif 'VTSSWS'.swapcase() in param:
            self.VTSSWS = param['VTSSWS'.swapcase()]
            self.VTSSWSgiven = True
        else:
            if self.VTSSWSgiven == False:
                self.VTSSWS = 10.0
        if 'VTSSWD' in param:
            self.VTSSWD = param['VTSSWD']
            self.VTSSWDgiven = True
        elif 'VTSSWD'.swapcase() in param:
            self.VTSSWD = param['VTSSWD'.swapcase()]
            self.VTSSWDgiven = True
        else:
            if self.VTSSWDgiven == False:
                self.VTSSWD = self.VTSSWS
        if 'VTSSWGS' in param:
            self.VTSSWGS = param['VTSSWGS']
            self.VTSSWGSgiven = True
        elif 'VTSSWGS'.swapcase() in param:
            self.VTSSWGS = param['VTSSWGS'.swapcase()]
            self.VTSSWGSgiven = True
        else:
            if self.VTSSWGSgiven == False:
                self.VTSSWGS = 10.0
        if 'VTSSWGD' in param:
            self.VTSSWGD = param['VTSSWGD']
            self.VTSSWGDgiven = True
        elif 'VTSSWGD'.swapcase() in param:
            self.VTSSWGD = param['VTSSWGD'.swapcase()]
            self.VTSSWGDgiven = True
        else:
            if self.VTSSWGDgiven == False:
                self.VTSSWGD = self.VTSSWGS
        if 'XRCRG1' in param:
            self.XRCRG1 = param['XRCRG1']
            self.XRCRG1given = True
        elif 'XRCRG1'.swapcase() in param:
            self.XRCRG1 = param['XRCRG1'.swapcase()]
            self.XRCRG1given = True
        else:
            if self.XRCRG1given == False:
                self.XRCRG1 = 12.0
        if 'XRCRG2' in param:
            self.XRCRG2 = param['XRCRG2']
            self.XRCRG2given = True
        elif 'XRCRG2'.swapcase() in param:
            self.XRCRG2 = param['XRCRG2'.swapcase()]
            self.XRCRG2given = True
        else:
            if self.XRCRG2given == False:
                self.XRCRG2 = 1.0
        if 'GBMIN' in param:
            self.GBMIN = param['GBMIN']
            self.GBMINgiven = True
        elif 'GBMIN'.swapcase() in param:
            self.GBMIN = param['GBMIN'.swapcase()]
            self.GBMINgiven = True
        else:
            if self.GBMINgiven == False:
                self.GBMIN = 1e-12
        if 'RBPS0' in param:
            self.RBPS0 = param['RBPS0']
            self.RBPS0given = True
        elif 'RBPS0'.swapcase() in param:
            self.RBPS0 = param['RBPS0'.swapcase()]
            self.RBPS0given = True
        else:
            if self.RBPS0given == False:
                self.RBPS0 = 50.0
        if 'RBPSL' in param:
            self.RBPSL = param['RBPSL']
            self.RBPSLgiven = True
        elif 'RBPSL'.swapcase() in param:
            self.RBPSL = param['RBPSL'.swapcase()]
            self.RBPSLgiven = True
        else:
            if self.RBPSLgiven == False:
                self.RBPSL = 0.0
        if 'RBPSW' in param:
            self.RBPSW = param['RBPSW']
            self.RBPSWgiven = True
        elif 'RBPSW'.swapcase() in param:
            self.RBPSW = param['RBPSW'.swapcase()]
            self.RBPSWgiven = True
        else:
            if self.RBPSWgiven == False:
                self.RBPSW = 0.0
        if 'RBPSNF' in param:
            self.RBPSNF = param['RBPSNF']
            self.RBPSNFgiven = True
        elif 'RBPSNF'.swapcase() in param:
            self.RBPSNF = param['RBPSNF'.swapcase()]
            self.RBPSNFgiven = True
        else:
            if self.RBPSNFgiven == False:
                self.RBPSNF = 0.0
        if 'RBPD0' in param:
            self.RBPD0 = param['RBPD0']
            self.RBPD0given = True
        elif 'RBPD0'.swapcase() in param:
            self.RBPD0 = param['RBPD0'.swapcase()]
            self.RBPD0given = True
        else:
            if self.RBPD0given == False:
                self.RBPD0 = 50.0
        if 'RBPDL' in param:
            self.RBPDL = param['RBPDL']
            self.RBPDLgiven = True
        elif 'RBPDL'.swapcase() in param:
            self.RBPDL = param['RBPDL'.swapcase()]
            self.RBPDLgiven = True
        else:
            if self.RBPDLgiven == False:
                self.RBPDL = 0.0
        if 'RBPDW' in param:
            self.RBPDW = param['RBPDW']
            self.RBPDWgiven = True
        elif 'RBPDW'.swapcase() in param:
            self.RBPDW = param['RBPDW'.swapcase()]
            self.RBPDWgiven = True
        else:
            if self.RBPDWgiven == False:
                self.RBPDW = 0.0
        if 'RBPDNF' in param:
            self.RBPDNF = param['RBPDNF']
            self.RBPDNFgiven = True
        elif 'RBPDNF'.swapcase() in param:
            self.RBPDNF = param['RBPDNF'.swapcase()]
            self.RBPDNFgiven = True
        else:
            if self.RBPDNFgiven == False:
                self.RBPDNF = 0.0
        if 'RBPBX0' in param:
            self.RBPBX0 = param['RBPBX0']
            self.RBPBX0given = True
        elif 'RBPBX0'.swapcase() in param:
            self.RBPBX0 = param['RBPBX0'.swapcase()]
            self.RBPBX0given = True
        else:
            if self.RBPBX0given == False:
                self.RBPBX0 = 100.0
        if 'RBPBXL' in param:
            self.RBPBXL = param['RBPBXL']
            self.RBPBXLgiven = True
        elif 'RBPBXL'.swapcase() in param:
            self.RBPBXL = param['RBPBXL'.swapcase()]
            self.RBPBXLgiven = True
        else:
            if self.RBPBXLgiven == False:
                self.RBPBXL = 0.0
        if 'RBPBXW' in param:
            self.RBPBXW = param['RBPBXW']
            self.RBPBXWgiven = True
        elif 'RBPBXW'.swapcase() in param:
            self.RBPBXW = param['RBPBXW'.swapcase()]
            self.RBPBXWgiven = True
        else:
            if self.RBPBXWgiven == False:
                self.RBPBXW = 0.0
        if 'RBPBXNF' in param:
            self.RBPBXNF = param['RBPBXNF']
            self.RBPBXNFgiven = True
        elif 'RBPBXNF'.swapcase() in param:
            self.RBPBXNF = param['RBPBXNF'.swapcase()]
            self.RBPBXNFgiven = True
        else:
            if self.RBPBXNFgiven == False:
                self.RBPBXNF = 0.0
        if 'RBPBY0' in param:
            self.RBPBY0 = param['RBPBY0']
            self.RBPBY0given = True
        elif 'RBPBY0'.swapcase() in param:
            self.RBPBY0 = param['RBPBY0'.swapcase()]
            self.RBPBY0given = True
        else:
            if self.RBPBY0given == False:
                self.RBPBY0 = 100.0
        if 'RBPBYL' in param:
            self.RBPBYL = param['RBPBYL']
            self.RBPBYLgiven = True
        elif 'RBPBYL'.swapcase() in param:
            self.RBPBYL = param['RBPBYL'.swapcase()]
            self.RBPBYLgiven = True
        else:
            if self.RBPBYLgiven == False:
                self.RBPBYL = 0.0
        if 'RBPBYW' in param:
            self.RBPBYW = param['RBPBYW']
            self.RBPBYWgiven = True
        elif 'RBPBYW'.swapcase() in param:
            self.RBPBYW = param['RBPBYW'.swapcase()]
            self.RBPBYWgiven = True
        else:
            if self.RBPBYWgiven == False:
                self.RBPBYW = 0.0
        if 'RBPBYNF' in param:
            self.RBPBYNF = param['RBPBYNF']
            self.RBPBYNFgiven = True
        elif 'RBPBYNF'.swapcase() in param:
            self.RBPBYNF = param['RBPBYNF'.swapcase()]
            self.RBPBYNFgiven = True
        else:
            if self.RBPBYNFgiven == False:
                self.RBPBYNF = 0.0
        if 'RBSBX0' in param:
            self.RBSBX0 = param['RBSBX0']
            self.RBSBX0given = True
        elif 'RBSBX0'.swapcase() in param:
            self.RBSBX0 = param['RBSBX0'.swapcase()]
            self.RBSBX0given = True
        else:
            if self.RBSBX0given == False:
                self.RBSBX0 = 100.0
        if 'RBSBY0' in param:
            self.RBSBY0 = param['RBSBY0']
            self.RBSBY0given = True
        elif 'RBSBY0'.swapcase() in param:
            self.RBSBY0 = param['RBSBY0'.swapcase()]
            self.RBSBY0given = True
        else:
            if self.RBSBY0given == False:
                self.RBSBY0 = 100.0
        if 'RBDBX0' in param:
            self.RBDBX0 = param['RBDBX0']
            self.RBDBX0given = True
        elif 'RBDBX0'.swapcase() in param:
            self.RBDBX0 = param['RBDBX0'.swapcase()]
            self.RBDBX0given = True
        else:
            if self.RBDBX0given == False:
                self.RBDBX0 = 100.0
        if 'RBDBY0' in param:
            self.RBDBY0 = param['RBDBY0']
            self.RBDBY0given = True
        elif 'RBDBY0'.swapcase() in param:
            self.RBDBY0 = param['RBDBY0'.swapcase()]
            self.RBDBY0given = True
        else:
            if self.RBDBY0given == False:
                self.RBDBY0 = 100.0
        if 'RBSDBXL' in param:
            self.RBSDBXL = param['RBSDBXL']
            self.RBSDBXLgiven = True
        elif 'RBSDBXL'.swapcase() in param:
            self.RBSDBXL = param['RBSDBXL'.swapcase()]
            self.RBSDBXLgiven = True
        else:
            if self.RBSDBXLgiven == False:
                self.RBSDBXL = 0.0
        if 'RBSDBXW' in param:
            self.RBSDBXW = param['RBSDBXW']
            self.RBSDBXWgiven = True
        elif 'RBSDBXW'.swapcase() in param:
            self.RBSDBXW = param['RBSDBXW'.swapcase()]
            self.RBSDBXWgiven = True
        else:
            if self.RBSDBXWgiven == False:
                self.RBSDBXW = 0.0
        if 'RBSDBXNF' in param:
            self.RBSDBXNF = param['RBSDBXNF']
            self.RBSDBXNFgiven = True
        elif 'RBSDBXNF'.swapcase() in param:
            self.RBSDBXNF = param['RBSDBXNF'.swapcase()]
            self.RBSDBXNFgiven = True
        else:
            if self.RBSDBXNFgiven == False:
                self.RBSDBXNF = 0.0
        if 'RBSDBYL' in param:
            self.RBSDBYL = param['RBSDBYL']
            self.RBSDBYLgiven = True
        elif 'RBSDBYL'.swapcase() in param:
            self.RBSDBYL = param['RBSDBYL'.swapcase()]
            self.RBSDBYLgiven = True
        else:
            if self.RBSDBYLgiven == False:
                self.RBSDBYL = 0.0
        if 'RBSDBYW' in param:
            self.RBSDBYW = param['RBSDBYW']
            self.RBSDBYWgiven = True
        elif 'RBSDBYW'.swapcase() in param:
            self.RBSDBYW = param['RBSDBYW'.swapcase()]
            self.RBSDBYWgiven = True
        else:
            if self.RBSDBYWgiven == False:
                self.RBSDBYW = 0.0
        if 'RBSDBYNF' in param:
            self.RBSDBYNF = param['RBSDBYNF']
            self.RBSDBYNFgiven = True
        elif 'RBSDBYNF'.swapcase() in param:
            self.RBSDBYNF = param['RBSDBYNF'.swapcase()]
            self.RBSDBYNFgiven = True
        else:
            if self.RBSDBYNFgiven == False:
                self.RBSDBYNF = 0.0
        if 'EF' in param:
            self.EF = param['EF']
            self.EFgiven = True
        elif 'EF'.swapcase() in param:
            self.EF = param['EF'.swapcase()]
            self.EFgiven = True
        else:
            if self.EFgiven == False:
                self.EF = 1.0
        if 'EM' in param:
            self.EM = param['EM']
            self.EMgiven = True
        elif 'EM'.swapcase() in param:
            self.EM = param['EM'.swapcase()]
            self.EMgiven = True
        else:
            if self.EMgiven == False:
                self.EM = 41000000.0
        if 'NOIA' in param:
            self.NOIA = param['NOIA']
            self.NOIAgiven = True
        elif 'NOIA'.swapcase() in param:
            self.NOIA = param['NOIA'.swapcase()]
            self.NOIAgiven = True
        else:
            if self.NOIAgiven == False:
                self.NOIA = 6.25e+40
        if 'NOIB' in param:
            self.NOIB = param['NOIB']
            self.NOIBgiven = True
        elif 'NOIB'.swapcase() in param:
            self.NOIB = param['NOIB'.swapcase()]
            self.NOIBgiven = True
        else:
            if self.NOIBgiven == False:
                self.NOIB = 3.125e+25
        if 'NOIC' in param:
            self.NOIC = param['NOIC']
            self.NOICgiven = True
        elif 'NOIC'.swapcase() in param:
            self.NOIC = param['NOIC'.swapcase()]
            self.NOICgiven = True
        else:
            if self.NOICgiven == False:
                self.NOIC = 875000000.0
        if 'LINTNOI' in param:
            self.LINTNOI = param['LINTNOI']
            self.LINTNOIgiven = True
        elif 'LINTNOI'.swapcase() in param:
            self.LINTNOI = param['LINTNOI'.swapcase()]
            self.LINTNOIgiven = True
        else:
            if self.LINTNOIgiven == False:
                self.LINTNOI = 0.0
        if 'NOIA1' in param:
            self.NOIA1 = param['NOIA1']
            self.NOIA1given = True
        elif 'NOIA1'.swapcase() in param:
            self.NOIA1 = param['NOIA1'.swapcase()]
            self.NOIA1given = True
        else:
            if self.NOIA1given == False:
                self.NOIA1 = 0.0
        if 'NOIAX' in param:
            self.NOIAX = param['NOIAX']
            self.NOIAXgiven = True
        elif 'NOIAX'.swapcase() in param:
            self.NOIAX = param['NOIAX'.swapcase()]
            self.NOIAXgiven = True
        else:
            if self.NOIAXgiven == False:
                self.NOIAX = 1.0
        if 'NTNOI' in param:
            self.NTNOI = param['NTNOI']
            self.NTNOIgiven = True
        elif 'NTNOI'.swapcase() in param:
            self.NTNOI = param['NTNOI'.swapcase()]
            self.NTNOIgiven = True
        else:
            if self.NTNOIgiven == False:
                self.NTNOI = 1.0
        if 'RNOIA' in param:
            self.RNOIA = param['RNOIA']
            self.RNOIAgiven = True
        elif 'RNOIA'.swapcase() in param:
            self.RNOIA = param['RNOIA'.swapcase()]
            self.RNOIAgiven = True
        else:
            if self.RNOIAgiven == False:
                self.RNOIA = 0.577
        if 'RNOIB' in param:
            self.RNOIB = param['RNOIB']
            self.RNOIBgiven = True
        elif 'RNOIB'.swapcase() in param:
            self.RNOIB = param['RNOIB'.swapcase()]
            self.RNOIBgiven = True
        else:
            if self.RNOIBgiven == False:
                self.RNOIB = 0.5164
        if 'RNOIC' in param:
            self.RNOIC = param['RNOIC']
            self.RNOICgiven = True
        elif 'RNOIC'.swapcase() in param:
            self.RNOIC = param['RNOIC'.swapcase()]
            self.RNOICgiven = True
        else:
            if self.RNOICgiven == False:
                self.RNOIC = 0.395
        if 'TNOIA' in param:
            self.TNOIA = param['TNOIA']
            self.TNOIAgiven = True
        elif 'TNOIA'.swapcase() in param:
            self.TNOIA = param['TNOIA'.swapcase()]
            self.TNOIAgiven = True
        else:
            if self.TNOIAgiven == False:
                self.TNOIA = 1.5
        if 'TNOIB' in param:
            self.TNOIB = param['TNOIB']
            self.TNOIBgiven = True
        elif 'TNOIB'.swapcase() in param:
            self.TNOIB = param['TNOIB'.swapcase()]
            self.TNOIBgiven = True
        else:
            if self.TNOIBgiven == False:
                self.TNOIB = 3.5
        if 'TNOIC' in param:
            self.TNOIC = param['TNOIC']
            self.TNOICgiven = True
        elif 'TNOIC'.swapcase() in param:
            self.TNOIC = param['TNOIC'.swapcase()]
            self.TNOICgiven = True
        else:
            if self.TNOICgiven == False:
                self.TNOIC = 0.0
        if 'BINUNIT' in param:
            self.BINUNIT = param['BINUNIT']
            self.BINUNITgiven = True
        elif 'BINUNIT'.swapcase() in param:
            self.BINUNIT = param['BINUNIT'.swapcase()]
            self.BINUNITgiven = True
        else:
            if self.BINUNITgiven == False:
                self.BINUNIT = 1.0
        if 'DLBIN' in param:
            self.DLBIN = param['DLBIN']
            self.DLBINgiven = True
        elif 'DLBIN'.swapcase() in param:
            self.DLBIN = param['DLBIN'.swapcase()]
            self.DLBINgiven = True
        else:
            if self.DLBINgiven == False:
                self.DLBIN = 0.0
        if 'DWBIN' in param:
            self.DWBIN = param['DWBIN']
            self.DWBINgiven = True
        elif 'DWBIN'.swapcase() in param:
            self.DWBIN = param['DWBIN'.swapcase()]
            self.DWBINgiven = True
        else:
            if self.DWBINgiven == False:
                self.DWBIN = 0.0
        if 'TNOM' in param:
            self.TNOM = param['TNOM']
            self.TNOMgiven = True
        elif 'TNOM'.swapcase() in param:
            self.TNOM = param['TNOM'.swapcase()]
            self.TNOMgiven = True
        else:
            if self.TNOMgiven == False:
                self.TNOM = 27.0
        if 'TBGASUB' in param:
            self.TBGASUB = param['TBGASUB']
            self.TBGASUBgiven = True
        elif 'TBGASUB'.swapcase() in param:
            self.TBGASUB = param['TBGASUB'.swapcase()]
            self.TBGASUBgiven = True
        else:
            if self.TBGASUBgiven == False:
                self.TBGASUB = 0.000473
        if 'TBGBSUB' in param:
            self.TBGBSUB = param['TBGBSUB']
            self.TBGBSUBgiven = True
        elif 'TBGBSUB'.swapcase() in param:
            self.TBGBSUB = param['TBGBSUB'.swapcase()]
            self.TBGBSUBgiven = True
        else:
            if self.TBGBSUBgiven == False:
                self.TBGBSUB = 636.0
        if 'TNFACTOR' in param:
            self.TNFACTOR = param['TNFACTOR']
            self.TNFACTORgiven = True
        elif 'TNFACTOR'.swapcase() in param:
            self.TNFACTOR = param['TNFACTOR'.swapcase()]
            self.TNFACTORgiven = True
        else:
            if self.TNFACTORgiven == False:
                self.TNFACTOR = 0.0
        if 'UTE' in param:
            self.UTE = param['UTE']
            self.UTEgiven = True
        elif 'UTE'.swapcase() in param:
            self.UTE = param['UTE'.swapcase()]
            self.UTEgiven = True
        else:
            if self.UTEgiven == False:
                self.UTE = -1.5
        if 'LUTE' in param:
            self.LUTE = param['LUTE']
            self.LUTEgiven = True
        elif 'LUTE'.swapcase() in param:
            self.LUTE = param['LUTE'.swapcase()]
            self.LUTEgiven = True
        else:
            if self.LUTEgiven == False:
                self.LUTE = 0.0
        if 'WUTE' in param:
            self.WUTE = param['WUTE']
            self.WUTEgiven = True
        elif 'WUTE'.swapcase() in param:
            self.WUTE = param['WUTE'.swapcase()]
            self.WUTEgiven = True
        else:
            if self.WUTEgiven == False:
                self.WUTE = 0.0
        if 'PUTE' in param:
            self.PUTE = param['PUTE']
            self.PUTEgiven = True
        elif 'PUTE'.swapcase() in param:
            self.PUTE = param['PUTE'.swapcase()]
            self.PUTEgiven = True
        else:
            if self.PUTEgiven == False:
                self.PUTE = 0.0
        if 'UTEL' in param:
            self.UTEL = param['UTEL']
            self.UTELgiven = True
        elif 'UTEL'.swapcase() in param:
            self.UTEL = param['UTEL'.swapcase()]
            self.UTELgiven = True
        else:
            if self.UTELgiven == False:
                self.UTEL = 0.0
        if 'UA1' in param:
            self.UA1 = param['UA1']
            self.UA1given = True
        elif 'UA1'.swapcase() in param:
            self.UA1 = param['UA1'.swapcase()]
            self.UA1given = True
        else:
            if self.UA1given == False:
                self.UA1 = 0.001
        if 'LUA1' in param:
            self.LUA1 = param['LUA1']
            self.LUA1given = True
        elif 'LUA1'.swapcase() in param:
            self.LUA1 = param['LUA1'.swapcase()]
            self.LUA1given = True
        else:
            if self.LUA1given == False:
                self.LUA1 = 0.0
        if 'WUA1' in param:
            self.WUA1 = param['WUA1']
            self.WUA1given = True
        elif 'WUA1'.swapcase() in param:
            self.WUA1 = param['WUA1'.swapcase()]
            self.WUA1given = True
        else:
            if self.WUA1given == False:
                self.WUA1 = 0.0
        if 'PUA1' in param:
            self.PUA1 = param['PUA1']
            self.PUA1given = True
        elif 'PUA1'.swapcase() in param:
            self.PUA1 = param['PUA1'.swapcase()]
            self.PUA1given = True
        else:
            if self.PUA1given == False:
                self.PUA1 = 0.0
        if 'UA1L' in param:
            self.UA1L = param['UA1L']
            self.UA1Lgiven = True
        elif 'UA1L'.swapcase() in param:
            self.UA1L = param['UA1L'.swapcase()]
            self.UA1Lgiven = True
        else:
            if self.UA1Lgiven == False:
                self.UA1L = 0.0
        if 'UC1' in param:
            self.UC1 = param['UC1']
            self.UC1given = True
        elif 'UC1'.swapcase() in param:
            self.UC1 = param['UC1'.swapcase()]
            self.UC1given = True
        else:
            if self.UC1given == False:
                self.UC1 = 5.6e-11
        if 'LUC1' in param:
            self.LUC1 = param['LUC1']
            self.LUC1given = True
        elif 'LUC1'.swapcase() in param:
            self.LUC1 = param['LUC1'.swapcase()]
            self.LUC1given = True
        else:
            if self.LUC1given == False:
                self.LUC1 = 0.0
        if 'WUC1' in param:
            self.WUC1 = param['WUC1']
            self.WUC1given = True
        elif 'WUC1'.swapcase() in param:
            self.WUC1 = param['WUC1'.swapcase()]
            self.WUC1given = True
        else:
            if self.WUC1given == False:
                self.WUC1 = 0.0
        if 'PUC1' in param:
            self.PUC1 = param['PUC1']
            self.PUC1given = True
        elif 'PUC1'.swapcase() in param:
            self.PUC1 = param['PUC1'.swapcase()]
            self.PUC1given = True
        else:
            if self.PUC1given == False:
                self.PUC1 = 0.0
        if 'UD1' in param:
            self.UD1 = param['UD1']
            self.UD1given = True
        elif 'UD1'.swapcase() in param:
            self.UD1 = param['UD1'.swapcase()]
            self.UD1given = True
        else:
            if self.UD1given == False:
                self.UD1 = 0.0
        if 'LUD1' in param:
            self.LUD1 = param['LUD1']
            self.LUD1given = True
        elif 'LUD1'.swapcase() in param:
            self.LUD1 = param['LUD1'.swapcase()]
            self.LUD1given = True
        else:
            if self.LUD1given == False:
                self.LUD1 = 0.0
        if 'WUD1' in param:
            self.WUD1 = param['WUD1']
            self.WUD1given = True
        elif 'WUD1'.swapcase() in param:
            self.WUD1 = param['WUD1'.swapcase()]
            self.WUD1given = True
        else:
            if self.WUD1given == False:
                self.WUD1 = 0.0
        if 'PUD1' in param:
            self.PUD1 = param['PUD1']
            self.PUD1given = True
        elif 'PUD1'.swapcase() in param:
            self.PUD1 = param['PUD1'.swapcase()]
            self.PUD1given = True
        else:
            if self.PUD1given == False:
                self.PUD1 = 0.0
        if 'UD1L' in param:
            self.UD1L = param['UD1L']
            self.UD1Lgiven = True
        elif 'UD1L'.swapcase() in param:
            self.UD1L = param['UD1L'.swapcase()]
            self.UD1Lgiven = True
        else:
            if self.UD1Lgiven == False:
                self.UD1L = 0.0
        if 'EU1' in param:
            self.EU1 = param['EU1']
            self.EU1given = True
        elif 'EU1'.swapcase() in param:
            self.EU1 = param['EU1'.swapcase()]
            self.EU1given = True
        else:
            if self.EU1given == False:
                self.EU1 = 0.0
        if 'LEU1' in param:
            self.LEU1 = param['LEU1']
            self.LEU1given = True
        elif 'LEU1'.swapcase() in param:
            self.LEU1 = param['LEU1'.swapcase()]
            self.LEU1given = True
        else:
            if self.LEU1given == False:
                self.LEU1 = 0.0
        if 'WEU1' in param:
            self.WEU1 = param['WEU1']
            self.WEU1given = True
        elif 'WEU1'.swapcase() in param:
            self.WEU1 = param['WEU1'.swapcase()]
            self.WEU1given = True
        else:
            if self.WEU1given == False:
                self.WEU1 = 0.0
        if 'PEU1' in param:
            self.PEU1 = param['PEU1']
            self.PEU1given = True
        elif 'PEU1'.swapcase() in param:
            self.PEU1 = param['PEU1'.swapcase()]
            self.PEU1given = True
        else:
            if self.PEU1given == False:
                self.PEU1 = 0.0
        if 'UCSTE' in param:
            self.UCSTE = param['UCSTE']
            self.UCSTEgiven = True
        elif 'UCSTE'.swapcase() in param:
            self.UCSTE = param['UCSTE'.swapcase()]
            self.UCSTEgiven = True
        else:
            if self.UCSTEgiven == False:
                self.UCSTE = -0.004775
        if 'LUCSTE' in param:
            self.LUCSTE = param['LUCSTE']
            self.LUCSTEgiven = True
        elif 'LUCSTE'.swapcase() in param:
            self.LUCSTE = param['LUCSTE'.swapcase()]
            self.LUCSTEgiven = True
        else:
            if self.LUCSTEgiven == False:
                self.LUCSTE = 0.0
        if 'WUCSTE' in param:
            self.WUCSTE = param['WUCSTE']
            self.WUCSTEgiven = True
        elif 'WUCSTE'.swapcase() in param:
            self.WUCSTE = param['WUCSTE'.swapcase()]
            self.WUCSTEgiven = True
        else:
            if self.WUCSTEgiven == False:
                self.WUCSTE = 0.0
        if 'PUCSTE' in param:
            self.PUCSTE = param['PUCSTE']
            self.PUCSTEgiven = True
        elif 'PUCSTE'.swapcase() in param:
            self.PUCSTE = param['PUCSTE'.swapcase()]
            self.PUCSTEgiven = True
        else:
            if self.PUCSTEgiven == False:
                self.PUCSTE = 0.0
        if 'TETA0' in param:
            self.TETA0 = param['TETA0']
            self.TETA0given = True
        elif 'TETA0'.swapcase() in param:
            self.TETA0 = param['TETA0'.swapcase()]
            self.TETA0given = True
        else:
            if self.TETA0given == False:
                self.TETA0 = 0.0
        if 'PRT' in param:
            self.PRT = param['PRT']
            self.PRTgiven = True
        elif 'PRT'.swapcase() in param:
            self.PRT = param['PRT'.swapcase()]
            self.PRTgiven = True
        else:
            if self.PRTgiven == False:
                self.PRT = 0.0
        if 'LPRT' in param:
            self.LPRT = param['LPRT']
            self.LPRTgiven = True
        elif 'LPRT'.swapcase() in param:
            self.LPRT = param['LPRT'.swapcase()]
            self.LPRTgiven = True
        else:
            if self.LPRTgiven == False:
                self.LPRT = 0.0
        if 'WPRT' in param:
            self.WPRT = param['WPRT']
            self.WPRTgiven = True
        elif 'WPRT'.swapcase() in param:
            self.WPRT = param['WPRT'.swapcase()]
            self.WPRTgiven = True
        else:
            if self.WPRTgiven == False:
                self.WPRT = 0.0
        if 'PPRT' in param:
            self.PPRT = param['PPRT']
            self.PPRTgiven = True
        elif 'PPRT'.swapcase() in param:
            self.PPRT = param['PPRT'.swapcase()]
            self.PPRTgiven = True
        else:
            if self.PPRTgiven == False:
                self.PPRT = 0.0
        if 'AT' in param:
            self.AT = param['AT']
            self.ATgiven = True
        elif 'AT'.swapcase() in param:
            self.AT = param['AT'.swapcase()]
            self.ATgiven = True
        else:
            if self.ATgiven == False:
                self.AT = -0.00156
        if 'LAT' in param:
            self.LAT = param['LAT']
            self.LATgiven = True
        elif 'LAT'.swapcase() in param:
            self.LAT = param['LAT'.swapcase()]
            self.LATgiven = True
        else:
            if self.LATgiven == False:
                self.LAT = 0.0
        if 'WAT' in param:
            self.WAT = param['WAT']
            self.WATgiven = True
        elif 'WAT'.swapcase() in param:
            self.WAT = param['WAT'.swapcase()]
            self.WATgiven = True
        else:
            if self.WATgiven == False:
                self.WAT = 0.0
        if 'PAT' in param:
            self.PAT = param['PAT']
            self.PATgiven = True
        elif 'PAT'.swapcase() in param:
            self.PAT = param['PAT'.swapcase()]
            self.PATgiven = True
        else:
            if self.PATgiven == False:
                self.PAT = 0.0
        if 'ATL' in param:
            self.ATL = param['ATL']
            self.ATLgiven = True
        elif 'ATL'.swapcase() in param:
            self.ATL = param['ATL'.swapcase()]
            self.ATLgiven = True
        else:
            if self.ATLgiven == False:
                self.ATL = 0.0
        if 'TDELTA' in param:
            self.TDELTA = param['TDELTA']
            self.TDELTAgiven = True
        elif 'TDELTA'.swapcase() in param:
            self.TDELTA = param['TDELTA'.swapcase()]
            self.TDELTAgiven = True
        else:
            if self.TDELTAgiven == False:
                self.TDELTA = 0.0
        if 'PTWGT' in param:
            self.PTWGT = param['PTWGT']
            self.PTWGTgiven = True
        elif 'PTWGT'.swapcase() in param:
            self.PTWGT = param['PTWGT'.swapcase()]
            self.PTWGTgiven = True
        else:
            if self.PTWGTgiven == False:
                self.PTWGT = 0.0
        if 'LPTWGT' in param:
            self.LPTWGT = param['LPTWGT']
            self.LPTWGTgiven = True
        elif 'LPTWGT'.swapcase() in param:
            self.LPTWGT = param['LPTWGT'.swapcase()]
            self.LPTWGTgiven = True
        else:
            if self.LPTWGTgiven == False:
                self.LPTWGT = 0.0
        if 'WPTWGT' in param:
            self.WPTWGT = param['WPTWGT']
            self.WPTWGTgiven = True
        elif 'WPTWGT'.swapcase() in param:
            self.WPTWGT = param['WPTWGT'.swapcase()]
            self.WPTWGTgiven = True
        else:
            if self.WPTWGTgiven == False:
                self.WPTWGT = 0.0
        if 'PPTWGT' in param:
            self.PPTWGT = param['PPTWGT']
            self.PPTWGTgiven = True
        elif 'PPTWGT'.swapcase() in param:
            self.PPTWGT = param['PPTWGT'.swapcase()]
            self.PPTWGTgiven = True
        else:
            if self.PPTWGTgiven == False:
                self.PPTWGT = 0.0
        if 'PTWGTL' in param:
            self.PTWGTL = param['PTWGTL']
            self.PTWGTLgiven = True
        elif 'PTWGTL'.swapcase() in param:
            self.PTWGTL = param['PTWGTL'.swapcase()]
            self.PTWGTLgiven = True
        else:
            if self.PTWGTLgiven == False:
                self.PTWGTL = 0.0
        if 'KT1' in param:
            self.KT1 = param['KT1']
            self.KT1given = True
        elif 'KT1'.swapcase() in param:
            self.KT1 = param['KT1'.swapcase()]
            self.KT1given = True
        else:
            if self.KT1given == False:
                self.KT1 = -0.11
        if 'KT1EXP' in param:
            self.KT1EXP = param['KT1EXP']
            self.KT1EXPgiven = True
        elif 'KT1EXP'.swapcase() in param:
            self.KT1EXP = param['KT1EXP'.swapcase()]
            self.KT1EXPgiven = True
        else:
            if self.KT1EXPgiven == False:
                self.KT1EXP = 1.0
        if 'KT1L' in param:
            self.KT1L = param['KT1L']
            self.KT1Lgiven = True
        elif 'KT1L'.swapcase() in param:
            self.KT1L = param['KT1L'.swapcase()]
            self.KT1Lgiven = True
        else:
            if self.KT1Lgiven == False:
                self.KT1L = 0.0
        if 'LKT1' in param:
            self.LKT1 = param['LKT1']
            self.LKT1given = True
        elif 'LKT1'.swapcase() in param:
            self.LKT1 = param['LKT1'.swapcase()]
            self.LKT1given = True
        else:
            if self.LKT1given == False:
                self.LKT1 = 0.0
        if 'WKT1' in param:
            self.WKT1 = param['WKT1']
            self.WKT1given = True
        elif 'WKT1'.swapcase() in param:
            self.WKT1 = param['WKT1'.swapcase()]
            self.WKT1given = True
        else:
            if self.WKT1given == False:
                self.WKT1 = 0.0
        if 'PKT1' in param:
            self.PKT1 = param['PKT1']
            self.PKT1given = True
        elif 'PKT1'.swapcase() in param:
            self.PKT1 = param['PKT1'.swapcase()]
            self.PKT1given = True
        else:
            if self.PKT1given == False:
                self.PKT1 = 0.0
        if 'KT2' in param:
            self.KT2 = param['KT2']
            self.KT2given = True
        elif 'KT2'.swapcase() in param:
            self.KT2 = param['KT2'.swapcase()]
            self.KT2given = True
        else:
            if self.KT2given == False:
                self.KT2 = 0.022
        if 'LKT2' in param:
            self.LKT2 = param['LKT2']
            self.LKT2given = True
        elif 'LKT2'.swapcase() in param:
            self.LKT2 = param['LKT2'.swapcase()]
            self.LKT2given = True
        else:
            if self.LKT2given == False:
                self.LKT2 = 0.0
        if 'WKT2' in param:
            self.WKT2 = param['WKT2']
            self.WKT2given = True
        elif 'WKT2'.swapcase() in param:
            self.WKT2 = param['WKT2'.swapcase()]
            self.WKT2given = True
        else:
            if self.WKT2given == False:
                self.WKT2 = 0.0
        if 'PKT2' in param:
            self.PKT2 = param['PKT2']
            self.PKT2given = True
        elif 'PKT2'.swapcase() in param:
            self.PKT2 = param['PKT2'.swapcase()]
            self.PKT2given = True
        else:
            if self.PKT2given == False:
                self.PKT2 = 0.0
        if 'IIT' in param:
            self.IIT = param['IIT']
            self.IITgiven = True
        elif 'IIT'.swapcase() in param:
            self.IIT = param['IIT'.swapcase()]
            self.IITgiven = True
        else:
            if self.IITgiven == False:
                self.IIT = 0.0
        if 'LIIT' in param:
            self.LIIT = param['LIIT']
            self.LIITgiven = True
        elif 'LIIT'.swapcase() in param:
            self.LIIT = param['LIIT'.swapcase()]
            self.LIITgiven = True
        else:
            if self.LIITgiven == False:
                self.LIIT = 0.0
        if 'WIIT' in param:
            self.WIIT = param['WIIT']
            self.WIITgiven = True
        elif 'WIIT'.swapcase() in param:
            self.WIIT = param['WIIT'.swapcase()]
            self.WIITgiven = True
        else:
            if self.WIITgiven == False:
                self.WIIT = 0.0
        if 'PIIT' in param:
            self.PIIT = param['PIIT']
            self.PIITgiven = True
        elif 'PIIT'.swapcase() in param:
            self.PIIT = param['PIIT'.swapcase()]
            self.PIITgiven = True
        else:
            if self.PIITgiven == False:
                self.PIIT = 0.0
        if 'IGT' in param:
            self.IGT = param['IGT']
            self.IGTgiven = True
        elif 'IGT'.swapcase() in param:
            self.IGT = param['IGT'.swapcase()]
            self.IGTgiven = True
        else:
            if self.IGTgiven == False:
                self.IGT = 2.5
        if 'LIGT' in param:
            self.LIGT = param['LIGT']
            self.LIGTgiven = True
        elif 'LIGT'.swapcase() in param:
            self.LIGT = param['LIGT'.swapcase()]
            self.LIGTgiven = True
        else:
            if self.LIGTgiven == False:
                self.LIGT = 0.0
        if 'WIGT' in param:
            self.WIGT = param['WIGT']
            self.WIGTgiven = True
        elif 'WIGT'.swapcase() in param:
            self.WIGT = param['WIGT'.swapcase()]
            self.WIGTgiven = True
        else:
            if self.WIGTgiven == False:
                self.WIGT = 0.0
        if 'PIGT' in param:
            self.PIGT = param['PIGT']
            self.PIGTgiven = True
        elif 'PIGT'.swapcase() in param:
            self.PIGT = param['PIGT'.swapcase()]
            self.PIGTgiven = True
        else:
            if self.PIGTgiven == False:
                self.PIGT = 0.0
        if 'TGIDL' in param:
            self.TGIDL = param['TGIDL']
            self.TGIDLgiven = True
        elif 'TGIDL'.swapcase() in param:
            self.TGIDL = param['TGIDL'.swapcase()]
            self.TGIDLgiven = True
        else:
            if self.TGIDLgiven == False:
                self.TGIDL = 0.0
        if 'LTGIDL' in param:
            self.LTGIDL = param['LTGIDL']
            self.LTGIDLgiven = True
        elif 'LTGIDL'.swapcase() in param:
            self.LTGIDL = param['LTGIDL'.swapcase()]
            self.LTGIDLgiven = True
        else:
            if self.LTGIDLgiven == False:
                self.LTGIDL = 0.0
        if 'WTGIDL' in param:
            self.WTGIDL = param['WTGIDL']
            self.WTGIDLgiven = True
        elif 'WTGIDL'.swapcase() in param:
            self.WTGIDL = param['WTGIDL'.swapcase()]
            self.WTGIDLgiven = True
        else:
            if self.WTGIDLgiven == False:
                self.WTGIDL = 0.0
        if 'PTGIDL' in param:
            self.PTGIDL = param['PTGIDL']
            self.PTGIDLgiven = True
        elif 'PTGIDL'.swapcase() in param:
            self.PTGIDL = param['PTGIDL'.swapcase()]
            self.PTGIDLgiven = True
        else:
            if self.PTGIDLgiven == False:
                self.PTGIDL = 0.0
        if 'TCJ' in param:
            self.TCJ = param['TCJ']
            self.TCJgiven = True
        elif 'TCJ'.swapcase() in param:
            self.TCJ = param['TCJ'.swapcase()]
            self.TCJgiven = True
        else:
            if self.TCJgiven == False:
                self.TCJ = 0.0
        if 'TCJSW' in param:
            self.TCJSW = param['TCJSW']
            self.TCJSWgiven = True
        elif 'TCJSW'.swapcase() in param:
            self.TCJSW = param['TCJSW'.swapcase()]
            self.TCJSWgiven = True
        else:
            if self.TCJSWgiven == False:
                self.TCJSW = 0.0
        if 'TCJSWG' in param:
            self.TCJSWG = param['TCJSWG']
            self.TCJSWGgiven = True
        elif 'TCJSWG'.swapcase() in param:
            self.TCJSWG = param['TCJSWG'.swapcase()]
            self.TCJSWGgiven = True
        else:
            if self.TCJSWGgiven == False:
                self.TCJSWG = 0.0
        if 'TPB' in param:
            self.TPB = param['TPB']
            self.TPBgiven = True
        elif 'TPB'.swapcase() in param:
            self.TPB = param['TPB'.swapcase()]
            self.TPBgiven = True
        else:
            if self.TPBgiven == False:
                self.TPB = 0.0
        if 'TPBSW' in param:
            self.TPBSW = param['TPBSW']
            self.TPBSWgiven = True
        elif 'TPBSW'.swapcase() in param:
            self.TPBSW = param['TPBSW'.swapcase()]
            self.TPBSWgiven = True
        else:
            if self.TPBSWgiven == False:
                self.TPBSW = 0.0
        if 'TPBSWG' in param:
            self.TPBSWG = param['TPBSWG']
            self.TPBSWGgiven = True
        elif 'TPBSWG'.swapcase() in param:
            self.TPBSWG = param['TPBSWG'.swapcase()]
            self.TPBSWGgiven = True
        else:
            if self.TPBSWGgiven == False:
                self.TPBSWG = 0.0
        if 'XTIS' in param:
            self.XTIS = param['XTIS']
            self.XTISgiven = True
        elif 'XTIS'.swapcase() in param:
            self.XTIS = param['XTIS'.swapcase()]
            self.XTISgiven = True
        else:
            if self.XTISgiven == False:
                self.XTIS = 3.0
        if 'XTID' in param:
            self.XTID = param['XTID']
            self.XTIDgiven = True
        elif 'XTID'.swapcase() in param:
            self.XTID = param['XTID'.swapcase()]
            self.XTIDgiven = True
        else:
            if self.XTIDgiven == False:
                self.XTID = self.XTIS
        if 'XTSS' in param:
            self.XTSS = param['XTSS']
            self.XTSSgiven = True
        elif 'XTSS'.swapcase() in param:
            self.XTSS = param['XTSS'.swapcase()]
            self.XTSSgiven = True
        else:
            if self.XTSSgiven == False:
                self.XTSS = 0.02
        if 'XTSD' in param:
            self.XTSD = param['XTSD']
            self.XTSDgiven = True
        elif 'XTSD'.swapcase() in param:
            self.XTSD = param['XTSD'.swapcase()]
            self.XTSDgiven = True
        else:
            if self.XTSDgiven == False:
                self.XTSD = self.XTSS
        if 'XTSSWS' in param:
            self.XTSSWS = param['XTSSWS']
            self.XTSSWSgiven = True
        elif 'XTSSWS'.swapcase() in param:
            self.XTSSWS = param['XTSSWS'.swapcase()]
            self.XTSSWSgiven = True
        else:
            if self.XTSSWSgiven == False:
                self.XTSSWS = 0.02
        if 'XTSSWD' in param:
            self.XTSSWD = param['XTSSWD']
            self.XTSSWDgiven = True
        elif 'XTSSWD'.swapcase() in param:
            self.XTSSWD = param['XTSSWD'.swapcase()]
            self.XTSSWDgiven = True
        else:
            if self.XTSSWDgiven == False:
                self.XTSSWD = self.XTSSWS
        if 'XTSSWGS' in param:
            self.XTSSWGS = param['XTSSWGS']
            self.XTSSWGSgiven = True
        elif 'XTSSWGS'.swapcase() in param:
            self.XTSSWGS = param['XTSSWGS'.swapcase()]
            self.XTSSWGSgiven = True
        else:
            if self.XTSSWGSgiven == False:
                self.XTSSWGS = 0.02
        if 'XTSSWGD' in param:
            self.XTSSWGD = param['XTSSWGD']
            self.XTSSWGDgiven = True
        elif 'XTSSWGD'.swapcase() in param:
            self.XTSSWGD = param['XTSSWGD'.swapcase()]
            self.XTSSWGDgiven = True
        else:
            if self.XTSSWGDgiven == False:
                self.XTSSWGD = self.XTSSWGS
        if 'TNJTS' in param:
            self.TNJTS = param['TNJTS']
            self.TNJTSgiven = True
        elif 'TNJTS'.swapcase() in param:
            self.TNJTS = param['TNJTS'.swapcase()]
            self.TNJTSgiven = True
        else:
            if self.TNJTSgiven == False:
                self.TNJTS = 0.0
        if 'TNJTSD' in param:
            self.TNJTSD = param['TNJTSD']
            self.TNJTSDgiven = True
        elif 'TNJTSD'.swapcase() in param:
            self.TNJTSD = param['TNJTSD'.swapcase()]
            self.TNJTSDgiven = True
        else:
            if self.TNJTSDgiven == False:
                self.TNJTSD = self.TNJTS
        if 'TNJTSSW' in param:
            self.TNJTSSW = param['TNJTSSW']
            self.TNJTSSWgiven = True
        elif 'TNJTSSW'.swapcase() in param:
            self.TNJTSSW = param['TNJTSSW'.swapcase()]
            self.TNJTSSWgiven = True
        else:
            if self.TNJTSSWgiven == False:
                self.TNJTSSW = 0.0
        if 'TNJTSSWD' in param:
            self.TNJTSSWD = param['TNJTSSWD']
            self.TNJTSSWDgiven = True
        elif 'TNJTSSWD'.swapcase() in param:
            self.TNJTSSWD = param['TNJTSSWD'.swapcase()]
            self.TNJTSSWDgiven = True
        else:
            if self.TNJTSSWDgiven == False:
                self.TNJTSSWD = self.TNJTSSW
        if 'TNJTSSWG' in param:
            self.TNJTSSWG = param['TNJTSSWG']
            self.TNJTSSWGgiven = True
        elif 'TNJTSSWG'.swapcase() in param:
            self.TNJTSSWG = param['TNJTSSWG'.swapcase()]
            self.TNJTSSWGgiven = True
        else:
            if self.TNJTSSWGgiven == False:
                self.TNJTSSWG = 0.0
        if 'TNJTSSWGD' in param:
            self.TNJTSSWGD = param['TNJTSSWGD']
            self.TNJTSSWGDgiven = True
        elif 'TNJTSSWGD'.swapcase() in param:
            self.TNJTSSWGD = param['TNJTSSWGD'.swapcase()]
            self.TNJTSSWGDgiven = True
        else:
            if self.TNJTSSWGDgiven == False:
                self.TNJTSSWGD = self.TNJTSSWG
        if 'RTH0' in param:
            self.RTH0 = param['RTH0']
            self.RTH0given = True
        elif 'RTH0'.swapcase() in param:
            self.RTH0 = param['RTH0'.swapcase()]
            self.RTH0given = True
        else:
            if self.RTH0given == False:
                self.RTH0 = 0.0
        if 'CTH0' in param:
            self.CTH0 = param['CTH0']
            self.CTH0given = True
        elif 'CTH0'.swapcase() in param:
            self.CTH0 = param['CTH0'.swapcase()]
            self.CTH0given = True
        else:
            if self.CTH0given == False:
                self.CTH0 = 1e-05
        if 'WTH0' in param:
            self.WTH0 = param['WTH0']
            self.WTH0given = True
        elif 'WTH0'.swapcase() in param:
            self.WTH0 = param['WTH0'.swapcase()]
            self.WTH0given = True
        else:
            if self.WTH0given == False:
                self.WTH0 = 0.0
        if 'SAREF' in param:
            self.SAREF = param['SAREF']
            self.SAREFgiven = True
        elif 'SAREF'.swapcase() in param:
            self.SAREF = param['SAREF'.swapcase()]
            self.SAREFgiven = True
        else:
            if self.SAREFgiven == False:
                self.SAREF = 1e-06
        if 'SBREF' in param:
            self.SBREF = param['SBREF']
            self.SBREFgiven = True
        elif 'SBREF'.swapcase() in param:
            self.SBREF = param['SBREF'.swapcase()]
            self.SBREFgiven = True
        else:
            if self.SBREFgiven == False:
                self.SBREF = 1e-06
        if 'WLOD' in param:
            self.WLOD = param['WLOD']
            self.WLODgiven = True
        elif 'WLOD'.swapcase() in param:
            self.WLOD = param['WLOD'.swapcase()]
            self.WLODgiven = True
        else:
            if self.WLODgiven == False:
                self.WLOD = 0.0
        if 'KU0' in param:
            self.KU0 = param['KU0']
            self.KU0given = True
        elif 'KU0'.swapcase() in param:
            self.KU0 = param['KU0'.swapcase()]
            self.KU0given = True
        else:
            if self.KU0given == False:
                self.KU0 = 0.0
        if 'KVSAT' in param:
            self.KVSAT = param['KVSAT']
            self.KVSATgiven = True
        elif 'KVSAT'.swapcase() in param:
            self.KVSAT = param['KVSAT'.swapcase()]
            self.KVSATgiven = True
        else:
            if self.KVSATgiven == False:
                self.KVSAT = 0.0
        if 'TKU0' in param:
            self.TKU0 = param['TKU0']
            self.TKU0given = True
        elif 'TKU0'.swapcase() in param:
            self.TKU0 = param['TKU0'.swapcase()]
            self.TKU0given = True
        else:
            if self.TKU0given == False:
                self.TKU0 = 0.0
        if 'LKU0' in param:
            self.LKU0 = param['LKU0']
            self.LKU0given = True
        elif 'LKU0'.swapcase() in param:
            self.LKU0 = param['LKU0'.swapcase()]
            self.LKU0given = True
        else:
            if self.LKU0given == False:
                self.LKU0 = 0.0
        if 'WKU0' in param:
            self.WKU0 = param['WKU0']
            self.WKU0given = True
        elif 'WKU0'.swapcase() in param:
            self.WKU0 = param['WKU0'.swapcase()]
            self.WKU0given = True
        else:
            if self.WKU0given == False:
                self.WKU0 = 0.0
        if 'PKU0' in param:
            self.PKU0 = param['PKU0']
            self.PKU0given = True
        elif 'PKU0'.swapcase() in param:
            self.PKU0 = param['PKU0'.swapcase()]
            self.PKU0given = True
        else:
            if self.PKU0given == False:
                self.PKU0 = 0.0
        if 'LLODKU0' in param:
            self.LLODKU0 = param['LLODKU0']
            self.LLODKU0given = True
        elif 'LLODKU0'.swapcase() in param:
            self.LLODKU0 = param['LLODKU0'.swapcase()]
            self.LLODKU0given = True
        else:
            if self.LLODKU0given == False:
                self.LLODKU0 = 0.0
        if 'WLODKU0' in param:
            self.WLODKU0 = param['WLODKU0']
            self.WLODKU0given = True
        elif 'WLODKU0'.swapcase() in param:
            self.WLODKU0 = param['WLODKU0'.swapcase()]
            self.WLODKU0given = True
        else:
            if self.WLODKU0given == False:
                self.WLODKU0 = 0.0
        if 'KVTH0' in param:
            self.KVTH0 = param['KVTH0']
            self.KVTH0given = True
        elif 'KVTH0'.swapcase() in param:
            self.KVTH0 = param['KVTH0'.swapcase()]
            self.KVTH0given = True
        else:
            if self.KVTH0given == False:
                self.KVTH0 = 0.0
        if 'LKVTH0' in param:
            self.LKVTH0 = param['LKVTH0']
            self.LKVTH0given = True
        elif 'LKVTH0'.swapcase() in param:
            self.LKVTH0 = param['LKVTH0'.swapcase()]
            self.LKVTH0given = True
        else:
            if self.LKVTH0given == False:
                self.LKVTH0 = 0.0
        if 'WKVTH0' in param:
            self.WKVTH0 = param['WKVTH0']
            self.WKVTH0given = True
        elif 'WKVTH0'.swapcase() in param:
            self.WKVTH0 = param['WKVTH0'.swapcase()]
            self.WKVTH0given = True
        else:
            if self.WKVTH0given == False:
                self.WKVTH0 = 0.0
        if 'PKVTH0' in param:
            self.PKVTH0 = param['PKVTH0']
            self.PKVTH0given = True
        elif 'PKVTH0'.swapcase() in param:
            self.PKVTH0 = param['PKVTH0'.swapcase()]
            self.PKVTH0given = True
        else:
            if self.PKVTH0given == False:
                self.PKVTH0 = 0.0
        if 'LLODVTH' in param:
            self.LLODVTH = param['LLODVTH']
            self.LLODVTHgiven = True
        elif 'LLODVTH'.swapcase() in param:
            self.LLODVTH = param['LLODVTH'.swapcase()]
            self.LLODVTHgiven = True
        else:
            if self.LLODVTHgiven == False:
                self.LLODVTH = 0.0
        if 'WLODVTH' in param:
            self.WLODVTH = param['WLODVTH']
            self.WLODVTHgiven = True
        elif 'WLODVTH'.swapcase() in param:
            self.WLODVTH = param['WLODVTH'.swapcase()]
            self.WLODVTHgiven = True
        else:
            if self.WLODVTHgiven == False:
                self.WLODVTH = 0.0
        if 'STK2' in param:
            self.STK2 = param['STK2']
            self.STK2given = True
        elif 'STK2'.swapcase() in param:
            self.STK2 = param['STK2'.swapcase()]
            self.STK2given = True
        else:
            if self.STK2given == False:
                self.STK2 = 0.0
        if 'LODK2' in param:
            self.LODK2 = param['LODK2']
            self.LODK2given = True
        elif 'LODK2'.swapcase() in param:
            self.LODK2 = param['LODK2'.swapcase()]
            self.LODK2given = True
        else:
            if self.LODK2given == False:
                self.LODK2 = 0.0
        if 'STETA0' in param:
            self.STETA0 = param['STETA0']
            self.STETA0given = True
        elif 'STETA0'.swapcase() in param:
            self.STETA0 = param['STETA0'.swapcase()]
            self.STETA0given = True
        else:
            if self.STETA0given == False:
                self.STETA0 = 0.0
        if 'LODETA0' in param:
            self.LODETA0 = param['LODETA0']
            self.LODETA0given = True
        elif 'LODETA0'.swapcase() in param:
            self.LODETA0 = param['LODETA0'.swapcase()]
            self.LODETA0given = True
        else:
            if self.LODETA0given == False:
                self.LODETA0 = 0.0
        if 'WEB' in param:
            self.WEB = param['WEB']
            self.WEBgiven = True
        elif 'WEB'.swapcase() in param:
            self.WEB = param['WEB'.swapcase()]
            self.WEBgiven = True
        else:
            if self.WEBgiven == False:
                self.WEB = 0.0
        if 'WEC' in param:
            self.WEC = param['WEC']
            self.WECgiven = True
        elif 'WEC'.swapcase() in param:
            self.WEC = param['WEC'.swapcase()]
            self.WECgiven = True
        else:
            if self.WECgiven == False:
                self.WEC = 0.0
        if 'KVTH0WE' in param:
            self.KVTH0WE = param['KVTH0WE']
            self.KVTH0WEgiven = True
        elif 'KVTH0WE'.swapcase() in param:
            self.KVTH0WE = param['KVTH0WE'.swapcase()]
            self.KVTH0WEgiven = True
        else:
            if self.KVTH0WEgiven == False:
                self.KVTH0WE = 0.0
        if 'LKVTH0WE' in param:
            self.LKVTH0WE = param['LKVTH0WE']
            self.LKVTH0WEgiven = True
        elif 'LKVTH0WE'.swapcase() in param:
            self.LKVTH0WE = param['LKVTH0WE'.swapcase()]
            self.LKVTH0WEgiven = True
        else:
            if self.LKVTH0WEgiven == False:
                self.LKVTH0WE = 0.0
        if 'WKVTH0WE' in param:
            self.WKVTH0WE = param['WKVTH0WE']
            self.WKVTH0WEgiven = True
        elif 'WKVTH0WE'.swapcase() in param:
            self.WKVTH0WE = param['WKVTH0WE'.swapcase()]
            self.WKVTH0WEgiven = True
        else:
            if self.WKVTH0WEgiven == False:
                self.WKVTH0WE = 0.0
        if 'PKVTH0WE' in param:
            self.PKVTH0WE = param['PKVTH0WE']
            self.PKVTH0WEgiven = True
        elif 'PKVTH0WE'.swapcase() in param:
            self.PKVTH0WE = param['PKVTH0WE'.swapcase()]
            self.PKVTH0WEgiven = True
        else:
            if self.PKVTH0WEgiven == False:
                self.PKVTH0WE = 0.0
        if 'K2WE' in param:
            self.K2WE = param['K2WE']
            self.K2WEgiven = True
        elif 'K2WE'.swapcase() in param:
            self.K2WE = param['K2WE'.swapcase()]
            self.K2WEgiven = True
        else:
            if self.K2WEgiven == False:
                self.K2WE = 0.0
        if 'LK2WE' in param:
            self.LK2WE = param['LK2WE']
            self.LK2WEgiven = True
        elif 'LK2WE'.swapcase() in param:
            self.LK2WE = param['LK2WE'.swapcase()]
            self.LK2WEgiven = True
        else:
            if self.LK2WEgiven == False:
                self.LK2WE = 0.0
        if 'WK2WE' in param:
            self.WK2WE = param['WK2WE']
            self.WK2WEgiven = True
        elif 'WK2WE'.swapcase() in param:
            self.WK2WE = param['WK2WE'.swapcase()]
            self.WK2WEgiven = True
        else:
            if self.WK2WEgiven == False:
                self.WK2WE = 0.0
        if 'PK2WE' in param:
            self.PK2WE = param['PK2WE']
            self.PK2WEgiven = True
        elif 'PK2WE'.swapcase() in param:
            self.PK2WE = param['PK2WE'.swapcase()]
            self.PK2WEgiven = True
        else:
            if self.PK2WEgiven == False:
                self.PK2WE = 0.0
        if 'KU0WE' in param:
            self.KU0WE = param['KU0WE']
            self.KU0WEgiven = True
        elif 'KU0WE'.swapcase() in param:
            self.KU0WE = param['KU0WE'.swapcase()]
            self.KU0WEgiven = True
        else:
            if self.KU0WEgiven == False:
                self.KU0WE = 0.0
        if 'LKU0WE' in param:
            self.LKU0WE = param['LKU0WE']
            self.LKU0WEgiven = True
        elif 'LKU0WE'.swapcase() in param:
            self.LKU0WE = param['LKU0WE'.swapcase()]
            self.LKU0WEgiven = True
        else:
            if self.LKU0WEgiven == False:
                self.LKU0WE = 0.0
        if 'WKU0WE' in param:
            self.WKU0WE = param['WKU0WE']
            self.WKU0WEgiven = True
        elif 'WKU0WE'.swapcase() in param:
            self.WKU0WE = param['WKU0WE'.swapcase()]
            self.WKU0WEgiven = True
        else:
            if self.WKU0WEgiven == False:
                self.WKU0WE = 0.0
        if 'PKU0WE' in param:
            self.PKU0WE = param['PKU0WE']
            self.PKU0WEgiven = True
        elif 'PKU0WE'.swapcase() in param:
            self.PKU0WE = param['PKU0WE'.swapcase()]
            self.PKU0WEgiven = True
        else:
            if self.PKU0WEgiven == False:
                self.PKU0WE = 0.0
        if 'SCREF' in param:
            self.SCREF = param['SCREF']
            self.SCREFgiven = True
        elif 'SCREF'.swapcase() in param:
            self.SCREF = param['SCREF'.swapcase()]
            self.SCREFgiven = True
        else:
            if self.SCREFgiven == False:
                self.SCREF = 1e-06
        if 'SSL0' in param:
            self.SSL0 = param['SSL0']
            self.SSL0given = True
        elif 'SSL0'.swapcase() in param:
            self.SSL0 = param['SSL0'.swapcase()]
            self.SSL0given = True
        else:
            if self.SSL0given == False:
                self.SSL0 = 400.0
        if 'SSL1' in param:
            self.SSL1 = param['SSL1']
            self.SSL1given = True
        elif 'SSL1'.swapcase() in param:
            self.SSL1 = param['SSL1'.swapcase()]
            self.SSL1given = True
        else:
            if self.SSL1given == False:
                self.SSL1 = 336000000.0
        if 'SSL2' in param:
            self.SSL2 = param['SSL2']
            self.SSL2given = True
        elif 'SSL2'.swapcase() in param:
            self.SSL2 = param['SSL2'.swapcase()]
            self.SSL2given = True
        else:
            if self.SSL2given == False:
                self.SSL2 = 0.185
        if 'SSL3' in param:
            self.SSL3 = param['SSL3']
            self.SSL3given = True
        elif 'SSL3'.swapcase() in param:
            self.SSL3 = param['SSL3'.swapcase()]
            self.SSL3given = True
        else:
            if self.SSL3given == False:
                self.SSL3 = 0.3
        if 'SSL4' in param:
            self.SSL4 = param['SSL4']
            self.SSL4given = True
        elif 'SSL4'.swapcase() in param:
            self.SSL4 = param['SSL4'.swapcase()]
            self.SSL4given = True
        else:
            if self.SSL4given == False:
                self.SSL4 = 1.4
        if 'SSL5' in param:
            self.SSL5 = param['SSL5']
            self.SSL5given = True
        elif 'SSL5'.swapcase() in param:
            self.SSL5 = param['SSL5'.swapcase()]
            self.SSL5given = True
        else:
            if self.SSL5given == False:
                self.SSL5 = 0.0
        if 'SSLEXP1' in param:
            self.SSLEXP1 = param['SSLEXP1']
            self.SSLEXP1given = True
        elif 'SSLEXP1'.swapcase() in param:
            self.SSLEXP1 = param['SSLEXP1'.swapcase()]
            self.SSLEXP1given = True
        else:
            if self.SSLEXP1given == False:
                self.SSLEXP1 = 0.49
        if 'SSLEXP2' in param:
            self.SSLEXP2 = param['SSLEXP2']
            self.SSLEXP2given = True
        elif 'SSLEXP2'.swapcase() in param:
            self.SSLEXP2 = param['SSLEXP2'.swapcase()]
            self.SSLEXP2given = True
        else:
            if self.SSLEXP2given == False:
                self.SSLEXP2 = 1.42
        if 'AVDSX' in param:
            self.AVDSX = param['AVDSX']
            self.AVDSXgiven = True
        elif 'AVDSX'.swapcase() in param:
            self.AVDSX = param['AVDSX'.swapcase()]
            self.AVDSXgiven = True
        else:
            if self.AVDSXgiven == False:
                self.AVDSX = 20.0
        if 'WEDGE' in param:
            self.WEDGE = param['WEDGE']
            self.WEDGEgiven = True
        elif 'WEDGE'.swapcase() in param:
            self.WEDGE = param['WEDGE'.swapcase()]
            self.WEDGEgiven = True
        else:
            if self.WEDGEgiven == False:
                self.WEDGE = 1e-08
        if 'DGAMMAEDGE' in param:
            self.DGAMMAEDGE = param['DGAMMAEDGE']
            self.DGAMMAEDGEgiven = True
        elif 'DGAMMAEDGE'.swapcase() in param:
            self.DGAMMAEDGE = param['DGAMMAEDGE'.swapcase()]
            self.DGAMMAEDGEgiven = True
        else:
            if self.DGAMMAEDGEgiven == False:
                self.DGAMMAEDGE = 0.0
        if 'DGAMMAEDGEL' in param:
            self.DGAMMAEDGEL = param['DGAMMAEDGEL']
            self.DGAMMAEDGELgiven = True
        elif 'DGAMMAEDGEL'.swapcase() in param:
            self.DGAMMAEDGEL = param['DGAMMAEDGEL'.swapcase()]
            self.DGAMMAEDGELgiven = True
        else:
            if self.DGAMMAEDGELgiven == False:
                self.DGAMMAEDGEL = 0.0
        if 'DGAMMAEDGELEXP' in param:
            self.DGAMMAEDGELEXP = param['DGAMMAEDGELEXP']
            self.DGAMMAEDGELEXPgiven = True
        elif 'DGAMMAEDGELEXP'.swapcase() in param:
            self.DGAMMAEDGELEXP = param['DGAMMAEDGELEXP'.swapcase()]
            self.DGAMMAEDGELEXPgiven = True
        else:
            if self.DGAMMAEDGELEXPgiven == False:
                self.DGAMMAEDGELEXP = 1.0
        if 'DVTEDGE' in param:
            self.DVTEDGE = param['DVTEDGE']
            self.DVTEDGEgiven = True
        elif 'DVTEDGE'.swapcase() in param:
            self.DVTEDGE = param['DVTEDGE'.swapcase()]
            self.DVTEDGEgiven = True
        else:
            if self.DVTEDGEgiven == False:
                self.DVTEDGE = 0.0
        if 'NDEPEDGE' in param:
            self.NDEPEDGE = param['NDEPEDGE']
            self.NDEPEDGEgiven = True
        elif 'NDEPEDGE'.swapcase() in param:
            self.NDEPEDGE = param['NDEPEDGE'.swapcase()]
            self.NDEPEDGEgiven = True
        else:
            if self.NDEPEDGEgiven == False:
                self.NDEPEDGE = 1e+24
        if 'LNDEPEDGE' in param:
            self.LNDEPEDGE = param['LNDEPEDGE']
            self.LNDEPEDGEgiven = True
        elif 'LNDEPEDGE'.swapcase() in param:
            self.LNDEPEDGE = param['LNDEPEDGE'.swapcase()]
            self.LNDEPEDGEgiven = True
        else:
            if self.LNDEPEDGEgiven == False:
                self.LNDEPEDGE = 0.0
        if 'WNDEPEDGE' in param:
            self.WNDEPEDGE = param['WNDEPEDGE']
            self.WNDEPEDGEgiven = True
        elif 'WNDEPEDGE'.swapcase() in param:
            self.WNDEPEDGE = param['WNDEPEDGE'.swapcase()]
            self.WNDEPEDGEgiven = True
        else:
            if self.WNDEPEDGEgiven == False:
                self.WNDEPEDGE = 0.0
        if 'PNDEPEDGE' in param:
            self.PNDEPEDGE = param['PNDEPEDGE']
            self.PNDEPEDGEgiven = True
        elif 'PNDEPEDGE'.swapcase() in param:
            self.PNDEPEDGE = param['PNDEPEDGE'.swapcase()]
            self.PNDEPEDGEgiven = True
        else:
            if self.PNDEPEDGEgiven == False:
                self.PNDEPEDGE = 0.0
        if 'NFACTOREDGE' in param:
            self.NFACTOREDGE = param['NFACTOREDGE']
            self.NFACTOREDGEgiven = True
        elif 'NFACTOREDGE'.swapcase() in param:
            self.NFACTOREDGE = param['NFACTOREDGE'.swapcase()]
            self.NFACTOREDGEgiven = True
        else:
            if self.NFACTOREDGEgiven == False:
                self.NFACTOREDGE = 0.0
        if 'LNFACTOREDGE' in param:
            self.LNFACTOREDGE = param['LNFACTOREDGE']
            self.LNFACTOREDGEgiven = True
        elif 'LNFACTOREDGE'.swapcase() in param:
            self.LNFACTOREDGE = param['LNFACTOREDGE'.swapcase()]
            self.LNFACTOREDGEgiven = True
        else:
            if self.LNFACTOREDGEgiven == False:
                self.LNFACTOREDGE = 0.0
        if 'WNFACTOREDGE' in param:
            self.WNFACTOREDGE = param['WNFACTOREDGE']
            self.WNFACTOREDGEgiven = True
        elif 'WNFACTOREDGE'.swapcase() in param:
            self.WNFACTOREDGE = param['WNFACTOREDGE'.swapcase()]
            self.WNFACTOREDGEgiven = True
        else:
            if self.WNFACTOREDGEgiven == False:
                self.WNFACTOREDGE = 0.0
        if 'PNFACTOREDGE' in param:
            self.PNFACTOREDGE = param['PNFACTOREDGE']
            self.PNFACTOREDGEgiven = True
        elif 'PNFACTOREDGE'.swapcase() in param:
            self.PNFACTOREDGE = param['PNFACTOREDGE'.swapcase()]
            self.PNFACTOREDGEgiven = True
        else:
            if self.PNFACTOREDGEgiven == False:
                self.PNFACTOREDGE = 0.0
        if 'CITEDGE' in param:
            self.CITEDGE = param['CITEDGE']
            self.CITEDGEgiven = True
        elif 'CITEDGE'.swapcase() in param:
            self.CITEDGE = param['CITEDGE'.swapcase()]
            self.CITEDGEgiven = True
        else:
            if self.CITEDGEgiven == False:
                self.CITEDGE = 0.0
        if 'LCITEDGE' in param:
            self.LCITEDGE = param['LCITEDGE']
            self.LCITEDGEgiven = True
        elif 'LCITEDGE'.swapcase() in param:
            self.LCITEDGE = param['LCITEDGE'.swapcase()]
            self.LCITEDGEgiven = True
        else:
            if self.LCITEDGEgiven == False:
                self.LCITEDGE = 0.0
        if 'WCITEDGE' in param:
            self.WCITEDGE = param['WCITEDGE']
            self.WCITEDGEgiven = True
        elif 'WCITEDGE'.swapcase() in param:
            self.WCITEDGE = param['WCITEDGE'.swapcase()]
            self.WCITEDGEgiven = True
        else:
            if self.WCITEDGEgiven == False:
                self.WCITEDGE = 0.0
        if 'PCITEDGE' in param:
            self.PCITEDGE = param['PCITEDGE']
            self.PCITEDGEgiven = True
        elif 'PCITEDGE'.swapcase() in param:
            self.PCITEDGE = param['PCITEDGE'.swapcase()]
            self.PCITEDGEgiven = True
        else:
            if self.PCITEDGEgiven == False:
                self.PCITEDGE = 0.0
        if 'CDSCDEDGE' in param:
            self.CDSCDEDGE = param['CDSCDEDGE']
            self.CDSCDEDGEgiven = True
        elif 'CDSCDEDGE'.swapcase() in param:
            self.CDSCDEDGE = param['CDSCDEDGE'.swapcase()]
            self.CDSCDEDGEgiven = True
        else:
            if self.CDSCDEDGEgiven == False:
                self.CDSCDEDGE = 1e-09
        if 'LCDSCDEDGE' in param:
            self.LCDSCDEDGE = param['LCDSCDEDGE']
            self.LCDSCDEDGEgiven = True
        elif 'LCDSCDEDGE'.swapcase() in param:
            self.LCDSCDEDGE = param['LCDSCDEDGE'.swapcase()]
            self.LCDSCDEDGEgiven = True
        else:
            if self.LCDSCDEDGEgiven == False:
                self.LCDSCDEDGE = 0.0
        if 'WCDSCDEDGE' in param:
            self.WCDSCDEDGE = param['WCDSCDEDGE']
            self.WCDSCDEDGEgiven = True
        elif 'WCDSCDEDGE'.swapcase() in param:
            self.WCDSCDEDGE = param['WCDSCDEDGE'.swapcase()]
            self.WCDSCDEDGEgiven = True
        else:
            if self.WCDSCDEDGEgiven == False:
                self.WCDSCDEDGE = 0.0
        if 'PCDSCDEDGE' in param:
            self.PCDSCDEDGE = param['PCDSCDEDGE']
            self.PCDSCDEDGEgiven = True
        elif 'PCDSCDEDGE'.swapcase() in param:
            self.PCDSCDEDGE = param['PCDSCDEDGE'.swapcase()]
            self.PCDSCDEDGEgiven = True
        else:
            if self.PCDSCDEDGEgiven == False:
                self.PCDSCDEDGE = 0.0
        if 'CDSCBEDGE' in param:
            self.CDSCBEDGE = param['CDSCBEDGE']
            self.CDSCBEDGEgiven = True
        elif 'CDSCBEDGE'.swapcase() in param:
            self.CDSCBEDGE = param['CDSCBEDGE'.swapcase()]
            self.CDSCBEDGEgiven = True
        else:
            if self.CDSCBEDGEgiven == False:
                self.CDSCBEDGE = 0.0
        if 'LCDSCBEDGE' in param:
            self.LCDSCBEDGE = param['LCDSCBEDGE']
            self.LCDSCBEDGEgiven = True
        elif 'LCDSCBEDGE'.swapcase() in param:
            self.LCDSCBEDGE = param['LCDSCBEDGE'.swapcase()]
            self.LCDSCBEDGEgiven = True
        else:
            if self.LCDSCBEDGEgiven == False:
                self.LCDSCBEDGE = 0.0
        if 'WCDSCBEDGE' in param:
            self.WCDSCBEDGE = param['WCDSCBEDGE']
            self.WCDSCBEDGEgiven = True
        elif 'WCDSCBEDGE'.swapcase() in param:
            self.WCDSCBEDGE = param['WCDSCBEDGE'.swapcase()]
            self.WCDSCBEDGEgiven = True
        else:
            if self.WCDSCBEDGEgiven == False:
                self.WCDSCBEDGE = 0.0
        if 'PCDSCBEDGE' in param:
            self.PCDSCBEDGE = param['PCDSCBEDGE']
            self.PCDSCBEDGEgiven = True
        elif 'PCDSCBEDGE'.swapcase() in param:
            self.PCDSCBEDGE = param['PCDSCBEDGE'.swapcase()]
            self.PCDSCBEDGEgiven = True
        else:
            if self.PCDSCBEDGEgiven == False:
                self.PCDSCBEDGE = 0.0
        if 'ETA0EDGE' in param:
            self.ETA0EDGE = param['ETA0EDGE']
            self.ETA0EDGEgiven = True
        elif 'ETA0EDGE'.swapcase() in param:
            self.ETA0EDGE = param['ETA0EDGE'.swapcase()]
            self.ETA0EDGEgiven = True
        else:
            if self.ETA0EDGEgiven == False:
                self.ETA0EDGE = 0.08
        if 'LETA0EDGE' in param:
            self.LETA0EDGE = param['LETA0EDGE']
            self.LETA0EDGEgiven = True
        elif 'LETA0EDGE'.swapcase() in param:
            self.LETA0EDGE = param['LETA0EDGE'.swapcase()]
            self.LETA0EDGEgiven = True
        else:
            if self.LETA0EDGEgiven == False:
                self.LETA0EDGE = 0.0
        if 'WETA0EDGE' in param:
            self.WETA0EDGE = param['WETA0EDGE']
            self.WETA0EDGEgiven = True
        elif 'WETA0EDGE'.swapcase() in param:
            self.WETA0EDGE = param['WETA0EDGE'.swapcase()]
            self.WETA0EDGEgiven = True
        else:
            if self.WETA0EDGEgiven == False:
                self.WETA0EDGE = 0.0
        if 'PETA0EDGE' in param:
            self.PETA0EDGE = param['PETA0EDGE']
            self.PETA0EDGEgiven = True
        elif 'PETA0EDGE'.swapcase() in param:
            self.PETA0EDGE = param['PETA0EDGE'.swapcase()]
            self.PETA0EDGEgiven = True
        else:
            if self.PETA0EDGEgiven == False:
                self.PETA0EDGE = 0.0
        if 'ETABEDGE' in param:
            self.ETABEDGE = param['ETABEDGE']
            self.ETABEDGEgiven = True
        elif 'ETABEDGE'.swapcase() in param:
            self.ETABEDGE = param['ETABEDGE'.swapcase()]
            self.ETABEDGEgiven = True
        else:
            if self.ETABEDGEgiven == False:
                self.ETABEDGE = -0.07
        if 'LETABEDGE' in param:
            self.LETABEDGE = param['LETABEDGE']
            self.LETABEDGEgiven = True
        elif 'LETABEDGE'.swapcase() in param:
            self.LETABEDGE = param['LETABEDGE'.swapcase()]
            self.LETABEDGEgiven = True
        else:
            if self.LETABEDGEgiven == False:
                self.LETABEDGE = 0.0
        if 'WETABEDGE' in param:
            self.WETABEDGE = param['WETABEDGE']
            self.WETABEDGEgiven = True
        elif 'WETABEDGE'.swapcase() in param:
            self.WETABEDGE = param['WETABEDGE'.swapcase()]
            self.WETABEDGEgiven = True
        else:
            if self.WETABEDGEgiven == False:
                self.WETABEDGE = 0.0
        if 'PETABEDGE' in param:
            self.PETABEDGE = param['PETABEDGE']
            self.PETABEDGEgiven = True
        elif 'PETABEDGE'.swapcase() in param:
            self.PETABEDGE = param['PETABEDGE'.swapcase()]
            self.PETABEDGEgiven = True
        else:
            if self.PETABEDGEgiven == False:
                self.PETABEDGE = 0.0
        if 'KT1EDGE' in param:
            self.KT1EDGE = param['KT1EDGE']
            self.KT1EDGEgiven = True
        elif 'KT1EDGE'.swapcase() in param:
            self.KT1EDGE = param['KT1EDGE'.swapcase()]
            self.KT1EDGEgiven = True
        else:
            if self.KT1EDGEgiven == False:
                self.KT1EDGE = -0.11
        if 'LKT1EDGE' in param:
            self.LKT1EDGE = param['LKT1EDGE']
            self.LKT1EDGEgiven = True
        elif 'LKT1EDGE'.swapcase() in param:
            self.LKT1EDGE = param['LKT1EDGE'.swapcase()]
            self.LKT1EDGEgiven = True
        else:
            if self.LKT1EDGEgiven == False:
                self.LKT1EDGE = 0.0
        if 'WKT1EDGE' in param:
            self.WKT1EDGE = param['WKT1EDGE']
            self.WKT1EDGEgiven = True
        elif 'WKT1EDGE'.swapcase() in param:
            self.WKT1EDGE = param['WKT1EDGE'.swapcase()]
            self.WKT1EDGEgiven = True
        else:
            if self.WKT1EDGEgiven == False:
                self.WKT1EDGE = 0.0
        if 'PKT1EDGE' in param:
            self.PKT1EDGE = param['PKT1EDGE']
            self.PKT1EDGEgiven = True
        elif 'PKT1EDGE'.swapcase() in param:
            self.PKT1EDGE = param['PKT1EDGE'.swapcase()]
            self.PKT1EDGEgiven = True
        else:
            if self.PKT1EDGEgiven == False:
                self.PKT1EDGE = 0.0
        if 'KT1LEDGE' in param:
            self.KT1LEDGE = param['KT1LEDGE']
            self.KT1LEDGEgiven = True
        elif 'KT1LEDGE'.swapcase() in param:
            self.KT1LEDGE = param['KT1LEDGE'.swapcase()]
            self.KT1LEDGEgiven = True
        else:
            if self.KT1LEDGEgiven == False:
                self.KT1LEDGE = 0.0
        if 'LKT1LEDGE' in param:
            self.LKT1LEDGE = param['LKT1LEDGE']
            self.LKT1LEDGEgiven = True
        elif 'LKT1LEDGE'.swapcase() in param:
            self.LKT1LEDGE = param['LKT1LEDGE'.swapcase()]
            self.LKT1LEDGEgiven = True
        else:
            if self.LKT1LEDGEgiven == False:
                self.LKT1LEDGE = 0.0
        if 'WKT1LEDGE' in param:
            self.WKT1LEDGE = param['WKT1LEDGE']
            self.WKT1LEDGEgiven = True
        elif 'WKT1LEDGE'.swapcase() in param:
            self.WKT1LEDGE = param['WKT1LEDGE'.swapcase()]
            self.WKT1LEDGEgiven = True
        else:
            if self.WKT1LEDGEgiven == False:
                self.WKT1LEDGE = 0.0
        if 'PKT1LEDGE' in param:
            self.PKT1LEDGE = param['PKT1LEDGE']
            self.PKT1LEDGEgiven = True
        elif 'PKT1LEDGE'.swapcase() in param:
            self.PKT1LEDGE = param['PKT1LEDGE'.swapcase()]
            self.PKT1LEDGEgiven = True
        else:
            if self.PKT1LEDGEgiven == False:
                self.PKT1LEDGE = 0.0
        if 'KT2EDGE' in param:
            self.KT2EDGE = param['KT2EDGE']
            self.KT2EDGEgiven = True
        elif 'KT2EDGE'.swapcase() in param:
            self.KT2EDGE = param['KT2EDGE'.swapcase()]
            self.KT2EDGEgiven = True
        else:
            if self.KT2EDGEgiven == False:
                self.KT2EDGE = 0.022
        if 'LKT2EDGE' in param:
            self.LKT2EDGE = param['LKT2EDGE']
            self.LKT2EDGEgiven = True
        elif 'LKT2EDGE'.swapcase() in param:
            self.LKT2EDGE = param['LKT2EDGE'.swapcase()]
            self.LKT2EDGEgiven = True
        else:
            if self.LKT2EDGEgiven == False:
                self.LKT2EDGE = 0.0
        if 'WKT2EDGE' in param:
            self.WKT2EDGE = param['WKT2EDGE']
            self.WKT2EDGEgiven = True
        elif 'WKT2EDGE'.swapcase() in param:
            self.WKT2EDGE = param['WKT2EDGE'.swapcase()]
            self.WKT2EDGEgiven = True
        else:
            if self.WKT2EDGEgiven == False:
                self.WKT2EDGE = 0.0
        if 'PKT2EDGE' in param:
            self.PKT2EDGE = param['PKT2EDGE']
            self.PKT2EDGEgiven = True
        elif 'PKT2EDGE'.swapcase() in param:
            self.PKT2EDGE = param['PKT2EDGE'.swapcase()]
            self.PKT2EDGEgiven = True
        else:
            if self.PKT2EDGEgiven == False:
                self.PKT2EDGE = 0.0
        if 'KT1EXPEDGE' in param:
            self.KT1EXPEDGE = param['KT1EXPEDGE']
            self.KT1EXPEDGEgiven = True
        elif 'KT1EXPEDGE'.swapcase() in param:
            self.KT1EXPEDGE = param['KT1EXPEDGE'.swapcase()]
            self.KT1EXPEDGEgiven = True
        else:
            if self.KT1EXPEDGEgiven == False:
                self.KT1EXPEDGE = 1.0
        if 'LKT1EXPEDGE' in param:
            self.LKT1EXPEDGE = param['LKT1EXPEDGE']
            self.LKT1EXPEDGEgiven = True
        elif 'LKT1EXPEDGE'.swapcase() in param:
            self.LKT1EXPEDGE = param['LKT1EXPEDGE'.swapcase()]
            self.LKT1EXPEDGEgiven = True
        else:
            if self.LKT1EXPEDGEgiven == False:
                self.LKT1EXPEDGE = 0.0
        if 'WKT1EXPEDGE' in param:
            self.WKT1EXPEDGE = param['WKT1EXPEDGE']
            self.WKT1EXPEDGEgiven = True
        elif 'WKT1EXPEDGE'.swapcase() in param:
            self.WKT1EXPEDGE = param['WKT1EXPEDGE'.swapcase()]
            self.WKT1EXPEDGEgiven = True
        else:
            if self.WKT1EXPEDGEgiven == False:
                self.WKT1EXPEDGE = 0.0
        if 'PKT1EXPEDGE' in param:
            self.PKT1EXPEDGE = param['PKT1EXPEDGE']
            self.PKT1EXPEDGEgiven = True
        elif 'PKT1EXPEDGE'.swapcase() in param:
            self.PKT1EXPEDGE = param['PKT1EXPEDGE'.swapcase()]
            self.PKT1EXPEDGEgiven = True
        else:
            if self.PKT1EXPEDGEgiven == False:
                self.PKT1EXPEDGE = 0.0
        if 'TNFACTOREDGE' in param:
            self.TNFACTOREDGE = param['TNFACTOREDGE']
            self.TNFACTOREDGEgiven = True
        elif 'TNFACTOREDGE'.swapcase() in param:
            self.TNFACTOREDGE = param['TNFACTOREDGE'.swapcase()]
            self.TNFACTOREDGEgiven = True
        else:
            if self.TNFACTOREDGEgiven == False:
                self.TNFACTOREDGE = 0.0
        if 'LTNFACTOREDGE' in param:
            self.LTNFACTOREDGE = param['LTNFACTOREDGE']
            self.LTNFACTOREDGEgiven = True
        elif 'LTNFACTOREDGE'.swapcase() in param:
            self.LTNFACTOREDGE = param['LTNFACTOREDGE'.swapcase()]
            self.LTNFACTOREDGEgiven = True
        else:
            if self.LTNFACTOREDGEgiven == False:
                self.LTNFACTOREDGE = 0.0
        if 'WTNFACTOREDGE' in param:
            self.WTNFACTOREDGE = param['WTNFACTOREDGE']
            self.WTNFACTOREDGEgiven = True
        elif 'WTNFACTOREDGE'.swapcase() in param:
            self.WTNFACTOREDGE = param['WTNFACTOREDGE'.swapcase()]
            self.WTNFACTOREDGEgiven = True
        else:
            if self.WTNFACTOREDGEgiven == False:
                self.WTNFACTOREDGE = 0.0
        if 'PTNFACTOREDGE' in param:
            self.PTNFACTOREDGE = param['PTNFACTOREDGE']
            self.PTNFACTOREDGEgiven = True
        elif 'PTNFACTOREDGE'.swapcase() in param:
            self.PTNFACTOREDGE = param['PTNFACTOREDGE'.swapcase()]
            self.PTNFACTOREDGEgiven = True
        else:
            if self.PTNFACTOREDGEgiven == False:
                self.PTNFACTOREDGE = 0.0
        if 'TETA0EDGE' in param:
            self.TETA0EDGE = param['TETA0EDGE']
            self.TETA0EDGEgiven = True
        elif 'TETA0EDGE'.swapcase() in param:
            self.TETA0EDGE = param['TETA0EDGE'.swapcase()]
            self.TETA0EDGEgiven = True
        else:
            if self.TETA0EDGEgiven == False:
                self.TETA0EDGE = 0.0
        if 'LTETA0EDGE' in param:
            self.LTETA0EDGE = param['LTETA0EDGE']
            self.LTETA0EDGEgiven = True
        elif 'LTETA0EDGE'.swapcase() in param:
            self.LTETA0EDGE = param['LTETA0EDGE'.swapcase()]
            self.LTETA0EDGEgiven = True
        else:
            if self.LTETA0EDGEgiven == False:
                self.LTETA0EDGE = 0.0
        if 'WTETA0EDGE' in param:
            self.WTETA0EDGE = param['WTETA0EDGE']
            self.WTETA0EDGEgiven = True
        elif 'WTETA0EDGE'.swapcase() in param:
            self.WTETA0EDGE = param['WTETA0EDGE'.swapcase()]
            self.WTETA0EDGEgiven = True
        else:
            if self.WTETA0EDGEgiven == False:
                self.WTETA0EDGE = 0.0
        if 'PTETA0EDGE' in param:
            self.PTETA0EDGE = param['PTETA0EDGE']
            self.PTETA0EDGEgiven = True
        elif 'PTETA0EDGE'.swapcase() in param:
            self.PTETA0EDGE = param['PTETA0EDGE'.swapcase()]
            self.PTETA0EDGEgiven = True
        else:
            if self.PTETA0EDGEgiven == False:
                self.PTETA0EDGE = 0.0
        if 'DVT0EDGE' in param:
            self.DVT0EDGE = param['DVT0EDGE']
            self.DVT0EDGEgiven = True
        elif 'DVT0EDGE'.swapcase() in param:
            self.DVT0EDGE = param['DVT0EDGE'.swapcase()]
            self.DVT0EDGEgiven = True
        else:
            if self.DVT0EDGEgiven == False:
                self.DVT0EDGE = 2.2
        if 'DVT1EDGE' in param:
            self.DVT1EDGE = param['DVT1EDGE']
            self.DVT1EDGEgiven = True
        elif 'DVT1EDGE'.swapcase() in param:
            self.DVT1EDGE = param['DVT1EDGE'.swapcase()]
            self.DVT1EDGEgiven = True
        else:
            if self.DVT1EDGEgiven == False:
                self.DVT1EDGE = 0.53
        if 'DVT2EDGE' in param:
            self.DVT2EDGE = param['DVT2EDGE']
            self.DVT2EDGEgiven = True
        elif 'DVT2EDGE'.swapcase() in param:
            self.DVT2EDGE = param['DVT2EDGE'.swapcase()]
            self.DVT2EDGEgiven = True
        else:
            if self.DVT2EDGEgiven == False:
                self.DVT2EDGE = 0.0
        if 'K2EDGE' in param:
            self.K2EDGE = param['K2EDGE']
            self.K2EDGEgiven = True
        elif 'K2EDGE'.swapcase() in param:
            self.K2EDGE = param['K2EDGE'.swapcase()]
            self.K2EDGEgiven = True
        else:
            if self.K2EDGEgiven == False:
                self.K2EDGE = 0.0
        if 'LK2EDGE' in param:
            self.LK2EDGE = param['LK2EDGE']
            self.LK2EDGEgiven = True
        elif 'LK2EDGE'.swapcase() in param:
            self.LK2EDGE = param['LK2EDGE'.swapcase()]
            self.LK2EDGEgiven = True
        else:
            if self.LK2EDGEgiven == False:
                self.LK2EDGE = 0.0
        if 'WK2EDGE' in param:
            self.WK2EDGE = param['WK2EDGE']
            self.WK2EDGEgiven = True
        elif 'WK2EDGE'.swapcase() in param:
            self.WK2EDGE = param['WK2EDGE'.swapcase()]
            self.WK2EDGEgiven = True
        else:
            if self.WK2EDGEgiven == False:
                self.WK2EDGE = 0.0
        if 'PK2EDGE' in param:
            self.PK2EDGE = param['PK2EDGE']
            self.PK2EDGEgiven = True
        elif 'PK2EDGE'.swapcase() in param:
            self.PK2EDGE = param['PK2EDGE'.swapcase()]
            self.PK2EDGEgiven = True
        else:
            if self.PK2EDGEgiven == False:
                self.PK2EDGE = 0.0
        if 'KVTH0EDGE' in param:
            self.KVTH0EDGE = param['KVTH0EDGE']
            self.KVTH0EDGEgiven = True
        elif 'KVTH0EDGE'.swapcase() in param:
            self.KVTH0EDGE = param['KVTH0EDGE'.swapcase()]
            self.KVTH0EDGEgiven = True
        else:
            if self.KVTH0EDGEgiven == False:
                self.KVTH0EDGE = 0.0
        if 'LKVTH0EDGE' in param:
            self.LKVTH0EDGE = param['LKVTH0EDGE']
            self.LKVTH0EDGEgiven = True
        elif 'LKVTH0EDGE'.swapcase() in param:
            self.LKVTH0EDGE = param['LKVTH0EDGE'.swapcase()]
            self.LKVTH0EDGEgiven = True
        else:
            if self.LKVTH0EDGEgiven == False:
                self.LKVTH0EDGE = 0.0
        if 'WKVTH0EDGE' in param:
            self.WKVTH0EDGE = param['WKVTH0EDGE']
            self.WKVTH0EDGEgiven = True
        elif 'WKVTH0EDGE'.swapcase() in param:
            self.WKVTH0EDGE = param['WKVTH0EDGE'.swapcase()]
            self.WKVTH0EDGEgiven = True
        else:
            if self.WKVTH0EDGEgiven == False:
                self.WKVTH0EDGE = 0.0
        if 'PKVTH0EDGE' in param:
            self.PKVTH0EDGE = param['PKVTH0EDGE']
            self.PKVTH0EDGEgiven = True
        elif 'PKVTH0EDGE'.swapcase() in param:
            self.PKVTH0EDGE = param['PKVTH0EDGE'.swapcase()]
            self.PKVTH0EDGEgiven = True
        else:
            if self.PKVTH0EDGEgiven == False:
                self.PKVTH0EDGE = 0.0
        if 'STK2EDGE' in param:
            self.STK2EDGE = param['STK2EDGE']
            self.STK2EDGEgiven = True
        elif 'STK2EDGE'.swapcase() in param:
            self.STK2EDGE = param['STK2EDGE'.swapcase()]
            self.STK2EDGEgiven = True
        else:
            if self.STK2EDGEgiven == False:
                self.STK2EDGE = 0.0
        if 'LSTK2EDGE' in param:
            self.LSTK2EDGE = param['LSTK2EDGE']
            self.LSTK2EDGEgiven = True
        elif 'LSTK2EDGE'.swapcase() in param:
            self.LSTK2EDGE = param['LSTK2EDGE'.swapcase()]
            self.LSTK2EDGEgiven = True
        else:
            if self.LSTK2EDGEgiven == False:
                self.LSTK2EDGE = 0.0
        if 'WSTK2EDGE' in param:
            self.WSTK2EDGE = param['WSTK2EDGE']
            self.WSTK2EDGEgiven = True
        elif 'WSTK2EDGE'.swapcase() in param:
            self.WSTK2EDGE = param['WSTK2EDGE'.swapcase()]
            self.WSTK2EDGEgiven = True
        else:
            if self.WSTK2EDGEgiven == False:
                self.WSTK2EDGE = 0.0
        if 'PSTK2EDGE' in param:
            self.PSTK2EDGE = param['PSTK2EDGE']
            self.PSTK2EDGEgiven = True
        elif 'PSTK2EDGE'.swapcase() in param:
            self.PSTK2EDGE = param['PSTK2EDGE'.swapcase()]
            self.PSTK2EDGEgiven = True
        else:
            if self.PSTK2EDGEgiven == False:
                self.PSTK2EDGE = 0.0
        if 'STETA0EDGE' in param:
            self.STETA0EDGE = param['STETA0EDGE']
            self.STETA0EDGEgiven = True
        elif 'STETA0EDGE'.swapcase() in param:
            self.STETA0EDGE = param['STETA0EDGE'.swapcase()]
            self.STETA0EDGEgiven = True
        else:
            if self.STETA0EDGEgiven == False:
                self.STETA0EDGE = 0.0
        if 'LSTETA0EDGE' in param:
            self.LSTETA0EDGE = param['LSTETA0EDGE']
            self.LSTETA0EDGEgiven = True
        elif 'LSTETA0EDGE'.swapcase() in param:
            self.LSTETA0EDGE = param['LSTETA0EDGE'.swapcase()]
            self.LSTETA0EDGEgiven = True
        else:
            if self.LSTETA0EDGEgiven == False:
                self.LSTETA0EDGE = 0.0
        if 'WSTETA0EDGE' in param:
            self.WSTETA0EDGE = param['WSTETA0EDGE']
            self.WSTETA0EDGEgiven = True
        elif 'WSTETA0EDGE'.swapcase() in param:
            self.WSTETA0EDGE = param['WSTETA0EDGE'.swapcase()]
            self.WSTETA0EDGEgiven = True
        else:
            if self.WSTETA0EDGEgiven == False:
                self.WSTETA0EDGE = 0.0
        if 'PSTETA0EDGE' in param:
            self.PSTETA0EDGE = param['PSTETA0EDGE']
            self.PSTETA0EDGEgiven = True
        elif 'PSTETA0EDGE'.swapcase() in param:
            self.PSTETA0EDGE = param['PSTETA0EDGE'.swapcase()]
            self.PSTETA0EDGEgiven = True
        else:
            if self.PSTETA0EDGEgiven == False:
                self.PSTETA0EDGE = 0.0
        if 'IGCLAMP' in param:
            self.IGCLAMP = param['IGCLAMP']
            self.IGCLAMPgiven = True
        elif 'IGCLAMP'.swapcase() in param:
            self.IGCLAMP = param['IGCLAMP'.swapcase()]
            self.IGCLAMPgiven = True
        else:
            if self.IGCLAMPgiven == False:
                self.IGCLAMP = 1.0
        if 'LP' in param:
            self.LP = param['LP']
            self.LPgiven = True
        elif 'LP'.swapcase() in param:
            self.LP = param['LP'.swapcase()]
            self.LPgiven = True
        else:
            if self.LPgiven == False:
                self.LP = 1e-05
        if 'RNOIK' in param:
            self.RNOIK = param['RNOIK']
            self.RNOIKgiven = True
        elif 'RNOIK'.swapcase() in param:
            self.RNOIK = param['RNOIK'.swapcase()]
            self.RNOIKgiven = True
        else:
            if self.RNOIKgiven == False:
                self.RNOIK = 0.0
        if 'TNOIK' in param:
            self.TNOIK = param['TNOIK']
            self.TNOIKgiven = True
        elif 'TNOIK'.swapcase() in param:
            self.TNOIK = param['TNOIK'.swapcase()]
            self.TNOIKgiven = True
        else:
            if self.TNOIKgiven == False:
                self.TNOIK = 0.0
        if 'TNOIK2' in param:
            self.TNOIK2 = param['TNOIK2']
            self.TNOIK2given = True
        elif 'TNOIK2'.swapcase() in param:
            self.TNOIK2 = param['TNOIK2'.swapcase()]
            self.TNOIK2given = True
        else:
            if self.TNOIK2given == False:
                self.TNOIK2 = 0.1
        if 'K0' in param:
            self.K0 = param['K0']
            self.K0given = True
        elif 'K0'.swapcase() in param:
            self.K0 = param['K0'.swapcase()]
            self.K0given = True
        else:
            if self.K0given == False:
                self.K0 = 0.0
        if 'LK0' in param:
            self.LK0 = param['LK0']
            self.LK0given = True
        elif 'LK0'.swapcase() in param:
            self.LK0 = param['LK0'.swapcase()]
            self.LK0given = True
        else:
            if self.LK0given == False:
                self.LK0 = 0.0
        if 'WK0' in param:
            self.WK0 = param['WK0']
            self.WK0given = True
        elif 'WK0'.swapcase() in param:
            self.WK0 = param['WK0'.swapcase()]
            self.WK0given = True
        else:
            if self.WK0given == False:
                self.WK0 = 0.0
        if 'PK0' in param:
            self.PK0 = param['PK0']
            self.PK0given = True
        elif 'PK0'.swapcase() in param:
            self.PK0 = param['PK0'.swapcase()]
            self.PK0given = True
        else:
            if self.PK0given == False:
                self.PK0 = 0.0
        if 'K01' in param:
            self.K01 = param['K01']
            self.K01given = True
        elif 'K01'.swapcase() in param:
            self.K01 = param['K01'.swapcase()]
            self.K01given = True
        else:
            if self.K01given == False:
                self.K01 = 0.0
        if 'LK01' in param:
            self.LK01 = param['LK01']
            self.LK01given = True
        elif 'LK01'.swapcase() in param:
            self.LK01 = param['LK01'.swapcase()]
            self.LK01given = True
        else:
            if self.LK01given == False:
                self.LK01 = 0.0
        if 'WK01' in param:
            self.WK01 = param['WK01']
            self.WK01given = True
        elif 'WK01'.swapcase() in param:
            self.WK01 = param['WK01'.swapcase()]
            self.WK01given = True
        else:
            if self.WK01given == False:
                self.WK01 = 0.0
        if 'PK01' in param:
            self.PK01 = param['PK01']
            self.PK01given = True
        elif 'PK01'.swapcase() in param:
            self.PK01 = param['PK01'.swapcase()]
            self.PK01given = True
        else:
            if self.PK01given == False:
                self.PK01 = 0.0
        if 'M0' in param:
            self.M0 = param['M0']
            self.M0given = True
        elif 'M0'.swapcase() in param:
            self.M0 = param['M0'.swapcase()]
            self.M0given = True
        else:
            if self.M0given == False:
                self.M0 = 1.0
        if 'LM0' in param:
            self.LM0 = param['LM0']
            self.LM0given = True
        elif 'LM0'.swapcase() in param:
            self.LM0 = param['LM0'.swapcase()]
            self.LM0given = True
        else:
            if self.LM0given == False:
                self.LM0 = 0.0
        if 'WM0' in param:
            self.WM0 = param['WM0']
            self.WM0given = True
        elif 'WM0'.swapcase() in param:
            self.WM0 = param['WM0'.swapcase()]
            self.WM0given = True
        else:
            if self.WM0given == False:
                self.WM0 = 0.0
        if 'PM0' in param:
            self.PM0 = param['PM0']
            self.PM0given = True
        elif 'PM0'.swapcase() in param:
            self.PM0 = param['PM0'.swapcase()]
            self.PM0given = True
        else:
            if self.PM0given == False:
                self.PM0 = 0.0
        if 'M01' in param:
            self.M01 = param['M01']
            self.M01given = True
        elif 'M01'.swapcase() in param:
            self.M01 = param['M01'.swapcase()]
            self.M01given = True
        else:
            if self.M01given == False:
                self.M01 = 0.0
        if 'LM01' in param:
            self.LM01 = param['LM01']
            self.LM01given = True
        elif 'LM01'.swapcase() in param:
            self.LM01 = param['LM01'.swapcase()]
            self.LM01given = True
        else:
            if self.LM01given == False:
                self.LM01 = 0.0
        if 'WM01' in param:
            self.WM01 = param['WM01']
            self.WM01given = True
        elif 'WM01'.swapcase() in param:
            self.WM01 = param['WM01'.swapcase()]
            self.WM01given = True
        else:
            if self.WM01given == False:
                self.WM01 = 0.0
        if 'PM01' in param:
            self.PM01 = param['PM01']
            self.PM01given = True
        elif 'PM01'.swapcase() in param:
            self.PM01 = param['PM01'.swapcase()]
            self.PM01given = True
        else:
            if self.PM01given == False:
                self.PM01 = 0.0
        if 'NEDGE' in param:
            self.NEDGE = param['NEDGE']
            self.NEDGEgiven = True
        elif 'NEDGE'.swapcase() in param:
            self.NEDGE = param['NEDGE'.swapcase()]
            self.NEDGEgiven = True
        else:
            if self.NEDGEgiven == False:
                self.NEDGE = 1.0
        if 'NOIA1_EDGE' in param:
            self.NOIA1_EDGE = param['NOIA1_EDGE']
            self.NOIA1_EDGEgiven = True
        elif 'NOIA1_EDGE'.swapcase() in param:
            self.NOIA1_EDGE = param['NOIA1_EDGE'.swapcase()]
            self.NOIA1_EDGEgiven = True
        else:
            if self.NOIA1_EDGEgiven == False:
                self.NOIA1_EDGE = 0.0
        if 'NOIAX_EDGE' in param:
            self.NOIAX_EDGE = param['NOIAX_EDGE']
            self.NOIAX_EDGEgiven = True
        elif 'NOIAX_EDGE'.swapcase() in param:
            self.NOIAX_EDGE = param['NOIAX_EDGE'.swapcase()]
            self.NOIAX_EDGEgiven = True
        else:
            if self.NOIAX_EDGEgiven == False:
                self.NOIAX_EDGE = 1.0
        if 'FNOIMOD' in param:
            self.FNOIMOD = param['FNOIMOD']
            self.FNOIMODgiven = True
        elif 'FNOIMOD'.swapcase() in param:
            self.FNOIMOD = param['FNOIMOD'.swapcase()]
            self.FNOIMODgiven = True
        else:
            if self.FNOIMODgiven == False:
                self.FNOIMOD = 0.0
        if 'LH' in param:
            self.LH = param['LH']
            self.LHgiven = True
        elif 'LH'.swapcase() in param:
            self.LH = param['LH'.swapcase()]
            self.LHgiven = True
        else:
            if self.LHgiven == False:
                self.LH = 1e-08
        if 'NOIA2' in param:
            self.NOIA2 = param['NOIA2']
            self.NOIA2given = True
        elif 'NOIA2'.swapcase() in param:
            self.NOIA2 = param['NOIA2'.swapcase()]
            self.NOIA2given = True
        else:
            if self.NOIA2given == False:
                self.NOIA2 = self.NOIA
        if 'HNDEP' in param:
            self.HNDEP = param['HNDEP']
            self.HNDEPgiven = True
        elif 'HNDEP'.swapcase() in param:
            self.HNDEP = param['HNDEP'.swapcase()]
            self.HNDEPgiven = True
        else:
            if self.HNDEPgiven == False:
                self.HNDEP = self.NDEP
        if 'ABULK' in param:
            self.ABULK = param['ABULK']
            self.ABULKgiven = True
        elif 'ABULK'.swapcase() in param:
            self.ABULK = param['ABULK'.swapcase()]
            self.ABULKgiven = True
        else:
            if self.ABULKgiven == False:
                self.ABULK = 1.0
        if 'C0' in param:
            self.C0 = param['C0']
            self.C0given = True
        elif 'C0'.swapcase() in param:
            self.C0 = param['C0'.swapcase()]
            self.C0given = True
        else:
            if self.C0given == False:
                self.C0 = 0.0
        if 'LC0' in param:
            self.LC0 = param['LC0']
            self.LC0given = True
        elif 'LC0'.swapcase() in param:
            self.LC0 = param['LC0'.swapcase()]
            self.LC0given = True
        else:
            if self.LC0given == False:
                self.LC0 = 0.0
        if 'WC0' in param:
            self.WC0 = param['WC0']
            self.WC0given = True
        elif 'WC0'.swapcase() in param:
            self.WC0 = param['WC0'.swapcase()]
            self.WC0given = True
        else:
            if self.WC0given == False:
                self.WC0 = 0.0
        if 'PC0' in param:
            self.PC0 = param['PC0']
            self.PC0given = True
        elif 'PC0'.swapcase() in param:
            self.PC0 = param['PC0'.swapcase()]
            self.PC0given = True
        else:
            if self.PC0given == False:
                self.PC0 = 0.0
        if 'C01' in param:
            self.C01 = param['C01']
            self.C01given = True
        elif 'C01'.swapcase() in param:
            self.C01 = param['C01'.swapcase()]
            self.C01given = True
        else:
            if self.C01given == False:
                self.C01 = 0.0
        if 'LC01' in param:
            self.LC01 = param['LC01']
            self.LC01given = True
        elif 'LC01'.swapcase() in param:
            self.LC01 = param['LC01'.swapcase()]
            self.LC01given = True
        else:
            if self.LC01given == False:
                self.LC01 = 0.0
        if 'WC01' in param:
            self.WC01 = param['WC01']
            self.WC01given = True
        elif 'WC01'.swapcase() in param:
            self.WC01 = param['WC01'.swapcase()]
            self.WC01given = True
        else:
            if self.WC01given == False:
                self.WC01 = 0.0
        if 'PC01' in param:
            self.PC01 = param['PC01']
            self.PC01given = True
        elif 'PC01'.swapcase() in param:
            self.PC01 = param['PC01'.swapcase()]
            self.PC01given = True
        else:
            if self.PC01given == False:
                self.PC01 = 0.0
        if 'C0SI' in param:
            self.C0SI = param['C0SI']
            self.C0SIgiven = True
        elif 'C0SI'.swapcase() in param:
            self.C0SI = param['C0SI'.swapcase()]
            self.C0SIgiven = True
        else:
            if self.C0SIgiven == False:
                self.C0SI = 1.0
        if 'LC0SI' in param:
            self.LC0SI = param['LC0SI']
            self.LC0SIgiven = True
        elif 'LC0SI'.swapcase() in param:
            self.LC0SI = param['LC0SI'.swapcase()]
            self.LC0SIgiven = True
        else:
            if self.LC0SIgiven == False:
                self.LC0SI = 0.0
        if 'WC0SI' in param:
            self.WC0SI = param['WC0SI']
            self.WC0SIgiven = True
        elif 'WC0SI'.swapcase() in param:
            self.WC0SI = param['WC0SI'.swapcase()]
            self.WC0SIgiven = True
        else:
            if self.WC0SIgiven == False:
                self.WC0SI = 0.0
        if 'PC0SI' in param:
            self.PC0SI = param['PC0SI']
            self.PC0SIgiven = True
        elif 'PC0SI'.swapcase() in param:
            self.PC0SI = param['PC0SI'.swapcase()]
            self.PC0SIgiven = True
        else:
            if self.PC0SIgiven == False:
                self.PC0SI = 0.0
        if 'C0SI1' in param:
            self.C0SI1 = param['C0SI1']
            self.C0SI1given = True
        elif 'C0SI1'.swapcase() in param:
            self.C0SI1 = param['C0SI1'.swapcase()]
            self.C0SI1given = True
        else:
            if self.C0SI1given == False:
                self.C0SI1 = 0.0
        if 'LC0SI1' in param:
            self.LC0SI1 = param['LC0SI1']
            self.LC0SI1given = True
        elif 'LC0SI1'.swapcase() in param:
            self.LC0SI1 = param['LC0SI1'.swapcase()]
            self.LC0SI1given = True
        else:
            if self.LC0SI1given == False:
                self.LC0SI1 = 0.0
        if 'WC0SI1' in param:
            self.WC0SI1 = param['WC0SI1']
            self.WC0SI1given = True
        elif 'WC0SI1'.swapcase() in param:
            self.WC0SI1 = param['WC0SI1'.swapcase()]
            self.WC0SI1given = True
        else:
            if self.WC0SI1given == False:
                self.WC0SI1 = 0.0
        if 'PC0SI1' in param:
            self.PC0SI1 = param['PC0SI1']
            self.PC0SI1given = True
        elif 'PC0SI1'.swapcase() in param:
            self.PC0SI1 = param['PC0SI1'.swapcase()]
            self.PC0SI1given = True
        else:
            if self.PC0SI1given == False:
                self.PC0SI1 = 0.0
        if 'C0SISAT' in param:
            self.C0SISAT = param['C0SISAT']
            self.C0SISATgiven = True
        elif 'C0SISAT'.swapcase() in param:
            self.C0SISAT = param['C0SISAT'.swapcase()]
            self.C0SISATgiven = True
        else:
            if self.C0SISATgiven == False:
                self.C0SISAT = 0.0
        if 'LC0SISAT' in param:
            self.LC0SISAT = param['LC0SISAT']
            self.LC0SISATgiven = True
        elif 'LC0SISAT'.swapcase() in param:
            self.LC0SISAT = param['LC0SISAT'.swapcase()]
            self.LC0SISATgiven = True
        else:
            if self.LC0SISATgiven == False:
                self.LC0SISAT = 0.0
        if 'WC0SISAT' in param:
            self.WC0SISAT = param['WC0SISAT']
            self.WC0SISATgiven = True
        elif 'WC0SISAT'.swapcase() in param:
            self.WC0SISAT = param['WC0SISAT'.swapcase()]
            self.WC0SISATgiven = True
        else:
            if self.WC0SISATgiven == False:
                self.WC0SISAT = 0.0
        if 'PC0SISAT' in param:
            self.PC0SISAT = param['PC0SISAT']
            self.PC0SISATgiven = True
        elif 'PC0SISAT'.swapcase() in param:
            self.PC0SISAT = param['PC0SISAT'.swapcase()]
            self.PC0SISATgiven = True
        else:
            if self.PC0SISATgiven == False:
                self.PC0SISAT = 0.0
        if 'C0SISAT1' in param:
            self.C0SISAT1 = param['C0SISAT1']
            self.C0SISAT1given = True
        elif 'C0SISAT1'.swapcase() in param:
            self.C0SISAT1 = param['C0SISAT1'.swapcase()]
            self.C0SISAT1given = True
        else:
            if self.C0SISAT1given == False:
                self.C0SISAT1 = 0.0
        if 'LC0SISAT1' in param:
            self.LC0SISAT1 = param['LC0SISAT1']
            self.LC0SISAT1given = True
        elif 'LC0SISAT1'.swapcase() in param:
            self.LC0SISAT1 = param['LC0SISAT1'.swapcase()]
            self.LC0SISAT1given = True
        else:
            if self.LC0SISAT1given == False:
                self.LC0SISAT1 = 0.0
        if 'WC0SISAT1' in param:
            self.WC0SISAT1 = param['WC0SISAT1']
            self.WC0SISAT1given = True
        elif 'WC0SISAT1'.swapcase() in param:
            self.WC0SISAT1 = param['WC0SISAT1'.swapcase()]
            self.WC0SISAT1given = True
        else:
            if self.WC0SISAT1given == False:
                self.WC0SISAT1 = 0.0
        if 'PC0SISAT1' in param:
            self.PC0SISAT1 = param['PC0SISAT1']
            self.PC0SISAT1given = True
        elif 'PC0SISAT1'.swapcase() in param:
            self.PC0SISAT1 = param['PC0SISAT1'.swapcase()]
            self.PC0SISAT1given = True
        else:
            if self.PC0SISAT1given == False:
                self.PC0SISAT1 = 0.0
        if 'minr' in param:
            self.minr = param['minr']
            self.minrgiven = True
        elif 'minr'.swapcase() in param:
            self.minr = param['minr'.swapcase()]
            self.minrgiven = True
        else:
            if self.minrgiven == False:
                self.minr = 0.001
        if 'HVMOD' in param:
            self.HVMOD = param['HVMOD']
            self.HVMODgiven = True
        elif 'HVMOD'.swapcase() in param:
            self.HVMOD = param['HVMOD'.swapcase()]
            self.HVMODgiven = True
        else:
            if self.HVMODgiven == False:
                self.HVMOD = 0.0
        if 'HVCAP' in param:
            self.HVCAP = param['HVCAP']
            self.HVCAPgiven = True
        elif 'HVCAP'.swapcase() in param:
            self.HVCAP = param['HVCAP'.swapcase()]
            self.HVCAPgiven = True
        else:
            if self.HVCAPgiven == False:
                self.HVCAP = 0.0
        if 'HVCAPS' in param:
            self.HVCAPS = param['HVCAPS']
            self.HVCAPSgiven = True
        elif 'HVCAPS'.swapcase() in param:
            self.HVCAPS = param['HVCAPS'.swapcase()]
            self.HVCAPSgiven = True
        else:
            if self.HVCAPSgiven == False:
                self.HVCAPS = 0.0
        if 'IIMOD' in param:
            self.IIMOD = param['IIMOD']
            self.IIMODgiven = True
        elif 'IIMOD'.swapcase() in param:
            self.IIMOD = param['IIMOD'.swapcase()]
            self.IIMODgiven = True
        else:
            if self.IIMODgiven == False:
                self.IIMOD = 0.0
        if 'NDRIFTD' in param:
            self.NDRIFTD = param['NDRIFTD']
            self.NDRIFTDgiven = True
        elif 'NDRIFTD'.swapcase() in param:
            self.NDRIFTD = param['NDRIFTD'.swapcase()]
            self.NDRIFTDgiven = True
        else:
            if self.NDRIFTDgiven == False:
                self.NDRIFTD = 5e+16
        if 'VDRIFT' in param:
            self.VDRIFT = param['VDRIFT']
            self.VDRIFTgiven = True
        elif 'VDRIFT'.swapcase() in param:
            self.VDRIFT = param['VDRIFT'.swapcase()]
            self.VDRIFTgiven = True
        else:
            if self.VDRIFTgiven == False:
                self.VDRIFT = 100000.0
        if 'MDRIFT' in param:
            self.MDRIFT = param['MDRIFT']
            self.MDRIFTgiven = True
        elif 'MDRIFT'.swapcase() in param:
            self.MDRIFT = param['MDRIFT'.swapcase()]
            self.MDRIFTgiven = True
        else:
            if self.MDRIFTgiven == False:
                self.MDRIFT = 1.0
        if 'NDRIFTS' in param:
            self.NDRIFTS = param['NDRIFTS']
            self.NDRIFTSgiven = True
        elif 'NDRIFTS'.swapcase() in param:
            self.NDRIFTS = param['NDRIFTS'.swapcase()]
            self.NDRIFTSgiven = True
        else:
            if self.NDRIFTSgiven == False:
                self.NDRIFTS = self.NDRIFTD
        if 'RDLCW' in param:
            self.RDLCW = param['RDLCW']
            self.RDLCWgiven = True
        elif 'RDLCW'.swapcase() in param:
            self.RDLCW = param['RDLCW'.swapcase()]
            self.RDLCWgiven = True
        else:
            if self.RDLCWgiven == False:
                self.RDLCW = 100.0
        if 'RSLCW' in param:
            self.RSLCW = param['RSLCW']
            self.RSLCWgiven = True
        elif 'RSLCW'.swapcase() in param:
            self.RSLCW = param['RSLCW'.swapcase()]
            self.RSLCWgiven = True
        else:
            if self.RSLCWgiven == False:
                self.RSLCW = 0.0
        if 'PDRWB' in param:
            self.PDRWB = param['PDRWB']
            self.PDRWBgiven = True
        elif 'PDRWB'.swapcase() in param:
            self.PDRWB = param['PDRWB'.swapcase()]
            self.PDRWBgiven = True
        else:
            if self.PDRWBgiven == False:
                self.PDRWB = 0.0
        if 'VFBDRIFT' in param:
            self.VFBDRIFT = param['VFBDRIFT']
            self.VFBDRIFTgiven = True
        elif 'VFBDRIFT'.swapcase() in param:
            self.VFBDRIFT = param['VFBDRIFT'.swapcase()]
            self.VFBDRIFTgiven = True
        else:
            if self.VFBDRIFTgiven == False:
                self.VFBDRIFT = -1.0
        if 'VFBOV' in param:
            self.VFBOV = param['VFBOV']
            self.VFBOVgiven = True
        elif 'VFBOV'.swapcase() in param:
            self.VFBOV = param['VFBOV'.swapcase()]
            self.VFBOVgiven = True
        else:
            if self.VFBOVgiven == False:
                self.VFBOV = -1.0
        if 'LOVER' in param:
            self.LOVER = param['LOVER']
            self.LOVERgiven = True
        elif 'LOVER'.swapcase() in param:
            self.LOVER = param['LOVER'.swapcase()]
            self.LOVERgiven = True
        else:
            if self.LOVERgiven == False:
                self.LOVER = 5e-07
        if 'LOVERACC' in param:
            self.LOVERACC = param['LOVERACC']
            self.LOVERACCgiven = True
        elif 'LOVERACC'.swapcase() in param:
            self.LOVERACC = param['LOVERACC'.swapcase()]
            self.LOVERACCgiven = True
        else:
            if self.LOVERACCgiven == False:
                self.LOVERACC = self.LOVER
        if 'NDR' in param:
            self.NDR = param['NDR']
            self.NDRgiven = True
        elif 'NDR'.swapcase() in param:
            self.NDR = param['NDR'.swapcase()]
            self.NDRgiven = True
        else:
            if self.NDRgiven == False:
                self.NDR = self.NDEP
        if 'SLHV' in param:
            self.SLHV = param['SLHV']
            self.SLHVgiven = True
        elif 'SLHV'.swapcase() in param:
            self.SLHV = param['SLHV'.swapcase()]
            self.SLHVgiven = True
        else:
            if self.SLHVgiven == False:
                self.SLHV = 0.0
        if 'SLHV1' in param:
            self.SLHV1 = param['SLHV1']
            self.SLHV1given = True
        elif 'SLHV1'.swapcase() in param:
            self.SLHV1 = param['SLHV1'.swapcase()]
            self.SLHV1given = True
        else:
            if self.SLHV1given == False:
                self.SLHV1 = 1.0
        if 'ALPHADR' in param:
            self.ALPHADR = param['ALPHADR']
            self.ALPHADRgiven = True
        elif 'ALPHADR'.swapcase() in param:
            self.ALPHADR = param['ALPHADR'.swapcase()]
            self.ALPHADRgiven = True
        else:
            if self.ALPHADRgiven == False:
                self.ALPHADR = self.ALPHA0
        if 'BETADR' in param:
            self.BETADR = param['BETADR']
            self.BETADRgiven = True
        elif 'BETADR'.swapcase() in param:
            self.BETADR = param['BETADR'.swapcase()]
            self.BETADRgiven = True
        else:
            if self.BETADRgiven == False:
                self.BETADR = self.BETA0
        if 'PRTHV' in param:
            self.PRTHV = param['PRTHV']
            self.PRTHVgiven = True
        elif 'PRTHV'.swapcase() in param:
            self.PRTHV = param['PRTHV'.swapcase()]
            self.PRTHVgiven = True
        else:
            if self.PRTHVgiven == False:
                self.PRTHV = 0.0
        if 'ATHV' in param:
            self.ATHV = param['ATHV']
            self.ATHVgiven = True
        elif 'ATHV'.swapcase() in param:
            self.ATHV = param['ATHV'.swapcase()]
            self.ATHVgiven = True
        else:
            if self.ATHVgiven == False:
                self.ATHV = 0.0
        if 'HVFACTOR' in param:
            self.HVFACTOR = param['HVFACTOR']
            self.HVFACTORgiven = True
        elif 'HVFACTOR'.swapcase() in param:
            self.HVFACTOR = param['HVFACTOR'.swapcase()]
            self.HVFACTORgiven = True
        else:
            if self.HVFACTORgiven == False:
                self.HVFACTOR = 0.001
        if 'DRII1' in param:
            self.DRII1 = param['DRII1']
            self.DRII1given = True
        elif 'DRII1'.swapcase() in param:
            self.DRII1 = param['DRII1'.swapcase()]
            self.DRII1given = True
        else:
            if self.DRII1given == False:
                self.DRII1 = 1.0
        if 'DRII2' in param:
            self.DRII2 = param['DRII2']
            self.DRII2given = True
        elif 'DRII2'.swapcase() in param:
            self.DRII2 = param['DRII2'.swapcase()]
            self.DRII2given = True
        else:
            if self.DRII2given == False:
                self.DRII2 = 5.0
        if 'DELTAII' in param:
            self.DELTAII = param['DELTAII']
            self.DELTAIIgiven = True
        elif 'DELTAII'.swapcase() in param:
            self.DELTAII = param['DELTAII'.swapcase()]
            self.DELTAIIgiven = True
        else:
            if self.DELTAIIgiven == False:
                self.DELTAII = 0.5
        self.calc(**param)

    # Clamped exponential function
    def lexp(self, x):
        if (x > 80.0):
            return 5.540622384e34 * (1.0 + x - 80.0)
        elif (x < -80.0):
            return 1.804851387e-35
        else:
            return exp(x)

    # Smoothing def for (max of x, x0 with deltax)
    def Smooth(self, x, x0, deltax):
        return 0.5 * (x + x0 + sqrt((x - x0) * (x - x0) + 0.25 * deltax * deltax))

    # Smoothing def for (min of x, x0 with deltax)
    def Smooth2(self, x, x0, deltax):
        return 0.5 * (x + x0 - sqrt((x - x0) * (x - x0) + 0.25 * deltax * deltax)) + 0.25 * deltax

    # Clamped log function
    def lln(self, x):
        return log(max(x, 1.0e-38))

    # Hyperbolic smoothing function
    def hypsmooth(self, x, c):
        return 0.5 * (x + sqrt(x * x + 4.0 * c * c))

    # Junction capacitance macro between S/D and bulk
    def JunCap(self, Czbx, Vbx_jct, PBX_t, MJX, czbx_p1, czbx_p2):
        if (Czbx > 0.0):
            T1 = Vbx_jct / PBX_t
            if (T1 < 0.9):
                arg = 1.0 - T1
                if (MJX == 0.5):
                    sarg = 1.0 / sqrt(arg)
                else:
                    sarg = self.lexp(-MJX * self.lln(arg))
                return PBX_t * Czbx * (1.0 - arg * sarg) / (1.0 - MJX)
            else:
                T2 = czbx_p1 * (T1 - 1.0) * (5.0 * MJX * (T1 - 1.0) + (1.0 + MJX))
                return PBX_t * Czbx * (T2 + czbx_p2)
        else:
            return 0.0

    # Normalized pinch-off voltage including PD
    def PO_psip(self, vg_vfb, gamma, DPD):
        T1       = 1.0 + DPD
        vgfbPD   = vg_vfb / T1
        gammaPD  = gamma / T1
        T1       = 0.5 * vgfbPD - 3.0 * (1.0 + gammaPD / 1.41421356237309504880)
        T2       = T1 + sqrt(T1 * T1 + 6.0 * vgfbPD)
        if (vgfbPD < 0.0):
            T3   = (vgfbPD - T2) / gammaPD
            return -self.lln(1.0 - T2 + T3 * T3)
        else:
            T3   = self.lexp(-T2)
            T1   = 0.5 * gammaPD
            T2   = sqrt(vgfbPD - 1.0 + T3 + T1 * T1) - T1
            return T2 * T2 + 1.0 - T3

    # Normalized charge-voltage relationship
    def BSIM_q(self, psip, phib, vch, gam):
        T8 = 0.5 * (psip + 1.0 + sqrt((psip - 1.0) * (psip - 1.0) + 0.25 * 2.0 * 2.0))
        sqrtpsip = sqrt(T8)
        T9 = 1.0 + gam / (2.0 * sqrtpsip)
        T0 = (1.0 + (gam / (2.0 * sqrtpsip))) / gam
        T1 = psip - 2.0 * phib - vch
        T2 = T1 - self.lln(4.0 * T0 * sqrtpsip)
        T8 = 0.5 * (T2 - 0.201491 - sqrt(T2 * (T2 + 0.402982) + 2.446562))
        sqrtpsisa = sqrtpsip
        if (T8 <= -68.0):
            T4 = -100.0
            T5 = 20.0
            if (T8 < T4 - 0.5 * T5):
                T3 = self.lexp(T4)
            else:
                if (T8 > T4 + 0.5 * T5):
                    T3 = self.lexp(T8)
                else:
                    T2 = (T8 - T4) / T5
                    T6 = T2 * T2
                    T3 = self.lexp(T4 + T5 * ((5.0 / 64.0) + 0.5 * T2 + T6 * ((15.0 / 16.0) - T6 * (1.25 - T6))))
            return T3 * (1.0 + T1 - T8 - self.lln(2.0 * T0 * (T3 * 2.0 * T0 + 2.0 * sqrtpsisa)))
        else:
            T3 = self.lexp(T8)
            sqrtpsisainv = 1.0 / sqrtpsisa
            T4 = 2.0 * T3 + self.lln(T3 * 2.0 * T0 * (T3 *  2.0 * T0 + 2.0 * sqrtpsisa)) - T1
            T5 = 2.0 + (1.0 / T3) + (T0 + sqrtpsisainv) / (T0 * T3 + sqrtpsisa)
            T3 = T3 - T4 / T5
            T4 = 2.0 * T3 + self.lln(T3 * 2.0 * T0 * (T3 * 2.0 * T0 + 2.0 * sqrtpsisa)) - T1
            T5 = 2.0 + (1.0 / T3) + (T0 + sqrtpsisainv) / (T0 * T3 + sqrtpsisa)
            T6 = ((T0 + sqrtpsisainv) / (T0 * T3 + sqrtpsisa)) * ((T0 + sqrtpsisainv) / (T0 * T3 + sqrtpsisa))
            T7 = -((1.0 / T3) * (1.0 / T3)) - (1.0 / (sqrtpsisa * sqrtpsisa * sqrtpsisa * (T0 * T3 + sqrtpsisa))) - T6
            return T3 - (T4 / T5) * (1.0 + T4 * T7 / (2.0 * T5 * T5))

    # Define GEOMOD and RGEOMOD in the modelcard
    def BSIMBULKNumFingerDiff(self, nf, minSD):
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

    def BSIMBULKRdsEndIso(self, Weffcj, Rsh, DMCG, DMCI, DMDG, nuEnd, rgeo, SRCFLAG):
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
                print("Warning: (instance %M) Specified RGEO = %d not matched (self.BSIMBULKRdsEndIso), Rend is set to zero.", rgeo)
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
                print("Warning: (instance %M) Specified RGEO=%d not matched (self.BSIMBULKRdsEndIso type 2), Rend is set to zero.", rgeo)
                Rend = 0.0
        return Rend

    def BSIMBULKRdsEndSha(self, Weffcj, Rsh, DMCG, DMCI, DMDG, nuEnd, rgeo, SRCFLAG):
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
                print("Warning: (instance %M) Specified RGEO = %d not matched (self.BSIMBULKRdsEndSha), Rend is set to zero.", rgeo)
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
                print("Warning: (instance %M) Specified RGEO=%d not matched (self.BSIMBULKRdsEndSha type 2), Rend is set to zero.", rgeo)
                Rend = 0.0
        return Rend

    def BSIMBULKRdseffGeo(self, nf, geo, rgeo, minSD, Weffcj, Rsh, DMCG, DMCI, DMDG, SRCFLAG):
        if (geo < 9):
            nuEndD, nuIntD, nuEndS, nuIntS = self.BSIMBULKNumFingerDiff(nf, minSD)
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
                Rend = self.BSIMBULKRdsEndIso(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndS, rgeo, 1)
            else:
                Rend = self.BSIMBULKRdsEndIso(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndD, rgeo, 0)
        elif (geo == 1):
            if (SRCFLAG == 1):
                Rend = self.BSIMBULKRdsEndIso(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndS, rgeo, 1)
            else:
                Rend = self.BSIMBULKRdsEndSha(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndD, rgeo, 0)
        elif (geo == 2):
            if (SRCFLAG == 1):
                Rend = self.BSIMBULKRdsEndSha(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndS, rgeo, 1)
            else:
                Rend = self.BSIMBULKRdsEndIso(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndD, rgeo, 0)
        elif (geo == 3):
            if (SRCFLAG == 1):
                Rend = self.BSIMBULKRdsEndSha(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndS, rgeo, 1)
            else:
                Rend = self.BSIMBULKRdsEndSha(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndD, rgeo, 0)
        elif (geo == 4):
            if (SRCFLAG == 1):
                Rend = self.BSIMBULKRdsEndIso(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndS, rgeo, 1)
            else:
                Rend = Rsh * DMDG / Weffcj
        elif (geo == 5):
            if (SRCFLAG == 1):
                Rend = self.BSIMBULKRdsEndSha(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndS, rgeo, 1)
            else:
                if (nuEndD == 0):
                    Rend = 0.0
                else:
                    Rend = Rsh * DMDG / (Weffcj * nuEndD)
        elif (geo == 6):
            if (SRCFLAG == 1):
                Rend = Rsh * DMDG / Weffcj
            else:
                Rend = self.BSIMBULKRdsEndIso(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndD, rgeo, 0)
        elif (geo == 7):
            if (SRCFLAG == 1):
                if (nuEndS == 0):
                    Rend = 0.0
                else:
                    Rend = Rsh * DMDG / (Weffcj * nuEndS)
            else:
                Rend = self.BSIMBULKRdsEndSha(Weffcj, Rsh, DMCG, DMCI, DMDG, nuEndD, rgeo, 0)
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
            print("Warning: (instance %M) Specified GEO=%d not matched (self.BSIMBULKRdseffGeo), Rint is set to zero.", geo)
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
    def BSIMBULKPAeffGeo(self, nf, geo, minSD, Weffcj, DMCG, DMCI, DMDG):
        if (geo < 9):
            nuEndD, nuIntD, nuEndS, nuIntS = self.BSIMBULKNumFingerDiff(nf, minSD)
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
            print("Warning: (instance %M) Specified GEO=%d not matched (self.BSIMBULKPAeffGeo), PS,PD,AS,AD set to zero.", geo)
            Ps = 0
            Pd = 0
            As = 0
            Ad = 0
        return Ps, Pd, As, Ad

    def calc(self, **param):
        # Bias-independent calculations
        if (self.TYPE == self.ntype):
            self.devsign = 1
        else:
            self.devsign = -1

        # Constants
        self.epssi    = self.EPSRSUB * self.EPS0
        self.epsox    = self.EPSROX * self.EPS0
        self.Cox      = self.EPSROX * self.EPS0 / self.TOXE
        self.epsratio = self.EPSRSUB / self.EPSROX

        # Physical oxide thickness
        if ("TOXP" not in param.keys()):
            self.BSIMBULKTOXP = (self.TOXE * self.EPSROX / 3.9) - self.DTOX
        else:
            self.BSIMBULKTOXP = self.TOXP
        self.L_mult = self.L * self.LMLT
        self.W_mult = self.W * self.WMLT
        self.Lnew = self.L_mult + self.XL
        if (self.Lnew <= 0.0):
            print("Fatal: Ldrawn * LMLT + XL = %e for %M is non-positive", Lnew)
        self.W_by_NF = self.W_mult / self.NF
        self.Wnew    = self.W_by_NF + self.XW
        if (self.Wnew <= 0.0):
            print("Fatal: W / NF * WMLT + XW = %e for %M is non-positive", Wnew)

        # Leff and Weff for I-V
        self.L_LLN      = self.Lnew**-self.LLN
        self.W_LWN      = self.Wnew**-self.LWN
        self.LW_LLN_LWN = self.L_LLN * self.W_LWN
        self.dLIV       = self.LINT + self.LL * self.L_LLN + self.LW * self.W_LWN + self.LWL * self.LW_LLN_LWN
        self.L_WLN      = self.Lnew**-self.WLN
        self.W_WWN      = self.Wnew**-self.WWN
        self.LW_WLN_WWN = self.L_WLN * self.W_WWN
        self.dWIV       = self.WINT + self.WL * self.L_WLN + self.WW * self.W_WWN + self.WWL * self.LW_WLN_WWN
        self.Leff       = self.Lnew - 2.0 * self.dLIV
        if (self.Leff <= 0.0):
            print("Fatal: Effective channel length = %e for  %M is non-positive", Leff)
        elif (self.Leff <= 1.0e-9):
            print("Warning: Effective channel length = %e for %M is <= 1.0e-9. Recommended Leff >= 1e-8", Leff)
        self.Weff = self.Wnew - 2.0 * self.dWIV
        if (self.Weff <= 0.0):
             print("Fatal: Effective channel Width = %e for %M is non-positive", Weff)
        elif (self.Weff <= 1.0e-9):
            print("Warning: Effective channel width = %e for %M is <= 1.0e-9. Recommended Weff >= 1e-8", Weff)

        # Leff and Weff for C-V
        self.dLCV = self.DLC + self.LLC * self.L_LLN + self.LWC * self.W_LWN + self.LWLC * self.LW_LLN_LWN
        self.dWCV = self.DWC + self.WLC * self.L_WLN + self.WWC * self.W_WWN + self.WWLC * self.LW_WLN_WWN
        self.Lact = self.Lnew - 2.0 * self.dLCV
        if (self.Lact <= 0.0):
             print("Fatal: Effective channel length for C-V = %e for %M is non-positive", Lact)
        elif (self.Lact <= 1.0e-9):
            print("Warning: Effective channel length for C-V = %e for %M is <= 1.0e-9. Recommended Lact >= 1e-8", Lact)
        self.Wact = self.Wnew - 2.0 * self.dWCV
        if (self.Wact <= 0.0):
            print("Fatal: Effective channel width for C-V = %e for %M is non-positive", Wact)
        elif (self.Wact <= 1.0e-9):
            print("Warning: Effective channel width for C-V = %e for %M is <= 1.0e-9. Recommended Wact >= 1e-8", Wact)

        # Weffcj for diode, GIDL etc.
        self.dWJ    = self.DWJ + self.WLC / self.Lnew**self.WLN + self.WWC / self.Wnew**self.WWN + self.WWLC / self.Lnew**self.WLN / self.Wnew**self.WWN
        self.Weffcj = self.Wnew - 2.0 * self.dWJ
        if (self.Weffcj <= 0.0):
            print("Fatal: Effective channel width for S/D junctions = %e for %M is non-positive", Weffcj)
        self.Inv_L     = 1.0e-6 / self.Leff
        self.Inv_W     = 1.0e-6 / self.Weff
        self.Inv_Lact  = 1.0e-6 / self.Lact
        self.Inv_Wact  = 1.0e-6 / self.Wact
        self.Inv_Llong = 1.0e-6 / self.LLONG
        self.Inv_Wwide = 1.0e-6 / self.WWIDE
        self.Inv_WL    = self.Inv_L * self.Inv_W

        # Effective length and width for binning
        self.L_LLN1 = self.L_LLN
        self.L_WLN1 = self.L_WLN
        if (self.DLBIN != 0.0):
            if (self.DLBIN <= -self.Lnew):
                print("Fatal: DLBIN for %M = %e is <= -Ldrawn * LMLT", DLBIN)
            else:
                self.L_LLN1 = (self.Lnew + self.DLBIN)**-self.LLN
                self.L_WLN1 = (self.Lnew + self.DLBIN)**-self.WLN
        self.W_LWN1 = self.W_LWN
        self.W_WWN1 = self.W_WWN
        if (self.DWBIN != 0.0):
            if (self.DWBIN <= -self.Wnew):
                print("Fatal: DWBIN for %M = %e is <= -Wdrawn * WMLT", DWBIN)
            else:
                self.W_LWN1 = (self.Wnew + self.DWBIN)**-self.LWN
                self.W_WWN1 = (self.Wnew + self.DWBIN)**-self.WWN
        self.LW_LLN_LWN1 = self.L_LLN1 * self.W_LWN1
        self.dLB         = self.LINT + self.LL * self.L_LLN1 + self.LW * self.W_LWN1 + self.LWL * self.LW_LLN_LWN1
        self.LW_WLN_WWN1 = self.L_WLN1 * self.W_WWN1
        self.dWB         = self.WINT + self.WL * self.L_WLN1 + self.WW * self.W_WWN1 + self.WWL * self.LW_WLN_WWN1
        self.Leff1 = self.Lnew - 2.0 * self.dLB + self.DLBIN
        if (self.Leff1 <= 0.0):
            print("Fatal: Effective channel length for binning = %e for %M is non-positive", Leff1)
        self.Weff1 = self.Wnew - 2.0 * self.dWB + self.DWBIN
        if (self.Weff1 <= 0.0):
            print("Fatal: Effective channel width for binning = %e for %M is non-positive", Weff1)
        if (self.BINUNIT == 1):
            self.BIN_L = 1.0e-6 / self.Leff1
            self.BIN_W = 1.0e-6 / self.Weff1
        else:
            self.BIN_L = 1.0 / self.Leff1
            self.BIN_W = 1.0 / self.Weff1
        self.BIN_WL         = self.BIN_L * self.BIN_W
        self.VFB_i          = self.VFB + self.BIN_L * self.LVFB + self.BIN_W * self.WVFB + self.BIN_WL * self.PVFB
        self.VFBCV_i        = self.VFBCV + self.BIN_L * self.LVFBCV + self.BIN_W * self.WVFBCV + self.BIN_WL * self.PVFBCV
        self.NSD_i          = self.NSD + self.BIN_L * self.LNSD + self.BIN_W * self.WNSD + self.BIN_WL * self.PNSD
        self.NDEP_i         = self.NDEP + self.BIN_L * self.LNDEP + self.BIN_W * self.WNDEP + self.BIN_WL * self.PNDEP
        self.NDEPCV_i       = self.NDEPCV + self.BIN_L * self.LNDEPCV + self.BIN_W * self.WNDEPCV + self.BIN_WL * self.PNDEPCV
        self.NGATE_i        = self.NGATE + self.BIN_L * self.LNGATE + self.BIN_W * self.WNGATE + self.BIN_WL * self.PNGATE
        self.CIT_i          = self.CIT + self.BIN_L * self.LCIT + self.BIN_W * self.WCIT + self.BIN_WL * self.PCIT
        self.NFACTOR_i      = self.NFACTOR + self.BIN_L * self.LNFACTOR + self.BIN_W * self.WNFACTOR + self.BIN_WL * self.PNFACTOR
        self.CDSCD_i        = self.CDSCD + self.BIN_L * self.LCDSCD + self.BIN_W * self.WCDSCD + self.BIN_WL * self.PCDSCD
        self.CDSCB_i        = self.CDSCB + self.BIN_L * self.LCDSCB + self.BIN_W * self.WCDSCB + self.BIN_WL * self.PCDSCB
        self.DVTP0_i        = self.DVTP0 + self.BIN_L * self.LDVTP0 + self.BIN_W * self.WDVTP0 + self.BIN_WL * self.PDVTP0
        self.DVTP1_i        = self.DVTP1 + self.BIN_L * self.LDVTP1 + self.BIN_W * self.WDVTP1 + self.BIN_WL * self.PDVTP1
        self.DVTP2_i        = self.DVTP2 + self.BIN_L * self.LDVTP2 + self.BIN_W * self.WDVTP2 + self.BIN_WL * self.PDVTP2
        self.DVTP3_i        = self.DVTP3 + self.BIN_L * self.LDVTP3 + self.BIN_W * self.WDVTP3 + self.BIN_WL * self.PDVTP3
        self.DVTP4_i        = self.DVTP4 + self.BIN_L * self.LDVTP4 + self.BIN_W * self.WDVTP4 + self.BIN_WL * self.PDVTP4
        self.DVTP5_i        = self.DVTP5 + self.BIN_L * self.LDVTP5 + self.BIN_W * self.WDVTP5 + self.BIN_WL * self.PDVTP5
        self.K2_i           = self.K2 + self.BIN_L * self.LK2 + self.BIN_W * self.WK2 + self.BIN_WL * self.PK2
        self.K1_i           = self.K1 + self.BIN_L * self.LK1 + self.BIN_W * self.WK1 + self.BIN_WL * self.PK1
        self.XJ_i           = self.XJ + self.BIN_L * self.LXJ + self.BIN_W * self.WXJ + self.BIN_WL * self.PXJ
        self.PHIN_i         = self.PHIN + self.BIN_L * self.LPHIN + self.BIN_W * self.WPHIN + self.BIN_WL * self.PPHIN
        self.ETA0_i         = self.ETA0 + self.BIN_L * self.LETA0 + self.BIN_W * self.WETA0 + self.BIN_WL * self.PETA0
        self.ETAB_i         = self.ETAB + self.BIN_L * self.LETAB + self.BIN_W * self.WETAB + self.BIN_WL * self.PETAB
        self.DELTA_i        = self.DELTA + self.BIN_L * self.LDELTA + self.BIN_W * self.WDELTA + self.BIN_WL * self.PDELTA
        self.U0_i           = self.U0 + self.BIN_L * self.LU0 + self.BIN_W * self.WU0 + self.BIN_WL * self.PU0
        self.UA_i           = self.UA + self.BIN_L * self.LUA + self.BIN_W * self.WUA + self.BIN_WL * self.PUA
        self.UD_i           = self.UD + self.BIN_L * self.LUD + self.BIN_W * self.WUD + self.BIN_WL * self.PUD
        self.EU_i           = self.EU + self.BIN_L * self.LEU + self.BIN_W * self.WEU + self.BIN_WL * self.PEU
        self.UCS_i          = self.UCS + self.BIN_L * self.LUCS + self.BIN_W * self.WUCS + self.BIN_WL * self.PUCS
        self.UC_i           = self.UC + self.BIN_L * self.LUC + self.BIN_W * self.WUC + self.BIN_WL * self.PUC
        self.PCLM_i         = self.PCLM + self.BIN_L * self.LPCLM + self.BIN_W * self.WPCLM + self.BIN_WL * self.PPCLM
        self.PCLMCV_i       = self.PCLMCV + self.BIN_L * self.LPCLMCV + self.BIN_W * self.WPCLMCV + self.BIN_WL * self.PPCLMCV
        self.RSW_i          = self.RSW + self.BIN_L * self.LRSW + self.BIN_W * self.WRSW + self.BIN_WL * self.PRSW
        self.RDW_i          = self.RDW + self.BIN_L * self.LRDW + self.BIN_W * self.WRDW + self.BIN_WL * self.PRDW
        self.PRWG_i         = self.PRWG + self.BIN_L * self.LPRWG + self.BIN_W * self.WPRWG + self.BIN_WL * self.PPRWG
        self.PRWB_i         = self.PRWB + self.BIN_L * self.LPRWB + self.BIN_W * self.WPRWB + self.BIN_WL * self.PPRWB
        self.WR_i           = self.WR + self.BIN_L * self.LWR + self.BIN_W * self.WWR + self.BIN_WL * self.PWR
        self.RSWMIN_i       = self.RSWMIN + self.BIN_L * self.LRSWMIN + self.BIN_W * self.WRSWMIN + self.BIN_WL * self.PRSWMIN
        self.RDWMIN_i       = self.RDWMIN + self.BIN_L * self.LRDWMIN + self.BIN_W * self.WRDWMIN + self.BIN_WL * self.PRDWMIN
        self.RDSW_i         = self.RDSW + self.BIN_L * self.LRDSW + self.BIN_W * self.WRDSW + self.BIN_WL * self.PRDSW
        self.RDSWMIN_i      = self.RDSWMIN + self.BIN_L * self.LRDSWMIN + self.BIN_W * self.WRDSWMIN + self.BIN_WL * self.PRDSWMIN
        self.PTWG_i         = self.PTWG + self.BIN_L * self.LPTWG + self.BIN_W * self.WPTWG + self.BIN_WL * self.PPTWG
        self.PDIBLC_i       = self.PDIBLC + self.BIN_L * self.LPDIBLC + self.BIN_W * self.WPDIBLC + self.BIN_WL * self.PPDIBLC
        self.PDIBLCB_i      = self.PDIBLCB + self.BIN_L * self.LPDIBLCB + self.BIN_W * self.WPDIBLCB + self.BIN_WL * self.PPDIBLCB
        self.PSCBE1_i       = self.PSCBE1 + self.BIN_L * self.LPSCBE1 + self.BIN_W * self.WPSCBE1 + self.BIN_WL * self.PPSCBE1
        self.PSCBE2_i       = self.PSCBE2 + self.BIN_L * self.LPSCBE2 + self.BIN_W * self.WPSCBE2 + self.BIN_WL * self.PPSCBE2
        self.PDITS_i        = self.PDITS + self.BIN_L * self.LPDITS + self.BIN_W * self.WPDITS + self.BIN_WL * self.PPDITS
        self.PDITSD_i       = self.PDITSD + self.BIN_L * self.LPDITSD + self.BIN_W * self.WPDITSD + self.BIN_WL * self.PPDITSD
        self.FPROUT_i       = self.FPROUT + self.BIN_L * self.LFPROUT + self.BIN_W * self.WFPROUT + self.BIN_WL * self.PFPROUT
        self.PVAG_i         = self.PVAG + self.BIN_L * self.LPVAG + self.BIN_W * self.WPVAG + self.BIN_WL * self.PPVAG
        self.VSAT_i         = self.VSAT + self.BIN_L * self.LVSAT + self.BIN_W * self.WVSAT + self.BIN_WL * self.PVSAT
        self.PSAT_i         = self.PSAT + self.BIN_L * self.LPSAT + self.BIN_W * self.WPSAT + self.BIN_WL * self.PPSAT
        self.VSATCV_i       = self.VSATCV + self.BIN_L * self.LVSATCV + self.BIN_W * self.WVSATCV + self.BIN_WL * self.PVSATCV
        self.CF_i           = self.CF + self.BIN_L * self.LCF + self.BIN_W * self.WCF + self.BIN_WL * self.PCF
        self.CGSL_i         = self.CGSL + self.BIN_L * self.LCGSL + self.BIN_W * self.WCGSL + self.BIN_WL * self.PCGSL
        self.CGDL_i         = self.CGDL + self.BIN_L * self.LCGDL + self.BIN_W * self.WCGDL + self.BIN_WL * self.PCGDL
        self.CKAPPAS_i      = self.CKAPPAS + self.BIN_L * self.LCKAPPAS + self.BIN_W * self.WCKAPPAS + self.BIN_WL * self.PCKAPPAS
        self.CKAPPAD_i      = self.CKAPPAD + self.BIN_L * self.LCKAPPAD + self.BIN_W * self.WCKAPPAD + self.BIN_WL * self.PCKAPPAD
        self.ALPHA0_i       = self.ALPHA0 + self.BIN_L * self.LALPHA0 + self.BIN_W * self.WALPHA0 + self.BIN_WL * self.PALPHA0
        self.BETA0_i        = self.BETA0 + self.BIN_L * self.LBETA0 + self.BIN_W * self.WBETA0 + self.BIN_WL * self.PBETA0
        self.KVTH0WE_i      = self.KVTH0WE + self.BIN_L * self.LKVTH0WE  + self.BIN_W * self.WKVTH0WE + self.BIN_WL * self.PKVTH0WE
        self.K2WE_i         = self.K2WE + self.BIN_L * self.LK2WE + self.BIN_W * self.WK2WE + self.BIN_WL * self.PK2WE
        self.KU0WE_i        = self.KU0WE + self.BIN_L * self.LKU0WE + self.BIN_W * self.WKU0WE + self.BIN_WL * self.PKU0WE
        self.AGIDL_i        = self.AGIDL + self.BIN_L * self.LAGIDL + self.BIN_W * self.WAGIDL + self.BIN_WL * self.PAGIDL
        self.BGIDL_i        = self.BGIDL + self.BIN_L * self.LBGIDL + self.BIN_W * self.WBGIDL + self.BIN_WL * self.PBGIDL
        self.CGIDL_i        = self.CGIDL + self.BIN_L * self.LCGIDL + self.BIN_W * self.WCGIDL + self.BIN_WL * self.PCGIDL
        self.EGIDL_i        = self.EGIDL + self.BIN_L * self.LEGIDL + self.BIN_W * self.WEGIDL + self.BIN_WL * self.PEGIDL
        self.AGISL_i        = self.AGISL + self.BIN_L * self.LAGISL + self.BIN_W * self.WAGISL + self.BIN_WL * self.PAGISL
        self.BGISL_i        = self.BGISL + self.BIN_L * self.LBGISL + self.BIN_W * self.WBGISL + self.BIN_WL * self.PBGISL
        self.CGISL_i        = self.CGISL + self.BIN_L * self.LCGISL + self.BIN_W * self.WCGISL + self.BIN_WL * self.PCGISL
        self.EGISL_i        = self.EGISL + self.BIN_L * self.LEGISL + self.BIN_W * self.WEGISL + self.BIN_WL * self.PEGISL
        self.UTE_i          = self.UTE + self.BIN_L * self.LUTE + self.BIN_W * self.WUTE + self.BIN_WL * self.PUTE
        self.UA1_i          = self.UA1 + self.BIN_L * self.LUA1 + self.BIN_W * self.WUA1 + self.BIN_WL * self.PUA1
        self.UC1_i          = self.UC1 + self.BIN_L * self.LUC1 + self.BIN_W * self.WUC1 + self.BIN_WL * self.PUC1
        self.UD1_i          = self.UD1 + self.BIN_L * self.LUD1 + self.BIN_W * self.WUD1 + self.BIN_WL * self.PUD1
        self.EU1_i          = self.EU1 + self.BIN_L * self.LEU1 + self.BIN_W * self.WEU1 + self.BIN_WL * self.PEU1
        self.UCSTE_i        = self.UCSTE + self.BIN_L * self.LUCSTE + self.BIN_W * self.WUCSTE + self.BIN_WL * self.PUCSTE
        self.PRT_i          = self.PRT + self.BIN_L * self.LPRT + self.BIN_W * self.WPRT + self.BIN_WL * self.PPRT
        self.AT_i           = self.AT + self.BIN_L * self.LAT + self.BIN_W * self.WAT + self.BIN_WL * self.PAT
        self.PTWGT_i        = self.PTWGT + self.BIN_L * self.LPTWGT + self.BIN_W * self.WPTWGT + self.BIN_WL * self.PPTWGT
        self.IIT_i          = self.IIT + self.BIN_L * self.LIIT + self.BIN_W * self.WIIT + self.BIN_WL * self.PIIT
        self.TGIDL_i        = self.TGIDL + self.BIN_L * self.LTGIDL + self.BIN_W * self.WTGIDL + self.BIN_WL * self.PTGIDL
        self.IGT_i          = self.IGT + self.BIN_L * self.LIGT + self.BIN_W * self.WIGT + self.BIN_WL * self.PIGT
        self.AIGBINV_i      = self.AIGBINV + self.BIN_L * self.LAIGBINV + self.BIN_W * self.WAIGBINV + self.BIN_WL * self.PAIGBINV
        self.BIGBINV_i      = self.BIGBINV + self.BIN_L * self.LBIGBINV + self.BIN_W * self.WBIGBINV + self.BIN_WL * self.PBIGBINV
        self.CIGBINV_i      = self.CIGBINV + self.BIN_L * self.LCIGBINV + self.BIN_W * self.WCIGBINV + self.BIN_WL * self.PCIGBINV
        self.EIGBINV_i      = self.EIGBINV + self.BIN_L * self.LEIGBINV + self.BIN_W * self.WEIGBINV + self.BIN_WL * self.PEIGBINV
        self.NIGBINV_i      = self.NIGBINV + self.BIN_L * self.LNIGBINV + self.BIN_W * self.WNIGBINV + self.BIN_WL * self.PNIGBINV
        self.AIGBACC_i      = self.AIGBACC + self.BIN_L * self.LAIGBACC + self.BIN_W * self.WAIGBACC + self.BIN_WL * self.PAIGBACC
        self.BIGBACC_i      = self.BIGBACC + self.BIN_L * self.LBIGBACC + self.BIN_W * self.WBIGBACC + self.BIN_WL * self.PBIGBACC
        self.CIGBACC_i      = self.CIGBACC + self.BIN_L * self.LCIGBACC + self.BIN_W * self.WCIGBACC + self.BIN_WL * self.PCIGBACC
        self.NIGBACC_i      = self.NIGBACC + self.BIN_L * self.LNIGBACC + self.BIN_W * self.WNIGBACC + self.BIN_WL * self.PNIGBACC
        self.AIGC_i         = self.AIGC + self.BIN_L * self.LAIGC + self.BIN_W * self.WAIGC + self.BIN_WL * self.PAIGC
        self.BIGC_i         = self.BIGC + self.BIN_L * self.LBIGC + self.BIN_W * self.WBIGC + self.BIN_WL * self.PBIGC
        self.CIGC_i         = self.CIGC + self.BIN_L * self.LCIGC + self.BIN_W * self.WCIGC + self.BIN_WL * self.PCIGC
        self.AIGS_i         = self.AIGS + self.BIN_L * self.LAIGS + self.BIN_W * self.WAIGS + self.BIN_WL * self.PAIGS
        self.BIGS_i         = self.BIGS + self.BIN_L * self.LBIGS + self.BIN_W * self.WBIGS + self.BIN_WL * self.PBIGS
        self.CIGS_i         = self.CIGS + self.BIN_L * self.LCIGS + self.BIN_W * self.WCIGS + self.BIN_WL * self.PCIGS
        self.AIGD_i         = self.AIGD + self.BIN_L * self.LAIGD + self.BIN_W * self.WAIGD + self.BIN_WL * self.PAIGD
        self.BIGD_i         = self.BIGD + self.BIN_L * self.LBIGD + self.BIN_W * self.WBIGD + self.BIN_WL * self.PBIGD
        self.CIGD_i         = self.CIGD + self.BIN_L * self.LCIGD + self.BIN_W * self.WCIGD + self.BIN_WL * self.PCIGD
        self.POXEDGE_i      = self.POXEDGE + self.BIN_L * self.LPOXEDGE + self.BIN_W * self.WPOXEDGE + self.BIN_WL * self.PPOXEDGE
        self.DLCIG_i        = self.DLCIG + self.BIN_L * self.LDLCIG + self.BIN_W * self.WDLCIG + self.BIN_WL * self.PDLCIG
        self.DLCIGD_i       = self.DLCIGD + self.BIN_L * self.LDLCIGD + self.BIN_W * self.WDLCIGD + self.BIN_WL * self.PDLCIGD
        self.NTOX_i         = self.NTOX + self.BIN_L * self.LNTOX + self.BIN_W * self.WNTOX + self.BIN_WL * self.PNTOX
        self.KT1_i          = self.KT1 + self.BIN_L * self.LKT1 + self.BIN_W * self.WKT1 + self.BIN_WL * self.PKT1
        self.KT2_i          = self.KT2 + self.BIN_L * self.LKT2 + self.BIN_W * self.WKT2 + self.BIN_WL * self.PKT2
        self.PSATB_i        = self.PSATB + self.BIN_L * self.LPSATB + self.BIN_W * self.WPSATB + self.BIN_WL * self.PPSATB
        self.A1_i           = self.A1 + self.BIN_L * self.LA1 + self.BIN_W * self.WA1 + self.BIN_WL * self.PA1
        self.A11_i          = self.A11 + self.BIN_L * self.LA11 + self.BIN_W * self.WA11 + self.BIN_WL * self.PA11
        self.A2_i           = self.A2 + self.BIN_L * self.LA2 + self.BIN_W * self.WA2 + self.BIN_WL * self.PA2
        self.A21_i          = self.A21 + self.BIN_L * self.LA21 + self.BIN_W * self.WA21 + self.BIN_WL * self.PA21
        self.K0_i           = self.K0 + self.BIN_L * self.LK0 + self.BIN_W * self.WK0 + self.BIN_WL * self.PK0
        self.M0_i           = self.M0 + self.BIN_L * self.LM0 + self.BIN_W * self.WM0 + self.BIN_WL * self.PM0
        self.K01_i          = self.K01 + self.BIN_L * self.LK01 + self.BIN_W * self.WK01 + self.BIN_WL * self.PK01
        self.M01_i          = self.M01 + self.BIN_L * self.LM01 + self.BIN_W * self.WM01 + self.BIN_WL * self.PM01
        self.NFACTOREDGE_i  = self.NFACTOREDGE + self.BIN_L * self.LNFACTOREDGE + self.BIN_W * self.WNFACTOREDGE + self.BIN_WL * self.PNFACTOREDGE
        self.NDEPEDGE_i     = self.NDEPEDGE + self.BIN_L * self.LNDEPEDGE + self.BIN_W * self.WNDEPEDGE + self.BIN_WL * self.PNDEPEDGE
        self.CITEDGE_i      = self.CITEDGE + self.BIN_L * self.LCITEDGE + self.BIN_W * self.WCITEDGE + self.BIN_WL * self.PCITEDGE
        self.CDSCDEDGE_i    = self.CDSCDEDGE + self.BIN_L * self.LCDSCDEDGE + self.BIN_W * self.WCDSCDEDGE + self.BIN_WL * self.PCDSCDEDGE
        self.CDSCBEDGE_i    = self.CDSCBEDGE + self.BIN_L * self.LCDSCBEDGE + self.BIN_W * self.WCDSCBEDGE + self.BIN_WL * self.PCDSCBEDGE
        self.ETA0EDGE_i     = self.ETA0EDGE + self.BIN_L * self.LETA0EDGE + self.BIN_W * self.WETA0EDGE + self.BIN_WL * self.PETA0EDGE
        self.ETABEDGE_i     = self.ETABEDGE + self.BIN_L * self.LETABEDGE + self.BIN_W * self.WETABEDGE + self.BIN_WL * self.PETABEDGE
        self.KT1EDGE_i      = self.KT1EDGE + self.BIN_L * self.LKT1EDGE + self.BIN_W * self.WKT1EDGE + self.BIN_WL * self.PKT1EDGE
        self.KT1LEDGE_i     = self.KT1LEDGE + self.BIN_L * self.LKT1LEDGE + self.BIN_W * self.WKT1LEDGE + self.BIN_WL * self.PKT1LEDGE
        self.KT2EDGE_i      = self.KT2EDGE + self.BIN_L * self.LKT2EDGE + self.BIN_W * self.WKT2EDGE + self.BIN_WL * self.PKT2EDGE
        self.KT1EXPEDGE_i   = self.KT1EXPEDGE + self.BIN_L * self.LKT1EXPEDGE + self.BIN_W * self.WKT1EXPEDGE + self.BIN_WL * self.PKT1EXPEDGE
        self.TNFACTOREDGE_i = self.TNFACTOREDGE + self.BIN_L * self.LTNFACTOREDGE + self.BIN_W * self.WTNFACTOREDGE + self.BIN_WL * self.PTNFACTOREDGE
        self.TETA0EDGE_i    = self.TETA0EDGE + self.BIN_L * self.LTETA0EDGE + self.BIN_W * self.WTETA0EDGE + self.BIN_WL * self.PTETA0EDGE
        self.K2EDGE_i       = self.K2EDGE + self.BIN_L * self.LK2EDGE + self.BIN_W * self.WK2EDGE + self.BIN_WL * self.PK2EDGE
        self.KVTH0EDGE_i    = self.KVTH0EDGE + self.BIN_L * self.LKVTH0EDGE + self.BIN_W * self.WKVTH0EDGE + self.BIN_WL * self.PKVTH0EDGE
        self.STK2EDGE_i     = self.STK2EDGE + self.BIN_L * self.LSTK2EDGE + self.BIN_W * self.WSTK2EDGE + self.BIN_WL * self.PSTK2EDGE
        self.STETA0EDGE_i   = self.STETA0EDGE + self.BIN_L * self.LSTETA0EDGE + self.BIN_W * self.WSTETA0EDGE + self.BIN_WL * self.PSTETA0EDGE
        self.C0_i           = self.C0 + self.BIN_L * self.LC0 + self.BIN_W * self.WC0 + self.BIN_WL * self.PC0
        self.C01_i          = self.C01 + self.BIN_L * self.LC01 + self.BIN_W * self.WC01 + self.BIN_WL * self.PC01
        self.C0SI_i         = self.C0SI + self.BIN_L * self.LC0SI + self.BIN_W * self.WC0SI + self.BIN_WL * self.PC0SI
        self.C0SI1_i        = self.C0SI1 + self.BIN_L * self.LC0SI1 + self.BIN_W * self.WC0SI1 + self.BIN_WL * self.PC0SI1
        self.C0SISAT_i      = self.C0SISAT + self.BIN_L * self.LC0SISAT + self.BIN_W * self.WC0SISAT + self.BIN_WL * self.PC0SISAT
        self.C0SISAT1_i     = self.C0SISAT1 + self.BIN_L * self.LC0SISAT1 + self.BIN_W * self.WC0SISAT1 + self.BIN_WL * self.PC0SISAT1

        if (self.ASYMMOD != 0):
            self.CDSCDR_i  = self.CDSCDR + self.BIN_L * self.LCDSCDR + self.BIN_W * self.WCDSCDR + self.BIN_WL * self.PCDSCDR
            self.ETA0R_i   = self.ETA0R + self.BIN_L * self.LETA0R + self.BIN_W * self.WETA0R + self.BIN_WL * self.PETA0R
            self.U0R_i     = self.U0R + self.BIN_L * self.LU0R + self.BIN_W * self.WU0R + self.BIN_WL * self.PU0R
            self.UAR_i     = self.UAR + self.BIN_L * self.LUAR + self.BIN_W * self.WUAR + self.BIN_WL * self.PUAR
            self.UDR_i     = self.UDR + self.BIN_L * self.LUDR + self.BIN_W * self.WUDR + self.BIN_WL * self.PUDR
            self.UCSR_i    = self.UCSR + self.BIN_L * self.LUCSR + self.BIN_W * self.WUCSR + self.BIN_WL * self.PUCSR
            self.UCR_i     = self.UCR + self.BIN_L * self.LUCR + self.BIN_W * self.WUCR + self.BIN_WL * self.PUCR
            self.PCLMR_i   = self.PCLMR + self.BIN_L * self.LPCLMR + self.BIN_W * self.WPCLMR + self.BIN_WL * self.PPCLMR
            self.PDIBLCR_i = self.PDIBLCR + self.BIN_L * self.LPDIBLCR + self.BIN_W * self.WPDIBLCR + self.BIN_WL * self.PPDIBLCR
            self.VSATR_i   = self.VSATR + self.BIN_L * self.LVSATR + self.BIN_W * self.WVSATR + self.BIN_WL * self.PVSATR
            self.PSATR_i   = self.PSATR + self.BIN_L * self.LPSATR + self.BIN_W * self.WPSATR + self.BIN_WL * self.PPSATR
            self.PTWGR_i   = self.PTWGR + self.BIN_L * self.LPTWGR + self.BIN_W * self.WPTWGR + self.BIN_WL * self.PPTWGR
        else:
            self.CDSCDR_i  = 0.0
            self.ETA0R_i   = 0.0
            self.U0R_i     = 0.0
            self.UAR_i     = 0.0
            self.UDR_i     = 0.0
            self.UCSR_i    = 0.0
            self.UCR_i     = 0.0
            self.PCLMR_i   = 0.0
            self.PDIBLCR_i = 0.0
            self.VSATR_i   = 0.0
            self.PSATR_i   = 0.0
            self.PTWGR_i   = 0.0

        # Geometrical scaling
        self.T0        = self.NDEPL1 * max(self.Inv_L**self.NDEPLEXP1 - self.Inv_Llong**self.NDEPLEXP1, 0.0) + self.NDEPL2 * max(self.Inv_L**self.NDEPLEXP2 - self.Inv_Llong**self.NDEPLEXP2, 0.0)
        self.T1        = self.NDEPW * max(self.Inv_W**self.NDEPWEXP - self.Inv_Wwide**self.NDEPWEXP, 0.0) + self.NDEPWL * (self.Inv_W * self.Inv_L)**self.NDEPWLEXP
        self.NDEP_i    = self.NDEP_i * (1.0 + self.T0 + self.T1)
        self.T0        = self.NFACTORL * max(self.Inv_L**self.NFACTORLEXP - self.Inv_Llong**self.NFACTORLEXP, 0.0)
        self.T1        = self.NFACTORW * max(self.Inv_W**self.NFACTORWEXP - self.Inv_Wwide**self.NFACTORWEXP, 0.0) + self.NFACTORWL * self.Inv_WL**self.NFACTORWLEXP
        self.NFACTOR_i = self.NFACTOR_i * (1.0 + self.T0 + self.T1)
        self.T0        = (1.0 + self.CDSCDL * max(self.Inv_L**self.CDSCDLEXP - self.Inv_Llong**self.CDSCDLEXP, 0.0))
        self.CDSCD_i   = self.CDSCD_i * self.T0
        if (self.ASYMMOD != 0):
            self.CDSCDR_i = self.CDSCDR_i * self.T0
        self.CDSCB_i = self.CDSCB_i * (1.0 + self.CDSCBL * max(self.Inv_L**self.CDSCBLEXP - self.Inv_Llong**self.CDSCBLEXP, 0.0))
        self.U0_i    = self.MULU0 * self.U0_i
        if (self.MOBSCALE != 1):
            if (self.U0LEXP > 0.0):
                self.U0_i = self.U0_i * (1.0 - self.U0L * max(self.Inv_L**self.U0LEXP - self.Inv_Llong**self.U0LEXP, 0.0))
                if (self.ASYMMOD != 0):
                    self.U0R_i = self.U0R_i * (1.0 - self.U0L * max(self.Inv_L**self.U0LEXP - self.Inv_Llong**self.U0LEXP, 0.0))
            else:
                self.U0_i = self.U0_i * (1.0 - self.U0L)
                if (self.ASYMMOD != 0):
                    self.U0R_i = self.U0R_i * (1.0 - self.U0L)
        else:
            self.U0_i = self.U0_i * (1.0 - (self.UP1 * self.lexp(-self.Leff / self.LP1)) - (self.UP2 * self.lexp(-self.Leff / self.LP2)))
            if (self.ASYMMOD != 0):
                self.U0R_i = self.U0R_i * (1.0 - (self.UP1 * self.lexp(-self.Leff / self.LP1)) - (self.UP2 * self.lexp(-self.Leff / self.LP2)))
        self.T0   = self.UAL * max(self.Inv_L**self.UALEXP - self.Inv_Llong**self.UALEXP, 0.0)
        self.T1   = self.UAW * max(self.Inv_W**self.UAWEXP - self.Inv_Wwide**self.UAWEXP, 0.0) + self.UAWL * self.Inv_WL**self.UAWLEXP
        self.UA_i = self.UA_i * (1.0 + self.T0 + self.T1)
        if (self.ASYMMOD != 0):
            self.UAR_i = self.UAR_i * (1.0 + self.T0 + self.T1)
        self.T0   = self.EUL * max(self.Inv_L**self.EULEXP - self.Inv_Llong**self.EULEXP, 0.0)
        self.T1   = self.EUW * max(self.Inv_W**self.EUWEXP - self.Inv_Wwide**self.EUWEXP, 0.0) + self.EUWL * self.Inv_WL**self.EUWLEXP
        self.EU_i = self.EU_i * (1.0 + self.T0 + self.T1)
        self.T0   = 1.0 + self.UDL * max(self.Inv_L**self.UDLEXP - self.Inv_Llong**self.UDLEXP, 0.0)
        self.UD_i = self.UD_i * self.T0
        if (self.ASYMMOD != 0):
            self.UDR_i = self.UDR_i * self.T0
        self.T0   = self.UCL * max(self.Inv_L**self.UCLEXP - self.Inv_Llong**self.UCLEXP, 0.0)
        self.T1   = self.UCW * max(self.Inv_W**self.UCWEXP - self.Inv_Wwide**self.UCWEXP, 0.0) + self.UCWL * self.Inv_WL**self.UCWLEXP
        self.UC_i = self.UC_i * (1.0 + self.T0 + self.T1)
        if (self.ASYMMOD != 0):
            self.UCR_i = self.UCR_i * (1.0 + self.T0 + self.T1)
        self.T0     = max(self.Inv_L**self.DSUB - self.Inv_Llong**self.DSUB, 0.0)
        self.ETA0_i = self.ETA0_i * self.T0
        if (self.ASYMMOD != 0):
            self.ETA0R_i = self.ETA0R_i * self.T0
        self.ETAB_i   = self.ETAB_i * max(self.Inv_L**self.ETABEXP - self.Inv_Llong**self.ETABEXP, 0.0)
        self.T0       = 1.0 + self.PDIBLCL * max(self.Inv_L**self.PDIBLCLEXP - self.Inv_Llong**self.PDIBLCLEXP, 0.0)
        self.PDIBLC_i = self.PDIBLC_i * self.T0
        if (self.ASYMMOD != 0):
            self.PDIBLCR_i = self.PDIBLCR_i * self.T0
        self.T0       = self.DELTA_i * (1.0 + self.DELTAL * max(self.Inv_L**self.DELTALEXP - self.Inv_Llong**self.DELTALEXP, 0.0))
        self.DELTA_i  = min(self.T0, 0.5)
        self.FPROUT_i = self.FPROUT_i * (1.0 + self.FPROUTL * max(self.Inv_L**self.FPROUTLEXP - self.Inv_Llong**self.FPROUTLEXP, 0.0))
        self.T0       = (1.0 + self.PCLML * max(self.Inv_L**self.PCLMLEXP - self.Inv_Llong**self.PCLMLEXP, 0.0))
        self.PCLM_i   = self.PCLM_i * self.T0
        self.PCLM_i   = max(self.PCLM_i, 0.0)
        if (self.ASYMMOD != 0):
            self.PCLMR_i = self.PCLMR_i * self.T0
            self.PCLMR_i = max(self.PCLMR_i, 0.0)
        self.T0     = self.VSATL * max(self.Inv_L**self.VSATLEXP - self.Inv_Llong**self.VSATLEXP, 0.0)
        self.T1     = self.VSATW * max(self.Inv_W**self.VSATWEXP - self.Inv_Wwide**self.VSATWEXP, 0.0) + self.VSATWL * self.Inv_WL**self.VSATWLEXP
        self.VSAT_i = self.VSAT_i * (1.0 + self.T0 + self.T1)
        if (self.ASYMMOD != 0):
            self.VSATR_i = self.VSATR_i * (1.0 + self.T0 + self.T1)
        self.PSAT_i = max(self.PSAT_i * (1.0 + self.PSATL * max(self.Inv_L**self.PSATLEXP - self.Inv_Llong**self.PSATLEXP, 0.0)), 0.25)
        if (self.ASYMMOD != 0):
            self.PSATR_i = max(self.PSATR_i * (1.0 + self.PSATL * max(self.Inv_L**self.PSATLEXP - self.Inv_Llong**self.PSATLEXP, 0.0)), 0.25)
        self.T0     = (1.0 + self.PTWGL * max(self.Inv_L**self.PTWGLEXP - self.Inv_Llong**self.PTWGLEXP, 0.0))
        self.PTWG_i = self.PTWG_i * self.T0
        if (self.ASYMMOD != 0):
            self.PTWGR_i = self.PTWGR_i * self.T0
        self.ALPHA0_i = self.ALPHA0_i * (1.0 + self.ALPHA0L * max(self.Inv_L**self.ALPHA0LEXP - self.Inv_Llong**self.ALPHA0LEXP, 0.0))
        self.AGIDL_i  = self.AGIDL_i * (1.0 + self.AGIDLL * self.Inv_L + self.AGIDLW * self.Inv_W)
        self.AGISL_i  = self.AGISL_i * (1.0 + self.AGISLL * self.Inv_L + self.AGISLW * self.Inv_W)
        self.AIGC_i   = self.AIGC_i * (1.0 + self.AIGCL * self.Inv_L + self.AIGCW * self.Inv_W)
        self.AIGS_i   = self.AIGS_i * (1.0 + self.AIGSL * self.Inv_L + self.AIGSW * self.Inv_W)
        self.AIGD_i   = self.AIGD_i * (1.0 + self.AIGDL * self.Inv_L + self.AIGDW * self.Inv_W)
        self.PIGCD_i  = self.PIGCD * (1.0 + self.PIGCDL * self.Inv_L)
        self.T0       = self.NDEPCVL1 * max(self.Inv_Lact**self.NDEPCVLEXP1 - self.Inv_Llong**self.NDEPCVLEXP1, 0.0) + self.NDEPCVL2 * max(self.Inv_Lact**self.NDEPCVLEXP2 - self.Inv_Llong**self.NDEPCVLEXP2, 0.0)
        self.T1       = self.NDEPCVW * max(self.Inv_Wact**self.NDEPCVWEXP - self.Inv_Wwide**self.NDEPCVWEXP, 0.0) + self.NDEPCVWL * (self.Inv_Wact * self.Inv_Lact)**self.NDEPCVWLEXP
        self.NDEPCV_i = self.NDEPCV_i * (1.0 + self.T0 + self.T1)
        self.T0       = self.VFBCVL * max(self.Inv_Lact**self.VFBCVLEXP - self.Inv_Llong**self.VFBCVLEXP, 0.0)
        self.T1       = self.VFBCVW * max(self.Inv_Wact**self.VFBCVWEXP - self.Inv_Wwide**self.VFBCVWEXP, 0.0) + self.VFBCVWL * self.Inv_WL**self.VFBCVWLEXP
        self.VFBCV_i  = self.VFBCV_i * (1.0 + self.T0 + self.T1)
        self.T0       = self.VSATCVL * max(self.Inv_Lact**self.VSATCVLEXP - self.Inv_Llong**self.VSATCVLEXP, 0.0)
        self.T1       = self.VSATCVW * max(self.Inv_W**self.VSATCVWEXP - self.Inv_Wwide**self.VSATCVWEXP, 0.0) + self.VSATCVWL * self.Inv_WL**self.VSATCVWLEXP
        self.VSATCV_i = self.VSATCV_i * (1.0 + self.T0 + self.T1)
        self.PCLMCV_i = self.PCLMCV_i * (1.0 + self.PCLMCVL * max(self.Inv_Lact**self.PCLMCVLEXP - self.Inv_Llong**self.PCLMCVLEXP, 0.0))
        self.PCLMCV_i = max(self.PCLMCV_i, 0.0)
        self.T0       = self.K1L * max(self.Inv_L**self.K1LEXP - self.Inv_Llong**self.K1LEXP, 0.0)
        self.T1       = self.K1W * max(self.Inv_W**self.K1WEXP - self.Inv_Wwide**self.K1WEXP, 0.0) + self.K1WL * self.Inv_WL**self.K1WLEXP
        self.K1_i     = self.K1_i * (1.0 + self.T0 + self.T1)
        self.T0       = self.K2L * max(self.Inv_L**self.K2LEXP - self.Inv_Llong**self.K2LEXP, 0.0)
        self.T1       = self.K2W * max(self.Inv_W**self.K2WEXP - self.Inv_Wwide**self.K2WEXP, 0.0) + self.K2WL * self.Inv_WL**self.K2WLEXP
        self.K2_i     = self.K2_i * (1.0 + self.T0 + self.T1)
        self.PRWB_i   = self.PRWB_i * (1.0 + self.PRWBL * max(self.Inv_L**self.PRWBLEXP - self.Inv_Llong**self.PRWBLEXP, 0.0))

        # Global scaling parameters for temperature
        self.UTE_i   = self.UTE_i * (1.0 + self.Inv_L * self.UTEL)
        self.UA1_i   = self.UA1_i * (1.0 + self.Inv_L * self.UA1L)
        self.UD1_i   = self.UD1_i * (1.0 + self.Inv_L * self.UD1L)
        self.AT_i    = self.AT_i * (1.0 + self.Inv_L * self.ATL)
        self.PTWGT_i = self.PTWGT_i * (1.0 + self.Inv_L * self.PTWGTL)

        if (self.RDSMOD == 1):
            self.RSW_i = self.RSW_i * (1.0 + self.RSWL * max(self.Inv_L**self.RSWLEXP - self.Inv_Llong**self.RSWLEXP, 0.0))
            self.RDW_i = self.RDW_i * (1.0 + self.RDWL * max(self.Inv_L**self.RDWLEXP - self.Inv_Llong**self.RDWLEXP, 0.0))
        else:
            self.RDSW_i = self.RDSW_i * (1.0 + self.RDSWL * max(self.Inv_L**self.RDSWLEXP - self.Inv_Llong**self.RDSWLEXP, 0.0))

        # Parameter checking
        if (self.UCS_i < 1.0):
            self.UCS_i = 1.0
        elif (self.UCS_i > 2.0):
            self.UCS_i = 2.0
        if (self.ASYMMOD != 0):
            if (self.UCSR_i < 1.0):
                self.UCSR_i = 1.0
            elif (self.UCSR_i > 2.0):
                self.UCSR_i = 2.0
        if (self.CGIDL_i < 0.0):
            print("Fatal: CGIDL_i = %e is negative.", CGIDL_i)
        if (self.CGISL_i < 0.0):
            print("Fatal: CGISL_i = %e is negative.", CGISL_i)
        if (self.CKAPPAD_i <= 0.0):
            print("Fatal: CKAPPAD_i = %e is non-positive.", CKAPPAD_i)
        if (self.CKAPPAS_i <= 0.0):
            print("Fatal: CKAPPAS_i = %e is non-positive.", CKAPPAS_i)
        if (self.PDITS_i < 0.0):
            print("Fatal: PDITS_i = %e is negative.", PDITS_i)
        if (self.CIT_i < 0.0):
            print("Fatal: CIT_i = %e is negative.", CIT_i)
        if (self.NFACTOR_i < 0.0):
            print("Fatal: NFACTOR_i = %e is negative.", NFACTOR_i)
        if (self.K1_i < 0.0):
            print("Fatal: K1_i = %e is negative.", K1_i)
        if (self.NSD_i <= 0.0):
            print("Fatal: NSD_i = %e is non-positive.", NSD_i)
        if (self.NDEP_i <= 0.0):
            print("Fatal: NDEP_i = %e is non-positive.", NDEP_i)
        if (self.NDEPCV_i <= 0.0):
            print("Fatal: NDEPCV_i = %e is non-positive.", NDEPCV_i)
        if (self.IGBMOD != 0):
            if (self.NIGBINV_i <= 0.0):
                print("Fatal: NIGBINV_i = %e is non-positive.", NIGBINV_i)
            if (self.NIGBACC_i <= 0.0):
                print("Fatal: NIGBACC_i = %e is non-positive.", NIGBACC_i)
        if (self.IGCMOD != 0):
            if (self.POXEDGE_i <= 0.0):
                print("Fatal: POXEDGE_i = %e is non-positive.", POXEDGE_i)
        if (self.CDSCD_i < 0.0):
            print("Fatal: CDSCD_i = %e is negative.", CDSCD_i)
        if (self.ASYMMOD != 0):
            if (self.CDSCDR_i < 0.0):
                print("Fatal: CDSCDR_i = %e is negative.", CDSCDR_i)
        if (self.DLCIG_i < 0.0):
            print("Warning: DLCIG = %e is negative, setting it to 0.", DLCIG_i)
            self.DLCIG_i = 0.0
        if (self.DLCIGD_i < 0.0):
            print("Warning: DLCIGD = %e is negative, setting it to 0.", DLCIGD_i)
            self.DLCIGD_i = 0.0
        if (self.M0_i < 0.0):
            print("Warning: M0_i = %e is negative, setting it to 0.", M0_i)
            self.M0_i = 0.0
        if (self.U0_i <= 0.0):
            print("Warning: U0_i = %e is non-positive, setting it to the default value.", U0_i)
            self.U0_i = 0.067
        if (self.UA_i < 0.0):
            print("Warning: UA_i = %e is negative, setting it to 0.", UA_i)
            self.UA_i = 0.0
        if (self.EU_i < 0.0):
            print("Warning: EU_i = %e is negative, setting it to 0.", EU_i)
            self.EU_i = 0.0
        if (self.UD_i < 0.0):
            print("Warning: UD_i = %e is negative, setting it to 0.", UD_i)
            self.UD_i = 0.0
        if (self.UCS_i < 0.0):
            print("Warning: UCS_i = %e is negative, setting it to 0.", UCS_i)
            self.UCS_i = 0.0

        # Process drain series resistance
        self.DMCGeff = self.DMCG - self.DMCGT
        self.DMCIeff = self.DMCI
        self.DMDGeff = self.DMDG - self.DMCGT

        # Processing S/D resistances and conductances
        if "NRS" in param.keys():
            self.RSourceGeo = self.RSH * self.NRS
        elif (self.RGEOMOD > 0 and self.RSH > 0.0):
            self.RSourceGeo = self.BSIMBULKRdseffGeo(self.NF, self.GEOMOD, self.RGEOMOD, self.MINZ, self.Weff, self.RSH, self.DMCGeff, self.DMCIeff, self.DMDGeff, 1)
        else:
            self.RSourceGeo = 0.0

        if "NRD" in param.keys():
            self.RDrainGeo = self.RSH * self.NRD
        elif (self.RGEOMOD > 0 and self.RSH > 0.0):
            self.RDrainGeo = self.BSIMBULKRdseffGeo(self.NF, self.GEOMOD, self.RGEOMOD, self.MINZ, self.Weff, self.RSH, self.DMCGeff, self.DMCIeff, self.DMDGeff, 0)
        else:
            self.RDrainGeo = 0.0

        # Clamping of S/D resistances
        if (self.RDSMOD == 0):
            if (self.RSourceGeo < self.minr):
                self.RSourceGeo = 0.0
            if (self.RDrainGeo < self.minr):
                self.RDrainGeo = 0.0
        else:
            if (self.RSourceGeo <= self.minr):
                self.RSourceGeo = self.minr
            if (self.RDrainGeo <= self.minr):
                self.RDrainGeo = self.minr
        if (self.RDSMOD == 1):
            if (self.RSWMIN_i <= 0.0):
                self.RSWMIN_i = 0.0
            if (self.RDWMIN_i <= 0.0):
                self.RDWMIN_i = 0.0
            if (self.RSW_i <= 0.0):
                self.RSW_i = 0.0
            if (self.RDW_i <= 0.0):
                self.RDW_i = 0.0
        else:
            if (self.RDSWMIN_i <= 0.0):
                self.RDSWMIN_i = 0.0
            if (self.RDSW_i <= 0.0):
                self.RDSW_i = 0.0

        # Body resistance network
        if (self.RBODYMOD != 0):
            self.Lnl  = self.lln(self.Leff * 1.0e6)
            self.Lnw  = self.lln(self.Weff * 1.0e6)
            self.Lnnf = self.lln(self.NF)
            self.Bodymode = 5
            self.Rbpb = self.RBPB
            self.Rbpd = self.RBPD
            self.Rbps = self.RBPS
            self.Rbdb = self.RBDB
            self.Rbsb = self.RBSB
            if ("RBPS0" not in param.keys()) or ("RBPD0" not in param.keys()):
                self.Bodymode = 1
            elif ("RBSBX0" not in param.keys()) and ("RBSBY0" not in param.keys()) or ("RBDBX0" not in param.keys()) and ("RBDBY0" not in param.keys()):
                self.Bodymode = 3
            if (self.RBODYMOD == 2):
                if (self.Bodymode == 5):
                    self.Rbsbx = self.RBSBX0 * self.lexp(self.RBSDBXL * self.Lnl + self.RBSDBXW * self.Lnw + self.RBSDBXNF * self.Lnnf)
                    self.Rbsby = self.RBSBY0 * self.lexp(self.RBSDBYL * self.Lnl + self.RBSDBYW * self.Lnw + self.RBSDBYNF * self.Lnnf)
                    self.Rbsb  = self.Rbsbx * self.Rbsby / (self.Rbsbx + self.Rbsby)
                    self.Rbdbx = self.RBDBX0 * self.lexp(self.RBSDBXL * self.Lnl + self.RBSDBXW * self.Lnw + self.RBSDBXNF * self.Lnnf)
                    self.Rbdby = self.RBDBY0 * self.lexp(self.RBSDBYL * self.Lnl + self.RBSDBYW * self.Lnw + self.RBSDBYNF * self.Lnnf)
                    self.Rbdb  = self.Rbdbx * self.Rbdby / (self.Rbdbx + self.Rbdby)
                if (self.Bodymode == 3 or self.Bodymode == 5):
                    self.Rbps = self.RBPS0 * self.lexp(self.RBPSL * self.Lnl + self.RBPSW * self.Lnw + self.RBPSNF * self.Lnnf)
                    self.Rbpd = self.RBPD0 * self.lexp(self.RBPDL * self.Lnl + self.RBPDW * self.Lnw + self.RBPDNF * self.Lnnf)
                self.Rbpbx = self.RBPBX0 * self.lexp(self.RBPBXL * self.Lnl + self.RBPBXW * self.Lnw + self.RBPBXNF * self.Lnnf)
                self.Rbpby = self.RBPBY0 * self.lexp(self.RBPBYL * self.Lnl + self.RBPBYW * self.Lnw + self.RBPBYNF * self.Lnnf)
                self.Rbpb  = self.Rbpbx * self.Rbpby / (self.Rbpbx + self.Rbpby)
            if (self.RBODYMOD == 1 or (self.RBODYMOD == 2 and self.Bodymode == 5)):
                if (self.Rbdb < 1.0e-3):
                    Grbdb = 1.0e3  # in mho
                else:
                    self.Grbdb = self.GBMIN + 1.0 / self.Rbdb
                if (self.Rbpb < 1.0e-3):
                    self.Grbpb = 1.0e3
                else:
                    self.Grbpb = self.GBMIN + 1.0 / self.Rbpb
                if (self.Rbps < 1.0e-3):
                    self.Grbps = 1.0e3
                else:
                    self.Grbps = self.GBMIN + 1.0 / self.Rbps
                if (self.Rbsb < 1.0e-3):
                    self.Grbsb = 1.0e3
                else:
                    self.Grbsb = self.GBMIN + 1.0 / self.Rbsb
                if (self.Rbpd < 1.0e-3):
                    self.Grbpd = 1.0e3
                else:
                    self.Grbpd = self.GBMIN + 1.0 / self.Rbpd
            elif (self.RBODYMOD == 2 and self.Bodymode == 3):
                self.Grbdb = self.GBMIN
                self.Grbsb = self.GBMIN
                if (self.Rbpb < 1.0e-3):
                    self.Grbpb = 1.0e3
                else:
                    self.Grbpb = self.GBMIN + 1.0 / self.Rbpb
                if (self.Rbps < 1.0e-3):
                    self.Grbps = 1.0e3
                else:
                    self.Grbps = self.GBMIN + 1.0 / self.Rbps
                if (self.Rbpd < 1.0e-3):
                    self.Grbpd = 1.0e3
                else:
                    self.Grbpd = self.GBMIN + 1.0 / self.Rbpd
            elif (self.RBODYMOD == 2 and self.Bodymode == 1):
                self.Grbdb = self.GBMIN
                self.Grbsb = self.GBMIN
                self.Grbps = 1.0e3
                self.Grbpd = 1.0e3
                if (self.Rbpb < 1.0e-3):
                    self.Grbpb = 1.0e3
                else:
                    self.Grbpb = self.GBMIN + 1.0 / self.Rbpb

        # Gate process resistance
        self.Grgeltd = self.RSHG * (self.XGW + self.Weffcj / 3.0 / self.NGCON) / (self.NGCON * self.NF * (self.Lnew - self.XGL))
        if (self.Grgeltd > 0.0):
            self.Grgeltd = 1.0 / self.Grgeltd
        else:
            self.Grgeltd = 1.0e3
            if (self.RGATEMOD != 0):
                print("Warning: (instance %M) The gate conductance reset to 1.0e3 mho.")

        self.T0           = self.TOXE * self.TOXE
        self.T1           = self.TOXE * self.POXEDGE_i
        self.T2           = self.T1 * self.T1
        self.ToxRatio     = self.lexp(self.NTOX_i * self.lln(self.TOXREF / self.TOXE)) / self.T0
        self.ToxRatioEdge = self.lexp(self.NTOX_i * self.lln(self.TOXREF / self.T1)) / self.T2
        self.Aechvb       = 4.97232e-7 if (self.TYPE == self.ntype) else 3.42537e-7
        self.Bechvb       = 7.45669e11 if (self.TYPE == self.ntype) else 1.16645e12
        self.AechvbEdge   = self.Aechvb * self.Weff * self.ToxRatioEdge
        self.BechvbEdge   = -self.Bechvb * self.TOXE * self.POXEDGE_i
        self.Aechvb       = self.Aechvb * (self.Weff * self.Leff * self.ToxRatio)
        self.Bechvb       = -self.Bechvb * self.TOXE
        self.Weff_SH      = self.WTH0 + self.Weff

        # Parameters for self-heating effects
        if (self.SHMOD != 0) and (self.RTH0 > 0.0) and (self.Weff_SH > 0.0):
            self.gth = self.Weff_SH * self.NF / self.RTH0
            self.cth = self.CTH0 * self.Weff_SH * self.NF
        else:
            # Set gth to some value to prevent a singular G matrix
            self.gth = 1.0
            self.cth = 0.0

        # Temperature-dependent calculations
        if (self.TNOM <= -self.P_CELSIUS0):
            self.T0 = self.REFTEMP - self.P_CELSIUS0
            print("Warning: TNOM = %e C <= %e C. Setting TNOM to %e C.", TNOM, -P_CELSIUS0, T0)
            self.Tnom = self.REFTEMP
        else:
            self.Tnom = self.TNOM + self.P_CELSIUS0
        self.DevTemp = self.TEMP + self.P_CELSIUS0 + self.DTEMP

        self.Vt         = self.KboQ * self.DevTemp
        self.inv_Vt     = 1.0 / self.Vt
        self.TRatio     = self.DevTemp / self.Tnom
        self.delTemp    = self.DevTemp - self.Tnom
        self.Vtm        = self.KboQ * self.DevTemp
        self.Vtm0       = self.KboQ * self.Tnom
        self.Eg         = self.BG0SUB - self.TBGASUB * self.DevTemp * self.DevTemp / (self.DevTemp + self.TBGBSUB)
        self.Eg0        = self.BG0SUB - self.TBGASUB * self.Tnom * self.Tnom / (self.Tnom + self.TBGBSUB)
        self.T1         = (self.DevTemp / self.Tnom) * sqrt(self.DevTemp / self.Tnom)
        self.ni         = self.NI0SUB * self.T1 * self.lexp(self.Eg / (2.0 * self.Vtm0) - self.Eg / (2.0 * self.Vtm))
        if ((self.SHMOD != 0) and (self.RTH0 > 0.0) and (self.Weff_SH > 0.0)):
            self.T0   = self.lln(self.NDEP_i / self.ni)
            self.phib = sqrt(self.T0 * self.T0 + 1.0e-6)
        else:
            self.phib = self.lln(self.NDEP_i / self.ni)
        if ((self.SHMOD != 0) and (self.RTH0 > 0.0) and (self.Weff_SH > 0.0)):
            self.T0  = self.lln(self.NDEPEDGE_i * self.NSD_i / (self.ni * self.ni))
            self.Vbi_edge = sqrt(self.T0 * self.T0 + 1.0e-6)
        else:
            self.Vbi_edge = self.lln(self.NDEPEDGE_i * self.NSD_i / (self.ni * self.ni))
        if (self.NGATE_i > 0.0):
            self.Vfbsdr = -self.devsign * self.Vt * self.lln(self.NGATE_i / self.NSD_i) + self.VFBSDOFF
        else:
            self.Vfbsdr = 0.0

        # Short channel effects
        self.Phist     = max(0.4 + self.Vt * self.phib + self.PHIN_i, 0.4)
        self.sqrtPhist = sqrt(self.Phist)
        self.T1DEP     = sqrt(2.0 * self.epssi / (self.q * self.NDEP_i))
        self.litl      = sqrt((self.epssi / self.epsox) * self.TOXE * self.XJ_i)
        self.NFACTOR_t = self.NFACTOR_i * self.hypsmooth((1.0 + self.TNFACTOR * (self.TRatio - 1.0)), 1e-3)
        self.ETA0_t    = self.ETA0_i * (1.0 + self.TETA0 * (self.TRatio - 1.0))
        if (self.ASYMMOD != 0):
            self.ETA0R_t = self.ETA0R_i * (1.0 + self.TETA0 * (self.TRatio - 1.0))

        # Mobility degradation
        self.eta_mu = (self.Oneby3 * self.ETAMOB) if (self.TYPE != self.ntype) else (0.5 * self.ETAMOB)
        self.U0_t   = self.U0_i * self.TRatio**self.UTE_i
        self.UA_t   = self.UA_i * self.hypsmooth(1.0 + self.UA1_i * self.delTemp - 1.0e-6, 1.0e-3)
        self.UC_t   = self.UC_i * self.hypsmooth(1.0 + self.UC1_i * self.delTemp - 1.0e-6, 1.0e-3)
        self.UD_t   = self.UD_i * self.TRatio**self.UD1_i
        self.UCS_t  = self.UCS_i * self.TRatio**self.UCSTE_i
        self.EU_t   = self.EU_i * self.hypsmooth((1.0 + self.EU1_i * (self.TRatio - 1.0)), 1e-3)
        if (self.ASYMMOD != 0):
            self.U0R_t  = self.U0R_i * self.TRatio**self.UTE_i
            self.UAR_t  = self.UAR_i * self.hypsmooth(1.0 + self.UA1_i * self.delTemp - 1.0e-6, 1.0e-3)
            self.UCR_t  = self.UCR_i * self.hypsmooth(1.0 + self.UC1_i * self.delTemp - 1.0e-6, 1.0e-3)
            self.UDR_t  = self.UDR_i * self.TRatio**self.UD1_i
            self.UCSR_t = self.UCSR_i * self.TRatio**self.UCSTE_i
        else:
            self.U0R_t  = 0.0
            self.UAR_t  = 0.0
            self.UCR_t  = 0.0
            self.UDR_t  = 0.0
            self.UCSR_t = 0.0
        self.rdstemp = self.TRatio**self.PRT_i
        self.VSAT_t  = self.VSAT_i * self.TRatio**-self.AT_i
        if (self.VSAT_t < 100.0):
            print("Warning: VSAT(%f) = %e is less than 100, setting it to 100.", DevTemp, VSAT_t)
            self.VSAT_t = 100.0
        if (self.HVMOD == 1):
            self.rdstemphv = self.TRatio**self.PRTHV
            self.VDRIFT_t  = self.VDRIFT * self.TRatio**-self.ATHV
        if (self.ASYMMOD != 0):
            self.VSATR_t = self.VSATR_i * self.TRatio**-self.AT_i
            if(self.VSATR_t < 100.0):
                print("Warning: VSATR(%f) = %e is less than 100, setting it to 100.", DevTemp, VSATR_t)
                self.VSATR_t = 100.0

        self.VSATCV_t = self.VSATCV_i * self.TRatio**-self.AT_i
        if (self.VSATCV_t < 100.0):
            print("Warning: VSATCV(%f) = %e is less than 100, setting it to 100.", DevTemp, VSATCV_t)
            self.VSATCV_t = 100.0
        self.DELTA_t = 1.0 / ( self.hypsmooth((1.0 / self.DELTA_i) * (1.0 + self.TDELTA * self.delTemp) - 2.0 , 1.0e-3) + 2.0)
        self.PTWG_t  = self.PTWG_i * self.hypsmooth(1.0 - self.PTWGT_i * self.delTemp - 1.0e-6, 1.0e-3)
        if (self.ASYMMOD != 0):
            self.PTWGR_t = self.PTWGR_i * self.hypsmooth(1.0 - self.PTWGT_i * self.delTemp - 1.0e-6, 1.0e-3)
        self.A1_t    = self.A1_i * self.hypsmooth(1.0 + self.A11_i * self.delTemp - 1.0e-6, 1.0e-3)
        self.A2_t    = self.A2_i * self.hypsmooth(1.0 + self.A21_i * self.delTemp - 1.0e-6, 1.0e-3)
        self.BETA0_t = self.BETA0_i * self.TRatio**self.IIT_i
        self.BGIDL_t = self.BGIDL_i * self.hypsmooth(1.0 + self.TGIDL_i * self.delTemp - 1.0e-6, 1.0e-3)
        self.BGISL_t = self.BGISL_i * self.hypsmooth(1.0 + self.TGIDL_i * self.delTemp - 1.0e-6, 1.0e-3)
        self.igtemp  = self.lexp(self.IGT_i * self.lln(self.TRatio))
        self.K0_t    = self.K0_i * self.hypsmooth(1.0 + self.K01_i * self.delTemp - 1.0e-6, 1.0e-3)
        self.M0_t    = self.M0_i * self.hypsmooth(1.0 + self.M01_i * self.delTemp - 1.0e-6, 1.0e-3)
        self.C0_t    = self.C0_i * self.hypsmooth(1.0 + self.C01_i * self.delTemp - 1.0e-6, 1.0e-3)
        self.C0SI_t  = self.C0SI_i * self.hypsmooth(1.0 + self.C0SI1_i * self.delTemp - 1.0e-6, 1.0e-3)
        self.C0SISAT_t = self.C0SISAT_i * self.hypsmooth(1.0 + self.C0SISAT1_i * self.delTemp - 1.0e-6, 1.0e-3)

        # Diode model temperature effects
        self.CJS_t     = self.CJS * self.hypsmooth(1.0 + self.TCJ * self.delTemp - 1.0e-6, 1.0e-3)
        self.CJD_t     = self.CJD * self.hypsmooth(1.0 + self.TCJ * self.delTemp - 1.0e-6, 1.0e-3)
        self.CJSWS_t   = self.CJSWS * self.hypsmooth(1.0 + self.TCJSW * self.delTemp - 1.0e-6, 1.0e-3)
        self.CJSWD_t   = self.CJSWD * self.hypsmooth(1.0 + self.TCJSW * self.delTemp - 1.0e-6, 1.0e-3)
        self.CJSWGS_t  = self.CJSWGS * self.hypsmooth(1.0 + self.TCJSWG * self.delTemp - 1.0e-6, 1.0e-3)
        self.CJSWGD_t  = self.CJSWGD * self.hypsmooth(1.0 + self.TCJSWG * self.delTemp - 1.0e-6, 1.0e-3)
        self.PBS_t     = self.hypsmooth(self.PBS - self.TPB * self.delTemp - 0.01, 1.0e-3) + 0.01
        self.PBD_t     = self.hypsmooth(self.PBD - self.TPB * self.delTemp - 0.01, 1.0e-3) + 0.01
        self.PBSWS_t   = self.hypsmooth(self.PBSWS - self.TPBSW * self.delTemp - 0.01, 1.0e-3) + 0.01
        self.PBSWD_t   = self.hypsmooth(self.PBSWD - self.TPBSW * self.delTemp - 0.01, 1.0e-3) + 0.01
        self.PBSWGS_t  = self.hypsmooth(self.PBSWGS - self.TPBSWG * self.delTemp - 0.01, 1.0e-3) + 0.01
        self.PBSWGD_t  = self.hypsmooth(self.PBSWGD - self.TPBSWG * self.delTemp - 0.01, 1.0e-3) + 0.01
        self.T0        = self.Eg0 / self.Vtm0 - self.Eg / self.Vtm
        self.T1        = self.lln(self.TRatio)
        self.T3        = self.lexp((self.T0 + self.XTIS * self.T1) / self.NJS)
        self.JSS_t     = self.JSS * self.T3
        self.JSWS_t    = self.JSWS * self.T3
        self.JSWGS_t   = self.JSWGS * self.T3
        self.T3        = self.lexp((self.T0 + self.XTID * self.T1) / self.NJD)
        self.JSD_t     = self.JSD * self.T3
        self.JSWD_t    = self.JSWD * self.T3
        self.JSWGD_t   = self.JSWGD * self.T3
        self.JTSS_t    = self.JTSS * self.lexp(self.Eg0 * self.XTSS * (self.TRatio - 1.0) / self.Vtm)
        self.JTSSWS_t  = self.JTSSWS * self.lexp(self.Eg0 * self.XTSSWS * (self.TRatio - 1.0) / self.Vtm)
        self.JTSSWGS_t = self.JTSSWGS * (sqrt(self.JTWEFF / self.Weffcj) + 1.0) * self.lexp(self.Eg0 * self.XTSSWGS * (self.TRatio - 1) / self.Vtm)
        self.JTSD_t    = self.JTSD * self.lexp(self.Eg0 * self.XTSD * (self.TRatio - 1.0) / self.Vtm)
        self.JTSSWD_t  = self.JTSSWD * self.lexp(self.Eg0 * self.XTSSWD * (self.TRatio - 1.0) / self.Vtm)
        self.JTSSWGD_t = self.JTSSWGD * (sqrt(self.JTWEFF / self.Weffcj) + 1.0) * self.lexp(self.Eg0 * self.XTSSWGD * (self.TRatio - 1) / self.Vtm)

        # All NJT*'s smoothed to 0.01 to prevent divide by zero/negative values
        self.NJTS_t     = self.hypsmooth(self.NJTS * (1.0 + self.TNJTS * (self.TRatio - 1.0)) - 0.01, 1.0e-3) + 0.01
        self.NJTSSW_t   = self.hypsmooth(self.NJTSSW * (1.0 + self.TNJTSSW * (self.TRatio - 1.0)) - 0.01, 1.0e-3) + 0.01
        self.NJTSSWG_t  = self.hypsmooth(self.NJTSSWG * (1.0 + self.TNJTSSWG * (self.TRatio - 1.0)) - 0.01, 1.0e-3) + 0.01
        self.NJTSD_t    = self.hypsmooth(self.NJTSD * (1.0 + self.TNJTSD * (self.TRatio - 1.0)) - 0.01, 1.0e-3) + 0.01
        self.NJTSSWD_t  = self.hypsmooth(self.NJTSSWD * (1.0 + self.TNJTSSWD * (self.TRatio - 1.0)) - 0.01, 1.0e-3) + 0.01
        self.NJTSSWGD_t = self.hypsmooth(self.NJTSSWGD * (1.0 + self.TNJTSSWGD * (self.TRatio - 1.0)) - 0.01, 1.0e-3) + 0.01

        # Effective S/D junction area and perimeters
        self.temp_PSeff, self.temp_PDeff, self.temp_ASeff, self.temp_ADeff = self.BSIMBULKPAeffGeo(self.NF, self.GEOMOD, self.MINZ, self.Weffcj, self.DMCGeff, self.DMCIeff, self.DMDGeff)
        if "AS" in param.keys():
            self.ASeff = self.AS * self.WMLT * self.LMLT
        else:
            self.ASeff = self.temp_ASeff
        if (self.ASeff < 0.0):
            print("Warning: (instance %M) ASeff = %e is negative. Set to 0.0.", ASeff)
            self.ASeff = 0.0
        if "AD" in param.keys():
            self.ADeff = self.AD * self.WMLT * self.LMLT
        else:
            self.ADeff = self.temp_ADeff
        if (self.ADeff < 0.0):
            print("Warning: (instance %M) ADeff = %e is negative. Set to 0.0.", ADeff)
            self.ADeff = 0.0
        if "PS" in param.keys():
            if (self.PERMOD == 0):
                # PS does not include gate-edge perimeters
                self.PSeff = self.PS * self.WMLT
            else:
                # PS includes gate-edge perimeters
                self.PSeff = max(self.PS * self.WMLT - self.Weffcj * self.NF, 0.0)
        else:
            self.PSeff = self.temp_PSeff
            if (self.PSeff < 0.0):
                print("Warning: (instance %M) PSeff = %e is negative. Set to 0.0.", PSeff)
                self.PSeff = 0.0
        if "PD" in param.keys():
            if (self.PERMOD == 0):
                # PD does not include gate-edge perimeters
                self.PDeff = self.PD * self.WMLT
            else:
                # PD includes gate-edge perimeters
                self.PDeff = max(self.PD * self.WMLT - self.Weffcj * self.NF, 0.0)
        else:
            self.PDeff = self.temp_PDeff
            if (self.PDeff < 0.0):
                print("Warning: (instance %M) PDeff = %e is negative. Set to 0.0.", PDeff)
                self.PDeff = 0.0

        self.Isbs = self.ASeff * self.JSS_t + self.PSeff * self.JSWS_t + self.Weffcj * self.NF * self.JSWGS_t
        if (self.Isbs > 0.0):
            self.Nvtms    = self.Vtm * self.NJS
            self.XExpBVS  = self.lexp(-self.BVS / self.Nvtms) * self.XJBVS
            self.T2       = max(self.IJTHSFWD / self.Isbs, 10.0)
            self.Tb       = 1.0 + self.T2 - self.XExpBVS
            self.VjsmFwd  = self.Nvtms * self.lln(0.5 * (self.Tb + sqrt(self.Tb * self.Tb + 4.0 * self.XExpBVS)))
            self.T0       = self.lexp(self.VjsmFwd / self.Nvtms)
            self.IVjsmFwd = self.Isbs * (self.T0 - self.XExpBVS / self.T0 + self.XExpBVS - 1.0)
            self.SslpFwd  = self.Isbs * (self.T0 + self.XExpBVS / self.T0) / self.Nvtms
            self.T2       = self.hypsmooth(self.IJTHSREV / self.Isbs - 10.0, 1.0e-3) + 10.0
            self.VjsmRev  = -self.BVS - self.Nvtms * self.lln((self.T2 - 1.0) / self.XJBVS)
            self.T1       = self.XJBVS * self.lexp(-(self.BVS + self.VjsmRev) / self.Nvtms)
            self.IVjsmRev = self.Isbs * (1.0 + self.T1)
            self.SslpRev  = -self.Isbs * self.T1 / self.Nvtms
        else:
            self.Nvtms    = 0.0
            self.XExpBVS  = 0.0
            self.VjsmFwd  = 0.0
            self.IVjsmFwd = 0.0
            self.SslpFwd  = 0.0
            self.VjsmRev  = 0.0
            self.IVjsmRev = 0.0
            self.SslpRev  = 0.0

        # Drain-side junction currents
        self.Isbd = self.ADeff * self.JSD_t + self.PDeff * self.JSWD_t + self.Weffcj * self.NF * self.JSWGD_t
        if (self.Isbd > 0.0):
            self.Nvtmd    = self.Vtm * self.NJD
            self.XExpBVD  = self.lexp(-self.BVD / self.Nvtmd) * self.XJBVD
            self.T2       = max(self.IJTHDFWD / self.Isbd, 10.0)
            self.Tb       = 1.0 + self.T2 - self.XExpBVD
            self.VjdmFwd  = self.Nvtmd * self.lln(0.5 * (self.Tb + sqrt(self.Tb * self.Tb + 4.0 * self.XExpBVD)))
            self.T0       = self.lexp(self.VjdmFwd / self.Nvtmd)
            self.IVjdmFwd = self.Isbd * (self.T0 - self.XExpBVD / self.T0 + self.XExpBVD - 1.0)
            self.DslpFwd  = self.Isbd * (self.T0 + self.XExpBVD / self.T0) / self.Nvtmd
            self.T2       = self.hypsmooth(self.IJTHDREV / self.Isbd - 10.0, 1.0e-3) + 10.0
            self.VjdmRev  = -self.BVD - self.Nvtmd * self.lln((self.T2 - 1.0) / self.XJBVD)
            self.T1       = self.XJBVD * self.lexp(-(self.BVD + self.VjdmRev) / self.Nvtmd)
            self.IVjdmRev = self.Isbd * (1.0 + self.T1)
            self.DslpRev  = -self.Isbd * self.T1 / self.Nvtmd
        else:
            self.Nvtmd    = 0.0
            self.XExpBVD  = 0.0
            self.VjdmFwd  = 0.0
            self.IVjdmFwd = 0.0
            self.DslpFwd  = 0.0
            self.VjdmRev  = 0.0
            self.IVjdmRev = 0.0
            self.DslpRev  = 0.0

        # STI stress equations
        if ((self.SA > 0.0) and (self.SB > 0.0) and ((self.NF == 1.0) or ((self.NF > 1.0) and (self.SD > 0.0)))):
            self.T0              = self.Lnew**self.LLODKU0
            self.W_tmp_stress    = self.Wnew + self.WLOD
            self.T1              = self.W_tmp_stress**self.WLODKU0
            self.tmp1_stress     = self.LKU0 / self.T0 + self.WKU0 / self.T1 + self.PKU0 / (self.T0 * self.T1)
            self.kstress_u0      = 1.0 + self.tmp1_stress
            self.T0              = self.Lnew**self.LLODVTH
            self.T1              = self.W_tmp_stress**self.WLODVTH
            self.tmp1_stress_vth = self.LKVTH0 / self.T0 + self.WKVTH0 / self.T1 + self.PKVTH0 / (self.T0 * self.T1)
            self.kstress_vth0    = 1.0 + self.tmp1_stress_vth
            self.T0              = self.TRatio - 1.0
            self.ku0_temp        = self.kstress_u0 * (1.0 + self.TKU0 * self.T0) + 1.0e-9
            for i in range(self.NF):
                self.T0     = 1.0 / self.NF / (self.SA + 0.5 * self.L_mult + i * (self.SD + self.L_mult))
                self.T1     = 1.0 / self.NF / (self.SB + 0.5 * self.L_mult + i * (self.SD + self.L_mult))
                self.Inv_sa = self.Inv_sa + self.T0
                self.Inv_sb = self.Inv_sb + self.T1
            self.Inv_saref   = 1.0 / (self.SAREF + 0.5 * self.L_mult)
            self.Inv_sbref   = 1.0 / (self.SBREF + 0.5 * self.L_mult)
            self.Inv_odref   = self.Inv_saref + self.Inv_sbref
            self.rho_ref     = (self.KU0 / self.ku0_temp) * self.Inv_odref
            self.Inv_od      = self.Inv_sa + self.Inv_sb
            self.rho         = (self.KU0 / self.ku0_temp) * self.Inv_od
            self.mu0_mult    = (1.0 + self.rho) / (1.0 + self.rho_ref)
            self.vsat_mult   = (1.0 + self.rho * self.KVSAT) / (1.0 + self.rho_ref * self.KVSAT)
            self.vth0_stress = (self.KVTH0 / self.kstress_vth0) * (self.Inv_od - self.Inv_odref)
            self.k2_stress   = (self.STK2 / self.kstress_vth0**self.LODK2) * (self.Inv_od - self.Inv_odref)
            self.eta_stress  = (self.STETA0 / self.kstress_vth0**self.LODETA0) * (self.Inv_od - self.Inv_odref)
            self.U0_t        = self.U0_t * self.mu0_mult
            self.VSAT_t      = self.VSAT_t * self.vsat_mult
            self.K2_i        = self.K2_i + self.k2_stress
            self.ETA0_t      = self.ETA0_t + self.eta_stress
            if (self.EDGEFET == 1):
                self.vth0_stress_EDGE = (self.KVTH0EDGE_i / self.kstress_vth0) * (self.Inv_od - self.Inv_odref)
                self.k2_stress_EDGE   = (self.STK2EDGE_i / self.kstress_vth0**self.LODK2) * (self.Inv_od - self.Inv_odref)
                self.eta_stress_EDGE  = (self.STETA0EDGE_i / self.kstress_vth0**self.LODETA0) * (self.Inv_od - self.Inv_odref)
            self.K2EDGE_i   = self.K2EDGE_i + self.k2_stress_EDGE
            self.ETA0EDGE_i = self.ETA0EDGE_i + self.eta_stress_EDGE
        else:
            self.vth0_stress = 0.0
            self.vth0_stress_EDGE = 0.0

        # Well proximity effect
        if (self.WPEMOD == 1):
            self.Wdrn      = self.W / self.NF
            self.local_sca = self.SCA
            self.local_scb = self.SCB
            self.local_scc = self.SCC
            if ("SCA" not in param.keys()) and ("SCB" not in param.keys()) and ("SCC" not in param.keys()):
                if ("SC" in param.keys()) and (self.SC > 0.0):
                    self.T1        = self.SC + self.Wdrn
                    self.T2        = 1.0 / self.SCREF
                    self.local_sca = self.SCREF * self.SCREF / (self.SC * self.T1)
                    self.local_scb = ((0.1 * self.SC + 0.01 * self.SCREF) * self.lexp(-10.0 * self.SC * self.T2)  - (0.1 * self.T1 + 0.01 * self.SCREF) * self.lexp(-10.0 * self.T1 * self.T2)) / self.Wdrn
                    self.local_scc = ((0.05 * self.SC + 0.0025 * self.SCREF) * self.lexp(-20.0 * self.SC * self.T2)  - (0.05 * self.T1 + 0.0025 * self.SCREF) * self.lexp(-20.0 * self.T1 * self.T2)) / self.Wdrn
                else:
                    print("Warning: (Instance %M) No WPE as none of SCA, SCB, SCC, SC is given and/or SC not positive.")
        else:
            self.local_sca = 0.0
            self.local_scb = 0.0
            self.local_scc = 0.0

        self.vth0_well = self.KVTH0WE_i * (self.local_sca + self.WEB * self.local_scb + self.WEC * self.local_scc)
        self.k2_well   = self.K2WE_i * (self.local_sca + self.WEB * self.local_scb + self.WEC * self.local_scc)
        self.mu_well   = 1.0 + self.KU0WE_i * (self.local_sca + self.WEB * self.local_scb + self.WEC * self.local_scc)
        self.U0_t      = self.U0_t * self.mu_well
        self.K2_i      = self.K2_i + self.k2_well

        # Load terminal voltages
        self.Vg            = self.devsign * (self.VG - self.VB)
        self.Vd            = self.devsign * (self.VD - self.VB)
        self.Vs            = self.devsign * (self.VS - self.VB)
        self.Vds           = self.Vd - self.Vs
        self.Vds_noswap    = self.Vds
        self.Vsb_noswap    = self.Vs
        self.Vdb_noswap    = self.Vd
        self.Vbs_jct       = self.devsign * (self.VB - self.VS)
        self.Vbd_jct       = self.devsign * (self.VB - self.VD)
        self.Vgd_noswap    = self.Vg - self.Vd
        self.Vgs_noswap    = self.Vg - self.Vs
        self.Vgd_ov_noswap = self.devsign * (self.VG - self.VD)
        self.Vgs_ov_noswap = self.devsign * (self.VG - self.VS)

        # Terminal voltage conditioning
        # Source-drain interchange
        self.sigvds = 1.0
        if (self.Vds < 0.0):
            self.sigvds = -1.0
            self.Vd = self.devsign * (self.VS - self.VB)
            self.Vs = self.devsign * (self.VD - self.VB)
        self.Vds  = self.Vd - self.Vs
        self.T0   = self.AVDSX * self.Vds
        if (self.T0 > self.EXPL_THRESHOLD):
           self.T1 = self.T0
        else:
           self.T1 = log(1.0 + exp(self.T0))
        self.Vdsx = ((2.0 / self.AVDSX) * self.T1) - self.Vds - ((2.0 / self.AVDSX) * log(2.0))
        self.Vbsx = -(self.Vs + 0.5 * (self.Vds - self.Vdsx))

        # Asymmetry model
        self.T0 = tanh(0.6 * self.Vds_noswap / self.Vtm)
        self.wf = 0.5 + 0.5 * self.T0
        self.wr = 1.0 - self.wf
        if (self.ASYMMOD != 0):
            self.CDSCD_a  = self.CDSCDR_i * self.wr + self.CDSCD_i * self.wf
            self.ETA0_a   = self.ETA0R_t * self.wr + self.ETA0_t * self.wf
            self.PDIBLC_a = self.PDIBLCR_i * self.wr + self.PDIBLC_i * self.wf
            self.PCLM_a   = self.PCLMR_i * self.wr + self.PCLM_i * self.wf
            self.PSAT_a   = self.PSATR_i * self.wr + self.PSAT_i * self.wf
            self.VSAT_a   = self.VSATR_t * self.wr + self.VSAT_t * self.wf
            self.PTWG_a   = self.PTWGR_t * self.wr + self.PTWG_t * self.wf
            self.U0_a     = self.U0R_t * self.wr + self.U0_t * self.wf
            self.UA_a     = self.UAR_t * self.wr + self.UA_t * self.wf
            self.UC_a     = self.UCR_t * self.wr + self.UC_t * self.wf
            self.UD_a     = self.UDR_t * self.wr + self.UD_t * self.wf
            self.UCS_a    = self.UCSR_t * self.wr + self.UCS_t * self.wf
        else:
            self.CDSCD_a  = self.CDSCD_i
            self.ETA0_a   = self.ETA0_t
            self.PDIBLC_a = self.PDIBLC_i
            self.PCLM_a   = self.PCLM_i
            self.PSAT_a   = self.PSAT_i
            self.VSAT_a   = self.VSAT_t
            self.PTWG_a   = self.PTWG_t
            self.U0_a     = self.U0_t
            self.UA_a     = self.UA_t
            self.UC_a     = self.UC_t
            self.UD_a     = self.UD_t
            self.UCS_a    = self.UCS_t

        # SCE, DIBL, SS degradation effects, Ref: BSIM4
        self.PhistVbs = self.Smooth(self.Phist - self.Vbsx, 0.05, 0.1)
        self.sqrtPhistVbs = sqrt(self.PhistVbs)
        self.Xdep         = self.T1DEP * self.sqrtPhistVbs
        self.Cdep         = self.epssi / self.Xdep
        self.cdsc         = self.CIT_i + self.NFACTOR_t + self.CDSCD_a * self.Vdsx - self.CDSCB_i * self.Vbsx
        self.T1           = 1.0 + self.cdsc/self.Cox
        self.n = self.Smooth(self.T1, 1.0, 0.05)
        self.nVt     = self.n * self.Vt
        self.inv_nVt = 1.0 / self.nVt

        # Vth shift for DIBL
        self.dVth_dibl = -(self.ETA0_a + self.ETAB_i * self.Vbsx) * self.Vdsx
        self.dVth_dibl = self.Smooth2(self.dVth_dibl, 0.0, 5.0e-5)

        # Vth shift with temperature
        self.dvth_temp = (self.KT1_i + self.KT1L / self.Leff + self.KT2_i * self.Vbsx) * (self.TRatio**self.KT1EXP - 1.0)

        # Vth correction for pocket implants
        if (self.DVTP0_i > 0.0):
            self.T0 = -self.DVTP1_i * self.Vdsx
            if (self.T0 < -self.EXPL_THRESHOLD):
                self.T2 = self.MIN_EXPL
            else:
                self.T2 = self.lexp(self.T0)
            self.T3        = self.Leff + self.DVTP0_i * (1.0 + self.T2)
            self.dVth_ldop = -self.nVt * self.lln(self.Leff / self.T3)
        else:
            self.dVth_ldop = 0.0
        self.T4        = self.DVTP5_i + self.DVTP2_i / self.Leff**self.DVTP3_i
        self.dVth_ldop = self.dVth_ldop - self.T4 * tanh(self.DVTP4_i * self.Vdsx)

        # Normalization of terminal and flatband voltage by nVt
        self.VFB_i = self.VFB_i + self.DELVTO
        self.vg    = self.Vg * self.inv_nVt
        self.vs    = self.Vs * self.inv_nVt
        self.vfb   = self.VFB_i * self.inv_nVt

        # Compute dVth_VNUD with "first-order" and "second-order" body-bias effect
        self.dVth_VNUD = self.K1_i * (self.sqrtPhistVbs - self.sqrtPhist) - self.K2_i * self.Vbsx
        self.Vth_shift = self.dVth_dibl + self.dVth_ldop + self.dVth_VNUD - self.dvth_temp + self.vth0_stress + self.vth0_well
        self.vgfb      = self.vg - self.vfb - self.Vth_shift * self.inv_nVt

        # Threshold voltage for operating point information
        self.gam     = sqrt(2.0 * self.q * self.epssi * self.NDEP_i * self.inv_Vt) / self.Cox
        self.q_vth   = 0.5
        self.T0      = self.hypsmooth((2.0 * self.phib + self.Vs * self.inv_Vt), 1.0e-3)
        self.nq      = 1.0 + self.gam / (2.0 * sqrt(self.T0))
        self.psip_th = self.hypsmooth((self.Vs * self.inv_Vt + 2.0 * self.phib + self.lln(self.q_vth) + 2.0 * self.q_vth + self.lln(2.0 * self.nq / self.gam * (2.0 * self.q_vth * self.nq / self.gam + 2.0 * sqrt(self.T0)))), 1.0e-3)
        self.VTH     = self.devsign * (self.VFB_i + (self.psip_th - self.Vs * self.inv_Vt) * self.Vt + self.Vt * self.gam * sqrt(self.psip_th) + self.Vth_shift)

        # Normalized body factor
        self.gam     = sqrt(2.0 * self.q * self.epssi * self.NDEP_i * self.inv_nVt) / self.Cox
        self.inv_gam = 1.0 / self.gam

        # psip: pinch-off voltage
        self.phib_n = self.phib / self.n
        self.psip = self.PO_psip(self.vgfb, self.gam, 0.0)

        # Normalized inversion charge at source end of channel
        self.qs = self.BSIM_q(self.psip, self.phib_n, self.vs, self.gam)

        # Average charge-surface potential slope, Ref: Charge-based MOS Transistor Modeling by C. Enz & E. Vittoz
        self.psipclamp = self.Smooth(self.psip, 1.0, 2.0)
        self.sqrtpsip = sqrt(self.psipclamp)

        # Source side surface potential
        self.psiavg = self.psip - 2.0 * self.qs
        self.T0 = self.Smooth(self.psiavg, 1.0, 2.0)
        self.nq = 1.0 + self.gam / (self.sqrtpsip + sqrt(self.T0))

        # Drain saturation voltage
        self.EeffFactor = 1.0e-8 / (self.epsratio * self.TOXE)
        self.T0 = self.nVt * (self.vgfb - self.psip - 2.0 * self.qs * (self.nq - 1.0))
        self.qbs = self.Smooth(self.T0, 0.0, 0.1)

        # Source side qi and qb for Vdsat- normalized to Cox
        self.qis = 2.0 * self.nq * self.nVt * self.qs
        self.Eeffs = self.EeffFactor * (self.qbs + self.eta_mu * self.qis)

        # Ref: BSIM4 mobility model
        self.T2 = (0.5 * (1.0 + (self.qis / self.qbs)))**self.UCS_a
        self.T3 = (self.UA_a + self.UC_a * self.Vbsx) * self.Eeffs**self.EU_t + self.UD_a / self.T2
        self.T4 = 1.0 + self.T3
        self.Dmobs = self.Smooth(self.T4, 1.0, 0.0015)
        self.WeffWRFactor = 1.0 / ((self.Weff * 1.0e6)**self.WR_i * self.NF)

        if (self.RDSMOD == 1):
            self.Rdss = 0.0
        else:
            self.T0   = 1.0 + self.PRWG_i * self.qis
            self.T1   = self.PRWB_i * (self.sqrtPhistVbs - self.sqrtPhist)
            self.T2   = 1.0 / self.T0 + self.T1
            self.T3   = self.T2 + sqrt(self.T2 * self.T2 + 0.01)
            self.Rdss = (self.RDSWMIN_i + self.RDSW_i * self.T3) * self.WeffWRFactor * self.NF * self.rdstemp
            if (self.RDSMOD == 2):
                self.Rdss = (self.RSourceGeo + (self.RDSWMIN_i + self.RDSW_i * self.T3) * self.WeffWRFactor * self.NF + self.RDrainGeo) * self.rdstemp

        self.T0  = self.Dmobs**(1.0 / self.PSAT_a)
        self.T11 = self.PSATB_i * self.Vbsx
        self.T12 = sqrt(0.1 + self.T11 * self.T11)
        self.T1  = 0.5*(1 - self.T11 + sqrt((1 - self.T11) * (1 - self.T11) + self.T12))
        self.T2  = 10.0 * self.PSATX * self.qs * self.T1 / (10.0 * self.PSATX + self.qs * self.T1)
        if (self.PTWG_a < 0.0):
            self.LambdaC = 2.0 * ((self.U0_a / self.T0) * self.nVt / (self.VSAT_a * self.Leff)) * (1.0 / (1.0 - self.PTWG_a * self.T2))
        else:
            self.LambdaC = 2.0 * ((self.U0_a / self.T0) * self.nVt / (self.VSAT_a * self.Leff)) * (1.0 + self.PTWG_a * self.T2)

        # qdsat for external Rds
        if (self.Rdss == 0):
            # Accurate qdsat derived from consistent I-V
            self.T0 = 0.5 * self.LambdaC * (self.qs * self.qs + self.qs) / (1.0 + 0.5 * self.LambdaC * (1.0 + self.qs))
            self.T1 = 2.0 * self.LambdaC * (self.qs - self.T0)
            self.T2 = sqrt(1.0 + self.T1 * self.T1)
            self.ln_T1_T2 = asinh(self.T1)
            if (self.T1 != 0.0):
                self.T3 = self.T2 + (1.0 / self.T1) * self.ln_T1_T2
            else:
                self.T3 = self.T2 + (1.0 / self.T2)
            self.T4 = self.T0 * self.T3 - self.LambdaC * ((self.qs * self.qs + self.qs) - (self.T0 * self.T0 + self.T0))
            if (self.T1 != 0.0):
                self.T5 = -2.0 * self.LambdaC * (self.T1 * self.T2 - self.ln_T1_T2) / (self.T1 * self.T1)
            else:
                self.T5 = -2.0 * self.LambdaC * (self.T1/self.T2) * (self.T1/self.T2) *(self.T1/self.T2)

            self.T6 = self.T0 * self.T5 + self.T3 + self.LambdaC * (2.0 * self.T0 + 1.0)
            self.T0 = self.T0 - (self.T4 / self.T6)
            self.T1 = 2.0 * self.LambdaC * (self.qs - self.T0)
            self.T2 = sqrt(1.0 + self.T1 * self.T1)
            self.ln_T1_T2 = asinh(self.T1)
            if (self.T1 != 0.0):
                self.T3 = self.T2 + (1.0 / self.T1) * self.ln_T1_T2
            else:
                self.T3 = self.T2 + (1.0 / self.T2)
            self.T4 = self.T0 * self.T3 - self.LambdaC * ((self.qs * self.qs + self.qs) - (self.T0 * self.T0 + self.T0))
            if (self.T1 != 0.0):
                self.T5 = -2.0 * self.LambdaC * (self.T1 * self.T2 - self.ln_T1_T2) / (self.T1 * self.T1)
            else:
                self.T5 = (self.T1 / self.T2) * (self.T1 / self.T2) * (self.T1 / self.T2)

            self.T6    = self.T0 * self.T5 + self.T3 + self.LambdaC * (2.0 * self.T0 + 1.0)
            self.qdsat = self.T0 - (self.T4/self.T6)
        # qdsat for internal Rds, Ref: BSIM4
        else:
            # Accurate qdsat derived from consistent I-V
            self.T11 = self.Weff * 2.0 * self.nq * self.Cox * self.nVt * self.VSAT_a
            self.T12 = self.T11 * self.LambdaC * self.Rdss / (2.0 * self.nVt)
            self.T0  = 0.5 * self.LambdaC * (self.qs * self.qs + self.qs) / (1.0 + 0.5 * self.LambdaC * (1.0 + self.qs))
            self.T1  = 2.0 * self.LambdaC * (self.qs - self.T0)
            self.T2  = sqrt(1.0 + self.T1 * self.T1)
            self.ln_T1_T2 = asinh(self.T1)
            if (self.T1 != 0.0):
                self.T3 = self.T2 + (1.0 / self.T1) * self.ln_T1_T2
            else:
                self.T3 = self.T2 + (1.0 / self.T2)
            self.T4 = self.T0 * self.T3 + self.T12 * self.T0 * (self.qs + self.T0 + 1.0) - self.LambdaC * ((self.qs * self.qs + self.qs) - (self.T0 * self.T0 + self.T0))
            if (self.T1 != 0.0):
                self.T5 = -2.0 * self.LambdaC * (self.T1 * self.T2 - self.ln_T1_T2) / (self.T1 * self.T1)
            else:
                self.T5 = -2.0 * self.LambdaC * (self.T1 / self.T2) * (self.T1 / self.T2) * (self.T1 / self.T2)
            self.T6 = self.T0 * self.T5 + self.T3 + self.T12 * (self.qs + 2.0 * self.T0 + 1.0) + self.LambdaC * (2.0 * self.T0 + 1.0)
            self.T0 = self.T0 - self.T4 / self.T6
            self.T1 = 2.0 * self.LambdaC * (self.qs - self.T0)
            self.T2 = sqrt(1.0 + self.T1 * self.T1)
            self.ln_T1_T2 = asinh(self.T1)
            if (self.T1 != 0):
                self.T3 = self.T2 + (1.0 / self.T1) * self.ln_T1_T2
            else:
                self.T3 = self.T2 + (1.0 / self.T2)
            self.T4 = self.T0 * self.T3 + self.T12 * self.T0 * (self.qs + self.T0 + 1.0) - self.LambdaC * ((self.qs * self.qs + self.qs) - (self.T0 * self.T0 + self.T0))
            if (self.T1 != 0.0):
                self.T5 = -2.0 * self.LambdaC * (self.T1 * self.T2 - self.ln_T1_T2) / (self.T1 * self.T1)
            else:
                self.T5 = -2.0 * self.LambdaC * (self.T1 / self.T2) * (self.T1 / self.T2) * (self.T1 / self.T2)
            self.T6    = self.T0 * self.T5 + self.T3 + self.T12 * (self.qs + 2.0 * self.T0 + 1.0) + self.LambdaC * (2.0 * self.T0 + 1.0)
            self.qdsat = self.T0 - self.T4 / self.T6
        self.vdsat = self.psip - 2.0 * self.phib_n - (2.0 * self.qdsat + self.lln((self.qdsat * 2.0 * self.nq * self.inv_gam) * ((self.qdsat * 2.0 * self.nq * self.inv_gam) + (self.gam / (self.nq - 1.0)))))
        self.Vdsat = self.vdsat * self.nVt

        # Normalized charge qdeff at drain end of channel
        # Vdssat clamped to avoid negative values during transient simulation
        self.Vdssat = self.Smooth(self.Vdsat - self.Vs, 0.0, 1.0e-3)
        self.T7      = (self.Vds / self.Vdssat)**(1.0 / self.DELTA_t)
        self.T8      = (1.0 + self.T7)**-self.DELTA_t
        self.Vdseff  = self.Vds * self.T8
        self.vdeff   = (self.Vdseff + self.Vs) * self.inv_nVt
        self.qdeff = self.BSIM_q(self.psip, self.phib_n, self.vdeff, self.gam)

        # Reevaluation of nq to include qdeff
        self.psiavg = self.psip - self.qs - self.qdeff -1.0
        self.T0 = self.Smooth(self.psiavg, 1.0, 2.0)
        self.T2 = sqrt(self.T0)
        self.nq = 1.0 + self.gam / (self.sqrtpsip + self.T2)

        # Inversion and bulk charge
        self.DQSD2 = (self.qs - self.qdeff) * (self.qs - self.qdeff)
        self.T0    = 1.0 / (1.0 + self.qs + self.qdeff)
        self.T1    = self.DQSD2 * self.T0
        self.Qb    = self.vgfb - self.psip - (self.nq - 1.0) * (self.qs + self.qdeff + self.Oneby3 * self.T1)
        self.T2    = self.Oneby3 * self.nq
        self.T3    = self.T1 * self.T0
        self.Qs    = self.T2 * (2.0 * self.qs + self.qdeff + 0.5 * (1.0 + 0.8 * self.qs + 1.2 * self.qdeff) * self.T3)
        self.Qd    = self.T2 * (self.qs + 2.0 * self.qdeff + 0.5 * (1.0 + 1.2 * self.qs + 0.8 * self.qdeff) * self.T3)

        # Mobility degradation, Ref: BSIM4
        # Average charges (qba and qia) - normalized to Cox
        self.qba = self.Smooth(self.nVt * self.Qb, 0.0, 0.1)
        self.qia   = self.nVt * (self.Qs + self.Qd)

        self.Eeffm = self.EeffFactor * (self.qba + self.eta_mu * self.qia)
        self.T2    = (0.5 * (1.0 + (self.qia / self.qba)))**self.UCS_a
        self.T3    = (self.UA_a + self.UC_a * self.Vbsx) * self.Eeffm**self.EU_t + self.UD_a / self.T2
        self.T4    = 1.0 + self.T3
        self.Dmob = self.Smooth(self.T4, 1.0, 0.0015)

        # Output conductance
        self.Esat  = 2.0 * self.VSAT_a / (self.U0_a / self.Dmob)
        self.EsatL = self.Esat * self.Leff
        if (self.PVAG_i > 0.0):
            self.PVAGfactor = 1.0 + self.PVAG_i * self.qia / self.EsatL
        else:
            self.PVAGfactor = 1.0 / (1.0 - self.PVAG_i * self.qia / self.EsatL)

        # Output conductance due to DIBL, Ref: BSIM4
        self.DIBLfactor = self.PDIBLC_a
        self.diffVds    = self.Vds - self.Vdseff
        self.Vgst2Vtm   = self.qia + 2.0 * self.nVt
        if (self.DIBLfactor > 0.0):
            self.T3     = self.Vgst2Vtm / (self.Vdssat + self.Vgst2Vtm)
            self.T4     = self.hypsmooth((1.0 + self.PDIBLCB_i * self.Vbsx), 1.0e-3)
            self.T5     = 1.0 / self.T4
            self.VaDIBL = self.Vgst2Vtm / self.DIBLfactor * self.T3 * self.PVAGfactor * self.T5
            self.Moc    = 1.0 + self.diffVds / self.VaDIBL
        else:
            self.Moc = 1.0

        # Degradation factor due to pocket implants, Ref: BSIM4
        if (self.FPROUT_i <= 0.0):
            self.Fp = 1.0
        else:
            self.T9 = self.FPROUT_i * sqrt(self.Leff) / self.Vgst2Vtm
            self.Fp = 1.0 / (1.0 + self.T9)

        # Channel length modulation, Ref: BSIM4
        self.Vasat = self.Vdssat + self.EsatL
        if (self.PCLM_a != 0.0):
            if (self.PCLMG < 0.0):
                self.T1 = self.PCLM_a / (1.0 - self.PCLMG * self.qia / self.EsatL) / self.Fp
            else:
                self.T1 = self.PCLM_a * (1.0 + self.PCLMG * self.qia / self.EsatL) / self.Fp

            self.MdL = 1.0 + self.T1 * self.lln(1.0 + self.diffVds / self.T1 / self.Vasat)
        else:
            self.MdL = 1.0
        self.Moc = self.Moc * self.MdL

        # Calculate Va_DITS, Ref: BSIM4
        self.T1 = self.lexp(self.PDITSD_i * self.Vds)
        if (self.PDITS_i > 0.0):
            self.T2      = 1.0 + self.PDITSL * self.Leff
            self.VaDITS  = (1.0 + self.T2 * self.T1) / self.PDITS_i
            self.VaDITS  = self.VaDITS * self.Fp
        else:
            self.VaDITS  = self.MAX_EXPL
        self.T4  = self.diffVds / self.VaDITS
        self.T0  = 1.0 + self.T4
        self.Moc = self.Moc * self.T0

        # Calculate Va_SCBE, Ref: BSIM4
        if (self.PSCBE2_i > 0.0):
            if (self.diffVds > self.PSCBE1_i * self.litl / self.EXPL_THRESHOLD):
                self.T0     = self.PSCBE1_i * self.litl / self.diffVds
                self.VaSCBE = self.Leff * self.lexp(self.T0) / self.PSCBE2_i
            else:
                self.VaSCBE = self.MAX_EXPL * self.Leff/self.PSCBE2_i
        else:
            self.VaSCBE = self.MAX_EXPL
        self.Mscbe = 1.0 + (self.diffVds / self.VaSCBE)
        self.Moc   = self.Moc * self.Mscbe

        # Velocity saturation
        self.T0  = self.Dmob**(1.0 / self.PSAT_a)
        self.T11 = self.PSATB_i * self.Vbsx
        self.T12 = sqrt(0.1+self.T11*self.T11)
        self.T1  = 0.5*(1-self.T11+sqrt((1-self.T11)*(1-self.T11)+self.T12))
        self.T2  = 10.0 * self.PSATX * self.qia * self.T1 / (10.0 * self.PSATX + self.qia * self.T1)
        if (self.PTWG_a < 0.0):
            self.LambdaC = 2.0 * ((self.U0_a / self.T0) * self.nVt / (self.VSAT_a * self.Leff)) * (1.0 / (1.0 - self.PTWG_a * self.T2))
        else:
            self.LambdaC = 2.0 * ((self.U0_a / self.T0) * self.nVt / (self.VSAT_a * self.Leff)) * (1.0 + self.PTWG_a * self.T2)
        self.T1 = 2.0 * self.LambdaC * (self.qs - self.qdeff)
        self.T2 = sqrt(1.0 + self.T1 * self.T1)
        if (self.T1 != 0.0):
            self.Dvsat = 0.5 * (self.T2 + (1.0 / self.T1) * asinh(self.T1))
        else:
            self.Dvsat = 0.5 * (self.T2 + (1.0 / self.T2))
        self.Dptwg = self.Dvsat

        # S/D series resistances, Ref: BSIM4
        if (self.RDSMOD == 1):
            self.Rdsi = 0.0
            self.Dr   = 1.0
            # Rs (Source side resistance for all fingers)
            self.T2      = self.Vgs_noswap - self.Vfbsdr
            self.T3      = sqrt(self.T2 * self.T2 + 0.01)
            self.Vgs_eff = 0.5 * (self.T2 + self.T3)
            self.T5      = 1.0 + self.PRWG_i * self.Vgs_eff
            self.T6      = (1.0 / self.T5) + self.PRWB_i * self.Vsb_noswap
            self.T4      = 0.5 * (self.T6 + sqrt(self.T6 * self.T6 + 0.01))
            self.Rsource = self.rdstemp * (self.RSourceGeo + (self.RSWMIN_i + self.RSW_i * self.T4) * self.WeffWRFactor)
            # Rd (Drain side resistance for all fingers)
            self.T2      = self.Vgd_noswap - self.Vfbsdr
            self.T3      = sqrt(self.T2 * self.T2 + 0.01)
            self.Vgd_eff = 0.5 * (self.T2 + self.T3)
            self.T5      = 1.0 + self.PRWG_i * self.Vgd_eff
            self.T6      = (1.0 / self.T5) + self.PRWB_i * self.Vdb_noswap
            self.T4      = 0.5 * (self.T6 + sqrt(self.T6 * self.T6 + 0.01))
            self.Rdrain  = self.rdstemp * (self.RDrainGeo + (self.RDWMIN_i + self.RDW_i * self.T4) * self.WeffWRFactor)
        else:
            # Ref: (1) BSIM4 (2) "Operation and Modeling of the MOS Transistor" by Yannis Tsividis
            self.T0      = 1.0 + self.PRWG_i * self.qia
            self.T1      = self.PRWB_i * (self.sqrtPhistVbs - self.sqrtPhist)
            self.T2      = 1.0 / self.T0 + self.T1
            self.T3      = 0.5 * (self.T2 + sqrt(self.T2 * self.T2 + 0.01))
            self.Rdsi    = self.rdstemp * (self.RDSWMIN_i + self.RDSW_i * self.T3) * self.WeffWRFactor * self.NF
            self.Rdrain  = self.RDrainGeo
            self.Rsource = self.RSourceGeo
            self.Dr      = 1.0 + self.U0_a /(self.Dvsat * self.Dmob) * self.Cox * self.Weff / self.Leff * self.qia * self.Rdsi
            if (self.RDSMOD == 2):
                self.Rdsi    = self.rdstemp * (self.RSourceGeo + (self.RDSWMIN_i + self.RDSW_i * self.T3) * self.WeffWRFactor * self.NF + self.RDrainGeo)
                self.Rdrain  = 0.0
                self.Rsource = 0.0
                self.Dr      = 1.0 + self.U0_a /(self.Dvsat * self.Dmob) * self.Cox * self.Weff / self.Leff * self.qia * self.Rdsi

        # Non-saturation effect
        self.T0   = self.A1_t + self.A2_t / (self.qia + 2.0 * self.n * self.Vtm)
        self.DQSD = self.qs - self.qdeff
        self.T1   = self.T0 * self.DQSD * self.DQSD
        self.T2   = self.T1 + 1.0 - 0.001
        self.T3   = -1.0 + 0.5 * (self.T2 + sqrt(self.T2 * self.T2 + 0.004))
        self.Nsat = 0.5 * (1.0 + sqrt(1.0 + self.T3))

        # MNUD model to enhance Id-Vd fitting flexibility
        self.T0   = (self.qs + self.qdeff)
        self.T1   = (self.qs - self.qdeff)
        self.T2   = self.T1 / (self.T0 + self.M0_t)
        self.T3   = self.K0_t * self.T2 * self.T2
        self.Mnud = 1.0 + self.T3

        # MNUD1 to enhance the fitting flexiblity for the gm/Id - similar approach used in BSIM-CMG
        self.T9    = self.C0_t / (max(0, self.C0SI_t + self.C0SISAT_t * self.T1 * self.T1) * self.T0 + 2.0 * self.n * self.Vtm)
        self.Mnud1 = self.lexp(-self.T9)
        self.Dtot  = self.Dmob * self.Dvsat * self.Dr

        # Effective mobility including mobility degradation
        self.ueff = self.U0_a / self.Dtot

        # I-V
        self.ids  = 2.0 * self.NF * self.nq * self.ueff * self.Weff / self.Leff * self.Cox * self.nVt * self.nVt * ((self.qs - self.qdeff) * (1.0 + self.qs + self.qdeff)) * self.Moc / self.Nsat * self.Mnud * self.Mnud1
        self.ids  = self.ids * self.IDS0MULT

        # High-voltage model s: Ref. - Harshit Agarwal et.al., IEEE TED vol. 66, issue 10, pp. 4258, 2019
        if (self.RDSMOD == 1 and self.HVMOD == 1):
            self.T4  = 1 + self.PDRWB * self.Vbsx
            self.T0  = self.ids
            self.T11 = self.NF * self.Weff * self.q  * self.VDRIFT_t
            if (self.RDLCW != 0):
                self.idrift_sat_d = self.T11 * self.NDRIFTD
                self.delta_hv = self.ids**(4 - self.MDRIFT) / (self.ids**(4 - self.MDRIFT) + self.HVFACTOR * self.idrift_sat_d**(4 - self.MDRIFT))
                self.T5  = self.T0/self.idrift_sat_d
                if (self.T5 >= 0.99):
                    self.T5  = 0.5 * ((self.T5 + 0.99) - sqrt( (self.T5 - 0.99) * (self.T5 - 0.99) + 1.0e-6) + 0.001)
                self.T0D = self.delta_hv * self.T5**self.MDRIFT
                self.T1D = 1.0 - self.T0D
                self.T2D = self.T1D**(1.0 / self.MDRIFT)
                self.rdrift_d = self.rdstemphv * self.RDLCW * self.WeffWRFactor/self.T2D * self.T4
                self.IDRIFTSATD = self.idrift_sat_d
                if (self.rdrift_d < 0):
                    self.rdrift_d = 0
            if (self.RSLCW != 0):
                self.idrift_sat_s = self.T11 * self.NDRIFTS
                self.delta_hv = self.ids**(4 - self.MDRIFT) / (self.ids**(4 - self.MDRIFT) + self.HVFACTOR * self.idrift_sat_s**(4 - self.MDRIFT))
                self.T5  = self.T0/self.idrift_sat_s
                if (self.T5 >= 0.99):
                    self.T5  = 0.5 * ((self.T5 + 0.99) - sqrt( (self.T5 - 0.99) * (self.T5 - 0.99) + 1.0e-6) + 0.001 )
                self.T0S = self.delta_hv * self.T5**self.MDRIFT
                self.T1S = 1.0 - self.T0S
                self.T2S = self.T1S**(1.0 / self.MDRIFT)
                self.rdrift_s = self.rdstemphv * self.RSLCW * self.WeffWRFactor/self.T2S * self.T4
                if (self.rdrift_s < 0.0):
                    self.rdrift_s = 0.0
            self.Rdrain  = self.Rdrain + self.rdrift_d
            self.Rsource = self.Rsource + self.rdrift_s

        # CV calculations for HVMOD
        if (self.RDSMOD == 1 and self.HVCAP == 1 and self.HVMOD == 1):
            self.vgfbdrift = -self.devsign * (self.VG - self.VD) - self.VFBOV
            self.vgfbdrift = self.vgfbdrift/self.Vt
            self.gamhv     = sqrt(2.0 * self.q * self.epssi * self.NDR * self.inv_Vt) / self.Cox
            self.phibHV    = self.lln(self.NDR / self.ni)
            self.psip_k = self.PO_psip(self.vgfbdrift, self.gamhv, 0.0)
            self.q_k = self.BSIM_q(self.psip_k, self.phibHV, self.devsign * (self.VD - self.VB) / self.Vt, self.gamhv)

            # calculate nq for the drift region
            self.psipclamp_hv = self.Smooth(self.psip_k, 1.0, 2.0)
            self.sqrtpsip_k = sqrt(self.psipclamp_hv)
            self.psiavg_hv = self.psip_k - 2.0 * self.q_k
            self.T0 = self.Smooth(self.psiavg_hv, 1.0, 2.0)
            self.nq_hv = 1.0 + self.gamhv / (self.sqrtpsip_k + sqrt(self.T0))
            self.psi_k = self.psip_k - 2 * self.q_k

            # contribution due to accumulation of the overlap region
            self.QBOV = self.NF * self.Wact * self.LOVER * self.EPS0 * self.EPSROX / self.BSIMBULKTOXP * self.Vt * (self.vgfbdrift - self.psi_k - 2 * self.nq_hv * self.q_k)

            # contribution due to inversion of the overlap region
            if (self.SLHV > 0):
                self.T1 = 1 + self.q_k / self.SLHV1
                self.T2 = self.SLHV * 1.9e-9 / self.T1
                self.T0 = 3.9 * self.EPS0 / (self.BSIMBULKTOXP * 3.9 / self.EPSROX + self.T2 / self.epsratio)
            else:
                self.T0 = self.EPS0 * self.EPSROX / self.BSIMBULKTOXP

            self.QIOV = self.NF * self.Wact * self.LOVERACC * 2 * self.nq_hv * self.Vt * self.T0 * self.q_k

            # For symmetric device, adding contribution of the source side drift region
            if (self.HVCAPS == 1):
                self.vgfbdrift = -self.devsign * (self.VG - self.VS) - self.VFBOV
                self.vgfbdrift = self.vgfbdrift/self.Vt
                self.psip_k = self.PO_psip(self.vgfbdrift, self.gamhv, 0.0)
                self.q_k = self.BSIM_q(self.psip_k, self.phibHV, self.devsign * (self.VS - self.VB) / self.Vt, self.gamhv)
                self.psipclamp_hv = self.Smooth(self.psip_k, 1.0, 2.0)
                self.sqrtpsip_k = sqrt(self.psipclamp_hv)
                self.psiavg_hv = self.psip_k - 2.0 * self.q_k
                self.T0 = self.Smooth(self.psiavg_hv, 1.0, 2.0)
                self.nq_hv = 1.0 + self.gamhv / (self.sqrtpsip_k + sqrt(self.T0))
                self.psi_k = self.psip_k - 2 * self.q_k
                self.QBOVS = self.NF * self.Wact * self.LOVER * self.EPS0 * self.EPSROX / self.BSIMBULKTOXP * self.Vt * (self.vgfbdrift - self.psi_k - 2 * self.nq_hv * self.q_k)
                if (self.SLHV > 0):
                    self.T1 = 1 + self.q_k / self.SLHV1
                    self.T2 = self.SLHV * 1.9e-9 / self.T1
                    self.T0 = 3.9 * self.EPS0 / (self.BSIMBULKTOXP * 3.9 / self.EPSROX + self.T2 / self.epsratio)
                else:
                    self.T0 = self.EPS0 * self.EPSROX / self.BSIMBULKTOXP
                self.QIOVS = self.NF * self.Wact * self.LOVERACC * 2 * self.nq_hv * self.Vt * self.T0 * self.q_k
        if (self.RGATEMOD > 1):
            self.idsovvds = self.ueff * self.Weff / self.Leff * self.Cox * self.qia
            self.T9       = self.XRCRG2 * self.Vt
            self.T0       = self.T9 * self.ueff * self.Weff / self.Leff * self.Cox
            self.Gcrg     = self.XRCRG1 * self.NF * (self.T0 + self.idsovvds)
            if (self.RGATEMOD == 2):
                self.T11  = self.Grgeltd + self.Gcrg
                self.Gcrg = self.Grgeltd * self.Gcrg / self.T11

        # Impact ionization currents, Ref: BSIM4
        if ((self.ALPHA0_i <= 0.0) or (self.BETA0_t <= 0.0)):
            self.Iii = 0.0
        elif (self.diffVds > self.BETA0_t / self.EXPL_THRESHOLD):
            self.T1  = -self.BETA0_t / self.diffVds
            self.Iii = self.ALPHA0_i * self.diffVds * self.ids * self.lexp(self.T1) / self.Mscbe
        else:
            self.Iii = self.ALPHA0_i * self.diffVds * self.ids * self.MIN_EXPL / self.Mscbe

        # Secondary impact ionization in the drift region
        if (self.HVMOD == 1 and self.IIMOD == 1):
            self.Ntot = self.DRII1 * self.ids/(self.NF * self.Weff * self.q  * self.VDRIFT_t )
            self.Nextra = self.Ntot/self.NDRIFTD - 1
            self.Nextra = self.Smooth(self.Nextra, 0, self.DELTAII)
            self.Nextra = self.NDRIFTD * self.Nextra
            self.T2 = self.Smooth(self.devsign * (self.VD - self.VB) - self.Vdseff - self.DRII2, 0, 0.05)
            self.T3 = 2.0 * self.q /(self.EPSRSUB * self.EPS0) * self.Nextra
            self.T3 = self.T3 * self.T2
            if (self.T3 > self.BETADR / self.EXPL_THRESHOLD):
                self.T1  = -self.BETADR/self.T3
                self.IsubDR = self.ALPHADR * self.T2 * self.ids * self.lexp(self.T1)
            else:
                self.IsubDR = self.ALPHADR * self.T2 * self.ids * self.MIN_EXPL
            self.Iii = self.Iii + self.IsubDR

        # Gate currents, Ref: BSIM4
        if ((self.IGCMOD != 0) or (self.IGBMOD != 0)):
            self.Voxm    = self.nVt * (self.vgfb - self.psip + self.qs + self.qdeff)
            self.T1      = sqrt(self.Voxm * self.Voxm + 1.0e-4)
            self.Voxmacc = 0.5 * (-self.Voxm + self.T1)
            self.Voxminv = 0.5 * (self.Voxm + self.T1)
            # Igbinv
            if (self.IGBMOD != 0):
                self.T1     = self.Voxm / self.NIGBACC_i / self.Vt
                self.Vaux_Igbacc = self.NIGBACC_i * self.Vt * self.lln(1.0 + self.lexp(-self.T1))
                self.T2     = self.AIGBACC_i - self.BIGBACC_i * self.Voxmacc
                self.T3     = 1.0 + self.CIGBACC_i * self.Voxmacc
                self.T4     = -7.45669e11 * self.TOXE * self.T2 * self.T3
                self.T5     = self.lexp(self.T4)
                self.T6     = 4.97232e-7
                self.igbacc = self.NF * self.Weff * self.Leff * self.T6 * self.ToxRatio * self.Vg * self.Vaux_Igbacc * self.T5
                self.igbacc = self.igbacc * self.igtemp
                self.T1     = (self.Voxm - self.EIGBINV_i) / self.NIGBINV_i / self.Vt
                self.Vaux_Igbinv = self.NIGBINV_i * self.Vt * self.lln(1.0 + self.lexp(self.T1))
                self.T2     = self.AIGBINV_i - self.BIGBINV_i * self.Voxminv
                self.T3     = 1.0 + self.CIGBINV_i * self.Voxminv
                self.T4     = -9.82222e11 * self.TOXE * self.T2 * self.T3
                self.T5     = self.lexp(self.T4)
                self.T6     = 3.75956e-7
                self.igbinv = self.NF * self.Weff * self.Leff * self.T6 * self.ToxRatio * self.Vg * self.Vaux_Igbinv * self.T5
                self.igbinv = self.igbinv * self.igtemp
                self.igb    = self.igbacc + self.igbinv
            if (self.IGCMOD != 0):
                # Igcinv
                self.T1   = self.AIGC_i - self.BIGC_i * self.Voxminv
                self.T2   = 1.0 + self.CIGC_i * self.Voxminv
                self.T3   = self.Bechvb * self.T1 * self.T2
                self.T4   = self.nq * self.nVt * (self.qs + self.qdeff) * self.lexp(self.T3)
                self.igc0 = self.NF * self.Aechvb * self.T4 * (self.Vg + 0.5 * self.Vdsx - 0.5 * (self.Vs + self.Vd)) * self.igtemp
                # Gate-current partitioning
                self.Vdseffx = sqrt(self.Vdseff * self.Vdseff + 0.01) - 0.1
                self.T1      = self.PIGCD_i * self.Vdseffx
                self.T1_exp  = self.lexp(-self.T1)
                self.T3      = self.T1 + self.T1_exp -1.0 + 1.0e-4
                self.T4      = 1.0 - (self.T1 + 1.0) * self.T1_exp + 1.0e-4
                self.T5      = self.T1 * self.T1 + 2.0e-4
                if (self.sigvds > 0):
                    self.igcd = self.igc0 * self.T4 / self.T5
                    self.igcs = self.igc0 * self.T3 / self.T5
                else:
                    self.igcs = self.igc0 * self.T4 / self.T5
                    self.igcd = self.igc0 * self.T3 / self.T5
                # Igs
                self.T2      = self.Vgs_noswap - self.Vfbsdr
                self.Vgs_eff = sqrt(self.T2 * self.T2 + 1.0e-4)
                if (self.IGCLAMP == 1):
                    self.T1 = self.hypsmooth((self.AIGS_i - self.BIGS_i * self.Vgs_eff), 1.0e-6)
                    if (self.CIGS_i < 0.01):
                        self.CIGS_i = 0.01
                else:
                    self.T1 = self.AIGS_i - self.BIGS_i * self.Vgs_eff

                self.T2       = 1.0 + self.CIGS_i * self.Vgs_eff
                self.T3       = self.BechvbEdge * self.T1 * self.T2
                self.T4       = self.lexp(self.T3)
                self.igs_mult = self.igtemp * self.NF * self.AechvbEdge * self.DLCIG_i
                self.igs      = self.igs_mult * self.Vgs_noswap * self.Vgs_eff * self.T4
                # Igd
                self.T2      = self.Vgd_noswap - self.Vfbsdr
                self.Vgd_eff = sqrt(self.T2 * self.T2 + 1.0e-4)
                if (self.IGCLAMP == 1):
                    self.T1 = self.hypsmooth((self.AIGD_i - self.BIGD_i * self.Vgd_eff), 1.0e-6)
                    if (self.CIGD_i < 0.01):
                        self.CIGD_i = 0.01
                else:
                    self.T1 = self.AIGD_i - self.BIGD_i * self.Vgd_eff
                self.T2       = 1.0 + self.CIGD_i * self.Vgd_eff
                self.T3       = self.BechvbEdge * self.T1 * self.T2
                self.T4       = self.lexp(self.T3)
                self.igd_mult = self.igtemp * self.NF * self.AechvbEdge * self.DLCIGD_i
                self.igd      = self.igd_mult * self.Vgd_noswap * self.Vgd_eff * self.T4

        # GIDL and GISL currents, Ref: BSIM4
        if (self.GIDLMOD != 0):
            self.T0 = self.epsratio * self.TOXE
            # GIDL
            if ((self.AGIDL_i <= 0.0) or (self.BGIDL_t <= 0.0) or (self.CGIDL_i < 0.0)):
                self.T6 = 0.0
            else:
                self.T1 = (-self.Vgd_noswap - self.EGIDL_i + self.Vfbsdr) / self.T0
                self.T1 = self.hypsmooth(self.T1, 1.0e-2)
                self.T2 = self.BGIDL_t / (self.T1 + 1.0e-3)
                if (self.CGIDL_i != 0.0):
                    self.T3 = self.Vdb_noswap * self.Vdb_noswap * self.Vdb_noswap
                    self.T4 = self.CGIDL_i + abs(self.T3) + 1.0e-4
                    self.T5 = self.hypsmooth(self.T3 / self.T4, 1.0e-6) - 1.0e-6
                else:
                    self.T5 = 1.0
                self.T6 = self.AGIDL_i * self.Weff * self.T1 * self.lexp(-self.T2) * self.T5

            self.igidl = self.T6
            # GISL
            if ((self.AGISL_i <= 0.0) or (self.BGISL_t <= 0.0) or (self.CGISL_i < 0.0)):
                self.T6 = 0.0
            else:
                self.T1 = (-self.Vgs_noswap - self.EGISL_i + self.Vfbsdr) / self.T0
                self.T1 = self.hypsmooth(self.T1, 1.0e-2)
                self.T2 = self.BGISL_t / (self.T1 + 1.0e-3)
                if (self.CGISL_i != 0.0):
                    self.T3 = self.Vsb_noswap * self.Vsb_noswap * self.Vsb_noswap
                    self.T4 = self.CGISL_i + abs(self.T3) + 1.0e-4
                    self.T5 = self.hypsmooth(self.T3 / self.T4, 1.0e-6) - 1.0e-6
                else:
                    self.T5 = 1.0
                self.T6 = self.AGISL_i * self.Weff * self.T1 * self.lexp(-self.T2) * self.T5
            self.igisl = self.T6

        # Junction currents and capacitances
        # Source-side junction currents
        if (self.Isbs > 0.0):
            if (self.Vbs_jct < self.VjsmRev):
                self.T0  = self.Vbs_jct / self.Nvtms
                self.T1  = self.lexp(self.T0) - 1.0
                self.T2  = self.IVjsmRev + self.SslpRev * (self.Vbs_jct - self.VjsmRev)
                self.Ibs = self.T1 * self.T2
            elif (self.Vbs_jct <= self.VjsmFwd):
                self.T0  = self.Vbs_jct / self.Nvtms
                self.T1  = (self.BVS + self.Vbs_jct) / self.Nvtms
                self.T2  = self.lexp(-self.T1)
                self.Ibs = self.Isbs * (self.lexp(self.T0) + self.XExpBVS - 1.0 - self.XJBVS * self.T2)
            else:
                self.Ibs = self.IVjsmFwd + self.SslpFwd * (self.Vbs_jct - self.VjsmFwd)
        else:
            self.Ibs = 0.0

        # Source-side junction tunneling currents
        if (self.JTSS_t > 0.0):
            if ((self.VTSS - self.Vbs_jct) < (self.VTSS * 1.0e-3)):
                self.T0  = -self.Vbs_jct / self.Vtm0 / self.NJTS_t
                self.T1  = self.lexp(self.T0 * 1.0e3) - 1.0
                self.Ibs = self.Ibs - self.ASeff * self.JTSS_t * self.T1
            else:
                self.T0  = -self.Vbs_jct / self.Vtm0 / self.NJTS_t
                self.T1  = self.lexp(self.T0 * self.VTSS / (self.VTSS - self.Vbs_jct)) - 1.0
                self.Ibs = self.Ibs - self.ASeff * self.JTSS_t * self.T1
        if (self.JTSSWS_t > 0.0):
            if ((self.VTSSWS - self.Vbs_jct) < (self.VTSSWS * 1.0e-3)):
                self.T0  = -self.Vbs_jct / self.Vtm0 / self.NJTSSW_t
                self.T1  = self.lexp(self.T0 * 1.0e3) - 1.0
                self.Ibs = self.Ibs - self.PSeff * self.JTSSWS_t * self.T1
            else:
                self.T0  = -self.Vbs_jct / self.Vtm0 / self.NJTSSW_t
                self.T1  = self.lexp(self.T0 * self.VTSSWS / (self.VTSSWS - self.Vbs_jct)) - 1.0
                self.Ibs = self.Ibs - self.PSeff * self.JTSSWS_t * self.T1
        if (self.JTSSWGS_t > 0.0):
            if ((self.VTSSWGS - self.Vbs_jct) < (self.VTSSWGS * 1.0e-3)):
                self.T0  = -self.Vbs_jct / self.Vtm0 / self.NJTSSWG_t
                self.T1  = self.lexp(self.T0 * 1.0e3) - 1.0
                self.Ibs = self.Ibs - self.Weffcj * self.NF * self.JTSSWGS_t * self.T1
            else:
                self.T0  = -self.Vbs_jct / self.Vtm0 / self.NJTSSWG_t
                self.T1  = self.lexp(self.T0 * self.VTSSWGS / (self.VTSSWGS - self.Vbs_jct)) - 1.0
                self.Ibs = self.Ibs - self.Weffcj * self.NF * self.JTSSWGS_t * self.T1

        # Drain-side junction currents
        if (self.Isbd > 0.0):
            if (self.Vbd_jct < self.VjdmRev):
                self.T0  = self.Vbd_jct / self.Nvtmd
                self.T1  = self.lexp(self.T0) - 1.0
                self.T2  = self.IVjdmRev + self.DslpRev * (self.Vbd_jct - self.VjdmRev)
                self.Ibd = self.T1 * self.T2
            elif (self.Vbd_jct <= self.VjdmFwd):
                self.T0  = self.Vbd_jct / self.Nvtmd
                self.T1  = (self.BVD + self.Vbd_jct) / self.Nvtmd
                self.T2  = self.lexp(-self.T1)
                self.Ibd = self.Isbd * (self.lexp(self.T0) + self.XExpBVD - 1.0 - self.XJBVD * self.T2)
            else:
                self.Ibd = self.IVjdmFwd + self.DslpFwd * (self.Vbd_jct - self.VjdmFwd)
        else:
            self.Ibd = 0.0

        # Drain-side junction tunneling currents
        if (self.JTSD_t > 0.0):
            if ((self.VTSD - self.Vbd_jct) < (self.VTSD * 1.0e-3)):
                self.T0  = -self.Vbd_jct / self.Vtm0 / self.NJTSD_t
                self.T1  = self.lexp(self.T0 * 1.0e3) - 1.0
                self.Ibd = self.Ibd - self.ADeff * self.JTSD_t * self.T1
            else:
                self.T0  = -self.Vbd_jct / self.Vtm0 / self.NJTSD_t
                self.T1  = self.lexp(self.T0 * self.VTSD/ (self.VTSD - self.Vbd_jct)) - 1.0
                self.Ibd = self.Ibd - self.ADeff * self.JTSD_t * self.T1
        if (self.JTSSWD_t > 0.0):
            if ((self.VTSSWD - self.Vbd_jct) < (self.VTSSWD * 1.0e-3)):
                self.T0  = -self.Vbd_jct / self.Vtm0 / self.NJTSSWD_t
                self.T1  = self.lexp(self.T0 * 1.0e3) - 1.0
                self.Ibd = self.Ibd - self.PDeff * self.JTSSWD_t * self.T1
            else:
                self.T0  = -self.Vbd_jct / self.Vtm0 / self.NJTSSWD_t
                self.T1  = self.lexp(self.T0 * self.VTSSWD / (self.VTSSWD - self.Vbd_jct)) - 1.0
                self.Ibd = self.Ibd - self.PDeff * self.JTSSWD_t * self.T1
        if (self.JTSSWGD_t > 0.0):
            if ((self.VTSSWGD - self.Vbd_jct) < (self.VTSSWGD * 1.0e-3)):
                self.T0  = -self.Vbd_jct / self.Vtm0 / self.NJTSSWGD_t
                self.T1  = self.lexp(self.T0 * 1.0e3) - 1.0
                self.Ibd = self.Ibd - self.Weffcj * self.NF * self.JTSSWGD_t * self.T1
            else:
                self.T0  = -self.Vbd_jct / self.Vtm0 / self.NJTSSWGD_t
                self.T1  = self.lexp(self.T0 * self.VTSSWGD / (self.VTSSWGD - self.Vbd_jct)) - 1.0
                self.Ibd = self.Ibd - self.Weffcj * self.NF * self.JTSSWGD_t * self.T1


        # Junction capacitances (no swapping)
        # Source-to-bulk junction
        self.Czbs       = self.CJS_t * self.ASeff
        self.Czbssw     = self.CJSWS_t * self.PSeff
        self.Czbsswg    = self.CJSWGS_t * self.Weffcj * self.NF
        self.czbs_p1    = 0.1**-self.MJS
        self.czbs_p2    = 1.0 / (1.0 - self.MJS) * (1.0 - 0.05 * self.MJS * (1.0 + self.MJS) * self.czbs_p1)
        self.czbssw_p1  = 0.1**-self.MJSWS
        self.czbssw_p2  = 1.0 / (1.0 - self.MJSWS) * (1.0 - 0.05 * self.MJSWS * (1.0 + self.MJSWS) * self.czbssw_p1)
        self.czbsswg_p1 = 0.1**-self.MJSWGS
        self.czbsswg_p2 = 1.0 / (1.0 - self.MJSWGS) * (1.0 - 0.05 * self.MJSWGS * (1.0 + self.MJSWGS) * self.czbsswg_p1)
        self.Qbsj1 = self.JunCap(self.Czbs, self.Vbs_jct, self.PBS_t, self.MJS, self.czbs_p1, self.czbs_p2)
        self.Qbsj2 = self.JunCap(self.Czbssw, self.Vbs_jct, self.PBSWS_t, self.MJSWS, self.czbssw_p1, self.czbssw_p2)
        self.Qbsj3 = self.JunCap(self.Czbsswg, self.Vbs_jct, self.PBSWGS_t, self.MJSWGS, self.czbsswg_p1, self.czbsswg_p2)
        self.Qbsj = self.Qbsj1 + self.Qbsj2 + self.Qbsj3

        # Drain-to-bulk junction
        self.Czbd       = self.CJD_t * self.ADeff
        self.Czbdsw     = self.CJSWD_t * self.PDeff
        self.Czbdswg    = self.CJSWGD_t * self.Weffcj * self.NF
        self.czbd_p1    = 0.1**-self.MJD
        self.czbd_p2    = 1.0 / (1.0 - self.MJD) * (1.0 - 0.05 * self.MJD * (1.0 + self.MJD) * self.czbd_p1)
        self.czbdsw_p1  = 0.1**-self.MJSWD
        self.czbdsw_p2  = 1.0 / (1.0 - self.MJSWD) * (1.0 - 0.05 * self.MJSWD * (1.0 + self.MJSWD) * self.czbdsw_p1)
        self.czbdswg_p1 = 0.1**-self.MJSWGD
        self.czbdswg_p2 = 1.0 / (1.0 - self.MJSWGD) * (1.0 - 0.05 * self.MJSWGD * (1.0 + self.MJSWGD) * self.czbdswg_p1)
        self.Qbdj1 = self.JunCap(self.Czbd, self.Vbd_jct, self.PBD_t, self.MJD, self.czbd_p1, self.czbd_p2)
        self.Qbdj2 = self.JunCap(self.Czbdsw, self.Vbd_jct, self.PBSWD_t, self.MJSWD, self.czbdsw_p1, self.czbdsw_p2)
        self.Qbdj3 = self.JunCap(self.Czbdswg, self.Vbd_jct, self.PBSWGD_t, self.MJSWGD, self.czbdswg_p1, self.czbdswg_p2)
        self.Qbdj = self.Qbdj1 + self.Qbdj2 + self.Qbdj3

        # Sub-surface leakage drain current
        if (self.SSLMOD != 0):
            self.T1 = (self.NDEP_i / 1.0e23)**self.SSLEXP1
            self.T2 = (300.0 / self.DevTemp)**self.SSLEXP2
            self.T3 = (self.devsign * self.SSL5 * (self.VB - self.VS)) / self.Vt
            self.SSL0_NT  = self.SSL0 * self.lexp(-self.T1 * self.T2)
            self.SSL1_NT  = self.SSL1 * self.T2 * self.T1
            self.PHIB_SSL = self.SSL3 * tanh(self.lexp(self.devsign * self.SSL4 * ((self.VG - self.VB) - self.VTH - (self.VS - self.VB))))
            self.Issl     = self.sigvds * self.NF * self.Weff * self.SSL0_NT * self.lexp(self.T3) * self.lexp(-self.SSL1_NT * self.Leff) * self.lexp(self.PHIB_SSL / self.Vt) * (self.lexp(self.SSL2 * self.Vdsx / self.Vt) - 1.0)

        # Harshit's new flicker noise model. Ref: H. Agarwal et. al., IEEE J-EDS, vol. 3, no. 4, April 2015.
        self.Nt      = 4.0 * self.Vt * self.q
        self.Esatnoi = 2.0 * self.VSAT_a / self.ueff
        if (self.EM <= 0.0):
           self.DelClm = 0.0
        else:
            self.T0     = (self.diffVds / self.litl + self.EM) / self.Esatnoi
            self.DelClm = self.litl * self.lln(self.T0)
            if (self.DelClm < 0.0):
                self.DelClm = 0.0

        self.Nstar = self.Vt / self.q * (self.Cox + self.Cdep + self.CIT_i)
        self.Nl    = 2.0 * self.nq * self.Cox * self.Vt * self.qdeff * self.Mnud1 * self.Mnud / self.q
        self.T0a   = self.q * self.q * self.q * self.Vt * abs(self.ids) * self.ueff
        self.T0b   = self.q * self.Vt * self.ids * self.ids
        self.T0c   = self.NOIA + self.NOIB * self.Nl + self.NOIC * self.Nl * self.Nl
        self.T0d   = (self.Nl + self.Nstar) * (self.Nl + self.Nstar)
        self.T0e   = self.NOIA * self.q * self.Vt
        if (self.FNOIMOD == 1):
            self.LH1 = self.LH
            if (self.Leff > self.LH1):
                self.T0 = (self.Leff - self.LH1)
            else:
                self.LH1 = self.Leff
                self.T0 = self.LH1
            if (self.LINTNOI >= self.T0 / 2.0):
                print("Warning: LINTNOI = %e is too large - Leff for noise is negative. Re-setting LINTNOI = 0.", LINTNOI)
                self.LINTNOI_i = 0.0
            else:
                self.LINTNOI_i = self.LINTNOI

            self.LeffnoiH = self.Leff
            self.vgfbh  = (self.Vg - self.VFB_i) / self.Vt
            self.gam_h  = sqrt(2.0 * self.q * self.epssi * self.HNDEP / self.Vt) / self.Cox
            self.phib_h = log(self.HNDEP / self.ni)

            # Pinch-Off potential for halo region
            self.psiph = self.PO_psip(self.vgfbh, self.gam_h, 0.0)

            # Normalized inversion charge at source end of halo MOSFET
            self.qsh = self.BSIM_q(self.psiph, self.phib_h, self.vs, self.gam_h)
            self.nq_h = 1.0 + self.gam_h / (2.0 * sqrt(self.psiph))

            # Setting mobility of halo region equal to the mobility of the channel. In general, U0H < ueff
            self.U0_i_h  = self.ueff
            self.beta_h  = self.U0_i_h * self.Cox * self.Weff
            self.beta_ch = self.ueff * self.Cox * self.Weff

            # Normalized drain current for halo transistor. Eq. (14) of the paper
            self.i1 = self.ids * self.LH1 / (2.0 * self.nq_h * self.beta_h * self.Vt * self.Vt)

            # Normalized drain current for channel transistor. Eq. (15) of the paper
            self.i2 = self.ids * (self.LeffnoiH - self.LH1) / (2.0 * self.nq * self.beta_ch * self.nVt * self.nVt)
            self.T0 = (1.0 + 4.0 * (self.qsh * self.qsh + self.qsh - self.i1))
            if (self.T0 < 1.0):
                self.qdh = 0.0
            else:
                # Drain charge of halo transistor. Eq. (16) of the paper
                self.qdh = -0.5 + 0.5 * sqrt(self.T0)

            # Source charge of channel transistor. Eq. (17) of the paper
            self.qsch   = -0.5 + 0.5 * sqrt(1.0 + 4.0 * (self.qdeff * self.qdeff + self.qdeff + self.i2))
            self.gds_h  = 2.0 * self.nq_h * self.beta_h * self.Vt * self.qdh
            self.gds_ch = 2.0 * self.nq * self.beta_ch * self.Vt * self.qdeff
            self.gm_ch  = 2.0 * self.beta_ch * self.Vt * (self.qsch - self.qdeff)
            self.R_ch   = self.gds_h * (self.LeffnoiH - self.LH1)
            self.R_h    = self.gm_ch * self.LH1 + self.gds_ch * self.LH1
            self.t_tot  = 1.0 / (self.R_ch + self.R_h) / (self.R_ch + self.R_h)
            self.CF_ch  = self.R_ch * self.R_ch * self.t_tot
            self.CF_h   = self.R_h * self.R_h * self.t_tot

            # Local noise source
            if (self.Leff != self.LH1):
                self.Np2       = 2.0 * self.nq * self.Cox * self.Vt * self.qsch / self.q
                self.Leffnoi   = self.LeffnoiH - 2.0 * self.LINTNOI_i-self.LH1
                self.Leffnoisq = self.Leffnoi * self.Leffnoi
                # Channel transistor LNS
                self.T1     = 1.0e10 * self.Cox * self.Leffnoisq
                self.T2     = self.NOIA * self.lln((self.Np2 + self.Nstar) / (self.Nl + self.Nstar))
                self.T3     = self.NOIB * (self.Np2 - self.Nl)
                self.T4     = 0.5 * self.NOIC * (self.Np2 * self.Np2 - self.Nl * self.Nl)
                self.T5     = 1.0e10 * self.Leffnoisq * self.Weff * self.NF
                self.Ssi_ch = self.T0a / self.T1 * (self.T2 + self.T3 + self.T4) + self.T0b / self.T5 * self.DelClm * self.T0c / self.T0d
                self.T6     = self.Weff * self.NF * self.Leffnoi * 1.0e10 * self.Nstar * self.Nstar
                self.Swi_ch = self.T0e / self.T6 * self.ids * self.ids
                self.T7 = self.Swi_ch + self.Ssi_ch
                if (self.T7 > 0.0):
                    self.FNPowerAt1Hz_ch = (self.Ssi_ch * self.Swi_ch) / self.T7
                else:
                    self.FNPowerAt1Hz_ch = 0.0
            else:
                self.FNPowerAt1Hz_ch = 0.0
            # Halo transistor LNS
            self.T8    = self.NOIA2 * self.q * self.Vt
            self.T9    = self.Weff * self.NF * self.LH1 * 1.0e10 * self.Nstar * self.Nstar
            self.Swi_h = self.T8 / self.T9 * self.ids * self.ids
            self.T10   = self.Swi_h
            if (self.T10 > 0.0):
                self.FNPowerAt1Hz_h = self.Swi_h
            else:
                self.FNPowerAt1Hz_h = 0.0
            # Overall noise
            self.FNPowerAt1Hz = self.FNPowerAt1Hz_ch * self.CF_ch + self.FNPowerAt1Hz_h * self.CF_h
        else:
            # Parameter checking
            if (self.LINTNOI >= self.Leff/2.0):
                print("Warning: LINTNOI = %e is too large - Leff for noise is negative. Re-setting LINTNOI = 0.", LINTNOI)
                self.LINTNOI_i = 0.0
            else:
                self.LINTNOI_i = self.LINTNOI

            if (self.NOIA > 0.0 or self.NOIB > 0.0 or self.NOIC > 0.0):
                self.Leffnoi   = self.Leff - 2.0 * self.LINTNOI_i
                self.Leffnoisq = self.Leffnoi * self.Leffnoi
                self.T0        = 1.0e10 * self.Cox * self.Leffnoisq
                self.N0        = 2.0 * self.nq * self.Cox * self.Vt * self.qs * self.Mnud1 * self.Mnud / self.q
                self.T1        = self.NOIA * self.lln((self.N0 + self.Nstar) / (self.Nl + self.Nstar))
                self.T2        = self.NOIB * (self.N0 - self.Nl)
                self.T3        = 0.5 * self.NOIC * (self.N0 * self.N0 - self.Nl * self.Nl)
                self.T4        = 1.0e10 * self.Leffnoisq * self.Weff * self.NF
                self.Ssi       = self.T0a / self.T0 * (self.T1 + self.T2 + self.T3) + self.T0b / self.T4 * self.DelClm * self.T0c / self.T0d
                self.T5        = self.Weff * self.NF * self.Leffnoi * 1.0e10 * self.Nstar * self.Nstar
                self.Swi       = self.T0e / self.T5 * self.ids * self.ids
                self.T6        = self.Swi + self.Ssi
                if (self.T6 > 0.0):
                    self.FNPowerAt1Hz = (self.Ssi * self.Swi) / self.T6 / (1 + self.NOIA1 * (self.qs-self.qdeff)**self.NOIAX)
                else:
                    self.FNPowerAt1Hz = 0.0
            else:
                self.FNPowerAt1Hz = 0.0
        self.T0         = self.qia / self.Esatnoi / self.Leff
        self.T1         = self.T0 * self.T0
        self.T3         = self.RNOIA * (1.0 + self.TNOIA * self.Leff * self.T1)
        self.T4         = self.RNOIB * (1.0 + self.TNOIB * self.Leff * self.T1)
        self.T5         = self.RNOIK * (1.0 + self.TNOIK * self.Leff * self.T1)
        self.ctnoi      = self.RNOIC * (1.0 + self.TNOIC * self.Leff * self.T1)
        self.betanoisq  = 3.0 * self.T3 * self.T3
        self.betanoisq  = (self.betanoisq - 1.0) * exp(-self.Leff / self.LP) + 1.0
        self.betaLowId  = self.T5 * self.T5
        self.thetanoisq = self.T4 * self.T4
        self.cm_igid    = 0.0

        # C-V model
        self.vgfbCV   = self.vgfb
        self.gamg2    = (2.0 * self.q * self.epssi * self.NGATE_i) / (self.Cox * self.Cox * self.Vt)
        self.invgamg2 = 0.0
        if (self.CVMOD == 1):
            self.VFBCV_i = self.VFBCV_i + self.DELVTO
            self.vg      = self.Vg * self.inv_Vt
            self.vs      = self.Vs * self.inv_Vt
            self.vfb     = self.VFBCV_i * self.inv_Vt
            self.vgfbCV  = self.vg - self.vfb
            self.phibCV    = self.lln(self.NDEPCV_i / self.ni)
            # Normalized body factor
            self.gamCV      = sqrt(2.0 * self.q * self.epssi * self.NDEPCV_i * self.inv_Vt) / self.Cox
            self.inv_gam  = 1.0 / self.gamCV
            self.gamg2    = (2.0 * self.q * self.epssi * self.NGATE_i) / (self.Cox * self.Cox * self.Vt)
            self.invgamg2 = (1.0 / self.gamg2) if (self.NGATE_i > 0.0) else 0.0
            self.DPD      = (self.NDEPCV_i / self.NGATE_i) if (self.NGATE_i > 0.0) else 0.0

            # psip: pinch-off voltage
            self.psip = self.PO_psip(self.vgfbCV, self.gamCV, self.DPD)

            # Normalized inversion charge at source end of channel
            self.qs = self.BSIM_q(self.psip, self.phibCV, self.vs, self.gamCV)
            self.psipclamp = self.Smooth(self.psip, 1.0, 2.0)
            self.sqrtpsip = sqrt(self.psipclamp)

            # Source side surface potential
            self.psiavg = self.psip - 2.0 * self.qs
            self.T0 = self.Smooth(self.psiavg, 1.0, 2.0)
            self.nq = 1.0 + self.gamCV / (self.sqrtpsip + sqrt(self.T0))

            # Drain saturation voltage
            self.T0 = self.Vt * (self.vgfbCV - self.psip - 2.0 * self.qs * (self.nq - 1.0))
            self.qbs = self.Smooth(self.T0, 0.0, 0.1)

            # Source side qi and qb for Vdsat (normalized to Cox)
            self.qis = 2.0 * self.nq * self.Vt * self.qs
            self.Eeffs = self.EeffFactor * (self.qbs + self.eta_mu * self.qis)

            # Ref: BSIM4 mobility model
            self.T3 = (self.UA_a + self.UC_a * self.Vbsx) * self.Eeffs**self.EU_t
            self.T4 = 1.0 + self.T3
            self.Dmobs = self.Smooth(self.T4, 1.0, 0.0015)
            self.LambdaC_by2 = (self.U0_a / self.Dmobs) * self.Vt / (self.VSATCV_t * self.Lact)
            self.qdsat       = self.LambdaC_by2 * (self.qs * self.qs + self.qs) / (1.0 + self.LambdaC_by2 * (1.0 + self.qs))
            self.vdsatcv     = self.psip - 2.0 * self.phibCV - (2.0 * self.qdsat + self.lln((self.qdsat * 2.0 * self.nq * self.inv_gam) * ((self.qdsat * 2.0 * self.nq * self.inv_gam) + (self.gam / (self.nq - 1.0)))))
            self.VdsatCV     = self.vdsatcv * self.Vt

            # Normalized charge qdeff at drain end of channel
            self.VdssatCV = self.Smooth(self.VdsatCV - self.Vs, 0.0, 1e-3)
            self.VdssatCV     = self.VdssatCV / self.ABULK
            self.T7     = (self.Vds / self.VdssatCV)**(1.0 / self.DELTA_t)
            self.T8     = (1.0 + self.T7)**-self.DELTA_t
            self.Vdseff = self.Vds * self.T8
            self.vdeff  = (self.Vdseff + self.Vs) * self.inv_Vt
            self.qdeff = self.BSIM_q(self.psip, self.phibCV, self.vdeff, self.gamCV)

            # Reevaluation of nq to include qdeff needed for gummel symmetry
            self.psiavg = self.psip - self.qs - self.qdeff - 1.0
            self.T0 = self.Smooth(self.psiavg, 1.0, 2.0)
            self.T2 = sqrt(self.T0)
            self.T3 = 1.0 + self.DPD + self.gamCV / (self.sqrtpsip + self.T2)
            self.T4 = 0.5 + self.DPD * self.T2 * self.inv_gam
            self.T5 = sqrt(self.T4 * self.T4 + self.T3 * (self.qs + self.qdeff) * self.invgamg2)
            self.nq = self.T3 / (self.T4 + self.T5)

            # C-V expressions including velocity saturation and CLM
            # Velocity saturation for C-V
            self.T0  = self.Vt * (self.vgfbCV - self.psip - 2.0 * self.qs * (self.nq - 1.0))
            self.qbs = self.Smooth(self.T0, 0.0, 0.1)
            self.T1  = self.Vt * (self.vgfbCV - self.psip - 2.0 * self.qdeff * (self.nq - 1.0))
            self.qbd = self.Smooth(self.T1, 0.0, 0.1)
            self.qb  = 0.5 * (self.qbs + self.qbd)
            self.qia = self.nq * self.Vt * (self.qs + self.qdeff)
            self.Eeffm = self.EeffFactor * (self.qb + self.eta_mu * self.qia)
            self.psip = self.PO_psip((self.vgfbCV + self.DELVFBACC * self.inv_Vt), self.gamCV, self.DPD)
            self.T3    = (self.UA_a + self.UC_a * self.Vbsx) * self.Eeffm**self.EU_t
            self.T4    = 1.0 + self.T3
            self.Dmob = self.Smooth(self.T4, 1.0, 0.0015)
            self.LambdaC = 2.0 * (self.U0_a / self.Dmob) * self.Vt / (self.VSATCV_t * self.Lact)
            self.dps     = self.qs - self.qdeff
            self.T1      = 2.0 * (self.LambdaC * self.dps) * (self.LambdaC * self.dps)
            self.zsat    = sqrt(1.0 + self.T1)
            self.Dvsat   = 0.5 * (1.0 + self.zsat)
            # CLM for C-V
            self.Esat    = 2.0 * self.VSATCV_t / (self.U0_a / self.Dmob)
            self.EsatL   = self.Esat * self.Lact
            self.Vasat   = self.VdssatCV + self.EsatL
            self.diffVds = self.Vds - self.Vdseff
        if (self.PCLMCV_i != 0.0):
            self.MdL = 1.0 + self.PCLMCV_i * self.lln(1.0 + self.diffVds / self.PCLMCV_i / self.Vasat)
        else:
            self.MdL = 1.0
        self.MdL_2       = self.MdL * self.MdL
        self.inv_MdL     = 1.0 / self.MdL
        self.inv_MdL_2   = 1.0 / self.MdL_2
        self.MdL_less_1  = self.MdL - 1.0
        self.vgpqm = self.vgfbCV - self.psip
        self.DQSD  = (self.qs - self.qdeff)
        self.DQSD2 = (self.qs - self.qdeff) * (self.qs - self.qdeff)
        self.sis   = self.vgpqm + 2.0 * self.qs
        self.sid   = self.vgpqm + 2.0 * self.qdeff
        self.T1 = self.Smooth(self.sis, 0.0, 0.5)
        self.T2 = self.Smooth(self.sid, 0.0, 0.5)
        self.Temps = sqrt(0.25 + self.T1 * self.invgamg2)
        self.Tempd = sqrt(0.25 + self.T2 * self.invgamg2)
        self.T1 = self.sis / (1.0 + 2.0 * self.Temps)
        self.T2 = self.sid / (1.0 + 2.0 * self.Tempd)
        self.T3 = self.Temps + self.Tempd
        self.T4 = self.Oneby3 * (self.DQSD2 / (self.T3 * self.T3 * self.T3))
        self.T5 = (self.ABULK*self.Dvsat * self.inv_MdL) / (1.0 + self.qs + self.qdeff)
        self.T6 = 0.8 * (self.T3 * self.T3 + self.Temps * self.Tempd) * self.T5
        self.T7 = self.T6 + (2.0 * self.invgamg2)
        self.T8 = self.Oneby3 * self.DQSD2 * self.T5
        self.dqgeff = self.sid * (2.0 * self.Tempd - 1.0) / (2.0 * self.Tempd + 1.0)
        self.qbeff  = self.vgpqm - 2.0 * (self.nq - 1.0) * self.qdeff + self.dqgeff
        self.Qb  = self.inv_MdL * (self.T1 + self.T2 + (self.T4 * self.T7 - self.nq * (self.qs + self.qdeff + self.T8))) + self.MdL_less_1 * self.qbeff
        self.T9  = self.qs + self.qdeff
        self.T10 = self.DQSD2 * self.T5 * self.T5
        self.Qi  = self.nq * self.inv_MdL * (self.T9 + self.Oneby3 * self.DQSD2 * self.T5) + 2.0 * self.nq * self.MdL_less_1 * self.qdeff
        self.Qd1 = self.nq * self.inv_MdL_2 * (0.5 * self.T9 - (self.DQSD / 6.0) * (1.0 - self.DQSD * self.T5 - 0.2 * self.T10))
        self.Qd2 = self.nq * (self.MdL - self.inv_MdL) * self.qdeff
        self.Qd  = self.Qd1 + self.Qd2
        self.Qs  = self.Qi - self.Qd

        # Quantum mechanical effects
        self.qbaCV = self.Smooth(self.Vt * self.Qb, 0.0, 0.1)
        self.qiaCV      = self.Vt * (self.Qs + self.Qd)
        self.T0         = (self.qiaCV + self.ETAQM * self.qbaCV) / self.QM0
        self.T1         = 1.0 + self.T0**(0.7 * self.BDOS)
        self.XDCinv     = self.ADOS * 1.9e-9 / self.T1
        self.Coxeffinv  = 3.9 * self.EPS0 / (self.BSIMBULKTOXP * 3.9 / self.EPSROX + self.XDCinv / self.epsratio)
        self.QBi        = -self.NF * self.Wact * self.Lact * (self.EPS0 * self.EPSROX / self.BSIMBULKTOXP) * self.Vt * self.Qb
        self.WLCOXVtinv = self.NF * self.Wact * self.Lact * self.Coxeffinv * self.Vt
        self.QSi        = -self.WLCOXVtinv * self.Qs
        self.QDi        = -self.WLCOXVtinv * self.Qd
        self.QGi        = -(self.QBi + self.QSi + self.QDi)

        # Outer fringing capacitances
        if ("CF" not in param.keys()):
            self.CF_i = 2.0 * self.EPSROX * self.EPS0 / self.M_PI * self.lln(self.CFRCOEFF * (1.0 + 0.4e-6 / self.TOXE))
        self.Cgsof = self.CGSO + self.CF_i
        self.Cgdof = self.CGDO + self.CF_i

        # Overlap capacitances
        if (self.COVMOD == 0):
            self.Qovs = -self.Wact * self.NF * self.Cgsof * self.Vgs_ov_noswap
            self.Qovd = -self.Wact * self.NF * self.Cgdof * self.Vgd_ov_noswap
        else:
            self.T0    = sqrt((self.Vgs_ov_noswap - self.Vfbsdr + self.DELTA_1) * (self.Vgs_ov_noswap - self.Vfbsdr + self.DELTA_1) + 4.0 * self.DELTA_1)
            self.Vgsov = 0.5 * (self.Vgs_ov_noswap - self.Vfbsdr + self.DELTA_1 - self.T0)
            self.T1    = sqrt(1.0 - 4.0 * self.Vgsov / self.CKAPPAS_i)
            self.Qovs  = -self.Wact * self.NF * (self.Cgsof * self.Vgs_ov_noswap + self.CGSL_i * (self.Vgs_ov_noswap - self.Vfbsdr - self.Vgsov - 0.5 * self.CKAPPAS_i * (-1.0 + self.T1)))
            self.T0    = sqrt((self.Vgd_ov_noswap - self.Vfbsdr + self.DELTA_1) * (self.Vgd_ov_noswap - self.Vfbsdr + self.DELTA_1) + 4.0 * self.DELTA_1)
            self.Vgdov = 0.5 * (self.Vgd_ov_noswap - self.Vfbsdr + self.DELTA_1 - self.T0)
            self.T2    = sqrt(1.0 - 4.0 * self.Vgdov / self.CKAPPAD_i)
            self.Qovd  = -self.Wact * self.NF * (self.Cgdof * self.Vgd_ov_noswap + self.CGDL_i * (self.Vgd_ov_noswap - self.Vfbsdr - self.Vgdov - 0.5 * self.CKAPPAD_i * (-1.0 + self.T2)))
        self.Qovb = -self.devsign * self.NF * self.Lact * self.CGBO * (self.VG - self.VB)
        self.Qovg = -(self.Qovs + self.Qovd + self.Qovb)

        # Edge FET model
        if (self.EDGEFET == 1):
            self.phib_edge     = self.lln(self.NDEPEDGE_i / self.ni)
            self.Phist         = max(0.4 + self.Vt * self.phib_edge + self.PHIN_i, 0.4)
            self.sqrtPhist     = sqrt(self.Phist)
            self.T1DEP         = sqrt(2.0 * self.epssi / (self.q * self.NDEPEDGE_i))
            self.NFACTOREDGE_t = self.NFACTOREDGE_i * self.hypsmooth((1.0 + self.TNFACTOREDGE_i * (self.TRatio - 1.0)), 1e-3)
            self.ETA0EDGE_t    = self.ETA0EDGE_i * (1.0 + self.TETA0EDGE_i * (self.TRatio - 1.0))
            self.PhistVbs = self.Smooth(self.Phist - self.Vbsx, 0.05, 0.1)
            self.sqrtPhistVbs  = sqrt(self.PhistVbs)
            self.Xdep          = self.T1DEP * self.sqrtPhistVbs
            self.Cdep          = self.epssi / self.Xdep
            self.cdsc          = self.CITEDGE_i + self.NFACTOREDGE_t + self.CDSCDEDGE_i * self.Vdsx - self.CDSCBEDGE_i * self.Vbsx
            self.T1            = 1.0 + self.cdsc/self.Cox
            self.n = self.Smooth(self.T1, 1.0, 0.05)
            self.nVt       = self.n * self.Vt
            self.inv_nVt   = 1.0 / self.nVt
            self.vg        = self.Vg * self.inv_nVt
            self.vs        = self.Vs * self.inv_nVt
            self.vfb       = self.VFB_i * self.inv_nVt
            self.dvth_dibl = -(self.ETA0EDGE_t + self.ETABEDGE_i * self.Vbsx) * self.Vdsx
            self.dvth_temp = (self.KT1EDGE_i + self.KT1LEDGE_i / self.Leff + self.KT2EDGE_i * self.Vbsx) * (self.TRatio**self.KT1EXPEDGE_i - 1.0)
            self.litl_edge = self.litl * (1.0 + self.DVT2EDGE * self.Vbsx)
            self.T0        = self.DVT1EDGE * self.Leff / self.litl_edge
            if (self.T0 < 40.0):
                self.theta_sce_edge = 0.5 * self.DVT0EDGE / (cosh(self.T0) - 1.0)
            else:
                self.theta_sce_edge = self.DVT0EDGE * self.lexp(-self.T0)
            self.dvth_sce  = self.theta_sce_edge * (self.Vbi_edge - self.Phist)
            self.Vth_shift = self.dvth_dibl - self.dvth_temp + self.dvth_sce + self.DVTEDGE + self.vth0_stress_EDGE - self.K2EDGE_i * self.Vbsx
            self.vgfb      = self.vg - self.vfb - self.Vth_shift * self.inv_nVt

            # Normalized body factor
            self.DGAMMAEDGE_i = self.DGAMMAEDGE * (1.0 + self.DGAMMAEDGEL * self.Leff**-self.DGAMMAEDGELEXP)
            self.gam_edge          = sqrt(2.0 * self.q * self.epssi * self.NDEPEDGE_i * self.inv_nVt) / self.Cox
            self.gam_edge          = self.gam_edge * (1.0 + self.DGAMMAEDGE_i)
            self.inv_gam           = 1.0 / self.gam_edge

            # psip: pinch-off voltage
            self.phib_n_edge  = self.phib_edge / self.n
            self.psip = self.PO_psip(self.vgfb, self.gam_edge, 0.0)
            self.qs_edge = self.BSIM_q(self.psip, self.phib_n_edge, self.vs, self.gam_edge)

            # Approximate pinch-off voltage
            self.vdsatedge = 2.0 * self.nVt * self.qs_edge + 2.0 * self.nVt
            self.Vdsatedge = self.vdsatedge
            self.Vdsatedge = self.Vdsatedge + self.Vs

            # Vdssat clamped to avoid negative values during transient simulation
            self.Vdssate = self.Smooth(self.Vdsatedge - self.Vs, 0.0, 1.0e-3)
            self.T7     = (self.Vds / self.Vdssate)**(1.0 / self.DELTA_t)
            self.T8     = (1.0 + self.T7)**-self.DELTA_t
            self.Vdseff = self.Vds * self.T8
            self.vdeff  = (self.Vdseff + self.Vs) * self.inv_nVt
            self.qdeff_edge = self.BSIM_q(self.psip, self.phib_n_edge, self.vdeff, self.gam_edge)

            # Nq calculation for Edge FET
            self.psipclamp = self.Smooth(self.psip, 1.0, 2.0)
            self.sqrtpsip = sqrt(self.psipclamp)
            self.psiavg   = self.psip - self.qs_edge - self.qdeff_edge -1.0
            self.T0 = self.Smooth(self.psiavg, 1.0, 2.0)
            self.T2       = sqrt(self.T0)
            self.nq_edge  = 1.0 + self.gam_edge / (self.sqrtpsip + self.T2)
            self.ids_edge = 2.0 * self.NF * self.nq_edge * self.ueff * self.WEDGE / self.Leff * self.Cox * self.nVt * self.nVt * ((self.qs_edge - self.qdeff_edge) * (1.0 + self.qs_edge + self.qdeff_edge)) * self.Moc
            self.ids      = self.ids_edge + self.ids


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

filepath = "modelcard.l"
model = read_mdl(filepath)

biasT = {
    "VD": 1.0,
    "VG": 1.0,
    "VS": 0.0,
    "VB": 0.0,
    "TEMP": -40.0,
}

yy=bsimbulk(**model, **biasT, **{"A21":-0.01})

sweep = np.arange(0,1.1,0.1)

print(f"{'VG':4}", f"{'ids':15}", f"{'ueff':15}")
for x in sweep:
    yy.param_update(**{'VG':x})
    print(f"{x:.2f}", f"{yy.ids:.9e}", f"{yy.ueff:.9e}")
