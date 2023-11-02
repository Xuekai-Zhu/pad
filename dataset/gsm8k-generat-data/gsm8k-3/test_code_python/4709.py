def solution():
    """On Monday Elisa paints 30 square feet of her house's walls. On Tuesday she paints twice that amount. On Wednesday she finishes up by painting half as many square feet as she painted on Monday. How many square feet total does Elisa paint in her house?"""
    # Define the amount of square feet painted on each day
    monday_paint = 30
    tuesday_paint = 2 * monday_paint
    wednesday_paint = 0.5 * monday_paint

    # Calculate the total square feet painted
    total_paint = monday_paint + tuesday_paint + wednesday_paint

    # Display the total square feet painted
    result = total_paint
    return result

print(solution())