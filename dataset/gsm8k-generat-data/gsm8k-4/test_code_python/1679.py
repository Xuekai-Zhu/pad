def solution():
    """A park is 1000 feet long and 2000 feet wide. If there is 1 tree per 20 square feet, how many trees are there in the park?"""
    # Define the area of the park
    park_area = 1000 * 2000

    # Calculate the number of trees in the park
    trees = park_area / 20

    # Return the result
    result = trees
    return result

print(solution())