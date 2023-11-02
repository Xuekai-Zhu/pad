def solution():
    """Carla is making smoothies. If she uses 500 ml of watermelon puree and 100 ml of cream, how many 150 ml servings can she make?"""
    # Calculate the total amount of liquid used
    total_liquid = 500 + 100

    # Calculate the number of 150 ml servings that can be made
    servings = total_liquid // 150

    # Display the number of servings
    result = servings
    return result

print(solution())