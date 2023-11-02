def solution():
    """Sam went for a run in the morning. In the afternoon, he went grocery shopping and walked twice the distance through the store as he had run that morning. That evening, he went on a bike ride with his family and biked for 12 miles. In all, he went 18 miles that day. How many miles was Sam’s morning run?"""
    total_distance = 18
    afternoon_distance = total_distance - 12  # remaining distance after the bike ride
    shopping_distance = afternoon_distance / 3  # Sam walked twice the distance he ran, so total distance is (1 + 2) = 3 parts
    morning_run = shopping_distance / 2  # Sam ran 1 part in the morning
    result = morning_run
    return result

print(solution())