def solution():
    """Sam went for a run in the morning. In the afternoon, he went grocery shopping and walked twice the distance through the store as he had run that morning. That evening, he went on a bike ride with his family and biked for 12 miles. In all, he went 18 miles that day. How many miles was Sam’s morning run?"""
    total_distance = 18
    bike_distance = 12
    afternoon_distance = total_distance - bike_distance
    afternoon_walk_distance = afternoon_distance / 3
    morning_run_distance = (afternoon_walk_distance / 2)
    result = morning_run_distance
    return result

print(solution())