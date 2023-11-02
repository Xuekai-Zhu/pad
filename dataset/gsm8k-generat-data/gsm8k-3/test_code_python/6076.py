def solution():
    """A farmer has 51 cows. The farmer adds five new cows to its herd and then sells a quarter of the herd. How many cows does the farmer have left?"""
    # Define the initial number of cows and the number of new cows added
    initial_cows = 51
    new_cows = 5

    # Calculate the total number of cows after adding the new cows
    total_cows = initial_cows + new_cows

    # Calculate the number of cows sold after selling a quarter of the herd
    cows_sold = total_cows // 4

    # Calculate the total number of cows left
    cows_left = total_cows - cows_sold

    # Display the number of cows left
    result = cows_left
    return result

print(solution())