def solution():
    
    bread_cost = 0.15
    ham_cost = 0.25
    cheese_cost = 0.35
    sandwich_cost = bread_cost * 2 + ham_cost + cheese_cost
    result = sandwich_cost * 100
    return result

print(solution())