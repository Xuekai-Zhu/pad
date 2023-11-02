def solution():
    """Chenny bought 9 plates at $2 each. She also bought spoons at $1.50 each. How many spoons did Chenny buy if she paid a total of $24 for the plates and spoon?"""
    # Define the cost of each plate and spoon
    PLATE_COST = 2
    SPOON_COST = 1.5

    # Define the number of plates bought
    plate_count = 9

    # Calculate the total cost of the plates
    plate_cost = plate_count * PLATE_COST

    # Calculate the cost of the spoons
    spoon_cost = 24 - plate_cost

    # Calculate the number of spoons bought
    spoon_count = spoon_cost / SPOON_COST

    # Display the number of spoons bought
    result = spoon_count
    return result

print(solution())