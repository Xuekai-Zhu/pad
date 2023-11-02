def solution():
    jillian_shells = 29
    savannah_shells = 17
    clayton_shells = 8
    num_friends = 2

    # Calculate the total number of shells collected
    total_shells = jillian_shells + savannah_shells + clayton_shells

    # Calculate the number of shells each friend gets
    shells_per_friend = total_shells // (num_friends * 1.0)

    result = shells_per_friend
    return result

print(solution())