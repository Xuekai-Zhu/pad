def solution():
    """A boy has 12 oranges. He gives one-third of this number to his brother, one-fourth of the remainder to his friend and keeps the rest for himself. How many does his friend get?"""
    # Define the number of oranges the boy has
    oranges = 12

    # Calculate one-third of the oranges to give to the brother
    brother_oranges = oranges // 3

    # Calculate the remainder of oranges after giving to the brother
    remaining_oranges = oranges - brother_oranges

    # Calculate one-fourth of the remaining oranges to give to the friend
    friend_oranges = remaining_oranges // 4

    # Display the number of oranges the friend gets
    result = friend_oranges
    return result

print(solution())