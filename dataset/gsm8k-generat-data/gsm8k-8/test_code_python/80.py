def solution():
    # Calculate how many cans Jennifer bought before meeting Mark
    jennifer_initial = 40

    # Calculate how many cans Jennifer bought for every 5 cans Mark bought
    additional_per_5 = 6

    # Calculate how many additional cans Jennifer bought for Mark's 50 cans
    mark_additional = (50 / 5) * additional_per_5

    # Calculate the total number of cans Jennifer bought
    total_cans = jennifer_initial + mark_additional

    # Get the result
    result = total_cans
    return result

print(solution())