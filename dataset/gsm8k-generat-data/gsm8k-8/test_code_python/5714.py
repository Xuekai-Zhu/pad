def solution():
    # Calculate the number of sandwiches served in an 8-hour day
    sandwiches_per_hour = 60 / 5
    sandwiches_per_day = sandwiches_per_hour * 8
    jalapeno_slices_per_sandwich = 4 * 8
    jalapeno_slices_per_day = sandwiches_per_day * jalapeno_slices_per_sandwich

    # Calculate the number of jalapeno peppers needed for the day
    jalapeno_peppers_per_slice = 1/8
    jalapeno_peppers_per_day = jalapeno_slices_per_day * jalapeno_peppers_per_slice
    result = jalapeno_peppers_per_day
    return result

print(solution())