def solution():
    price_paid = 12
    number_of_boxes = 10
    pouches_per_box = 6
    total_number_of_pouches = number_of_boxes * pouches_per_box
    price_per_pouch = price_paid / total_number_of_pouches
    result = price_per_pouch
    return result

print(solution())