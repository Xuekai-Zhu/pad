def solution():
    regular_price = 3  # price of regular size rubber duck
    large_price = 5  # price of large size rubber duck
    regular_count = 221  # number of regular size ducks sold
    large_count = 185  # number of large size ducks sold

    # Calculate the total amount of money raised for charity
    total_money_raised = (regular_price * regular_count) + (large_price * large_count)
    result = total_money_raised
    return result

print(solution())