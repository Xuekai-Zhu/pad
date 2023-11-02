def solution():
    """Elijah is painting his living room and decides to buy masking tape to make his painting neater. 2 of his walls are 4 meters wide and the other 2 walls are 6 meters wide. Elijah needs enough masking tape to cover the entire width of each wall and can order the exact amount of masking tape he needs. How many meters of masking tape does Elijah need to order?"""
    # Define the width of each wall
    wall1_width = 4
    wall2_width = 6
    wall3_width = 6
    wall4_width = 4

    # Calculate the total length of masking tape needed
    total_length = wall1_width + wall2_width + wall3_width + wall4_width

    # Display the total length
    result = total_length
    return result

print(solution())