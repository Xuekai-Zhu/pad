def solution():
    # Define the cost of the mountain cabin
    cabin_cost = 129000

    # Define the revenue from selling the trees
    cypress_revenue = 20 * 100
    maple_revenue = 24 * 300
    pine_revenue = 600 * 200
    total_revenue = cypress_revenue + maple_revenue + pine_revenue

    # Calculate the amount of money Gloria will have left after buying the cabin
    money_left = total_revenue - cabin_cost + 150
    result = money_left
    return result

print(solution())