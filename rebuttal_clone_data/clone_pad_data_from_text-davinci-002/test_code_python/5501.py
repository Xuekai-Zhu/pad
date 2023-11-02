def solution():
    original_red_apples = 200
    original_green_apples = 32
    truck_delivery = 340
    total_green_apples = original_green_apples + truck_delivery
    total_red_apples = original_red_apples
    difference = total_green_apples - total_red_apples
    result = difference
    return result

print(solution())