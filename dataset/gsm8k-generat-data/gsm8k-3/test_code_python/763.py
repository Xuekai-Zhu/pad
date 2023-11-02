def solution():
    """Josh has 18 yards of ribbon that is to be used equally to 6 gifts. If each gift will use 2 yards of ribbon, how many yards of ribbon will be left?"""
    # Define the total length of ribbon and the number of gifts
    total_ribbon = 18
    num_gifts = 6

    # Calculate the total length of ribbon used for all gifts
    total_used = num_gifts * 2

    # Calculate the length of ribbon remaining
    remaining_ribbon = total_ribbon - total_used

    # Display the length of ribbon remaining
    result = remaining_ribbon
    return result

print(solution())