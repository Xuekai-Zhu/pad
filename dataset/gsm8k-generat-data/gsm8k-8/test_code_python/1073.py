def solution():
    # Calculate the number of fish caught by fishers
    fish_caught_east = 3,200 * (2/5)
    fish_caught_west = 1,800 * (3/4)

    # Calculate the total number of fish caught
    total_fish_caught = fish_caught_east + fish_caught_west

    # Calculate the remaining number of fish in the sea
    remaining_fish = 1,800 + 3,200 + 500 - total_fish_caught
    result = remaining_fish
    return result

print(solution())