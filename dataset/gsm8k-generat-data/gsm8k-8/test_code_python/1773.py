def solution():
    # Define the number of gifts that can be wrapped with each roll
    roll1_gifts = 3
    roll2_gifts = 5

    # Define the total number of gifts to be wrapped
    total_gifts = 12

    # Calculate the number of gifts wrapped with the first two rolls
    first_two_gifts = roll1_gifts + roll2_gifts

    # Calculate the number of gifts wrapped with the third roll
    third_gifts = total_gifts - first_two_gifts

    result = third_gifts
    return result

print(solution())