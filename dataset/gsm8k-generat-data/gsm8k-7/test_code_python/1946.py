def solution():
    starting_amount = 200
    cost_per_trip = 2
    trips_per_month = 4
    months_per_year = 12

    # Calculate the total amount spent on store trips in a year
    total_spent = cost_per_trip * trips_per_month * months_per_year

    # Calculate the amount of money left in the piggy bank after a year
    ending_amount = starting_amount - total_spent
    result = ending_amount
    return result

print(solution())