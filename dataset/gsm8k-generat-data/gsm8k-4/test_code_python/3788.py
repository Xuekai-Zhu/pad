def solution():
    """Mabel is counting sharks in the ocean. She knows that of the fish that she sees, 25% will be sharks and 75% will be another type of fish. On day one she counts 15 fish. On day 2 she counts three times as many. How many sharks did she count over those two days?"""
    # Define the percentage of fish that are sharks
    shark_percentage = 0.25

    # Define the number of fish counted on day one
    day1_fish_count = 15

    # Define the number of fish counted on day two
    day2_fish_count = 3 * day1_fish_count

    # Calculate the number of sharks counted on day one
    day1_shark_count = day1_fish_count * shark_percentage

    # Calculate the number of sharks counted on day two
    day2_shark_count = day2_fish_count * shark_percentage

    # Calculate the total number of sharks counted over two days
    total_shark_count = day1_shark_count + day2_shark_count

    result = total_shark_count
    return result

print(solution())