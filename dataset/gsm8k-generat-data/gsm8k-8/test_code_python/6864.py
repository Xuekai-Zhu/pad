def solution():
    # Define the number of sets and cups per set
    num_sets = 4
    cups_per_set = 2 * 12

    # Calculate the total number of cups before any were damaged or unused
    total_cups = num_sets * cups_per_set

    # Calculate the number of cups used by subtracting the damaged and unused cups from the total
    cups_used = total_cups - 5 - 30
    result = cups_used
    return result

print(solution())