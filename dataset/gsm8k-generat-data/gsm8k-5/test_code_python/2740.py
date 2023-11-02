def solution():
    income = 30000  # John made $30,000 doing Uber
    initial_cost = 18000  # John bought the car for $18,000
    trade_in_value = 6000  # John got $6,000 back when he traded in the car

    # Calculate the total cost of depreciation for the car
    depreciation = initial_cost - trade_in_value

    # Calculate John's profit from driving Uber
    profit = income - depreciation
    result = profit
    return result

print(solution())