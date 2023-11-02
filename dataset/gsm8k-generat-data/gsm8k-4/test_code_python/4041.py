def solution():
    """A boy has 12 oranges. He gives one-third of this number to his brother, one-fourth of the remainder to his friend and keeps the rest for himself. How many does his friend get?"""
    # Define the initial number of oranges
    oranges = 12

    # Calculate the number of oranges given to his brother
    brother_oranges = oranges / 3

    # Calculate the remainder
    remainder_oranges = oranges - brother_oranges

    # Calculate the number of oranges given to his friend
    friend_oranges = remainder_oranges / 4

    # Return the number of oranges given to his friend
    result = friend_oranges
    return result

print(solution())