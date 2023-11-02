def solution():
    # Calculate the number of fish caught by fishers
    fish_caught = (2/5) * 3200 + (3/4) * 1800

    # Calculate the total number of fish left in the sea
    total_fish_left = 1800 + 3200 + 500 - fish_caught
    result = total_fish_left
    return result

print(solution())