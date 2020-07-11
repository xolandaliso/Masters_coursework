import numpy as np
import pylab as pl
import Closed_box_model as cbm
import Leaky_box_model as lbm
import Accreting_box_model as abm
import variables as vr


#Closed-box model
Mgas_cbm = cbm.C_box_model(vr.Mg_0, vr.Mzg_0, vr.Zg_0, vr.Mzst_0, vr.Mst_0)[0]        #reading gas mass
Ms_cbm = cbm.C_box_model(vr.Mg_0, vr.Mzg_0, vr.Zg_0, vr.Mzst_0, vr.Mst_0)[1]          #reading stellar mass i.e both total and each SP
Zg_cbm = cbm.C_box_model(vr.Mg_0, vr.Mzg_0, vr.Zg_0, vr.Mzst_0, vr.Mst_0)[2]          #reading gas metallicity
Mzs_cbm = cbm.C_box_model(vr.Mg_0, vr.Mzg_0, vr.Zg_0, vr.Mzst_0, vr.Mst_0)[4]          #Mzs
t_cbm = cbm.C_box_model(vr.Mg_0, vr.Mzg_0, vr.Zg_0, vr.Mzst_0, vr.Mst_0)[5]
sfr_cbm = np.ones(len(t_cbm))
Zs_cbm = Zg_cbm                                          #reading stellar metallicity as: Zs = Mzs/Ms

#Leaky-box model
Mgas_lbm = lbm.L_box_model(vr.Mg_0, vr.Mzg_0, vr.Zg_0, vr.Mzst_0, vr.Mst_0)[0]
Ms_lbm = lbm.L_box_model(vr.Mg_0, vr.Mzg_0, vr.Zg_0, vr.Mzst_0, vr.Mst_0)[1]
Zg_lbm = lbm.L_box_model(vr.Mg_0, vr.Mzg_0, vr.Zg_0, vr.Mzst_0, vr.Mst_0)[2]
Mzs_lbm = lbm.L_box_model(vr.Mg_0, vr.Mzg_0, vr.Zg_0, vr.Mzst_0, vr.Mst_0)[0][4]
t_lbm = lbm.L_box_model(vr.Mg_0, vr.Mzg_0, vr.Zg_0, vr.Mzst_0, vr.Mst_0)[5]
sfr_lbm = np.ones(len(t_lbm))
Zs_lbm = Zg_lbm

#Accreting-box model
Mgas_abm = abm.A_box_model(vr.Mg_0, vr.Mzg_0, vr.Zg_0, vr.Mzst_0, vr.Mst_0)[0]
Ms_abm = abm.A_box_model(vr.Mg_0, vr.Mzg_0, vr.Zg_0, vr.Mzst_0, vr.Mst_0)[1]
Zg_abm = abm.A_box_model(vr.Mg_0, vr.Mzg_0, vr.Zg_0, vr.Mzst_0, vr.Mst_0)[2]
Mzs_abm = abm.A_box_model(vr.Mg_0, vr.Mzg_0, vr.Zg_0, vr.Mzst_0, vr.Mst_0)[4]
t_abm = abm.A_box_model(vr.Mg_0, vr.Mzg_0, vr.Zg_0, vr.Mzst_0, vr.Mst_0)[5]
sfr_abm = np.ones(len(t_abm))
Zs_abm = Zg_abm
