def solution():
    """Annie calculated she has three times more toys than Mike, and two less than Tom. Mike has 6 toys. How many toys do Annie, Mike, and Tom have in total?"""
    # Define the number of toys Mike has
    mike_toys = 6

    # Calculate the number of toys Annie has
    annie_toys = mike_toys * 3

    # Calculate the number of toys Tom has
    tom_toys = annie_toys + 2

    # Calculate the total number of toys
    total_toys = mike_toys + annie_toys + tom_toys

    # Display the total number of toys
    result = total_toys
    return result

print(solution())