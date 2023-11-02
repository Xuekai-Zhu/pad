def solution():
    # Define the initial amount of money Sandra has
    sandra_money = 10

    # Add the money her mother gave her
    mother_money = 4
    sandra_money += mother_money

    # Add the money her father gave her
    father_money = 2 * mother_money
    sandra_money += father_money

    # Calculate the cost of the candies and jelly beans
    candy_cost = 14 * 0.5
    jellybean_cost = 20 * 0.2
    total_cost = candy_cost + jellybean_cost

    # Calculate the amount of money left after the purchase
    money_left = sandra_money - total_cost
    result = money_left
    return result

print(solution())