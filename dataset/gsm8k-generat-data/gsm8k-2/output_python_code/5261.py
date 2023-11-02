def solution():
    """Fabian went to a park to get some fresh air. He decided to walk there for 3 hours. Every hour he covers 5 kilometers. How many more hours did Fabian need to walk to reach a total of 30 kilometers?"""
    distance_covered = 5 * 3
    distance_remaining = 30 - distance_covered
    time_needed = distance_remaining / 5
    result = time_needed
    return result

print(solution())