def solution():
    total_earnings = 400
    cost_of_ingredients = 100
    remaining_total = total_earnings - cost_of_ingredients

    # Calculate the amount donated to the homeless shelter
    donation_to_homeless_shelter = (remaining_total / 2) + 10

    result = donation_to_homeless_shelter
    return result

print(solution())