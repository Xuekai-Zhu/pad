def solution():
    # Define the variables
    money_left = 104
    trips_per_month = 4
    amount_spent_per_trip = 2
    months_in_a_year = 12

    # Calculate the total amount spent in a year
    total_spent = trips_per_month * amount_spent_per_trip * months_in_a_year

    # Calculate the initial amount of money Randy had
    initial_amount = money_left + total_spent
    result = initial_amount
    return result

print(solution())