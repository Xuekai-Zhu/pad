def solution():
    """Jerry was asked by her mom to do grocery shopping. He needs to buy 2 liters of mustard oil that costs $13 per liter, 3 pounds of gluten-free penne pasta that costs $4 per pound, and 1 pound of pasta sauce that costs $5. If Jerry can keep the rest of the $50 after grocery shopping, how much money will he have?"""
    # Define the cost of each grocery item
    MUSTARD_OIL_PRICE = 13
    PENNE_PASTA_PRICE = 4
    PASTA_SAUCE_PRICE = 5

    # Define the quantity of each grocery item
    mustard_oil_liters = 2
    penne_pasta_pounds = 3
    pasta_sauce_pounds = 1

    # Calculate the total cost of the grocery items
    total_cost = (mustard_oil_liters * MUSTARD_OIL_PRICE) + (penne_pasta_pounds * PENNE_PASTA_PRICE) + PASTA_SAUCE_PRICE

    # Calculate how much money Jerry will have left after grocery shopping
    remaining_money = 50 - total_cost

    # Display the remaining money
    result = remaining_money
    return result

print(solution())