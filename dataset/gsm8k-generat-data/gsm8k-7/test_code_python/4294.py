def solution():
    saving_rates = [5, 10, 20] # weekly saving rates in dollars for each 4 week period
    saving_periods = [4, 4, 4] # number of weeks for each saving period
    total_weeks = sum(saving_periods)
    
    total_savings = 0
    for i in range(len(saving_rates)):
        savings = saving_rates[i] * saving_periods[i]
        total_savings += savings
    
    result = total_savings
    return result

print(solution())