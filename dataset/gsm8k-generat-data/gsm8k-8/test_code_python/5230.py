def solution():
    # Define the initial amount of money Tara has
    initial_amount = 90

    # Calculate the amount of money Tara will have after a year with 10% interest
    one_year_interest_rate = 0.1
    final_amount = initial_amount + (initial_amount * one_year_interest_rate)

    result = final_amount
    return result

print(solution())