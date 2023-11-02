def solution():
    """Mark and his sister Chris both leave their house for school at the same time. Mark travels at the same speed as Chris, who walks 3 miles per hour. After walking 3 miles Mark has to turn around and go home because he forgot his lunch. If the distance from their house to the school is 9 miles, how much longer does Mark spend walking than Chris?"""
    distance = 9
    speed = 3
    time_to_return_home = 3 / speed
    total_time_for_mark = time_to_return_home + (distance - 3) / (2 * speed)
    total_time_for_chris = distance / speed
    mark_extra_time = total_time_for_mark - total_time_for_chris
    result = mark_extra_time
    return result

print(solution())