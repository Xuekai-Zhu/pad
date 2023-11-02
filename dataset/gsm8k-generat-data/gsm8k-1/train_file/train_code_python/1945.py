def solution():
    """Randy has $200 in his piggy bank. He spends 2 dollars every time he goes to the store. He makes 4 trips to the store every month. How much money, in dollars, will be in his piggy bank after a year?"""
    starting_amount = 200
    cost_per_trip = 2
    trips_per_month = 4
    months_per_year = 12
    total_cost = cost_per_trip * trips_per_month * months_per_year
    result = starting_amount - total_cost
    return result

print(solution())