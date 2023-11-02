def solution():
    """When Mark bought his first tv it was was 24 inches wide and 16 inches tall. It cost $672. His new tv is 48 inches wide and 32 inches tall and costs $1152. 
    How much more expensive as measure by cost per square inch, was his first TV compared to his newest TV?"""
    # Calculate the area and cost per square inch of the first TV
    area1 = 24 * 16
    cost1 = 672
    cpsqin1 = cost1 / area1

    # Calculate the area and cost per square inch of the new TV
    area2 = 48 * 32
    cost2 = 1152
    cpsqin2 = cost2 / area2

    # Calculate the difference in cost per square inch
    diff = cpsqin1 - cpsqin2

    # Return the result
    result = round(diff, 2)
    return result

print(solution())