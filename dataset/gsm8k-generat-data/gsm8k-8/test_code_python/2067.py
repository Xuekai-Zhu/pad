def solution():
    # Calculate the total amount needed for the trip
    total_trip_cost = 6 * 450 + 3000

    # Calculate the total amount raised in the first 3 days
    first_3_days_total = 600 + 900 + 400

    # Calculate the total amount raised in the next 4 days
    next_4_days_total = 0.5 * first_3_days_total * 4

    # Calculate the total amount raised
    total_amount_raised = first_3_days_total + next_4_days_total

    # Calculate the amount each person still needs to raise
    amount_still_needed = total_trip_cost - total_amount_raised
    amount_per_person_needed = amount_still_needed / 6

    result = amount_per_person_needed
    return result

print(solution())