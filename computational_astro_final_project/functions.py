import numpy as np
import variables as v  #importing the scripts with initial conditions

def SFR(Mg):

	return (v.alpha_sf*(Mg - v.M_crit))/v.t_dyn

def beta(SFR):                     #a function that calculates the infall rate i.e beta

	return (1 - v.R)*SFR

def Z_inf(Z):                          #a function that calculates the infall metallicity for each Zg

	return 0.25*Z

def M_halo(Mst, M_h):                                             #a function to approximate the value of Mhalo usinng Bisection method

    diff = Mst - 2*v.N*M_h*((M_h/v.M1)**(-v.b) + (M_h/v.M1)**v.y)**(-1)        #Mst - 2*N*Mhalo(......) = 0
                                                                   #if diff == 0 then M_h will be found
    return diff

def prior(x, mean, sig):                              #function to calculate the prior
    
    chi_sq = (((x - mean)**2)/sig**2)
    return (1/np.sqrt(2*np.pi)*sig)*np.exp(-chi_sq/2)

def Likelihood(data, model, sig):                     #function to calculate the Likehood (takes the same form as the prior)
    
    chi_sq = ((data - model)**2)/sig**2
    return (1/np.sqrt(2*np.pi)*sig)*np.exp(-chi_sq/2)

dt = v.dt

def B_box_model(Mg_0, Mzg_0, Mst_0, Mzst_0, Zg_0):                 #function that model the evolution of the galaxy (i.e Breathing box model)
    t, SFR_lst = [], []
    Mg, Mzg, Zg, Zst, Mzst = [], [], [], [], [] 
    Mst = [[] for _ in range(2)] 
        
    for i in np.arange(0., 13.25e+9, 20e+6):

        if Mg_0 >= 0.:

            t.append(i/1e+9)                   #keeping track of time in Gyr
            SFR_lst.append(SFR(Mg_0))
            Mg_0 += (-SFR(Mg_0) + v.R)*dt

            Mzg_0 += (-Zg_0*SFR(Mg_0) + v.yz_prime*SFR(Mg_0))*dt

            Mst_sp = (SFR(Mg_0) - v.R*SFR(Mg_0))*dt
            Mst[1].append(Mst_sp)                         #Mst[1] stores the stellar mass of each SP

            Mst_0 += Mst_sp
            Mst[0].append(Mst_0)                         #Mst[0] stores total stellar mass at each time step

            Mzst_sp = (Zg_0*SFR(Mg_0) - Zg_0*v.R*SFR(Mg_0))*dt
            Mzst_0 += Mzst_sp
            Mzst.append(Mzst_0)

            Zs = Mzst_0/Mst_0
            Zst.append(Zs)

            Zg_0 = Mzg_0/Mg_0                            #this is equal to Zst_sp.
            Zg.append(Zg_0)

            Mg_0 += -v.alpha*SFR(Mg_0)*dt               #outflow of gass from the box

            Mzg_0 += -v.alpha*Zg_0*SFR(Mg_0)*dt

            Mg_0 += beta(SFR(Mg_0))*dt
            Mg.append(Mg_0)

            Mzg_0 += beta(SFR(Mg_0))*Z_inf(Zg_0)*dt
            Mzg.append(Mzg_0)

        else:                                         #once the gas mass runs out, the simulation stops.
            break

    return t, SFR_lst, Mg, Zg, Mst, Zst, Mzg, Mzst   


