def solution():
    trays_of_banana_pudding = 3
    wafers_per_tray = 80
    cookies_per_box = 60
    boxes_needed = (trays_of_banana_pudding * wafers_per_tray) // cookies_per_box
    price_per_box = 3.5
    total_cost = boxes_needed * price_per_box
    result = total_cost
    return result

print(solution())