def solution():
    # Calculate the number of tomatoes picked by Haruto
    picked_tomatoes = 127 - 19

    # Calculate the number of tomatoes he gave his friend
    friend_tomatoes = picked_tomatoes / 2

    # Calculate the number of tomatoes remaining
    remaining_tomatoes = picked_tomatoes - friend_tomatoes
    result = remaining_tomatoes
    return result

print(solution())