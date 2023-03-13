import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import minimize_scalar

#Loading data
data_exp = np.load('I_q_IPA_exp.npy')
data_mod = np.load('I_q_IPA_model.npy')

#defining necessary objects
fig, ax = plt.subplots()

#interpolating the model set
func_mod = interp1d(data_mod[:,0], data_mod[:,1])
data_mod_interpol = func_mod(data_exp[:,0])

def function(scale):
	return np.nansum((data_exp[:,1] - scale*data_mod_interpol)**2)

#Finding the scaling factor
factor = minimize_scalar(function)
print(factor)
data_mod_scaled = data_mod_interpol*(factor.x)
print(factor.x)

ax.scatter(data_exp[:,0], data_exp[:,1], c='green', marker='^')
ax.scatter(data_exp[:,0], data_mod_scaled, c='red', marker='*')

plt.show()
