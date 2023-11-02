def solution():
    # Calculate the number of fish in each aquarium
    billy_fish = 10
    tony_fish = 3 * billy_fish   # Tony has 3 times as many fish as Billy
    sarah_fish = tony_fish + 5  # Sarah has 5 more fish than Tony
    bobby_fish = 2 * sarah_fish # Bobby has twice as many fish as Sarah

    # Calculate the total number of fish
    total_fish = billy_fish + tony_fish + sarah_fish + bobby_fish
    result = total_fish
    return result

print(solution())