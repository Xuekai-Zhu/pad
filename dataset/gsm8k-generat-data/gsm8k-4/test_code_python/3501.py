def solution():
    """Chenny bought 9 plates at $2 each. She also bought spoons at $1.50 each. How many spoons did Chenny buy if she paid a total of $24 for the plates and spoon?"""
    # Define the price and quantity of plates
    plate_price = 2
    plate_quantity = 9

    # Define the total cost of the plates
    plate_cost = plate_price * plate_quantity

    # Define the total cost of the plates and spoons combined
    total_cost = 24

    # Calculate the cost of the spoons
    spoon_cost = total_cost - plate_cost

    # Calculate the number of spoons bought
    spoon_price = 1.5
    spoon_quantity = spoon_cost / spoon_price

    result = spoon_quantity
    return result

print(solution())