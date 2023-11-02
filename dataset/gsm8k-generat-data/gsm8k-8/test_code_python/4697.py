def solution():
    # Calculate Tony's number of fish
    billy_fish = 10
    tony_fish = 3 * billy_fish

    # Calculate Sarah's number of fish
    sarah_fish = tony_fish + 5

    # Calculate Bobby's number of fish
    bobby_fish = 2 * sarah_fish

    # Calculate the total number of fish
    total_fish = billy_fish + tony_fish + sarah_fish + bobby_fish
    result = total_fish
    return result

print(solution())