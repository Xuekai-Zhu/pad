def solution():
    """Ocho has 8 friends and half are girls. His friends who are boys like to play theater with him. How many boys play theater with him?"""
    # Define the total number of friends and the number of girls
    total_friends = 8
    girls = total_friends // 2

    # Calculate the number of boys
    boys = total_friends - girls

    # Return the number of boys who play theater with Ocho
    result = boys
    return result

print(solution())