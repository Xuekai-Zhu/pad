def solution():
    
    starting_balance = 125
    increase_percent = 0.25
    decrease_percent = 0.2
    babysitting_earnings = starting_balance * increase_percent
    new_balance = starting_balance + babysitting_earnings
    shoe_cost = new_balance * decrease_percent
    final_balance = new_balance - shoe_cost
    percent_of_starting_balance = (final_balance / starting_balance) * 100
    result = percent_of_starting_balance
    return result

print(solution())