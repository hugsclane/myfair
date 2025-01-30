

### TODO: HUGO - make the Model class, have it handle config correctly, and have it handle the kwargs from json and the CLI handled correclty.
# actual tears

from dis_gen import bernoulli_dist, binomial_dist, poisson_dist, pert_dist , lognormal_dist, genpareto_dist
import random
import seaborn as sns
import matplotlib.pyplot as plt
import math

class FAIRModel:

    def __init__(self):
        mag_dist = None
        lef_dist = None
        tef_dist = None
        risk_dist = None
        vuln = None

    ## -----------------------
    #  Visualization
    ## -----------------------

    def show_exceedance_curve(self):
        if self.risk_dist == None:
            raise ValueError("No risk distribution provided, Try running gen_risk_dist first")

        sns.set(style="whitegrid")
        # Sort the risk values in descending order
        risk_sorted = sorted(self.risk_dist, reverse=True)

        # Calculate the exceedance probability for each risk value
        exceedance_prob = [(i + 1) / len(risk_sorted) for i in range(len(risk_sorted))]

        # Plotting the Loss Exceedance Curve
        sns.lineplot(x=risk_sorted, y=exceedance_prob)
        plt.xlabel('Loss')
        plt.ylabel('Exceedance Probability')
        plt.title('Loss Exceedance Curve')
        plt.show()

    ## -----------------------
    # Distribution generation
    ## -----------------------
    def gen_risk_dist(self,**kwargs):
        ## -----------------------
        # Create distributions for Loss Event Frequency (LEF) and Magnitude (MAG)
        ## -----------------------
        # first we check which kwargs are provided and then we generate the appropriate distribution

        if kwargs.get("lef_decomposed") == True:
            #TODO: implement the lef_from_tef_vuln function
            #NOTE: here that if lef_decomposed is not in kwargs, this will assert false.
            self.lef_dist = self.lef_from_tef_vuln(kwargs.get("tef_dist"),kwargs.get("vuln"))
            self.mag_dist = self.gen_mag_dist(kwargs.get("mag_dist"))

        ## -----------------------
        # If the lef is not decomposed we will generate the lef and mag distributions
        ## -----------------------

        else:
            self.lef_dist = self.gen_lef_dist(kwargs.get("lef_dist"))
            self.mag_dist = self.gen_mag_dist(kwargs.get("mag_dist"))

        self.risk_dist = self.monte_carlo_sim(self.lef_dist,self.mag_dist,kwargs.get("n_simulations"))
        return self.risk_dist


    def gen_tef_dist(self,dist_dict):

        ## -----------------------
        # dict_dist has the following shape
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
            ## For my sanity,
            # this is just an integer because this is the specific number of
            # times a threat even will occur over the time period
            # it make total sense to return an integer here, stop worrying about it.
            return dist_dict.get("N")

        elif dist == "binomial":
            return binomial_dist(dist_dict.get("ptef"),dist_dict.get("n"))

        elif dist == "poisson":
            return poisson_dist(dist_dict.get("lmbda"))

        else:
            raise ValueError("Invalid distribution type")

    def gen_mag_dist(self,dist_dict):
        # # -----------------------
        # dict_dist has the following shape
        # {dist : pert, min: int, mode: int, max: int}
        # {dist : lognormal, mean: float, sigma: float}
        # {dist : genpareto, c: float}
        # # -----------------------

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

    def gen_lef_dist(self,dist_dict):
        ## -----------------------
        #   dist_dict has the following shape
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


    ## -----------------------
    #  Helper functions
    ## -----------------------

    def monte_carlo_sim(self,lef_dist,mag_dist,n_simulations):
        risk = list()

        for i in range(n_simulations):
            random_event,random_mag = random.choice(lef_dist),random.choice(mag_dist)
            risk_instance = random_event*random_mag
            risk.append(risk_instance)

        return risk

    def lef_from_tef_vuln(self,tef_dist,vuln):
        #:TODO: implement this function
        # Guide on page 22 of the FAIR book
        # 3.1.1.1 Decomposing Loss Event Frequency, Table 1: Mapping Threat Event Frequency (TEF) to Loss Event Frequency (LEF)

        return

    def vulnerability(self, tcap,rs):
    ## Monte Carlo Method allows us to use code existing in the dis_gen.py file
    ## the integration method is a more relibale way to prdouce the vulnerability feature.


    ##-----------------------
    # integration method
    ##-----------------------
    #  is the probabilty that TCap is greater than resitance
    #  tcap is the threat capability
    #  rs is the resistance
    #  our equation is either
    # the definite integral of xmin to xmax for f_Tcap(x) * F_RS(x) dx
    # where
    # tcap has a probailty density of f_Tcap(x)
    # and resistance has a cumulitve distribution of F_RS(x)
    # xmin = max(min(f_Tcap),min(F_RS))
    # xmax = min(max(f_Tcap),max(F_RS))
    # divide the integration range into n intervals
    # with a width of \delta
    # where \delta*n = xmax - xmin
    ##-o-o-o-o-o-o-o-o-o-o-o-
    # input: f_tcap, F_rs
    # output: float
    ##-----------------------

    ##-----------------------
    # monte carlo method
    ##-----------------------
        threat_success = 0
        threat_fail = 0
        for i in range(k):
            if random(tcap)> random(rs):
                threat_success += 1
            else:
                threat_fail += 1
        return threat_success/(threat_success + threat_fail)
    ##-o-o-o-o-o-o-o-o-o-o-o-
    # input: t_cap_dist, rs_dist
    # output: float
    ##-----------------------

    #placeholder
        return 0.2


if __name__ == "__main__":

    new_model = FAIRModel()
    new_model.gen_risk_dist(
        lef_dist = {"dist":"binomial","plef":0.3,"n":30},
        mag_dist = {"dist":"lognormal","mean":1,"sigma":1},
        n_simulations = 1000)
    new_model.show_exceedance_curve()
    #print(new_model.vulnerability(0.5,[0.1,0.2,0.3,0.4,0.5]))


    #u risk_calculator(
    #     lef_dist = {"dist":"binomial","plef":0.3,"n":30},
    #     mag_dist = {"dist":"lognormal","mean":1,"sigma":1},
    #     n_simulations = 1000)

    # risk_calculator(
    #     lef_dist = {"dist":"poisson","lmbda":3,"size":20},
    #     mag_dist = {"dist":"pert","min":100,"mode":25_000,"max":1_000_000},
    #     n_simulations = 1000)


    # # -----------------------
    # risk_calculator(
    #     lef_dist = {"dist":"bernoulli","plef":0.3},
    #     mag_dist = {"dist":"pert","min":100,"mode":25_000,"max":1_000_000},
    #     n_simulations = 1000)
    pass
