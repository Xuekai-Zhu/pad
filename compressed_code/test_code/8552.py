def solution():
    
    bathroom_area = 24
    kitchen_area = 80
    total_area = bathroom_area + kitchen_area
    mopping_rate = 8
    minutes_spent_mopping = total_area / mopping_rate
    result = minutes_spent_mopping
    return result

print(solution())