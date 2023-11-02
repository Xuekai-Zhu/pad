def solution():
    # Calculate the total flies caught on the first day
    first_day_flies = 5 + 6 - 1

    # Calculate the total number of flies for the week
    total_flies = first_day_flies + (2 * 6)

    # Calculate how many more flies Betty needs to catch for the week
    needed_flies = total_flies - first_day_flies
    result = needed_flies
    return result

print(solution())