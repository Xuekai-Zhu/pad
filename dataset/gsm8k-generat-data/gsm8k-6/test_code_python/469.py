def solution():
    # Calculate the total number of quarts needed to fill the hot tub
    total_quarts = 40 * 4  # 1 gallon = 4 quarts

    # Calculate the total number of bottles needed to fill the hot tub
    total_bottles = total_quarts / 4  # 1 bottle = 1 quart

    # Calculate the cost of the total bottles
    cost_per_bottle = 50
    discount = 20 / 100
    discounted_cost = cost_per_bottle - (cost_per_bottle * discount)
    total_cost = discounted_cost * total_bottles

    result = total_cost
    return result

print(solution())