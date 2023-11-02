def solution():
    num_males = 15
    num_girls = num_males + 10
    total_attendees = num_males + num_girls
    cans_per_attendee = 2
    cans_per_box = 8
    cost_per_box = 5

    # Calculate the total number of cans of soft drinks needed
    total_cans = total_attendees * cans_per_attendee

    # Calculate the total number of boxes of soft drinks needed
    total_boxes = total_cans / cans_per_box

    # Calculate the total cost of all boxes of soft drinks needed
    total_cost = total_boxes * cost_per_box
    result = total_cost
    return result

print(solution())