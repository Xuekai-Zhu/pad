def solution():
    freeze_time = 40  # in minutes
    smoothie_prep_time = 3  # in minutes per smoothie
    num_smoothies = 5

    # Calculate the total time to freeze the ice cubes
    total_freeze_time = freeze_time

    # Calculate the total time to turn the frozen ice cubes into smoothies
    total_smoothie_prep_time = num_smoothies * smoothie_prep_time

    # Calculate the total time to make 5 smoothies
    total_time = total_freeze_time + total_smoothie_prep_time
    result = total_time
    return result

print(solution())