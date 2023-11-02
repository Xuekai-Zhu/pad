def solution():
    """Jenny is trying to convince her cat to walk on a leash. The cat spends twenty minutes resisting. Then Jenny coaxes the cat to walk 64 feet at a rate of 8 feet/minute. How many minutes does this whole process take?"""
    resistance_time = 20
    distance = 64
    rate = 8
    walking_time = distance / rate
    total_time = resistance_time + walking_time
    result = total_time
    return result

print(solution())