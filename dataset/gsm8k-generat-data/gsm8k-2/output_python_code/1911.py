def solution():
    """Steven is preparing a shipment of boxes to deliver to a customer for his chemical supply business. The products are very delicate and must be carefully packed, so partially filled boxes can’t be shipped. Steven has three trucks that can be sent on each delivery. Each truck can carry a load of no more than 2,000 pounds of cargo. Some of the boxes weigh 10 pounds after being packed, and some of the boxes weigh 40 pounds when packed. Steven’s customer has ordered equal quantities of both the lighter and heavier products. How many boxes of products can Steven ship to his customer in each delivery?"""
    lighter_weight = 10
    heavier_weight = 40
    truck_capacity = 2000
    boxes_per_delivery = 0
    lighter_boxes = truck_capacity // lighter_weight // 3
    heavier_boxes = truck_capacity // heavier_weight // 3
    if lighter_boxes == heavier_boxes:
        boxes_per_delivery = 2 * lighter_boxes
    else:
        max_boxes = min(lighter_boxes, heavier_boxes)
        for i in range(1, max_boxes + 1):
            if lighter_boxes % i == 0 and heavier_boxes % i == 0:
                boxes_per_delivery = 2 * i
    result = boxes_per_delivery
    return result

print(solution())