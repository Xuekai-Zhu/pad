def solution():
    water_per_night = 1 / 5  # Mary Anne drinks 1/5 of a bottle of sparkling water every night
    bottles_per_year = 365  # Mary Anne drinks every night for a year
    cost_per_bottle = 2  # Each bottle of sparkling water costs $2

    # Calculate the total cost of sparkling water for the year
    total_cost = water_per_night * bottles_per_year * cost_per_bottle
    result = total_cost
    return result

print(solution())