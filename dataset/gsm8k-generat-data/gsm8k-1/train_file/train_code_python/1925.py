def solution():
    """James buys 10 boxes of Capri-sun. Each box has 6 pouches in it. If he paid $12 how many cents does each pouch cost?"""
    num_boxes = 10
    num_pouches_per_box = 6
    total_pouches = num_boxes * num_pouches_per_box
    total_cost = 1200  # $12 in cents
    cost_per_pouch = total_cost // total_pouches
    result = cost_per_pouch
    return result

print(solution())