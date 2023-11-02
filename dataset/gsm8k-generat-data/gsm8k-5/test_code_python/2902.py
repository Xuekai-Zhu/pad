def solution():
    # Total number of flowers planted
    total_planted = 2 * 5  # Two daughters planting 5 flowers each

    # Total number of flowers after growth and death
    total_after_growth = total_planted + 20  # 20 more flowers grown

    # Subtract the dead flowers
    total_alive = total_after_growth - 10

    # Divide the total alive flowers by the number of baskets
    flowers_per_basket = total_alive / 5

    result = flowers_per_basket
    return result

print(solution())