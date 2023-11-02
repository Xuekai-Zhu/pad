def solution():
    """The distance across a country is 8205 kilometers. Amelia started at one end and drove 907 kilometers on Monday and 582 kilometers on Tuesday. How many kilometers does Amelia still have to drive to make it across the country?"""
    total_distance = 8205
    distance_covered = 907 + 582
    remaining_distance = total_distance - distance_covered
    result = remaining_distance
    return result

print(solution())