def solution():
    """A farmer has 51 cows. The farmer adds five new cows to its herd and then sells a quarter of the herd. How many cows does the farmer have left?"""
    # Define the initial number of cows
    initial_cows = 51

    # Add the new cows to the herd
    total_cows = initial_cows + 5

    # Calculate the number of cows sold
    cows_sold = total_cows // 4

    # Calculate the remaining cows
    remaining_cows = total_cows - cows_sold

    # return the result
    result = remaining_cows
    return result

print(solution())