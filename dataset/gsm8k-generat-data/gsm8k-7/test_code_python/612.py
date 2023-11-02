def solution():
    total_caps = 125
    red_caps = 50

    # Calculate the number of green caps
    green_caps = total_caps - red_caps

    # Calculate the percentage of green caps
    green_percentage = (green_caps / total_caps) * 100
    result = green_percentage
    return result

print(solution())