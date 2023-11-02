def solution():
    # Calculate the number of chess players who have never lost to an AI
    never_lost = 40 // 4

    # Calculate the number of chess players who have lost to a computer at least once
    lost_to_computer = 40 - never_lost

    result = lost_to_computer
    return result

print(solution())