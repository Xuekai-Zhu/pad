def solution():
    total_money = 87
    cheese_price = 7
    beef_price = 5
    remaining_money = 61
    
    # Calculate the total cost of 1 pound of cheese and 1 pound of beef
    total_cost = cheese_price + beef_price
    
    # Calculate the total cost spent on cheese and beef
    spent_money = total_money - remaining_money
    
    # Calculate the weight of beef purchased
    beef_weight = spent_money // total_cost
    
    # Calculate the weight of cheese purchased
    cheese_weight = (total_money - (beef_weight * total_cost)) // cheese_price
    result = cheese_weight
    return result

print(solution())