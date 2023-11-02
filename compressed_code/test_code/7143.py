def solution():
    
    money_given = 50
    num_jerseys = 5
    cost_per_jersey = 2
    basketball_cost = 18
    shorts_cost = 8
    
    total_cost = (num_jerseys * cost_per_jersey) + basketball_cost + shorts_cost
    money_left = money_given - total_cost
    result = money_left
    
    return result

print(solution())