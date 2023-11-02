def solution():
    """Emma is planning a dinner party, so she went to a shop to buy the products she needs. She bought 8 kg of cheese and 7 kg of vegetables. One kilogram of cheese costs $4 and one kilogram of vegetable costs is $2 more expensive. How much did she pay for her shopping?"""
    
    # Define the cost of cheese and vegetables per kilogram
    CHEESE_PRICE = 4
    VEGETABLE_PRICE = 6

    # Define the quantity of cheese and vegetables purchased
    cheese_kg = 8
    vegetable_kg = 7

    # Calculate the total cost of cheese
    cheese_cost = cheese_kg * CHEESE_PRICE

    # Calculate the total cost of vegetables
    vegetable_cost = vegetable_kg * VEGETABLE_PRICE

    # Calculate the total cost of the shopping
    total_cost = cheese_cost + vegetable_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())