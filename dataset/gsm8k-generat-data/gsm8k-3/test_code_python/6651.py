def solution():
    """There are 285 sweets in the bowl. If 49 of the sweets are red and 59 of the sweets are green, how many of the sweets are neither red nor green?"""
    # Define the total number of sweets and the number of red and green sweets
    total_sweets = 285
    red_sweets = 49
    green_sweets = 59

    # Calculate the number of sweets that are neither red nor green
    neither_sweets = total_sweets - red_sweets - green_sweets

    # Display the number of sweets that are neither red nor green
    result = neither_sweets
    return result

print(solution())