def solution():
    """There were 15 males and 10 more girls at the party. Each attendee received 2 cans of soft drinks. If Mary bought several boxes of soft drinks where a box contains 8 cans and is priced at $5 for each box, how much did Mary spend on soft drinks?"""
    # Calculate the total number of attendees
    total_attendees = 15 + 15 + 10

    # Calculate the total number of cans of soft drinks needed
    total_cans = total_attendees * 2

    # Calculate the total number of boxes needed
    total_boxes = total_cans // 8 + (1 if total_cans % 8 > 0 else 0)

    # Calculate the total cost of the soft drinks
    total_cost = total_boxes * 5

    # return the result
    result = total_cost
    return result

print(solution())