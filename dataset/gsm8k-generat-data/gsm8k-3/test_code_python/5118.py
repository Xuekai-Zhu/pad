def solution():
    """On the first day of the garden center sale, 14 marigolds were sold. The next day 25 more marigolds were sold. On the third day the center sold two times the number of marigolds it did on the day before. How many marigolds were sold during the sale?"""
    # Define the number of marigolds sold on the first day
    marigolds_1 = 14

    # Calculate the number of marigolds sold on the second day
    marigolds_2 = marigolds_1 + 25

    # Calculate the number of marigolds sold on the third day
    marigolds_3 = marigolds_2 * 2

    # Calculate the total number of marigolds sold during the sale
    total_marigolds = marigolds_1 + marigolds_2 + marigolds_3

    # Display the total number of marigolds sold
    result = total_marigolds
    return result

print(solution())