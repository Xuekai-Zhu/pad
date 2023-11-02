def solution():
    # Calculate the number of wafer cookies Brenda needs in all
    total_cookies = 80 * 3  # 80 cookies needed for each of the 3 trays

    # Calculate the number of boxes Brenda needs to buy
    boxes = total_cookies // 60 + 1  # round up to the nearest box

    # Calculate the total cost of the boxes Brenda needs to buy
    total_cost = boxes * 3.5

    result = total_cost
    return result

print(solution())