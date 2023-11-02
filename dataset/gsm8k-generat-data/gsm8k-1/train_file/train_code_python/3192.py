def solution():
    """It takes 40 minutes to freeze ice cubes and 3 minutes per smoothie to turn them into smoothies once they're frozen. How long does it take to make 5 smoothies?"""
    freeze_time = 40
    smoothie_time = 3
    num_smoothies = 5
    total_time = freeze_time + (smoothie_time * num_smoothies)
    result = total_time
    return result

print(solution())