def solution():
    # Define the cost per pound and the minimum purchase amount
    cost_per_pound = 3
    min_purchase = 15

    # Calculate the total cost of the minimum purchase
    min_cost = cost_per_pound * min_purchase

    # Calculate how much Baxter spent over the minimum
    over_min_spend = 105 - min_cost

    # Calculate how many pounds over the minimum Baxter purchased
    over_min_pounds = over_min_spend / cost_per_pound
    result = over_min_pounds
    return result

print(solution())