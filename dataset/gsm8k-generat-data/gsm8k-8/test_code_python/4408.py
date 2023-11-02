def solution():
    # Calculate the cost of the cheese and meat with coupons applied
    cheese_cost = 3.00  # 4.00 - 1.00 coupon
    meat_cost = 4.00  # 5.00 - 1.00 coupon

    # Calculate the total cost of the sandwich ingredients for one loaf of bread
    sandwich_cost = cheese_cost * 2 + meat_cost * 2

    # Calculate the total cost of one sandwich
    total_cost = sandwich_cost / 10 + 4.00  # Add the cost of the bread

    # Calculate the cost of each sandwich
    cost_per_sandwich = total_cost / 10
    result = cost_per_sandwich
    return result

print(solution())