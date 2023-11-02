def solution():
    num_boxes = 10  # James bought 10 boxes of Capri-sun
    num_pouches = 6  # Each box has 6 pouches
    total_pouches = num_boxes * num_pouches  # Total number of pouches James bought
    total_cost = 1200  # James paid $12, which is 1200 cents

    # Calculate the cost per pouch
    cost_per_pouch = total_cost / total_pouches
    result = cost_per_pouch
    return result

print(solution())