def solution():
    """Austin has 10 pairs of dress shoes he needs to polish over the weekend.  If he has polished 45% of individual shoes, how many more shoes does he need to polish?"""
    # Define the number of dress shoes Austin has
    dress_shoes = 10 * 2

    # Calculate the number of shoes Austin has polished
    polished_shoes = int(dress_shoes * 0.45)

    # Calculate how many more shoes Austin needs to polish
    remaining_shoes = dress_shoes - polished_shoes

    # Display how many more shoes Austin needs to polish
    result = remaining_shoes
    return result

print(solution())