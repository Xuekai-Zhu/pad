def solution():
    """Gary is restocking the grocery produce section. He adds 60 bundles of asparagus at $3.00 each, 40 boxes of grapes at $2.50 each, and 700 apples at $0.50 each. How much is all the produce he stocked worth?"""
    asparagus_bundles = 60
    asparagus_price = 3.00
    grape_boxes = 40
    grape_price = 2.50
    apples = 700
    apple_price = 0.50
    total_asparagus_cost = asparagus_bundles * asparagus_price
    total_grape_cost = grape_boxes * grape_price
    total_apple_cost = apples * apple_price
    total_cost = total_asparagus_cost + total_grape_cost + total_apple_cost
    result = total_cost
    return result

print(solution())