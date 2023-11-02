def solution():
    # Calculate the total amount of dye needed to dye 100 blouses
    total_dye = 100 * 20 * 10  # each blouse gets 20 dots, and each dot takes 10 ml of dye

    # Calculate the number of 400-ml bottles needed
    bottles_needed = total_dye // 400 + 1  # round up to the nearest bottle

    result = bottles_needed
    return result

print(solution())