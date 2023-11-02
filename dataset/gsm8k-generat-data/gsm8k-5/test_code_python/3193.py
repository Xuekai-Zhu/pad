def solution():
    freeze_time = 40  # It takes 40 minutes to freeze ice cubes
    smoothie_time = 3  # It takes 3 minutes per smoothie to turn frozen ice cubes into smoothies
    num_smoothies = 5  # We want to make 5 smoothies

    # Calculate the total time to make the smoothies
    total_time = freeze_time + (smoothie_time * num_smoothies)
    result = total_time
    return result

print(solution())