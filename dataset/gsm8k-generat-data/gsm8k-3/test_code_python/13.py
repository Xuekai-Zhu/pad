def solution():
    """Jasper will serve charcuterie at his dinner party. He buys 2 pounds of cheddar cheese for $10, a pound of cream cheese that cost half the price of the cheddar cheese, and a pack of cold cuts that cost twice the price of the cheddar cheese. How much does he spend on the ingredients?"""
    # Define the price and quantity of cheddar cheese
    cheddar_price = 10
    cheddar_quantity = 2

    # Calculate the price and quantity of cream cheese
    cream_price = cheddar_price / 2
    cream_quantity = 1

    # Calculate the price and quantity of cold cuts
    cuts_price = cheddar_price * 2
    cuts_quantity = 1

    # Calculate the total cost of the ingredients
    total_cost = cheddar_price * cheddar_quantity + cream_price * cream_quantity + cuts_price * cuts_quantity

    # Return the result
    result = total_cost
    return result

print(solution())