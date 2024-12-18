

from scipy.stats import bernoulli, binom, poisson , genpareto
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns


#Someone implemented a Beta-PERT distribution in python with almost identical
#tooling to scipy. Sadly its 4 years old and not maintained so it is not viable
#outside of demos
from pert import PERT

## I havent done curve fitting over the distrubtions to demonstrate
## what contiunous data would look like, It does make the pmf look better.
# from scipy.optimize import curve_fit


__seed__ = 42
__rvs_size__ = 10000


#---------------------------------------
# Loss Event Frequency (LEF) Distributions
#---------------------------------------


def bernoulli_dist(p,show_stats=False):

#Applicable if loss event only occurs once over the time horizon
#Bernoulli distribution follows Probabilty loss event frequency

    # There are many more efficient ways to genereate
    # identically distriubted random variables, the use of scipy
    # is to demonstrate methodolgy
    bernoulli_data = bernoulli(p)
    if show_stats:
        #From the scipy documentation, used to check if distribution is correct (eye balling)
        mean, var, skew, kurt = bernoulli_data.stats(moments='mvsk')
        print("Bernoulli Distribution Stats:")
        print("Mean: " + str(mean) + "\nVariance: " + str(var) + "\nSkewness: " + str(skew) + "\nKurtosis: " + str(kurt) + "\n")
        x = np.arange(bernoulli_data.ppf(0.01), bernoulli_data.ppf(0.99))
        fig, ax = plt.subplots(1, 1)
        ax.plot(x, bernoulli_data.pmf(x), 'bo', ms=8, label='bernoulli pmf')
        ax.vlines(x, 0, bernoulli_data.pmf(x), colors='b', lw=5, alpha=0.5)
        rv = bernoulli(p)
        ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
            label='frozen pmf')
        ax.legend(loc='best', frameon=False)
        plt.show()

    return bernoulli_data.rvs(size=__rvs_size__,random_state=__seed__)



# #-----------------------

#loss event occurs finite number of times, each opportunity has 
#the probability 
#binomial distribution follows the Probabilty loss event frequency
# and the number of loss opportunities.


def binomial_dist(p,n,show_stats=False):
    binomial_data = binom(n=n, p=p)
    if show_stats: 
        #From the scipy documentation, used to check if distribution is correct (eye balling)
        mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
        print("Binomial Distribution Stats:")
        print("Mean: " + str(mean) + "\nVariance: " + str(var) + "\nSkewness: " + str(skew) + "\nKurtosis: " + str(kurt) + "\n")
        fig, ax = plt.subplots(1, 1)
        x = np.arange(binomial_data.ppf(0.01), binomial_data.ppf(0.99))
        ax.plot(x, binomial_data.pmf(x), 'bo', ms=8, label='binom pmf')
        ax.vlines(x, 0, binomial_data.pmf(x), colors='b', lw=5, alpha=0.5)
        ax.vlines(x, 0, binomial_data.pmf(x), colors='k', linestyles='-', lw=1,
                label='frozen pmf')
        ax.legend(loc='best', frameon=False)
        plt.show()
    return binomial_data.rvs(size=__rvs_size__, random_state=__seed__)


#-----------------------
#loss event occurs and independent of the 
#number of throughout the timeperiod

#poisson distribution follows the the
#expected number of loss events over the time horizion t 
#so lambda is in the form of events per events per unit time.
def poisson_dist(lmbda,show_stats=False):
    poisson_data = poisson(lmbda)
    if show_stats:
        sns.kdeplot(poisson_data.rvs(__rvs_size__), fill=True)
        plt.title('Probabilty Mass Distribution')
        plt.xlabel('Loss Event Frequency')
        plt.ylabel('Density')
        plt.show()
        mean, var, skew, kurt = poisson.stats(lmbda, moments='mvsk')
        print("Poisson Distribution Stats:")
        print("Mean: " + str(mean) + "\nVariance: " + str(var) + "\nSkewness: " + str(skew) + "\nKurtosis: " + str(kurt) + "\n")
        #From the scipy documentation, used to check if distribution is correct (eye balling)
        # x = np.arange(poisson_data.ppf(0.01), poisson_data.ppf(0.99))
        # fig, ax = plt.subplots(1, 1)
        # ax.plot(x, poisson_data.pmf(x), 'bo', ms=8, label='poisson pmf')
        # ax.vlines(x, 0, poisson_data.pmf(x), colors='b', lw=5, alpha=0.5)
        # ax.vlines(x, 0, poisson_data.pmf(x), colors='k', linestyles='-', lw=1,
        #         label='frozen pmf')
        # ax.legend(loc='best', frameon=False)
        # plt.show()
    return poisson_data.rvs(size=__rvs_size__, random_state=__seed__)


#---------------------------------------
# Loss Magnitude (LM) distributions
#---------------------------------------

def pert_dist(min,mode,max,show_stats=False):
    #PERT distribution is used to model loss magnitude
    pert_data = PERT(min,mode,max)
    if show_stats:
        sns.kdeplot(pert_data.rvs(__rvs_size__,__seed__), fill=True)
        plt.title('Loss Magnitude Distribution')
        plt.xlabel('Loss Magnitude')
        plt.ylabel('Density')
        plt.show()
    return pert_data.rvs(__rvs_size__)

def lognormal_dist(mean,sigma,show_stats=False):
    #Lognormal distribution is used to model loss magnitude
    lognormal_data = np.random.lognormal(mean,sigma,__rvs_size__)
    if show_stats:
        sns.kdeplot(lognormal_data, fill=True)
        plt.title('Loss Magnitude Distribution')
        plt.xlabel('Loss Magnitude')
        plt.ylabel('Density')
        plt.show()
    return lognormal_data

def genpareto_dist(c,show_stats=False):
    #not fully implemented yet
    genpareto_data = genpareto(c)
    if show_stats:
        genpareto_samples = genpareto_data.rvs(__rvs_size__, random_state=__seed__)
        sns.kdeplot(genpareto_samples, fill=True)
        plt.title('Loss Magnitude Distribution')
        plt.xlabel('Loss Magnitude')
        plt.ylabel('Density')
        plt.show()
    return genpareto_data.rvs(__rvs_size__,random_state=__seed__)



if __name__ == "__main__":

    ber_p = 0.2
    bernoulli_dist(ber_p,show_stats=True)
    

    bi_p = 0.4
    n_loss_events = 20
    binomial_dist(bi_p,n_loss_events,show_stats=True)
    
    lmbda = 3
    poisson_dist(lmbda,20,show_stats=True)

    min = 10
    mode = 30
    max = 200

    pert_dist(min,mode,max,show_stats=True)
    
    mu = 0
    sigma = 1
    lognormal_dist(mu,sigma,show_stats=True)

    c = 0.1
    genpareto_dist(c,show_stats=True)
    pass