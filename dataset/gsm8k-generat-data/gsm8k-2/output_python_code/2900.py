def solution():
    """Jenny is trying to convince her cat to walk on a leash. The cat spends twenty minutes resisting. Then Jenny coaxes the cat to walk 64 feet at a rate of 8 feet/minute. How many minutes does this whole process take?"""
    resisting_time = 20
    walking_distance = 64
    walking_speed = 8
    walking_time = walking_distance / walking_speed
    total_time = resisting_time + walking_time
    result = total_time
    return result

print(solution())