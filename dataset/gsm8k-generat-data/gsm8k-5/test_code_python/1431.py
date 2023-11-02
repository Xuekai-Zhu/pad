def solution():
    distance_1 = 120  # Tony drives 120 miles from his town to his friend's town
    time_1 = 3  # Tony takes 3 hours to drive from his town to his friend's town
    speed = distance_1 / time_1  # Tony's speed is distance/time

    distance_2 = 200  # Tony drives 200 miles to see another friend
    time_2 = distance_2 / speed  # Calculate the time it would take Tony to drive 200 miles at the same speed

    result = time_2
    return result

print(solution())