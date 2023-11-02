def solution():
    # Calculate the total number of dozens of eggs sold
    total_sales = 120
    dozens_sold = total_sales / 3

    # Calculate the total number of eggs sold
    eggs_sold = dozens_sold * 12

    # Calculate the average number of eggs laid per hen per week
    hens = 10
    eggs_per_week_per_hen = eggs_sold / (hens * 4)

    result = eggs_per_week_per_hen
    return result

print(solution())