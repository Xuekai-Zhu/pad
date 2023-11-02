def solution():
    
    tea_cost = 10
    cheese_cost = tea_cost / 2
    butter_cost = cheese_cost * 0.8
    bread_cost = butter_cost / 2
    total_cost = tea_cost + cheese_cost + butter_cost + bread_cost
    result = total_cost
    return result

print(solution())