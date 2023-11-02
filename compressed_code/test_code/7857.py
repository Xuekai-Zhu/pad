def solution():
    
    total_cost = 87
    beef_cost = 5
    cheese_cost = 7
    remaining_cost = 61
    pounds_of_beef = 1
    cheese_remaining = total_cost - pounds_of_beef * beef_cost
    pounds_of_cheese = (cheese_remaining - remaining_cost) / cheese_cost
    result = pounds_of_cheese
    return result

print(solution())