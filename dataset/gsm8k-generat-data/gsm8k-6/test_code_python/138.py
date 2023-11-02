def solution():
    # Calculate the original cost and discounted cost of the gallon of milk
    milk_original_cost = 3
    milk_discounted_cost = 2

    # Calculate the discount on each box of cereal
    cereal_discount = 1

    # Calculate the total savings on whole milk and cereal
    milk_savings = (milk_original_cost - milk_discounted_cost) * 3
    cereal_savings = cereal_discount * 5

    # Calculate the total savings
    total_savings = milk_savings + cereal_savings
    result = total_savings
    return result

print(solution())