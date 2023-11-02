def solution():
    original_order = 25
    delivery_tip = 8
    tomatoes_substitute = 2.20
    lettuce_substitute = 1.75
    celery_substitute = 2

    # Calculate the total cost of the new order by substituting the items and adding delivery/tip
    new_order = original_order + tomatoes_substitute + lettuce_substitute + celery_substitute + delivery_tip
    result = new_order
    return result

print(solution())