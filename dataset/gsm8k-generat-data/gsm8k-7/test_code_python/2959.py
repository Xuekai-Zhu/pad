def solution():
    num_pebbles = 3 * 12  # 3 dozens of pebbles
    num_pebbles_per_friend = 4
    num_friends = num_pebbles // num_pebbles_per_friend
    result = num_friends
    return result

print(solution())