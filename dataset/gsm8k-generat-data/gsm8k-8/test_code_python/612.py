def solution():
    # Define the number of red caps and the total number of caps
    red_caps = 50
    total_caps = 125

    # Calculate the number of green caps
    green_caps = total_caps - red_caps

    # Calculate the percentage of green caps
    percentage_green = (green_caps / total_caps) * 100
    result = percentage_green
    return result

print(solution())