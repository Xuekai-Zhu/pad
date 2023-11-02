def solution():
    """A box of ice cream bars costs $7.50 and contains three bars. 6 friends want to each eat 2 bars. How much money will that require per person?"""
    box_price = 7.5
    bars_per_box = 3
    bars_per_person = 2
    total_bars_needed = 6 * bars_per_person
    boxes_needed = total_bars_needed / bars_per_box
    cost_per_person = box_price / boxes_needed / 6
    result = cost_per_person
    return result

print(solution())