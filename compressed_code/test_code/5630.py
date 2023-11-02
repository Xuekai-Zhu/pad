def solution():
    
    money_given = 20
    cost_per_slurpee = 2
    change_received = 8
    total_slurpees_bought = (money_given - change_received) / cost_per_slurpee
    result = total_slurpees_bought
    return result

print(solution())