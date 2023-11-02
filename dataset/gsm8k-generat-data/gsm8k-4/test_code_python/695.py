def solution():
    """Carla is making smoothies. If she uses 500 ml of watermelon puree and 100 ml of cream, how many 150 ml servings can she make?"""
    # Define the amount of watermelon puree and cream needed for one smoothie
    watermelon_per_smoothie = 500
    cream_per_smoothie = 100

    # Calculate the maximum number of servings that can be made
    max_servings = min(watermelon_per_smoothie, cream_per_smoothie) // 150

    # Return the result
    result = max_servings
    return result

print(solution())