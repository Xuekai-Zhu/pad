def solution():
    total_wolves = 4 + 16  # There are 4 hunting wolves and 16 additional wolves in the pack
    total_meat_needed = total_wolves * 8 * 5  # Each wolf needs 8 pounds of meat for 5 days

    # Calculate the number of deer needed to provide enough meat
    deer_needed = total_meat_needed / 200

    # Calculate the number of deer each wolf needs to kill
    deer_per_wolf = deer_needed / 4
    result = deer_per_wolf
    return result

print(solution())