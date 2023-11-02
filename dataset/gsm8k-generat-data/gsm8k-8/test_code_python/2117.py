def solution():
    # Calculate the speed of each friend in miles per minute
    friend_1_speed = 3 / 21
    friend_2_speed = 3 / 24

    # Calculate the time it takes each friend to run 5 miles
    friend_1_time = friend_1_speed * 5
    friend_2_time = friend_2_speed * 5

    # Calculate the combined time it takes for both friends to run 5 miles each
    combined_time = friend_1_time + friend_2_time
    result = combined_time
    return result

print(solution())