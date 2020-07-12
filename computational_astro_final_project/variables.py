import numpy as np

#initial_vars
Mg_0 = 5e+10
Zg_0 = 0.05
Mst_0 = 0.
Zs_0 = 0.
dt = 20e+6
#B_box_params
Z_sun = 0.0134
R = 0.43
M_crit = 2.5e+9
t_dyn = 1.5e+8
yz_prime = 0.02
alpha_sf = 0.05
alpha = 0.6

##for DM halo mass
N = 0.0351
M1 = 10**11.59
y = 0.608
b = 1.376     

###merging

alpha_bst = 0.56
beta_bst = 0.70
f_bh = 0.03
v_bh = 300
vir = 150 


####Observational MW properties
Mg_obs, SFR_obs, Zg_obs, Ms_obs, Zs_obs = 7e+9, 1.52, 1.26, 5.0e+10, 1.07	
fb_obs, fg_s_obs = 0.07, 0.12
###Observational Errors
SFR_err = 0.18
Ms_err = 1.0e+10
Zs_err = 0.40
f_b_err, fg_s_err = 0.01, 0.18
Mg_err, Zg_err = np.ones((2, 1)), np.ones((2, 1))


Mg_err[0], Mg_err[1] = (5e+9)*Mg_err[0], (10e+9)*Mg_err[1]    ##gas mass error
Zg_err[0], Zg_err[1] = 0.37*Zg_err[0], 0.74*Zg_err[1]   ##Zg error


