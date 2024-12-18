import argparse
import myfair_model as mf
from config import Config

# parser = argparse.ArgumentParser(description="MyFair CLI")
#   cli goes here


## this global definition is very temporary and will be replaced by the CLI
__seed__ = 42
__rvs_size__ = 1000


#We will now call config."variable" to access the variables
config = Config(
    __seed__,
    __rvs_size__
    )


## -----------------------
#   incident_loss kwargs should be passed in as  the following shape
#   time_period is in unit times "years"
#   incident_loss kwargs = {
#       "productivity_loss": {
#           "time_period": 1, 
#           "revenue_loss": 0,
#           "wages_loss": 0
#       },
#       "fine_judgement": {
#           "fines": 0,
#           "class_actions": 0,
#           "bail": 0,
#           "legal_fees": 0
#       },
#       "response_loss": {
#           "marketsshare_loss": 0,
#           "lower_sales_growth": 0,
#           "stock_price_losses": 0,
#           "increased_cost_of_capital": 0
#       },
#       "competitive_loss": {
#           "ip_loss": 0,
#           "trade_secret_loss": 0,
#           "merger_acquisition_data": 0,
#           "market_data": 0
#       },
#       "response_loss": {
#           "incident_response_cost": 0,
#           "forensic_analysis_cost": 0,
#           "management_cost": 0,
#           "customer_notification": 0,
#           "credit_monitoring": 0
#       }
#   }
#   all value are non-negative integers in dollar ammounts other than time_period


if __name__ == "__main__":
    from config import Config
    mf.risk_calculator(
        lef_dist = {"dist":"binomial","plef":0.3,"n":30},
        mag_dist = {"dist":"lognormal","mean":1,"sigma":1},
        n_simulations = 1000)
    
    pass