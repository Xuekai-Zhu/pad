def solution():
    """Josephine receives a bill from the hospital for 5000$. 50 percent of the bill is for medication. 25 percent of the remaining bill is for overnight stays, and 175$ is for food.
    The rest of the bill is for the ambulance ride. How much did the ambulance ride cost?"""
    total_bill = 5000
    medication_cost = total_bill * 0.5
    remaining_bill = total_bill - medication_cost
    overnight_stay_cost = remaining_bill * 0.25
    food_cost = 175
    ambulance_ride_cost = total_bill - medication_cost - overnight_stay_cost - food_cost
    result = ambulance_ride_cost
    return result

print(solution())