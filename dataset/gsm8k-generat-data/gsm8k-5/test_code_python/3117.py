def solution():
    hourly_rate = 15  # The singer charges $15 per hour
    hours = 3  # Mark hired the singer for 3 hours

    # Calculate the total cost of hiring the singer
    total_cost = hourly_rate * hours

    # Calculate the tip amount
    tip_percentage = 20  # Mark tipped the singer 20%
    tip_amount = total_cost * tip_percentage / 100

    # Calculate the final amount paid by Mark
    final_amount = total_cost + tip_amount
    result = final_amount
    return result

print(solution())