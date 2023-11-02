def solution():
    """Linda is repainting her bedroom. The wall area is 600 sq. ft. If a gallon of paint can cover 400 sq. ft., how many gallon cans of paint will Linda have to buy if she wants to do two coats?"""
    # Define the wall area and the area a gallon of paint covers
    wall_area = 600
    paint_coverage = 400

    # Calculate the total number of gallons needed for two coats
    total_gallons = wall_area / paint_coverage * 2

    # Round up to the nearest gallon
    total_gallons = math.ceil(total_gallons)

    # Display the total number of gallons needed
    result = total_gallons
    return result

print(solution())