def solution():
    sets_of_cups = 4  # Liezl prepared four sets of paper cups
    cups_in_set = 2 * 12  # Each set has 2 dozens or 24 paper cups
    total_cups = sets_of_cups * cups_in_set  # Total number of paper cups prepared

    # Calculate the number of cups used
    cups_used = total_cups - 5 - 30  # 5 cups were damaged and 30 were not used

    result = cups_used
    return result

print(solution())