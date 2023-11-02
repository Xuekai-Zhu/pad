def solution():
    # Calculate the total number of steps Austin descends in a minute
    steps_Austin = 30 * 9  # 30 steps per floor x 9 floors
    steps_per_second = steps_Austin/60  # steps descended per second by Austin

    # Calculate the total number of steps Jake descends
    steps_Jake = 30 * 8  # Jake descends 8 floors (from 9 to 1)

    # Calculate the time Jake needs to descend all the stairs in seconds
    time_Jake = steps_Jake/3  # Jake descends 3 steps every second

    # Calculate the time difference between Austin and Jake's arrival at the ground floor
    time_diff = time_Jake - 60  # Austin takes 60 seconds to descend to the ground floor

    result = time_diff
    return result

print(solution())