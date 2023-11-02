def solution():
    costume_cost = 250
    increase_percentage = 40
    increased_cost = costume_cost + (costume_cost * (increase_percentage / 100))
    deposit = increased_cost * 0.1
    final_cost = increased_cost - deposit
    result = final_cost
    
    return result

print(solution())