def solution():
    # Calculate the number of fish Alex caught
    fish_Alex = 7 * 8 + 23  # Alex caught 7 times as many fish as Jacob and lost 23 fish

    # Calculate the number of fish Jacob needs to catch to beat Alex by 1 fish
    fish_needed = fish_Alex - 1 - 8  # Jacob needs to beat Alex by 1 fish and he started with 8 fish
    result = fish_needed
    return result

print(solution())