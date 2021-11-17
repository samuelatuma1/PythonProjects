# sample data from the backend


# Please, test your code in assignments.ipynb
investments= [{'investment': 'Tesla', 'revenue': 24000, 'cost': 8000}, 
                        {'investment': 'Google', 'revenue': 20000, 'cost': 6400}, 
                        {'investment': 'Microsoft', 'revenue': 19600, 'cost': 5800}, 
                        {'investment': 'Applee', 'revenue': 21300, 'cost': 8120}, 
                        {'investment': 'IBM', 'revenue': 17400, 'cost': 9180}]

available = 20000

# best_investment_choice helps determine the best investment given a set of competing investments?
def best_investment_choice(investments = [], available=0):
    """
        Given a list of investments and the total available funding, returns the single investment that yields the most profit(revenue - cost)
    """
    best_investment = None
    best_worth = 0
    
    #Loop through investments
    
        # for each investment, check if its revenue - cost is greater than current best_worth, 
        # if its cost is less than or equal to available, and if it is not already in best_investments: 
        
            # if this is the case
             # -> set best_investment = this investment
        
            # -> set best_worth to its revenue - cost
        
    # Outside the for loop, return the best_investment
    return best_investment

# Given investments and available, complete the function optimize_investments such that it returns a list of best investment to maximize profit from a set of investments
def optimize_investments(investments=[], available=0):
    """
        uses a greedy approach to determine the best investments to make based on a list of available investments and available capital.
        Returns a dictionary containing the best investments(bests_investment) and the remaining_balance(available_balance)
    """
    
    best_investments = []
    
    # call best_investment to determine current best investment. 
    best_investment =  best_investment_choice(investments, available)
    
    while best_investment is not None:
        # Given that best_investment returns a value
        
        # Get index of the best_investment
        
        #add best_investment to best_investments
        
        # Reduce available by cost of this particular investment
        
        best_investment =  best_investment_choice(investments, available)
        
    return {"best_investments": best_investments, "available_balance": available}

## Expected result from sample data
{'best_investments': [{'investment': 'Tesla', 'revenue': 24000, 'cost': 8000},
  {'investment': 'Microsoft', 'revenue': 19600, 'cost': 5800}],
 'available_balance': 6200}



    
    
    