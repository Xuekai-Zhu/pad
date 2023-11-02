def solution():
    # Calculate the total number of peaches delivered to the market
    total_peaches = 25 * 5  # 25 peaches in each of the 5 baskets

    # Calculate the number of peaches remaining after the farmers ate 5
    remaining_peaches = total_peaches - 5

    # Calculate the number of boxes needed to pack the remaining peaches
    boxes = remaining_peaches // 15  # 15 peaches in each box

    result = boxes
    return result

print(solution())