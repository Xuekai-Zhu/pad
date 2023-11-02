def solution():
    # Calculate the diameter of the circle
    diameter = 14 * 2

    # Convert the diameter from feet to inches
    diameter_inches = diameter * 12

    # Calculate the number of 6-inch pencils that can be placed end-to-end across the diameter
    pencils = diameter_inches // 6

    result = pencils
    return result

print(solution())