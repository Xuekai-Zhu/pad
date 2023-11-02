def solution():
    """Laura needs to buy window treatments for 3 windows in her house. She will need to buy a set of sheers and a set of drapes for each window. The sheers cost $40.00 a pair and the drapes cost $60.00 a pair. How much will the window treatments cost?"""
    # Define the number of windows
    num_windows = 3

    # Define the cost of sheers and drapes
    sheer_cost = 40
    drape_cost = 60

    # Calculate the total cost of window treatments
    total_cost = (sheer_cost + drape_cost) * num_windows

    # return the result
    result = total_cost
    return result

print(solution())