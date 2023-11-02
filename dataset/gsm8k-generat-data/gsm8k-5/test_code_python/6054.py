def solution():
    total_fishermen = 20  # There were 20 fishermen in the lake
    total_fish_caught = 10000  # They caught a total of 10000 fish
    fish_caught_by_nineteenth = 400  # The 19th fisherman caught 400 fish

    # Calculate the number of fish caught by the twentieth fisherman
    fish_caught_by_twentieth = (total_fish_caught - (fish_caught_by_nineteenth * 19)) / 1
    result = fish_caught_by_twentieth
    return result

print(solution())