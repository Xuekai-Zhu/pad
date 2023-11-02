def solution():
    initial_friends = 20
    lost_friends = 2
    new_friends = 1

    # Calculate the final number of friends
    final_friends = initial_friends - lost_friends + new_friends
    result = final_friends
    return result

print(solution())