def solution():
    total_boxes = 33  # Kaylee needs to sell a total of 33 boxes
    sold_boxes = 12 + 5 + 4  # Kaylee has already sold 12 lemon, 5 chocolate, and 4 oatmeal biscuit boxes
    remaining_boxes = total_boxes - sold_boxes  # Kaylee still needs to sell this many boxes
    result = remaining_boxes
    return result

print(solution())