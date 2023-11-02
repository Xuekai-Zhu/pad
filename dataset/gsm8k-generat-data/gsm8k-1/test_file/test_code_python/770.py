def solution():
    """Jack decides to visit a museum 150 miles from home. He drives 75 mph there and back. He spends 6 hours at the museum. How long is he gone from home?"""
    distance_to_museum = 150
    speed = 75
    time_to_museum = distance_to_museum / speed
    time_at_museum = 6
    total_time = (time_to_museum * 2) + time_at_museum
    result = total_time
    return result

print(solution())