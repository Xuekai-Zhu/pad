def solution():
    """Bobby has an aquarium with twice as many fish as Sarah's has.  Sarah has 5 more fish in her aquarium than Tony does.  Tony has 3 times as many fish in his aquarium as Billy does.  Billy has 10 fish.  How many fish do all 4 people have put together?"""
    # Determine the number of fish in Billy's aquarium
    billy_fish = 10

    # Determine the number of fish in Tony's aquarium
    tony_fish = 3 * billy_fish

    # Determine the number of fish in Sarah's aquarium
    sarah_fish = tony_fish + 5

    # Determine the number of fish in Bobby's aquarium
    bobby_fish = 2 * sarah_fish

    # Determine the total number of fish
    total_fish = billy_fish + tony_fish + sarah_fish + bobby_fish

    # Display the total number of fish
    result = total_fish
    return result

print(solution())