def solution():
    """In mid-May, the river flowing through Moreland is five feet deep. By mid-June, the river is 10 feet deeper than mid-May. By mid-July, the river is three times deeper than mid-June. How many feet deep is the river by mid-July?"""
    # Define the depth of the river in mid-May
    depth_may = 5

    # Calculate the depth of the river in mid-June
    depth_june = depth_may + 10

    # Calculate the depth of the river in mid-July
    depth_july = depth_june * 3

    # return the result
    result = depth_july
    return result

print(solution())