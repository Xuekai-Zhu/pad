def solution():
    num_gallons = 10
    cups_per_gallon = 10
    cups_left = 5

    # Calculate the total number of cups of juice initially
    total_cups_initial = num_gallons * cups_per_gallon

    # Calculate the total number of cups of juice drunk
    total_cups_drunk = total_cups_initial - cups_left
    result = total_cups_drunk
    return result

print(solution())