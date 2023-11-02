def solution():
    """On Monday Elisa paints 30 square feet of her house's walls. On Tuesday she paints twice that amount. On Wednesday she finishes up by painting half as many square feet as she painted on Monday. How many square feet total does Elisa paint in her house?"""
    # Define the square footage painted on each day
    monday_paint = 30
    tuesday_paint = monday_paint * 2
    wednesday_paint = monday_paint / 2

    # Calculate the total square footage painted
    total_paint = monday_paint + tuesday_paint + wednesday_paint

    result = total_paint
    return result

print(solution())