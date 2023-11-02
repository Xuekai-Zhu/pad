def solution():
    """Josephine receives a bill from the hospital for 5000$.  50 percent of the bill is for medication.  25 percent of the remaining bill is for overnight stays, and 175$ is for food.  The rest of the bill is for the ambulance ride.  How much did the ambulance ride cost?"""
    # Calculate the cost of medication
    medication_cost = 5000 * 0.5

    # Calculate the remaining bill after medication
    remaining_bill = 5000 - medication_cost

    # Calculate the cost of overnight stays
    overnight_stay_cost = remaining_bill * 0.25

    # Subtract the cost of food and overnight stays from the remaining bill to get the cost of the ambulance ride
    ambulance_ride_cost = remaining_bill - (overnight_stay_cost + 175)

    # Display the cost of the ambulance ride
    result = ambulance_ride_cost
    return result

print(solution())