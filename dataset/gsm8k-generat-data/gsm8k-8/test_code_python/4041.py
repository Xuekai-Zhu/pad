def solution():
    # Define the number of oranges the boy has initially
    initial_oranges = 12

    # Calculate the number of oranges the boy gives to his brother
    brother_oranges = initial_oranges / 3

    # Calculate the remaining oranges
    remaining_oranges = initial_oranges - brother_oranges

    # Calculate the number of oranges the boy gives to his friend
    friend_oranges = remaining_oranges / 4

    result = friend_oranges
    return result

print(solution())