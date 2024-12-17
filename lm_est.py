import numpy as np

def incident_loss(**kwargs):
    ## -----------------------
    # this is a helper function that can handle some json input from kwargs and process it into a loss event
    # can be used to generate a handful of loss events.

    ## -----------------------
    #   incident loss returns a tuple structured as follows
    #   (total_loss,primary_loss,secondary_loss)
    ## -----------------------


    #productivty_loss kwargs
    time_period = kwargs.get('time_period', 1)
    revenue_loss = kwargs.get('revenue_loss', 0)
    wages_loss = kwargs.get('wages_loss', 0)
    
    ##---------------------------------------
    #fine_judgement kwargs
    fines = kwargs.get('fines', 0)
    class_actions = kwargs.get('class_actions', 0)
    bail = kwargs.get('Bail', 0)
    legal_fees = kwargs.get('legal_fees', 0)
    
    ##---------------------------------------
    #response_loss kwargs
    marketsshare_loss = kwargs.get('marketsshare_loss', 0)
    lower_sales_growth = kwargs.get('lower_sales_growth', 0)
    stock_price_losses = kwargs.get('stock_price_losses', 0)
    increased_cost_of_capital = kwargs.get('increased_cost_of_capital', 0)

    ##---------------------------------------
    #competitive_loss kwargs
    ip_loss = kwargs.get('ip_loss', 0)
    trade_secret_loss = kwargs.get('trade_secret_loss', 0)
    merger_acquisition_data = kwargs.get('merger_acquisition_data', 0)
    market_data = kwargs.get('market_data', 0)

    ##---------------------------------------
    #response_loss kwargs
    incident_response_cost = kwargs.get('incident_response_cost', 0)
    forensic_analysis_cost = kwargs.get('forensic_analysis_cost', 0)
    management_cost = kwargs.get('management_cost', 0)
    customer_notification = kwargs.get('customer_notification', 0)
    credit_monitoring = kwargs.get('credit_monitoring', 0)
    

    primary_losses = (
        productivity_loss(time_period,revenue_loss,wages_loss) +
        response_loss(incident_response_cost, forensic_analysis_cost , management_cost , customer_notification , credit_monitoring)[0]
    )

    ## see fines and judgment for an idea of how seconday loss event frequency is calculated
    secondary_losses = (
        response_loss(incident_response_cost, forensic_analysis_cost, management_cost, customer_notification, credit_monitoring)[1] +
        competitive_loss(ip_loss, trade_secret_loss, merger_acquisition_data, market_data) +
        reputation(marketsshare_loss, lower_sales_growth, stock_price_losses, increased_cost_of_capital) +
        fines_and_judgements(fines, class_actions, bail, legal_fees)
    ) 

    return (primary_losses + secondary_losses, primary_losses, secondary_losses)

#---------------------------------------
# Secondary Loss Contributions

def fines_and_judgements(fines, class_actions, Bail, legal_fees):
    rand = np.random.randint(0,100)
    ## I'm using mod numbers to simulate randomness, its just for fun, any random distribution can be used
    ## additionally seconday loss frequency should be its own distribution function, 
    ## but that is outside of the scope of this demo

    if rand % 50 != 0:
        class_actions = class_actions * 0
    if rand % 5 == 0:
        fines = fines * 1.5
    else:
        fines = fines * 0.5
    if rand != 0:
        Bail = 0 
    if rand > 50 :
        fines, class_actions, legal_fees = 0, 0, 0
    #fines and judgements are calculated in dollars
    return fines + Bail + class_actions + legal_fees

def reputation(marketsshare_loss, lower_sales_growth, stock_price_losses, increased_cost_of_capital):
    #reputation loss is calculated in dollars
   
    loss = marketsshare_loss + lower_sales_growth + stock_price_losses + increased_cost_of_capital
    rand = np.random.randint(0,1)

    if rand == 0:
        loss = 0
    return loss

def competitive_loss(ip_loss, trade_secret_loss, merger_acquisition_data, market_data):
    #competitive loss is calculated in dollars
    loss = ip_loss + trade_secret_loss + merger_acquisition_data + market_data
    rand = np.random.randint(0,1)
    if rand == 0:
        loss = 0
    return loss

##---------------------------------------
# Primary Loss Contributions

def productivity_loss(time_period=1, revenue_loss = 25_000, wages_loss = 5_000 ):
    #productivty loss is calculated in dollars over the unit years. 
    return time_period*(revenue_loss + wages_loss)

def response_loss(incident_response_cost, forensic_analysis_cost , management_cost , customer_notification , credit_monitoring ):
    #response loss is calculated in dollars
    snd_loss = customer_notification + credit_monitoring
    rand = np.random.randint(0,1)
    if rand == 0:
        snd_loss = 0
    return (incident_response_cost + forensic_analysis_cost + management_cost,snd_loss)

if __name__ == "__main__":

    ## -----------------------
    # Example of an input to the incident_loss function
    hacked = {
        "dict_dist": {
            "dist": "bernoulli",
            "plef": 0.5
        },
        "loss_m": {
            "productivity_loss": {
                "time_period": 1,
                "revenue_loss": 0,
                "wages_loss": 0
            },
            "fine_judgement": {
                "fines": 0,
                "class_actions": 0,
                "bail": 0,
                "legal_fees": 0
            },
            "response_loss": {
                "marketsshare_loss": 0,
                "lower_sales_growth": 0,
                "stock_price_losses": 0,
                "increased_cost_of_capital": 0
            },
            "competitive_loss": {
                "ip_loss": 0,
                "trade_secret_loss": 0,
                "merger_acquisition_data": 0,
                "market_data": 0
            },
            "response_loss": {
                "incident_response_cost": 0,
                "forensic_analysis_cost": 0,
                "management_cost": 0,
                "customer_notification": 0,
                "credit_monitoring": 0
            }
        }
    }
    pass