def solution():
    """Andy is mixing blue, green and white paint in a 1 : 2 : 5 ratio. If he uses 6 gallons of green paint, how many gallons of paint does he use total?"""
    # Define the ratio of blue, green, and white paint
    blue_green_white_ratio = [1, 2, 5]

    # Define the amount of green paint used
    green_paint_used = 6

    # Determine the total amount of paint used based on the amount of green paint used
    total_paint_used = sum(blue_green_white_ratio) / blue_green_white_ratio[1] * green_paint_used

    # Display the total amount of paint used
    result = total_paint_used
    return result

print(solution())