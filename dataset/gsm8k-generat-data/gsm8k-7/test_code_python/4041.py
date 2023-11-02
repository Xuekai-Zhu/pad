def solution():
    num_oranges = 12

    # Calculate the number of oranges that the boy gives to his brother
    brother_oranges = num_oranges / 3

    # Calculate the remainder of oranges
    remainder_oranges = num_oranges - brother_oranges

    # Calculate the number of oranges that the boy gives to his friend
    friend_oranges = remainder_oranges / 4
    result = friend_oranges
    return result

print(solution())