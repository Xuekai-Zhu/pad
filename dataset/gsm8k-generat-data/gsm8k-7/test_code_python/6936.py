def solution():
    num_asparagus_bundles = 60
    asparagus_price = 3.0

    num_grape_boxes = 40
    grape_price = 2.5

    num_apples = 700
    apple_price = 0.5

    # Calculate the total cost of all asparagus bundles
    total_asparagus_cost = num_asparagus_bundles * asparagus_price

    # Calculate the total cost of all grape boxes
    total_grape_cost = num_grape_boxes * grape_price

    # Calculate the total cost of all apples
    total_apple_cost = num_apples * apple_price

    # Calculate the total cost of all produce
    total_cost = total_asparagus_cost + total_grape_cost + total_apple_cost
    result = total_cost
    return result

print(solution())