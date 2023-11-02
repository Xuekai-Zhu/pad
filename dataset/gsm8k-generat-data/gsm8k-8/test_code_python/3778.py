def solution():
    # Define the initial length and target length of the highway
    initial_length = 200
    target_length = 650

    # Calculate the amount of highway built on the first two days
    day1_build = 50
    day2_build = 3 * day1_build
    total_build = day1_build + day2_build

    # Calculate the remaining distance to be built
    remaining_build = target_length - (initial_length + total_build)
    result = remaining_build
    return result

print(solution())