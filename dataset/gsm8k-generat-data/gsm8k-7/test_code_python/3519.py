def solution():
    cost_per_box = 7.5
    num_bars_per_box = 3
    num_friends = 6
    num_bars_per_friend = 2

    # Calculate the total number of bars needed
    total_bars_needed = num_friends * num_bars_per_friend

    # Calculate the total number of boxes needed
    total_boxes_needed = total_bars_needed / num_bars_per_box

    # Calculate the total cost of all boxes needed
    total_cost = total_boxes_needed * cost_per_box

    # Calculate the cost per person
    cost_per_person = total_cost / num_friends / num_bars_per_friend
    result = cost_per_person
    return result

print(solution())