def solution():
    
    total_bill = 5000
    medication_cost = total_bill * 0.5
    remaining_cost = total_bill - medication_cost
    overnight_stays = remaining_cost * 0.25
    food_cost = 175
    ambulance_cost = total_bill - medication_cost - overnight_stays - food_cost
    
    result = ambulance_cost
    return result

print(solution())