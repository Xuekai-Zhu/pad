def solution():
    # Calculate the total number of cups needed for 10 whole bottles
    cups_for_whole_bottles = 2 * 10

    # Calculate the total number of cups needed for 5 half-capacity bottles
    cups_for_half_bottles = 0.5 * 5

    # Calculate the total number of cups needed for all the bottles
    total_cups_needed = cups_for_whole_bottles + cups_for_half_bottles
    result = total_cups_needed
    return result

print(solution())