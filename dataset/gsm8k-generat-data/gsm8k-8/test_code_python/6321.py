def solution():
    # Define the prices of each ingredient
    salad_price = 3
    beef_price = 2 * salad_price
    potato_price = salad_price / 3
    juice_price = 1.5

    # Calculate the total cost of the ingredients
    total_cost = 2 * salad_price + 2 * beef_price + potato_price + 2 * juice_price

    result = total_cost
    return result

print(solution())