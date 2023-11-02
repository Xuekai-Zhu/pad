def solution():
    total_fishermen = 20
    total_fish_caught = 10000
    fish_caught_by_19 = 19 * 400

    # Calculate the number of fish caught by the twentieth fisherman
    fish_caught_by_20 = total_fish_caught - fish_caught_by_19
    result = fish_caught_by_20
    return result

print(solution())