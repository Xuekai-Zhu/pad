def solution():
    days = 40
    cups_per_day = 3
    pods_per_cup = 1
    pods_per_box = 30
    price_per_box = 8
    total_pods = days * cups_per_day * pods_per_cup
    total_boxes = total_pods / pods_per_box
    total_price = total_boxes * price_per_box
    result = total_price
    return result

print(solution())