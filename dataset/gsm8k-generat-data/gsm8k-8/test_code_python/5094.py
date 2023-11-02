def solution():
    # Calculate the medication cost
    medication_cost = 0.5 * 5000

    # Calculate the remaining bill after medication
    remaining_bill = 5000 - medication_cost

    # Calculate the overnight stay cost
    overnight_stay_cost = 0.25 * remaining_bill

    # Calculate the total cost of food and overnight stays
    food_and_overnight_cost = overnight_stay_cost + 175

    # Calculate the ambulance ride cost
    ambulance_ride_cost = remaining_bill - food_and_overnight_cost
    result = ambulance_ride_cost
    return result

print(solution())