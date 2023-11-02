def solution():
    # Calculate the total number of attendees at the party
    total_attendees = 15 + 10 + 15  # 15 males and 10 more females and 15 more people

    # Calculate the total number of cans of soft drinks needed
    total_cans = total_attendees * 2  # each attendee received 2 cans

    # Calculate the total number of boxes of soft drinks needed
    total_boxes = total_cans / 8  # each box contains 8 cans

    # Calculate the total cost of the soft drinks
    total_cost = total_boxes * 5  # each box costs $5

    result = total_cost
    return result

print(solution())