def solution():
    # Define constants
    COLORS = 4
    CRAYONS_PER_COLOR = 2
    BOXES_PER_HOUR = 5

    # Calculate total crayons per hour
    total_crayons_per_hour = COLORS * CRAYONS_PER_COLOR * BOXES_PER_HOUR

    # Calculate total crayons produced in 4 hours
    total_crayons = total_crayons_per_hour * 4

    result = total_crayons
    return result

print(solution())