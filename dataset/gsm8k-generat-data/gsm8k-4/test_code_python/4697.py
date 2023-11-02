def solution():
    """Bobby has an aquarium with twice as many fish as Sarah's has. Sarah has 5 more fish in her aquarium than Tony does. Tony has 3 times as many fish in his aquarium as Billy does. Billy has 10 fish. How many fish do all 4 people have put together?"""
    # Define the initial number of fish
    bobby_fish = None

    # Define the number of fish Sarah has
    sarah_fish = None

    # Define the number of fish Tony has
    tony_fish = None

    # Define the number of fish Billy has
    billy_fish = 10

    # Sarah has 5 more fish than Tony
    sarah_fish = 5 + tony_fish

    # Tony has 3 times as many fish as Billy
    tony_fish = 3 * billy_fish

    # Bobby has twice as many fish as Sarah
    bobby_fish = 2 * sarah_fish

    # Calculate the total number of fish
    total_fish = bobby_fish + sarah_fish + tony_fish + billy_fish

    # return the result
    result = total_fish
    return result

print(solution())