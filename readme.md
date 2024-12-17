# MyFAIR
Below is a map of progress made on MyFAIR with the following features planned.
For now the output is an loss exceedance curve based on the FAIR model.

### Usage Guide
For now the only way you can interact with Myfair is by editing the `main()` function
in `myfair_model.py` and running  `python myfair_model.py` from your terminal.

See notes in `main()`

Additionally if you would like to explore distributions used to produce the data, calling `python dis_gen.py` will show you either a probabilty frequency function or a probability density function for each distribution.

### Model Functionality
- [x] LEF
	- [ ] TEF
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
- [x] Loss Magnitude Data generation tooling
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

