def solution():
    """Emma is planning a dinner party, so she went to a shop to buy the products she needs. She bought 8 kg of cheese and 7 kg of vegetables. One kilogram of cheese costs $4 and one kilogram of vegetable costs is $2 more expensive. How much did she pay for her shopping?"""
    # Define the price of cheese per kilogram and the price difference for vegetables
    CHEESE_PRICE = 4
    VEGETABLE_PRICE_DIFF = 2

    # Define the quantity of cheese and vegetables purchased
    cheese_quantity = 8
    vegetable_quantity = 7

    # Calculate the total cost of the cheese and vegetables
    cheese_cost = cheese_quantity * CHEESE_PRICE
    vegetable_cost = (vegetable_quantity * (CHEESE_PRICE + VEGETABLE_PRICE_DIFF))

    # Calculate the total cost of the shopping
    total_cost = cheese_cost + vegetable_cost

    result = total_cost
    return result

print(solution())