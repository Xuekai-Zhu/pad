def solution():
    """Tom plants a tree that is 1 year old and 5 feet tall. It gains 3 feet per year. How old is it when it is 23 feet tall?"""
    # Define the initial height and age of the tree
    initial_height = 5
    initial_age = 1

    # Define the rate of growth of the tree
    growth_rate = 3

    # Initialize the height and age of the tree
    height = initial_height
    age = initial_age

    # Calculate the age of the tree when it reaches 23 feet tall
    while height < 23:
        age += 1
        height += growth_rate

    # return the result
    result = age
    return result

print(solution())