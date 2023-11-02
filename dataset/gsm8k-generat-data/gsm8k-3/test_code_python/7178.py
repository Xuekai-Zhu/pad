def solution():
    """When Mark bought his first tv it was was 24 inches wide and 16 inches tall. It cost $672.
    His new tv is 48 inches wide and 32 inches tall and costs $1152.
    How much more expensive as measure by cost per square inch, was his first TV compared to his newest TV?"""
    # Calculate the area of both TVs
    area_old = 24 * 16
    area_new = 48 * 32

    # Calculate the cost per square inch of both TVs
    cost_per_inch_old = 672 / area_old
    cost_per_inch_new = 1152 / area_new

    # Calculate the difference in cost per square inch
    difference = cost_per_inch_old - cost_per_inch_new

    # Display the difference in cost per square inch
    result = difference
    return result

print(solution())