def solution():
    num_apples = 20
    jane_apples = 5
    james_apples = jane_apples + 2

    # Calculate the total number of apples given to friends
    total_friend_apples = jane_apples + james_apples

    # Calculate the number of apples left with Martha
    remaining_apples = num_apples - total_friend_apples

    # Calculate the number of apples needed to give away to be left with only 4
    apples_to_give_away = remaining_apples - 4
    result = apples_to_give_away
    return result

print(solution())