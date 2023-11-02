def solution():
    # Calculate the total number of pancakes needed for everyone to have a second pancake
    total_pancakes = 12 + (8 * 1)  # 12 pancakes already made + 8 people each needing 1 more pancake
    more_pancakes = total_pancakes - 12  # calculate the additional pancakes needed
    result = more_pancakes
    return result

print(solution())