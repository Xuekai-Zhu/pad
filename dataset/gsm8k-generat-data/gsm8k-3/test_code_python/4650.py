def solution():
    """Sally eats 2 sandwiches on Saturday and 1 sandwich on Sunday. If each sandwich uses 2 pieces of bread, how many pieces of bread does Sally eat across Saturday and Sunday?"""
    # Define the number of sandwiches eaten on each day
    saturday_sandwiches = 2
    sunday_sandwiches = 1

    # Calculate the total number of sandwiches eaten
    total_sandwiches = saturday_sandwiches + sunday_sandwiches

    # Calculate the total number of pieces of bread eaten
    total_bread_pieces = total_sandwiches * 2

    # Display the total number of pieces of bread eaten
    result = total_bread_pieces
    return result

print(solution())