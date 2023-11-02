def solution():
    num_regular_ducks = 221
    regular_duck_price = 3.0

    num_large_ducks = 185
    large_duck_price = 5.0

    # Calculate the total amount of money raised for charity
    total_money_raised = (num_regular_ducks * regular_duck_price) + (num_large_ducks * large_duck_price)
    result = total_money_raised
    return result

print(solution())