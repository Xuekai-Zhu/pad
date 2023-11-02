def solution():
    cups_per_bottle = 2
    num_whole_bottles = 10
    num_half_bottles = 5
    half_cup_per_bottle = 1

    # Calculate the total cups needed for the whole bottles
    cups_for_whole_bottles = num_whole_bottles * cups_per_bottle

    # Calculate the total cups needed for the half bottles
    cups_for_half_bottles = num_half_bottles * half_cup_per_bottle

    # Calculate the total cups needed to fill up all the bottles
    total_cups_needed = cups_for_whole_bottles + cups_for_half_bottles
    result = total_cups_needed
    return result

print(solution())