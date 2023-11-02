def solution():
    """Dexter and Jay are using a gallon of white paint to paint the walls. Dexter used 3/8 of the gallon of paint while Jay used 5/8 of a gallon of paint. If a gallon is equal to 4 liters, how many liters of paint were left from Dexter and Jay combined?"""
    # Define the total amount of paint used in gallons
    total_paint_gallons = 1

    # Calculate the amount of paint used by Dexter and Jay in gallons
    dexter_paint_gallons = total_paint_gallons * 3/8
    jay_paint_gallons = total_paint_gallons * 5/8

    # Calculate the total amount of paint used by Dexter and Jay in liters
    total_paint_liters = (dexter_paint_gallons + jay_paint_gallons) * 4

    # Calculate the amount of paint left in liters
    paint_left_liters = 4 - total_paint_liters

    # return the result
    result = paint_left_liters
    return result

print(solution())