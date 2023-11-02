def solution():
    """Lisa is making a pizza. She uses 30 pieces of pepperoni for a pizza, twice as many pieces of ham, and 12 more pieces of sausage than pepperoni. If there are 6 slices of pizza, and everything was distributed evenly, how many pieces of meat altogether are on each slice?"""
    # Define the number of pieces of pepperoni, ham, and sausage for a pizza
    PEPPERONI_PIZZA = 30
    HAM_PIZZA = PEPPERONI_PIZZA * 2
    SAUSAGE_PIZZA = PEPPERONI_PIZZA + 12

    # Calculate the total number of pieces of meat for a pizza
    total_pieces = PEPPERONI_PIZZA + HAM_PIZZA + SAUSAGE_PIZZA

    # Calculate the number of pieces of meat on each slice
    pieces_per_slice = total_pieces // 6

    # Display the number of pieces of meat on each slice
    result = pieces_per_slice
    return result

print(solution())