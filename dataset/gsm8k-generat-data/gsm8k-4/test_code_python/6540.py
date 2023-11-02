def solution():
    """Annie calculated she has three times more toys than Mike, and two less than Tom. Mike has 6 toys. How many toys do Annie, Mike, and Tom have in total?"""
    # Define the number of toys that Mike has
    mike_toys = 6

    # Calculate the number of toys that Annie has, based on Mike's toys
    annie_toys = mike_toys * 3

    # Calculate the number of toys that Tom has, based on Annie's toys
    tom_toys = annie_toys - 2

    # Calculate the total number of toys
    total_toys = mike_toys + annie_toys + tom_toys

    # return the result
    result = total_toys
    return result

print(solution())