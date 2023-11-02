def solution():
    # Calculate the number of sandwiches sold in an 8-hour day
    sandwiches_per_hour = 60 / 5  # the Sandwich Shop serves a sandwich every 5 minutes
    sandwiches_per_day = sandwiches_per_hour * 8
    jalapeno_peppers_per_sandwich = 4 / 8  # each jalapeno pepper makes 8 slices
    jalapeno_peppers_per_day = sandwiches_per_day * jalapeno_peppers_per_sandwich
    result = jalapeno_peppers_per_day
    return result

print(solution())