def solution():
    borrowed_money = 100
    repayment_amount = 110
    ingredient_cost = 75
    num_snow_cones_sold = 200
    snow_cone_price = 0.75

    # Calculate how much Todd earned from selling snow cones
    earnings = num_snow_cones_sold * snow_cone_price

    # Calculate Todd's profit after paying back his brother and deducting ingredient costs
    profit = earnings - repayment_amount - ingredient_cost

    result = profit
    return result

print(solution())