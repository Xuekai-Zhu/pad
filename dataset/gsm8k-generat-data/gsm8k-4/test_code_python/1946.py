def solution():
    """Randy has $200 in his piggy bank. He spends 2 dollars every time he goes to the store. He makes 4 trips to the store every month. How much money, in dollars, will be in his piggy bank after a year?"""
    # Define the initial amount of money Randy has
    initial_money = 200

    # Define the cost of each trip to the store
    trip_cost = 2

    # Define the number of trips Randy makes each month
    trips_per_month = 4

    # Define the number of months in a year
    months_per_year = 12

    # Calculate the total cost of Randy's trips in a year
    total_trip_cost = trip_cost * trips_per_month * months_per_year

    # Calculate the amount of money Randy will have left after a year
    final_money = initial_money - total_trip_cost

    # return the result
    result = final_money
    return result

print(solution())