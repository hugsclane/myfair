# MyFAIR


### Usage Guide
For now the only way you can interact with Myfair is by editing the `main()` function
in `main.py` and running  `python main.py` from your terminal.

I highly recommend reading at least briefly the `myfair_model.py` file, There are a tonne of comments that should answer most of your questions.

Additionally if you would like to explore distributions used to produce the data, calling `python dis_gen.py` will show you either a probabilty frequency function or a probability density function for each distribution.

below is a sutible ways of calling the FAIRModel class

```
   new_model.gen_risk_dist(

        lef_dist = {"dist":"binomial","plef":0.3,"n":30},

        mag_dist = {"dist":"lognormal","mean":1,"sigma":1},

        n_simulations = 1000
   
   )

```
Loss Event Frequency distriubtions can be populated by passing a dictionary in these shapes:

```
	{dist : bernoulli, plef: float < 1}
	{dist : binomial, plef: float < 1, n: int > 0}
	{dist : poisson, lmbda: float > 0, size: int > 0}
```

Loss Event Magnitude distributions can be populated by passing a dictionary in these shapes:

```
	{dist : pert, min: int, mode: int, max: int}
	{dist : lognormal, mean: float, sigma: float}
	{dist : genpareto, c: float}
```

### Progress Map

Below is a map of progress made on MyFAIR with the following features planned.
For now the output is an loss exceedance curve based on the FAIR model.

This was developed as a demo ignoring some scalable best practices, I am aware that there are some shortcomings in not using interfaces but the scale of the project doesn't require them just yet.

### Model Functionality
- [x] LEF
	- [x] TEF
		- [ ] CF
		- [ ] PA
	- [ ] Vuln
		- [ ] TC
		- [ ] RS
- [x] LM
	- [ ] SLEF
	- [ ] SLM
## Usage:
- [ ] CLI 
- [ ] Documentation
- [x] Loss Magnitude Data generation tooling.

### Notes

##### On the data generation tooling.
A data structure and a method is demonstrated in lm_est.py, 
its purpose is to show how data input would be handeled by this tool.

It also the interface through which a data generation tool would be parsed to produce
data defined by real world costs as opposed to a distribution.

This kind of structure could be a solution to interfacing other data points, I.e. vuln, tc, rs ,cf, pa.

At the moment it can only handle modeling a few distributions. 

They are as follows:

##### Loss Event Frequency:
- Bernouli
- Binomial
- Poisson

#### Loss Magnitude Distribution
- PERT
- Log-normal
- Generalised-Pareto

