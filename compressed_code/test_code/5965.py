def solution():
    
    starting_balance = 5000
    motorcycle_cost = 2800
    balance_after_motorcycle = starting_balance - motorcycle_cost
    balance_after_concert = balance_after_motorcycle / 2
    balance_after_loss = balance_after_concert * 0.75
    result = balance_after_loss
    return result

print(solution())