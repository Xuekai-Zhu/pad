def solution():
    # Calculate the total number of wafer cookies needed
    total_cookies_needed = 80 * 3

    # Calculate the number of boxes needed, rounding up to ensure enough cookies
    boxes_needed = math.ceil(total_cookies_needed / 60)

    # Calculate the total cost of the boxes
    total_cost = boxes_needed * 3.50

    result = total_cost
    return result

print(solution())