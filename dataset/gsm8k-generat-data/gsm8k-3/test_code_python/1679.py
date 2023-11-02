def solution():
    """A park is 1000 feet long and 2000 feet wide. If there is 1 tree per 20 square feet, how many trees are there in the park?"""
    # Define the dimensions of the park
    length = 1000
    width = 2000

    # Calculate the area of the park in square feet
    area = length * width

    # Calculate the number of trees in the park
    trees = area / 20

    # Display the number of trees in the park
    result = trees
    return result

print(solution())