def solution():
    # Calculate the cost of each seed
    seed_cost = 0.005

    # Calculate the revenue from selling one ear of corn
    ear_revenue = 0.1

    # Calculate the profit from selling one ear of corn
    ear_profit = ear_revenue - seed_cost*4

    # Calculate the number of ears sold to make $40 profit
    ears_sold = int(40 / ear_profit)

    result = ears_sold
    return result

print(solution())