def solution():
    # Calculate the total cost of the ice cream box
    box_cost = 7.5

    # Calculate the total number of bars in the box
    total_bars = 3

    # Calculate the number of bars each friend will eat
    bars_per_friend = 2

    # Calculate the total number of bars needed for all friends
    total_bars_needed = bars_per_friend * 6

    # Calculate the total cost needed for all friends
    total_cost_needed = (total_bars_needed / total_bars) * box_cost

    # Calculate the cost per person
    cost_per_person = total_cost_needed / 6
    result = cost_per_person
    return result

print(solution())