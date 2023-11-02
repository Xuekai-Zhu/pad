def solution():
    # Calculate the total money Sandra has
    total_money = 10 + 4 + (2 * 4)  # Sandra's savings, mother's money and father's money

    # Calculate the cost of the candies and jelly beans
    candy_cost = 14 * 0.5
    jelly_bean_cost = 20 * 0.2

    # Calculate the remaining money after the purchase
    remaining_money = total_money - (candy_cost + jelly_bean_cost)
    result = remaining_money
    return result

print(solution())