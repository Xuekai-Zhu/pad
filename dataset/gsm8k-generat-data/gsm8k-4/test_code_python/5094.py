def solution():
    """Josephine receives a bill from the hospital for 5000$.  50 percent of the bill is for medication.  25 percent of the remaining bill is for overnight stays, and 175$ is for food.  The rest of the bill is for the ambulance ride.  How much did the ambulance ride cost?"""
    # Define the initial bill amount
    bill_amount = 5000

    # Calculate the amount for medication
    medication_amount = bill_amount * 0.5

    # Calculate the remaining bill amount
    remaining_amount = bill_amount - medication_amount

    # Calculate the amount for overnight stays
    overnight_amount = remaining_amount * 0.25

    # Subtract the amount for food
    remaining_amount -= 175

    # Calculate the amount for the ambulance ride
    ambulance_amount = remaining_amount - overnight_amount

    result = ambulance_amount
    return result

print(solution())