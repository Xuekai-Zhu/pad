def solution():
    total_caps = 125  # Ali has 125 bottle caps in total
    red_caps = 50  # Ali has 50 red caps

    # Calculate the number of green caps
    green_caps = total_caps - red_caps

    # Calculate the percentage of green caps
    percentage_green = (green_caps / total_caps) * 100
    result = percentage_green
    return result

print(solution())