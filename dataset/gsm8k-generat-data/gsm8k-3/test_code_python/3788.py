def solution():
    """Mabel is counting sharks in the ocean. She knows that of the fish that she sees, 25% will be sharks and 75% will be another type of fish. On day one she counts 15 fish. On day 2 she counts three times as many. How many sharks did she count over those two days?"""
    # Calculate the number of fish on day 1
    day1_fish = 15

    # Calculate the number of fish on day 2
    day2_fish = 3 * day1_fish

    # Calculate the number of sharks on day 1
    day1_sharks = 0.25 * day1_fish

    # Calculate the number of sharks on day 2
    day2_sharks = 0.25 * day2_fish

    # Calculate the total number of sharks over the two days
    total_sharks = day1_sharks + day2_sharks

    # Display the total number of sharks
    result = total_sharks
    return result

print(solution())