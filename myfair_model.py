# The intial structure planned was to create an appropriate 
# distribution for each node on the risk tree. 
# Then to corretly sum them up

from dis_gen import bernoulli_dist, binomial_dist, poisson_dist, pert_dist , lognormal_dist, genpareto_dist
import random
import seaborn as sns
import matplotlib.pyplot as plt

def risk_calculator(**kwargs):
    ## -----------------------
    # Create distributions for Loss Event Frequency (LEF) and Magnitude (MAG)
    # ------------------------
    # first we check which kwargs are provided and then we generate the appropriate distribution
    if kwargs.get("lef_decomposed") == True:
        #NOTE: here that if lef_decomposed is not in kwargs, this will assert false.
        lef_dist,gen_mag_dist = lef_from_tef_vuln(),gen_mag_dist(kwargs.get("mag_dist"))

    else:
        lef_dist,mag_dist = gen_lef_dist(kwargs.get("lef_dist")),gen_mag_dist(kwargs.get("mag_dist"))
    risk_dist = monte_carlo_sim(lef_dist,mag_dist,kwargs.get("n_simulations"))

    sns.set(style="whitegrid")
    risk_sorted = sorted(risk_dist, reverse=True)
    exceedance_prob = [(i + 1) / len(risk_sorted) for i in range(len(risk_sorted))]
    sns.lineplot(x=risk_sorted, y=exceedance_prob)
    plt.xlabel('Loss')
    plt.ylabel('Exceedance Probability')
    plt.title('Loss Exceedance Curve')
    plt.show()

def monte_carlo_sim(lef_dist,mag_dist,n_simulations):
    risk = list()
    for i in range(n_simulations):
        random_event,random_mag = random.choice(lef_dist),random.choice(mag_dist)
        risk_instance = random_event*random_mag
        risk.append(risk_instance)
    return risk

def gen_tef_dist(dist_dict):
    ## -----------------------
    # lef_from_tef_vuln has the following shape
    # for TEF happens N times,
    # {dist : linear , N: int}
    # for a specific number of n opputunities of TE to occur with p of actually occuring
    # {dist : binomial, ptef: float < 1, n: int > 0}
    # event threat over average unit t time
    # {dist : poisson, lmbda: float > 0, size: int > 0}
    ## -----------------------
    if dist_dict == None:
        raise ValueError("No distribution provided, Check your input or kwargs")
    dist = dist_dict.get("dist")
    if dist == "linear":
        ## bugger, the __size__ needs to be globally accesible here. Time to make the classes.
        return [1]*dist_dict.get("N")
    elif dist == "binomial":
        return binomial_dist(dist_dict.get("ptef"),dist_dict.get("n"))
    elif dist == "poisson":
        return poisson_dist(dist_dict.get("lmbda"),dist_dict.get("size"))
    else:
        raise ValueError("Invalid distribution type")

def gen_mag_dist(dist_dict):
    ## -----------------------
    # gen_mag_dist has the following shape
    # {dist : pert, min: int, mode: int, max: int}
    # {dist : lognormal, mean: float, sigma: float}
    # {dist : genpareto, c: float}
    ## -----------------------
    if dist_dict == None:
        raise ValueError("No distribution provided, Check your input or kwargs")
    dist = dist_dict.get("dist")
    if dist == "pert":
        return pert_dist(dist_dict.get("min"), dist_dict.get("mode"), dist_dict.get("max"))
    elif dist == "lognormal":
        return lognormal_dist(dist_dict.get("mean"), dist_dict.get("sigma"))
    elif dist == "genpareto":
        return genpareto_dist(dist_dict.get("c"))
    else: 
        raise ValueError("Invalid distribution type")

def gen_tef_dist(dist_dict):
    
    pass


def gen_lef_dist(dist_dict):

    ## -----------------------
    #   lef_dist has the following shape
    #       {dist : bernoulli, plef: float < 1}
    #       {dist : binomial, plef: float < 1, n: int > 0}
    #       {dist : poisson, lmbda: float > 0, size: int > 0}
    ## -----------------------
    if dist_dict == None:
        raise ValueError("No distribution provided, Check your input or kwargs")
    dist = dist_dict.get("dist")
    if dist == "bernoulli":
        return bernoulli_dist(dist_dict.get("plef"))
    elif dist == "binomial":
        return binomial_dist(dist_dict.get("plef"), dist_dict.get("n"))
    elif dist == "poisson":
        return poisson_dist(dist_dict.get("lmbda"), dist_dict.get("size"))
    else: 
        raise ValueError("Invalid distribution type")

if __name__ == "__main__":
    ## -----------------------
    # This will output a loss exceedance curve
    # ------------------------
    # risk_calculator(
    #     lef_dist = {"dist":"binomial","plef":0.3,"n":30},
    #     mag_dist = {"dist":"lognormal","mean":1,"sigma":1},
    #     n_simulations = 1000)
    
    # risk_calculator( 
    #     lef_dist = {"dist":"poisson","lmbda":3,"size":20},
    #     mag_dist = {"dist":"pert","min":100,"mode":25_000,"max":1_000_000},
    #     n_simulations = 1000)


    ## -----------------------
    # risk_calculator(
    #     lef_dist = {"dist":"bernoulli","plef":0.3},
    #     mag_dist = {"dist":"pert","min":100,"mode":25_000,"max":1_000_000},
    #     n_simulations = 1000)
    pass