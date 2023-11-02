def solution():
    
    total_bill = 5000
    medication_cost = total_bill * 0.5
    remaining_bill = total_bill - medication_cost
    overnight_stay_cost = remaining_bill * 0.25
    food_cost = 175
    ambulance_ride_cost = total_bill - medication_cost - overnight_stay_cost - food_cost
    result = ambulance_ride_cost
    return result

print(solution())