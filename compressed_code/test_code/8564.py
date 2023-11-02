def solution():
    
    starting_balance = 500
    rice_cost = 20*2
    wheat_flour_cost = 25*3
    soda_cost = 150
    total_cost = rice_cost + wheat_flour_cost + soda_cost
    remaining_balance = starting_balance - total_cost
    result = remaining_balance
    return result

print(solution())