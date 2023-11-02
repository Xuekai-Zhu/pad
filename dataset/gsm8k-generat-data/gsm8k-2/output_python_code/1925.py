def solution():
    """James buys 10 boxes of Capri-sun. Each box has 6 pouches in it. If he paid $12 how many cents does each pouch cost?"""
    num_boxes = 10
    pouches_per_box = 6
    total_pouches = num_boxes * pouches_per_box
    total_cost = 1200
    cost_per_pouch = total_cost / total_pouches
    cost_per_pouch_in_cents = cost_per_pouch * 100
    result = cost_per_pouch_in_cents
    return result

print(solution())