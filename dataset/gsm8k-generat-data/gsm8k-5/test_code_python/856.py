def solution():
    trips_per_month = 4  # Randy makes 4 trips to the store every month
    money_spent_per_trip = 2  # Randy spends $2 every time he goes to the store
    months_in_a_year = 12  # Randy wants to know how much money he had at first after a year

    # Calculate the total amount of money Randy spent in a year
    total_money_spent = trips_per_month * money_spent_per_trip * months_in_a_year

    # Calculate the amount of money Randy had at first
    initial_money = total_money_spent + 104
    result = initial_money
    return result

print(solution())