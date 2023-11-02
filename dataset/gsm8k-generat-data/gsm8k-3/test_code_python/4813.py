def solution():
    """Laura needs to buy window treatments for 3 windows in her house.  She will need to buy a set of sheers and a set of drapes for each window.  The sheers cost $40.00 a pair and the drapes cost $60.00 a pair.  How much will the window treatments cost?"""
    # Define the cost of the sheers and drapes
    SHEERS_PRICE = 40
    DRAPES_PRICE = 60

    # Define the number of windows
    windows = 3

    # Calculate the total cost of the sheers
    sheers_cost = windows * SHEERS_PRICE

    # Calculate the total cost of the drapes
    drapes_cost = windows * DRAPES_PRICE

    # Calculate the total cost of all the window treatments
    total_cost = sheers_cost + drapes_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())