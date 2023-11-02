def solution():
    """Sally eats 2 sandwiches on Saturday and 1 sandwich on Sunday. If each sandwich uses 2 pieces of bread, how many pieces of bread does Sally eat across Saturday and Sunday?"""
    # Define the number of sandwiches Sally eats
    saturday_sandwiches = 2
    sunday_sandwiches = 1

    # Define the number of bread pieces used per sandwich
    bread_per_sandwich = 2

    # Calculate the total number of bread pieces used
    total_bread_pieces = (saturday_sandwiches + sunday_sandwiches) * bread_per_sandwich

    # return the result
    result = total_bread_pieces
    return result

print(solution())