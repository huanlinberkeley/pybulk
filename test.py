import re

with open("param.txt", 'r') as f:
    lines = f.readlines()

param = ['L','W','NF','NRS','NRD','VFBSDOFF','MINZ','RGATEMOD','RBODYMOD','GEOMOD','RGEOMOD','RBPB','RBPD','RBPS','RBDB','RBSB','SA','SB','SD','SCA','SCB','SCC','SC','AS','AD','PS','PD','XGW','NGCON','DTEMP','MULU0','DELVTO','IDS0MULT','EDGEFET','SSLMOD','TYPE','CVMOD','COVMOD','RDSMOD','WPEMOD','ASYMMOD','GIDLMOD','IGCMOD','IGBMOD','TNOIMOD','SHMOD','MOBSCALE','LLONG','LMLT','WMLT','XL','WWIDE','XW','LINT','LL','LW','LWL','LLN','LWN','WINT','WL','WW','WWL','WLN','WWN','DLC','LLC','LWC','LWLC','DWC','WLC','WWC','WWLC','TOXE','TOXP','DTOX','NDEP','NDEPL1','NDEPLEXP1','NDEPL2','NDEPLEXP2','NDEPW','NDEPWEXP','NDEPWL','NDEPWLEXP','LNDEP','WNDEP','PNDEP','NDEPCV','NDEPCVL1','NDEPCVLEXP1','NDEPCVL2','NDEPCVLEXP2','NDEPCVW','NDEPCVWEXP','NDEPCVWL','NDEPCVWLEXP','LNDEPCV','WNDEPCV','PNDEPCV','NGATE','LNGATE','WNGATE','PNGATE','EASUB','NI0SUB','BG0SUB','EPSRSUB','EPSROX','XJ','LXJ','WXJ','PXJ','VFB','LVFB','WVFB','PVFB','VFBCV','LVFBCV','WVFBCV','PVFBCV','VFBCVL','VFBCVLEXP','VFBCVW','VFBCVWEXP','VFBCVWL','VFBCVWLEXP','DELVFBACC','PERMOD','DWJ','NSD','LNSD','WNSD','PNSD','DVTP0','LDVTP0','WDVTP0','PDVTP0','DVTP1','LDVTP1','WDVTP1','PDVTP1','DVTP2','LDVTP2','WDVTP2','PDVTP2','DVTP3','LDVTP3','WDVTP3','PDVTP3','DVTP4','LDVTP4','WDVTP4','PDVTP4','DVTP5','LDVTP5','WDVTP5','PDVTP5','PHIN','LPHIN','WPHIN','PPHIN','ETA0','LETA0','WETA0','PETA0','ETA0R','LETA0R','WETA0R','PETA0R','DSUB','ETAB','ETABEXP','LETAB','WETAB','PETAB','K1','K1L','K1LEXP','K1W','K1WEXP','K1WL','K1WLEXP','LK1','WK1','PK1','K2','K2L','K2LEXP','K2W','K2WEXP','K2WL','K2WLEXP','LK2','WK2','PK2','ADOS','BDOS','QM0','ETAQM','CIT','LCIT','WCIT','PCIT','NFACTOR','NFACTORL','NFACTORLEXP','NFACTORW','NFACTORWEXP','NFACTORWL','NFACTORWLEXP','LNFACTOR','WNFACTOR','PNFACTOR','CDSCD','CDSCDL','CDSCDLEXP','LCDSCD','WCDSCD','PCDSCD','CDSCDR','CDSCDLR','LCDSCDR','WCDSCDR','PCDSCDR','CDSCB','CDSCBL','CDSCBLEXP','LCDSCB','WCDSCB','PCDSCB','VSAT','LVSAT','WVSAT','PVSAT','VSATL','VSATLEXP','VSATW','VSATWEXP','VSATWL','VSATWLEXP','VSATR','LVSATR','WVSATR','PVSATR','DELTA','LDELTA','WDELTA','PDELTA','DELTAL','DELTALEXP','VSATCV','LVSATCV','WVSATCV','PVSATCV','VSATCVL','VSATCVLEXP','VSATCVW','VSATCVWEXP','VSATCVWL','VSATCVWLEXP','UP1','LP1','UP2','LP2','U0','U0L','U0LEXP','LU0','WU0','PU0','U0R','LU0R','WU0R','PU0R','ETAMOB','UA','UAL','UALEXP','UAW','UAWEXP','UAWL','UAWLEXP','LUA','WUA','PUA','UAR','LUAR','WUAR','PUAR','EU','LEU','WEU','PEU','EUL','EULEXP','EUW','EUWEXP','EUWL','EUWLEXP','UD','UDL','UDLEXP','LUD','WUD','PUD','UDR','LUDR','WUDR','PUDR','UCS','LUCS','WUCS','PUCS','UCSR','LUCSR','WUCSR','PUCSR','UC','UCL','UCLEXP','UCW','UCWEXP','UCWL','UCWLEXP','LUC','WUC','PUC','UCR','LUCR','WUCR','PUCR','PCLM','PCLML','PCLMLEXP','LPCLM','WPCLM','PPCLM','PCLMR','LPCLMR','WPCLMR','PPCLMR','PCLMG','PCLMCV','PCLMCVL','PCLMCVLEXP','LPCLMCV','WPCLMCV','PPCLMCV','PSCBE1','LPSCBE1','WPSCBE1','PPSCBE1','PSCBE2','LPSCBE2','WPSCBE2','PPSCBE2','PDITS','LPDITS','WPDITS','PPDITS','PDITSL','PDITSD','LPDITSD','WPDITSD','PPDITSD','RSH','PRWG','LPRWG','WPRWG','PPRWG','PRWB','LPRWB','WPRWB','PPRWB','PRWBL','PRWBLEXP','WR','LWR','WWR','PWR','RSWMIN','LRSWMIN','WRSWMIN','PRSWMIN','RSW','LRSW','WRSW','PRSW','RSWL','RSWLEXP','RDWMIN','LRDWMIN','WRDWMIN','PRDWMIN','RDW','LRDW','WRDW','PRDW','RDWL','RDWLEXP','RDSWMIN','LRDSWMIN','WRDSWMIN','PRDSWMIN','RDSW','RDSWL','RDSWLEXP','LRDSW','WRDSW','PRDSW','PSAT','LPSAT','WPSAT','PPSAT','PSATL','PSATLEXP','PSATB','PSATR','LPSATR','WPSATR','PPSATR','LPSATB','WPSATB','PPSATB','PSATX','PTWG','LPTWG','WPTWG','PPTWG','PTWGL','PTWGLEXP','PTWGR','LPTWGR','WPTWGR','PPTWGR','PTWGLR','PTWGLEXPR','A1','LA1','WA1','PA1','A11','LA11','WA11','PA11','A2','LA2','WA2','PA2','A21','LA21','WA21','PA21','PDIBLC','PDIBLCL','PDIBLCLEXP','LPDIBLC','WPDIBLC','PPDIBLC','PDIBLCR','PDIBLCLR','PDIBLCLEXPR','LPDIBLCR','WPDIBLCR','PPDIBLCR','PDIBLCB','LPDIBLCB','WPDIBLCB','PPDIBLCB','PVAG','LPVAG','WPVAG','PPVAG','FPROUT','FPROUTL','FPROUTLEXP','LFPROUT','WFPROUT','PFPROUT','ALPHA0','ALPHA0L','ALPHA0LEXP','LALPHA0','WALPHA0','PALPHA0','BETA0','LBETA0','WBETA0','PBETA0','AIGBACC','BIGBACC','CIGBACC','NIGBACC','AIGBINV','BIGBINV','CIGBINV','EIGBINV','NIGBINV','AIGC','BIGC','CIGC','AIGS','BIGS','CIGS','AIGD','BIGD','CIGD','DLCIG','DLCIGD','POXEDGE','NTOX','TOXREF','PIGCD','AIGCL','AIGCW','AIGSL','AIGSW','AIGDL','AIGDW','PIGCDL','LAIGBINV','WAIGBINV','PAIGBINV','LBIGBINV','WBIGBINV','PBIGBINV','LCIGBINV','WCIGBINV','PCIGBINV','LEIGBINV','WEIGBINV','PEIGBINV','LNIGBINV','WNIGBINV','PNIGBINV','LAIGBACC','WAIGBACC','PAIGBACC','LBIGBACC','WBIGBACC','PBIGBACC','LCIGBACC','WCIGBACC','PCIGBACC','LNIGBACC','WNIGBACC','PNIGBACC','LAIGC','WAIGC','PAIGC','LBIGC','WBIGC','PBIGC','LCIGC','WCIGC','PCIGC','LAIGS','WAIGS','PAIGS','LBIGS','WBIGS','PBIGS','LCIGS','WCIGS','PCIGS','LAIGD','WAIGD','PAIGD','LBIGD','WBIGD','PBIGD','LCIGD','WCIGD','PCIGD','LPOXEDGE','WPOXEDGE','PPOXEDGE','LDLCIG','WDLCIG','PDLCIG','LDLCIGD','WDLCIGD','PDLCIGD','LNTOX','WNTOX','PNTOX','AGIDL','AGIDLL','AGIDLW','LAGIDL','WAGIDL','PAGIDL','BGIDL','LBGIDL','WBGIDL','PBGIDL','CGIDL','LCGIDL','WCGIDL','PCGIDL','EGIDL','LEGIDL','WEGIDL','PEGIDL','AGISL','AGISLL','AGISLW','LAGISL','WAGISL','PAGISL','BGISL','LBGISL','WBGISL','PBGISL','CGISL','LCGISL','WCGISL','PCGISL','EGISL','LEGISL','WEGISL','PEGISL','CF','LCF','WCF','PCF','CFRCOEFF','CGSO','CGDO','CGBO','CGSL','LCGSL','WCGSL','PCGSL','CGDL','LCGDL','WCGDL','PCGDL','CKAPPAS','LCKAPPAS','WCKAPPAS','PCKAPPAS','CKAPPAD','LCKAPPAD','WCKAPPAD','PCKAPPAD','DMCG','DMCI','DMDG','DMCGT','XGL','RSHG','CJS','CJD','CJSWS','CJSWD','CJSWGS','CJSWGD','PBS','PBD','PBSWS','PBSWD','PBSWGS','PBSWGD','MJS','MJD','MJSWS','MJSWD','MJSWGS','MJSWGD','JSS','JSD','JSWS','JSWD','JSWGS','JSWGD','NJS','NJD','IJTHSFWD','IJTHDFWD','IJTHSREV','IJTHDREV','BVS','BVD','XJBVS','XJBVD','JTSS','JTSD','JTSSWS','JTSSWD','JTSSWGS','JTSSWGD','JTWEFF','NJTS','NJTSD','NJTSSW','NJTSSWD','NJTSSWG','NJTSSWGD','VTSS','VTSD','VTSSWS','VTSSWD','VTSSWGS','VTSSWGD','XRCRG1','XRCRG2','GBMIN','RBPS0','RBPSL','RBPSW','RBPSNF','RBPD0','RBPDL','RBPDW','RBPDNF','RBPBX0','RBPBXL','RBPBXW','RBPBXNF','RBPBY0','RBPBYL','RBPBYW','RBPBYNF','RBSBX0','RBSBY0','RBDBX0','RBDBY0','RBSDBXL','RBSDBXW','RBSDBXNF','RBSDBYL','RBSDBYW','RBSDBYNF','EF','EM','NOIA','NOIB','NOIC','LINTNOI','NOIA1','NOIAX','NTNOI','RNOIA','RNOIB','RNOIC','TNOIA','TNOIB','TNOIC','BINUNIT','DLBIN','DWBIN','TNOM','TBGASUB','TBGBSUB','TNFACTOR','UTE','LUTE','WUTE','PUTE','UTEL','UA1','LUA1','WUA1','PUA1','UA1L','UC1','LUC1','WUC1','PUC1','UD1','LUD1','WUD1','PUD1','UD1L','EU1','LEU1','WEU1','PEU1','UCSTE','LUCSTE','WUCSTE','PUCSTE','TETA0','PRT','LPRT','WPRT','PPRT','AT','LAT','WAT','PAT','ATL','TDELTA','PTWGT','LPTWGT','WPTWGT','PPTWGT','PTWGTL','KT1','KT1EXP','KT1L','LKT1','WKT1','PKT1','KT2','LKT2','WKT2','PKT2','IIT','LIIT','WIIT','PIIT','IGT','LIGT','WIGT','PIGT','TGIDL','LTGIDL','WTGIDL','PTGIDL','TCJ','TCJSW','TCJSWG','TPB','TPBSW','TPBSWG','XTIS','XTID','XTSS','XTSD','XTSSWS','XTSSWD','XTSSWGS','XTSSWGD','TNJTS','TNJTSD','TNJTSSW','TNJTSSWD','TNJTSSWG','TNJTSSWGD','RTH0','CTH0','WTH0','SAREF','SBREF','WLOD','KU0','KVSAT','TKU0','LKU0','WKU0','PKU0','LLODKU0','WLODKU0','KVTH0','LKVTH0','WKVTH0','PKVTH0','LLODVTH','WLODVTH','STK2','LODK2','STETA0','LODETA0','WEB','WEC','KVTH0WE','LKVTH0WE','WKVTH0WE','PKVTH0WE','K2WE','LK2WE','WK2WE','PK2WE','KU0WE','LKU0WE','WKU0WE','PKU0WE','SCREF','SSL0','SSL1','SSL2','SSL3','SSL4','SSL5','SSLEXP1','SSLEXP2','AVDSX','WEDGE','DGAMMAEDGE','DGAMMAEDGEL','DGAMMAEDGELEXP','DVTEDGE','NDEPEDGE','LNDEPEDGE','WNDEPEDGE','PNDEPEDGE','NFACTOREDGE','LNFACTOREDGE','WNFACTOREDGE','PNFACTOREDGE','CITEDGE','LCITEDGE','WCITEDGE','PCITEDGE','CDSCDEDGE','LCDSCDEDGE','WCDSCDEDGE','PCDSCDEDGE','CDSCBEDGE','LCDSCBEDGE','WCDSCBEDGE','PCDSCBEDGE','ETA0EDGE','LETA0EDGE','WETA0EDGE','PETA0EDGE','ETABEDGE','LETABEDGE','WETABEDGE','PETABEDGE','KT1EDGE','LKT1EDGE','WKT1EDGE','PKT1EDGE','KT1LEDGE','LKT1LEDGE','WKT1LEDGE','PKT1LEDGE','KT2EDGE','LKT2EDGE','WKT2EDGE','PKT2EDGE','KT1EXPEDGE','LKT1EXPEDGE','WKT1EXPEDGE','PKT1EXPEDGE','TNFACTOREDGE','LTNFACTOREDGE','WTNFACTOREDGE','PTNFACTOREDGE','TETA0EDGE','LTETA0EDGE','WTETA0EDGE','PTETA0EDGE','DVT0EDGE','DVT1EDGE','DVT2EDGE','K2EDGE','LK2EDGE','WK2EDGE','PK2EDGE','KVTH0EDGE','LKVTH0EDGE','WKVTH0EDGE','PKVTH0EDGE','STK2EDGE','LSTK2EDGE','WSTK2EDGE','PSTK2EDGE','STETA0EDGE','LSTETA0EDGE','WSTETA0EDGE','PSTETA0EDGE','IGCLAMP','LP','RNOIK','TNOIK','TNOIK2','K0','LK0','WK0','PK0','K01','LK01','WK01','PK01','M0','LM0','WM0','PM0','M01','LM01','WM01','PM01','NEDGE','NOIA1_EDGE','NOIAX_EDGE','FNOIMOD','LH','NOIA2','HNDEP','ABULK','C0','LC0','WC0','PC0','C01','LC01','WC01','PC01','C0SI','LC0SI','WC0SI','PC0SI','C0SI1','LC0SI1','WC0SI1','PC0SI1','C0SISAT','LC0SISAT','WC0SISAT','PC0SISAT','C0SISAT1','LC0SISAT1','WC0SISAT1','PC0SISAT1','minr','HVMOD','HVCAP','HVCAPS','IIMOD','NDRIFTD','VDRIFT','MDRIFT','NDRIFTS','RDLCW','RSLCW','PDRWB','VFBDRIFT','VFBOV','LOVER','LOVERACC','NDR','SLHV','SLHV1','ALPHADR','BETADR','PRTHV','ATHV','HVFACTOR','DRII1','DRII2','DELTAII',]

value = ['1.0e-5','1.0e-5','1','1.0','1.0','0.0','0','0','0','0','0','50.0','50.0','50.0','50.0','50.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','1','0.0','1.0','0.0','1.0','0','0','ntype','0','0','0','0','0','0','0','0','0','0','0','1.0e-5','1.0','1.0','0.0','1.0e-5','0.0','0.0','0.0','0.0','0.0','1.0','1.0','0.0','0.0','0.0','0.0','1.0','1.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','3.0e-9','TOXE','0.0','1e24','0.0','1.0','0.0','2.0','0.0','1.0','0.0','1.0','0.0','0.0','0.0','1e24','0.0','1.0','0.0','2.0','0.0','1.0','0.0','1.0','0.0','0.0','0.0','5e25','0.0','0.0','0.0','4.05','1.1e16','1.17','11.9','3.9','1.5e-7','0.0','0.0','0.0','-0.5','0.0','0.0','0.0','-0.5','0.0','0.0','0.0','0.0','1.0','0.0','1.0','0.0','1.0','0.0','1','DWC','1e26','0.0','0.0','0.0','0.0','0','0','0','0.0','0','0','0','0.0','0','0','0','0.0','0','0','0','0.0','0','0','0','0.0','0','0','0','0.045','0.0','0.0','0.0','0.08','0.0','0.0','0.0','ETA0','LETA0','WETA0','PETA0','1.0','-0.07','1.0','0.0','0.0','0.0','0.0','0.0','1.0','0.0','1.0','0.0','1.0','0.0','0.0','0.0','0.0','0.0','1.0','0.0','1.0','0.0','1.0','0.0','0.0','0.0','0.0','1.0','1.0e-3','0.54','0.0','0.0','0.0','0.0','0.0','0.0','1.0','0.0','1.0','0.0','1.0','0.0','0.0','0.0','1e-9','0.0','1.0','0.0','0.0','0.0','CDSCD','CDSCDL','LCDSCD','WCDSCD','PCDSCD','0.0','0.0','1.0','0.0','0.0','0.0','1e5','0.0','0.0','0.0','0.0','1.0','0.0','1.0','0.0','1.0','VSAT','LVSAT','WVSAT','PVSAT','0.125','0.0','0.0','0.0','0.0','1.0','1e5','0.0','0.0','0.0','0.0','1.0','0.0','1.0','0.0','1.0','0.0','1.0e-8','0.0','1.0e-8','67.0e-3','0.0','1.0','0.0','0.0','0.0','U0','LU0','WU0','PU0','1.0','0.001','0.0','1.0','0.0','1.0','0.0','1.0','0.0','0.0','0.0','UA','LUA','WUA','PUA','1.5','0.0','0.0','0.0','0.0','1.0','0.0','1.0','0.0','1.0','0.001','0.0','1.0','0.0','0.0','0.0','UD','LUD','WUD','PUD','2.0','0.0','0.0','0.0','UCS','LUCS','WUCS','PUCS','0.0','0.0','1.0','0.0','1.0','0.0','1.0','0.0','0.0','0.0','UC','LUC','WUC','PUC','0.0','0.0','1.0','0.0','0.0','0.0','PCLM','LPCLM','WPCLM','PPCLM','0.0','PCLM','PCLML','PCLMLEXP','LPCLM','WPCLM','PPCLM','4.24e8','0.0','0.0','0.0','1.0e-8','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','1.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','1.0','1.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','10.0','0.0','0.0','0.0','0.0','1.0','RSWMIN','LRSWMIN','WRSWMIN','PRSWMIN','RSW','LRSW','WRSW','PRSW','RSWL','RSWLEXP','0.0','0.0','0.0','0.0','20.0','0.0','1.0','0.0','0.0','0.0','1.0','0.0','0.0','0.0','0.0','1.0','0.0','PSAT','LPSAT','WPSAT','PPSAT','0.0','0.0','0.0','1.0','0.0','0.0','0.0','0.0','0.0','1.0','PTWG','LPTWG','WPTWG','PPTWG','PTWGL','PTWGLEXP','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','1.0','0.0','0.0','0.0','PDIBLC','PDIBLCL','PDIBLCLEXP','LPDIBLC','WPDIBLC','PPDIBLC','0.0','0.0','0.0','0.0','1.0','0.0','0.0','0.0','0.0','0.0','1.0','0.0','0.0','0.0','0.0','0.0','1.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','1.36e-2','1.71e-3','0.075','1.0','1.11e-2','9.49e-4','0.006','1.1','3.0','(1.36e-2 if (self.TYPE == ntype) else 9.8e-3)','(1.71e-3 if (self.TYPE == ntype) else 7.59e-4)','(0.075 if (self.TYPE == ntype) else 0.03)','(1.36e-2 if (self.TYPE == ntype) else 9.8e-3)','(1.71e-3 if (self.TYPE == ntype) else 7.59e-4)','(0.075 if (self.TYPE == ntype) else 0.03)','(1.36e-2 if (self.TYPE == ntype) else 9.8e-3)','(1.71e-3 if (self.TYPE == ntype) else 7.59e-4)','(0.075 if (self.TYPE == ntype) else 0.03)','LINT','DLCIG','1.0','1.0','3.0e-9','1.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','2.3e9','0.0','0.0','0.0','0.5','0.0','0.0','0.0','0.8','0.0','0.0','0.0','AGIDL','AGIDLL','AGIDLW','LAGIDL','WAGIDL','PAGIDL','BGIDL','LBGIDL','WBGIDL','PBGIDL','CGIDL','LCGIDL','WCGIDL','PCGIDL','EGIDL','LEGIDL','WEGIDL','PEGIDL','0.0','0.0','0.0','0.0','1.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.6','0.0','0.0','0.0','0.6','0.0','0.0','0.0','0.0','DMCG','0.0','0.0','0.0','0.1','5.0e-4','CJS','5.0e-10','CJSWS','0.0','CJSWGS','1.0','PBS','1.0','PBSWS','PBSWS','PBSWGS','0.5','MJS','0.33','MJSWS','MJSWS','MJSWGS','1.0e-4','JSS','0.0','JSWS','0.0','JSWGS','1.0','NJS','0.1','IJTHSFWD','0.1','IJTHSREV','10.0','BVS','1.0','XJBVS','0.0','JTSS','0.0','JTSSWS','0.0','JTSSWGS','0.0','20.0','NJTS','20.0','NJTSSW','20.0','NJTSSWG','10.0','VTSS','10.0','VTSSWS','10.0','VTSSWGS','12.0','1.0','1.0e-12','50.0','0.0','0.0','0.0','50.0','0.0','0.0','0.0','100.0','0.0','0.0','0.0','100.0','0.0','0.0','0.0','100.0','100.0','100.0','100.0','0.0','0.0','0.0','0.0','0.0','0.0','1.0','4.1e7','6.250e40','3.125e25','8.750e8','0.0','0.0','1.0','1.0','0.577','0.5164','0.395','1.5','3.5','0.0','1','0.0','0.0','27.0','4.73e-4','636.0','0.0','-1.5','0.0','0.0','0.0','0.0','1.0e-3','0.0','0.0','0.0','0.0','0.056e-9','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','-4.775e-3','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','-1.56e-3','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','-0.11','1.0','0.0','0.0','0.0','0.0','0.022','0.0','0.0','0.0','0.0','0.0','0.0','0.0','2.5','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','3.0','XTIS','0.02','XTSS','0.02','XTSSWS','0.02','XTSSWGS','0.0','TNJTS','0.0','TNJTSSW','0.0','TNJTSSWG','0.0','1.0e-5','0.0','1.0e-6','1.0e-6','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','1.0e-6','4.0e2','3.36e8','0.185','0.3','1.4','0','0.490','1.42','20.0','10.0e-9','0.0','0.0','1.0','0.0','1e24','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','1e-9','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.08','0.0','0.0','0.0','-0.07','0.0','0.0','0.0','-0.11','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.022','0.0','0.0','0.0','1.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','2.2','0.53','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','1','1.0e-5','0.0','0.0','0.1','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','1.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','1','0.0','1.0','0','1.0e-8','NOIA','NDEP','1.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','1.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','1.0e-3','0','0','0','0','5.0e16','1.0e5','1.0','NDRIFTD','100.0','0','0','-1','-1','500e-9','LOVER','NDEP','0','1.0','ALPHA0','BETA0','0.0','0','1e-3','1.0','5','0.5',]

with open("out.txt", 'w') as f:
    for line in lines:
        line = line.replace("//", "#")
        if line == '\n':
            pass
        elif re.match("#", line):
            pass
        else:
            paran_1st = line.find("(")
            comma_1st = line.find(",")
            comma_2nd = line.find(",", comma_1st+1)
            par = line[paran_1st+1:comma_1st].strip()
            val = line[comma_1st+1:comma_2nd].strip() 
            #param.append(par)
            value.append(val)
            #if val in param:
            #    f.write(f"self.{par} = self.{val}\n")
            #else:
            #    f.write(f"self.{par} = {val}\n")

    for i in value:
        f.write(f"\'{i}\',")