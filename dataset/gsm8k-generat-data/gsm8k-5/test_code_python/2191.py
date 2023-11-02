def solution():
    # Calculate the total number of attendees
    total_attendees = 15 + 10  # 15 males and 10 more girls

    # Calculate the total number of cans of soft drinks needed
    total_cans = total_attendees * 2

    # Calculate the total number of boxes of soft drinks needed
    total_boxes = total_cans // 8 + (total_cans % 8 > 0)  # Round up to the nearest box

    # Calculate the total cost of the soft drinks
    total_cost = total_boxes * 5  # $5 for each box

    result = total_cost
    return result

print(solution())