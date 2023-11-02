def solution():
    num_boxes = 10
    pouches_per_box = 6
    total_cost = 1200  # $12 * 100 cents/dollar

    # Calculate the total number of Capri-sun pouches
    total_pouches = num_boxes * pouches_per_box

    # Calculate the cost per pouch in cents
    cost_per_pouch = total_cost / total_pouches

    result = cost_per_pouch
    return result

print(solution())