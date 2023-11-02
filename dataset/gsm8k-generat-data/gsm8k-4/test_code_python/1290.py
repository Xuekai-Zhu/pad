def solution():
    """Andy is mixing blue, green and white paint in a 1 : 2 : 5 ratio. If he uses 6 gallons of green paint, how many gallons of paint does he use total?"""
    # Define the ratios of blue, green, and white paint
    blue_ratio = 1
    green_ratio = 2
    white_ratio = 5

    # Calculate the total ratio
    total_ratio = blue_ratio + green_ratio + white_ratio

    # Calculate the fraction of the total ratio that represents green paint
    green_fraction = green_ratio / total_ratio

    # Calculate the total amount of paint used, given that 6 gallons is 2/7 of the green paint used
    total_paint = (6 / green_fraction) * (total_ratio / green_ratio)

    result = round(total_paint)
    return result

print(solution())