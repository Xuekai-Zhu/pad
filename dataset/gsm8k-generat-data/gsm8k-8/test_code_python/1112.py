def solution():
    # Define the total number of berries and the ratios of each type
    total_berries = 42
    raspberry_ratio = 0.5
    blackberry_ratio = 1/3

    # Calculate the number of raspberries and blackberries
    raspberry_count = raspberry_ratio * total_berries
    blackberry_count = blackberry_ratio * total_berries

    # Calculate the number of blueberries by subtracting the raspberry and blackberry counts from the total count
    blueberry_count = total_berries - raspberry_count - blackberry_count
    result = blueberry_count
    return result

print(solution())