def solution():
    # Calculate the total number of peaches delivered to the market
    total_peaches = 25 * 5

    # Calculate the number of peaches remaining after the farmers ate some
    remaining_peaches = total_peaches - 5

    # Calculate the number of boxes needed to pack the remaining peaches
    boxes_needed = remaining_peaches // 15

    result = boxes_needed
    return result

print(solution())