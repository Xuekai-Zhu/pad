def solution():
    initial_amount = 200
    trips_per_month = 4
    dollars_spent_per_trip = 2
    months_in_year = 12
    total_spent = trips_per_month * dollars_spent_per_trip * months_in_year
    final_amount = initial_amount - total_spent
    result = final_amount
    return result

print(solution())