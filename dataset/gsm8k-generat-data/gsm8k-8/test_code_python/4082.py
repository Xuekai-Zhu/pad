def solution():
    # Define the number of water balloons Anthony filled up
    anthony_balloons = 44

    # Calculate the number of balloons Luke filled up
    luke_balloons = anthony_balloons / 4

    # Calculate the number of balloons Tom filled up
    tom_balloons = 3 * luke_balloons

    result = tom_balloons
    return result

print(solution())