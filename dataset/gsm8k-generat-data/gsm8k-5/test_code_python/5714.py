def solution():
    slices_per_pepper = 8  # Each jalapeno pepper makes 8 slices
    peppers_per_sandwich = 4  # Each sandwich has 4 strips of jalapeno pepper
    sandwiches_per_hour = 60 / 5  # The Sandwich Shop serves 12 sandwiches per hour
    sandwiches_per_day = sandwiches_per_hour * 8  # The Sandwich Shop serves sandwiches for 8 hours a day

    # Calculate the total number of slices of jalapeno pepper required
    total_slices = sandwiches_per_day * peppers_per_sandwich * slices_per_pepper
    result = total_slices / slices_per_pepper  # Convert the total number of slices to the number of peppers
    return result

print(solution())