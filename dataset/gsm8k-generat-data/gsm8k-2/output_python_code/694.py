def solution():
    """Carla is making smoothies. If she uses 500 ml of watermelon puree and 100 ml of cream, how many 150 ml servings can she make?"""
    total_volume = 500 + 100
    serving_volume = 150
    servings = total_volume // serving_volume
    result = servings
    return result

print(solution())