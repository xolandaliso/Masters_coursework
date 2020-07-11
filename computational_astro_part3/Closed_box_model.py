import numpy as np
import pylab as pl
import astropy.units as u

Mg_0 = 5.0e+9
Mst_0 = 0.
Zg_0 = 0
Mzg_0 = Zg_0*Mg_0   #from Zg = Mzg/Mg
Zst_0 = 0           #initially stars have zero metals
Mzst_0 = Zst_0*(-Mg_0)  #from Zst = Mzst/Mst


def C_box_model(Mg_0, Mzg_0, Zg_0, Mzst_0, Mst_0):
    
	psi, R, h, yz = 1.0, .43, 20e+6, .03   #h is dt
	t = []
	Mgas, Mzg, Zg, Mzst = [], [], [], [[] for _ in range(2)] 
	Mst = [[] for _ in range(2)] 

	for i in np.arange(0., 10e9 + 20e+6, 20e+6):
		if Mg_0 >= 0.:

			t.append(i/1e+9)
			Mg_0 += -(1 - R)*psi*h             #gas mass calculation using Euler
			Mgas.append(Mg_0)

			M_st = (1 - R)*psi*h                 #stellar mass at each time step
			Mst[1].append(M_st)

			Mst_0 += M_st                        #total stellar mass after each time step
			Mst[0].append(Mst_0)

			Mzg_0 += (-Zg_0*psi + yz*psi)*h      #mass of gas-phase metals
			Mzg.append(Mzg_0)

			Mzst_sp = (1 - R)*Zg_0*psi*h
			Mzst[1].append(Mzst_sp)        

			Mzst_0 += Mzst_sp          #stellar metallicity
			Mzst[0].append(Mzst_0)

			Zg_0 = Mzg_0/Mg_0                      #gas metallicity parameter
			Zg.append(Zg_0)

		else:
			break

	return Mgas, Mst, Zg, Mzg, Mzst, t
