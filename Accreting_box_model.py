import numpy as np
import pylab as pl
import astropy.units as u
import variables as vr

Mg_0 = 5.0e+9
Mst_0 = 0.
Zg_0 = 0
Mzg_0 = Zg_0*Mg_0   #from Zg = Mzg/Mg
Zst_0 = 0           #initially stars have zero metals
Mzst_0 = Zst_0*(-Mg_0)  #from Zst = Mzst/Mst

def A_box_model(Mg_0, Mzg_0, Zg_0, Mzst_0, Mst_0):
    
	psi, R, h, yz, alpha, Z_i = 1., .43, 20e+6, .03, .8, 0.0
	beta = (1 - R)*psi
	t = []   
	Mgas, Mzg, Zg, Mzst = [], [], [], [[] for _ in range(2)]
	Mst = [[] for _ in range(2)]

	for i in np.arange(0., 10e9 + 20e+6, 20e+6):
		
		if Mg_0 >= 0.:

			t.append(i/1e+9)
			Mg_0 += (-psi + R*psi + beta)*h
			Mgas.append(Mg_0)

			Mzg_0 += (-Zg_0*psi + yz*psi + Z_i*beta)*h
			Mzg.append(Mzg_0)

			Mst_sp = (psi - R*psi)*h
			Mst[1].append(Mst_sp)

			Mst_0 += Mst_sp
			Mst[0].append(Mst_0)

			Mzst_sp = (1 - R)*Zg_0*psi*h
			Mzst[1].append(Mzst_sp)

			Mzst_0 += Mzst_sp
			Mzst[0].append(Mzst_0)
			  
			Zg_0 = Mzg_0/Mg_0
			Zg.append(Zg_0)
		else:
			break

	return Mgas, Mst, Zg, Mzg, Mzst, t
