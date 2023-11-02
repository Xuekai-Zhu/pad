def solution():
    total_ribbon = 4.5
    ribbon_per_box = 0.7

    # Calculate the usable ribbon after taking into account leftover ribbon
    usable_ribbon = total_ribbon - 1

    # Calculate the number of boxes that can be tied
    boxes = usable_ribbon // ribbon_per_box
    result = boxes
    return result

print(solution())