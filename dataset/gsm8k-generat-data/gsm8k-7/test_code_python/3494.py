def solution():
    bathroom_area = 24
    kitchen_area = 80
    mop_rate = 8

    # Calculate the total area to be mopped
    total_area = bathroom_area + kitchen_area

    # Calculate the total time required to mop all areas
    total_time = total_area / mop_rate
    result = total_time
    return result

print(solution())