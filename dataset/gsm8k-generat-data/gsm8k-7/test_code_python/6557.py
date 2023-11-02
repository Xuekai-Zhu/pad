def solution():
    num_bass = 32
    num_trout = num_bass / 4
    num_blue_gill = num_bass * 2

    # Calculate the total number of fish caught
    total_fish = num_bass + num_trout + num_blue_gill
    result = total_fish
    return result

print(solution())