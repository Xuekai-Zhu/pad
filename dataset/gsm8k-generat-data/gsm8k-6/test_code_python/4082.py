def solution():
    # Calculate how many balloons Luke filled up
    luke_balloons = 1/4 * 44  # Luke filled up one fourth as many balloons as Anthony

    # Calculate how many balloons Tom filled up
    tom_balloons = 3 * luke_balloons  # Tom filled up 3 times as many balloons as Luke

    result = tom_balloons
    return result

print(solution())