def solution():
    num_grapes = 100
    num_strawberries = (3/5) * num_grapes
    num_friends = 2
    friend_share_fraction = 1/5

    # Calculate the number of grapes each friend receives
    num_grapes_per_friend = num_grapes * friend_share_fraction

    # Calculate the number of strawberries each friend receives
    num_strawberries_per_friend = num_strawberries * friend_share_fraction

    # Subtract the number of fruits given to friends from the total number of fruits
    total_fruits_left = (num_grapes + num_strawberries) - (num_grapes_per_friend + num_strawberries_per_friend) * num_friends
    result = total_fruits_left
    return result

print(solution())