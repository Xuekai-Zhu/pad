def solution():
    """Carla is making smoothies. If she uses 500 ml of watermelon puree and 100 ml of cream, how many 150 ml servings can she make?"""
    watermelon_puree = 500
    cream = 100
    total_volume = watermelon_puree + cream
    serving_size = 150
    servings = total_volume // serving_size
    result = servings
    return result

print(solution())