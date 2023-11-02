def solution():
    """A box of ice cream bars costs $7.50 and contains three bars. 6 friends want to each eat 2 bars. How much money will that require per person?"""
    cost_per_box = 7.5
    bars_per_box = 3
    bars_per_person = 2
    num_people = 6
    total_bars_needed = bars_per_person * num_people
    num_boxes_needed = total_bars_needed / bars_per_box
    total_cost = num_boxes_needed * cost_per_box
    cost_per_person = total_cost / num_people
    result = cost_per_person
    return result

print(solution())