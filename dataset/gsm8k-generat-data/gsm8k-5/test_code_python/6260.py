def solution():
    # Total amount of money Sandra has
    total_money = 10 + 4 + (2*4)  # $10 saved, $4 from mother, $8 from father

    # Cost of candies and jelly beans
    cost_of_candies = 14 * 0.5  # 14 candies at $0.5 each
    cost_of_jellybeans = 20 * 0.2  # 20 jelly beans at $0.2 each

    # Total cost of candies and jelly beans
    total_cost = cost_of_candies + cost_of_jellybeans

    # Calculate the remaining amount of money
    remaining_money = total_money - total_cost
    result = remaining_money
    return result

print(solution())