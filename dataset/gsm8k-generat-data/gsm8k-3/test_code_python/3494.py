def solution():
    """Jack needs to mop the bathroom and the kitchen. If the bathroom floor is 24 square feet and the kitchen floor is 80 square feet, and Jack can mop 8 square feet per minute, how many minutes does he spend mopping?"""
    # Define the size of the bathroom and kitchen floors
    bathroom_size = 24
    kitchen_size = 80

    # Define Jack's mopping rate
    mopping_rate = 8

    # Calculate the total area that Jack needs to mop
    total_area = bathroom_size + kitchen_size

    # Calculate the total time that Jack spends mopping
    total_time = total_area / mopping_rate

    # Display the total time
    result = total_time
    return result

print(solution())