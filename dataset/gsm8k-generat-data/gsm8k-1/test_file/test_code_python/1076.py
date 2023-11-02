def solution():
    """If every second, a bubbling spring creates a new jellyfish, how many jellyfish would 5 springs working at the same rate create in 4 hours?"""
    seconds_per_hour = 3600
    springs = 5
    jellyfish_per_second = 1
    total_jellyfish = seconds_per_hour * 4 * springs * jellyfish_per_second
    result = total_jellyfish
    return result

print(solution())