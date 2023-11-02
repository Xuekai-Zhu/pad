def solution():
    # Calculate the cost of buying the same amount of mayo in 16-oz bottles
    num_bottles = 128 / 16 # 1 gallon is equal to 128 oz
    cost_per_bottle = 3
    total_cost_bottles = num_bottles * cost_per_bottle

    # Calculate the savings of buying the gallon container
    gallon_cost = 8
    savings = total_cost_bottles - gallon_cost

    result = savings
    return result

print(solution())