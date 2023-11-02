def solution():
    # Calculate the total number of cookies
    cookies = 6 * 12

    # Calculate the total cost of making the cookies
    cost = cookies * 0.25

    # Calculate the total revenue from selling the cookies
    revenue = cookies * 1.5

    # Calculate the profit
    profit = revenue - cost

    # Calculate how much each charity gets
    charity_share = profit / 2

    result = charity_share
    return result

print(solution())