def solution():
    """James has 3 gallons of milk. He drank 13 ounces of the milk. If there are 128 ounces in a gallon, how many ounces of milk does James have left?"""
    # Define the amount of milk in one gallon
    GALLON = 128
    
    # Define the initial amount of milk and the amount James drank
    initial_milk = 3 * GALLON
    drank_milk = 13
    
    # Calculate the amount of milk James has left
    remaining_milk = initial_milk - drank_milk
    
    # Display the amount of milk James has left
    result = remaining_milk
    return result

print(solution())