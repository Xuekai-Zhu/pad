def solution():
    # Calculate the number of slices of bread used from Monday to Friday
    weekday_bread = 2 * 5

    # Calculate the number of slices of bread used on Saturday
    saturday_bread = 2 * 2

    # Calculate the total number of slices of bread used
    total_bread = weekday_bread + saturday_bread

    # Calculate the number of slices of bread left
    bread_left = 22 - total_bread
    result = bread_left
    return result

print(solution())