def solution():
    # Calculate the number of girls in the class
    girls = 2 * (30 - 10) / 3

    # Calculate the total number of cups brought by the boys
    boys_cups = 10 * 5

    # Calculate the total number of cups brought by the class
    total_cups = boys_cups + girls * cups_per_girl

    # Calculate the cups brought per girl
    cups_per_girl = (90 - boys_cups) / girls

    result = cups_per_girl
    return result

print(solution())