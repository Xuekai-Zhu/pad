def solution():
    # Calculate the number of girls at the party
    girls = 15 + 10

    # Calculate the total number of attendees
    total_attendees = 15 + girls

    # Calculate the total number of cans of soft drinks required
    total_cans = total_attendees * 2

    # Calculate the total number of boxes required
    boxes = total_cans // 8 + (1 if total_cans % 8 != 0 else 0)

    # Calculate the total cost of the boxes
    cost = boxes * 5

    result = cost
    return result

print(solution())