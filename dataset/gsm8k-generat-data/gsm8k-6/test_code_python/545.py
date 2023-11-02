def solution():
    # Calculate the number of green leaves remaining on each tea leaf plant after one-third of them turn yellow and fall off
    green_leaves_remaining = (2/3) * 18  # one-third of the green leaves turn yellow and fall off, leaving two-thirds remaining
    # Calculate the total number of green leaves remaining on all three tea leaf plants
    total_green_leaves_remaining = 3 * green_leaves_remaining
    result = total_green_leaves_remaining
    return result

print(solution())