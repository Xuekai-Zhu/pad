def solution():
    """A marathon is 26 miles. He can run the first 10 miles in 1 hour. For the remaining miles he runs at 80% that pace. How long does the race take?"""
    total_distance = 26
    first_10_pace = 1  # hour
    remaining_pace = first_10_pace * 1.25  # 80% of first 10 pace
    remaining_distance = total_distance - 10
    total_time = first_10_pace + (remaining_pace * remaining_distance)
    result = total_time
    return result

print(solution())