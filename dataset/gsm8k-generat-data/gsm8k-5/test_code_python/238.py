def solution():
    # Calculate the total amount made from brownies sold
    brownie_sales = 4 * 3

    # Calculate the total amount made from lemon squares sold
    lemon_sales = 5 * 2

    # Calculate the total amount earned so far
    total_sales = brownie_sales + lemon_sales

    # Calculate the remaining amount needed to reach the goal
    remaining_amount = 50 - total_sales

    # Calculate the number of cookies needed to reach the remaining amount
    cookies_needed = remaining_amount / 4
    result = cookies_needed
    return result

print(solution())