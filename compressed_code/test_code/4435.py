def solution():
    
    hair_cost = 50
    nail_cost = 30
    tip_rate = 0.2
    hair_tip = hair_cost * tip_rate
    nail_tip = nail_cost * tip_rate
    total_cost = hair_cost + nail_cost + hair_tip + nail_tip
    result = total_cost
    return result

print(solution())