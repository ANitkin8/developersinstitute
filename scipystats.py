#exercise 1
import scipy
print(scipy.__version__)

#exercise 2
import scipy.stats as stats
import numpy as np
data = [12, 15, 13, 12, 18, 20, 22, 21]
mean_data = stats.tmean(data)
median_data =np.median(data) #scipy doesnt have a median function
variance_data = stats.tvar(data)
std_dev_data = stats.tstd(data)

#exercise 3
import matplotlib.pyplot as plt
from scipy.stats import norm

dist = np.random.normal(loc=50 ,scale=10, size=1000)
plt.hist(dist, bins=30)
plt.title('Normal Distribution Mean=50 std=10')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

#exercise 4
from scipy.stats import ttest_ind
data1 = np.random.normal(50, 10, 100)
data2 = np.random.normal(60, 10, 100)
#calculate the means
mean_data1 = stats.tmean(data1)
mean_data2 = stats.tmean(data2)
#calculate stand deviations
std_data1 = stats.tstd(data1)
std_data2 = stats.tstd(data2)
#peform the T-test
t_stat, p_val = ttest_ind(data1, data2)

#exercise 5
house_sizes = [50, 70, 80, 100, 120]
house_prices = [150000, 200000, 210000, 250000, 280000]
# Performing linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(house_sizes, house_prices)
print(f"slope is {slope}, intercept is {intercept}")
ninetysqm_house = 90*slope + intercept
#the data shows the price increases about 1829 USD per sqm

#exercise 6
fertilizer_1 = [5, 6, 7, 6, 5]
fertilizer_2 = [7, 8, 7, 9, 8]
fertilizer_3 = [4, 5, 4, 3, 4]
# Performing one-way ANOVA
f_value, p_value = stats.f_oneway(fertilizer_1, fertilizer_2, fertilizer_3)
print("F-value:", f_value)
print("P-value:", p_value)
#these fertilizers have significantly different effects, and based on the p-value its very rare to find so much variation
#if the p-value was greater than 0.05, the variation would be considered less significant


