def solution():
    # Define the number of friends
    num_friends = 3

    # Calculate the total number of pizza slices
    total_slices = 2 * 16

    # Calculate the number of pepperoni slices
    pepperoni_slices = total_slices // 2 + 1

    # Calculate the number of cheese slices
    cheese_slices = total_slices // 2 - 7

    # Calculate the total number of slices eaten by all friends
    friend_slices = pepperoni_slices + (num_friends - 1) * (pepperoni_slices // 2 + cheese_slices // 2)

    # Calculate the number of slices eaten by each friend
    slices_per_friend = friend_slices // num_friends
    result = slices_per_friend
    return result

print(solution())