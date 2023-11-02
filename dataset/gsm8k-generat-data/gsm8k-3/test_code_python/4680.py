def solution():
    """Adam bought 3 kilograms of nuts and 2.5 kilograms of dried fruits at a store. One kilogram of nuts costs $12 and one kilogram of dried fruit costs $8. How much did his purchases cost?"""
    # Define the cost of nuts and dried fruits per kilogram
    NUT_PRICE = 12
    FRUIT_PRICE = 8

    # Define the amount of nuts and dried fruits purchased
    nuts = 3 # in kilograms
    fruits = 2.5 # in kilograms

    # Calculate the cost of the nuts and dried fruits separately
    nuts_cost = nuts * NUT_PRICE
    fruits_cost = fruits * FRUIT_PRICE

    # Calculate the total cost of the purchase
    total_cost = nuts_cost + fruits_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())