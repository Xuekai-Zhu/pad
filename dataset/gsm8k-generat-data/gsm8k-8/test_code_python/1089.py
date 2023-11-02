def solution():
    # Define the starting number of cans
    start_cans = 12

    # Calculate the number of cans after application
    after_cans = (start_cans / 2) - 3

    # Calculate the number of remaining cans
    remaining_cans = start_cans - after_cans

    result = remaining_cans
    return result

print(solution())