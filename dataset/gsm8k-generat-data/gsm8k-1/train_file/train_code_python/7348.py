def solution():
    """Kara mixes cups of sugar and water in the ratio of 1:2 to make one liter of lemonade. Calculate the total number of cups of sugar used if she used 84 cups to make lemonade."""
    total_cups = 84
    ratio_sugar = 1
    ratio_water = 2
    total_ratio = ratio_sugar + ratio_water
    cups_of_sugar = (ratio_sugar / total_ratio) * total_cups
    result = cups_of_sugar
    return result

print(solution())