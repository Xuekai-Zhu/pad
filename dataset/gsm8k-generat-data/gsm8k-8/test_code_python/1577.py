def solution():
    # Define the initial amount of money and the interest rate
    initial_amount = 100
    interest_rate = 0.1

    # Calculate the amount of money after one year
    year_one_amount = initial_amount * (1 + interest_rate) + 10

    # Calculate the amount of money after two years
    year_two_amount = year_one_amount * (1 + interest_rate) + 10

    result = year_two_amount
    return result

print(solution())