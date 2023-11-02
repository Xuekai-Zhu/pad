def solution():
    money_received = 200
    cost_per_bird = 20
    total_birds_bought = money_received / cost_per_bird
    total_wings = total_birds_bought * 2
    result = total_wings
    return result

print(solution())