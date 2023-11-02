def solution():
    stanley_cups_per_hour = 4
    carl_cups_per_hour = 7
    num_hours = 3

    # Calculate the total number of cups Stanley sold in 3 hours
    total_stanley_cups = stanley_cups_per_hour * num_hours

    # Calculate the total number of cups Carl sold in 3 hours
    total_carl_cups = carl_cups_per_hour * num_hours

    # Calculate the difference in the number of cups sold
    cups_difference = total_carl_cups - total_stanley_cups
    result = cups_difference
    return result

print(solution())