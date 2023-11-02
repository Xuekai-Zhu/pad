def solution():
    """Steven is preparing a shipment of boxes to deliver to a customer for his chemical supply business. The products are very delicate and must be carefully packed, so partially filled boxes can’t be shipped. Steven has three trucks that can be sent on each delivery. Each truck can carry a load of no more than 2,000 pounds of cargo. Some of the boxes weigh 10 pounds after being packed, and some of the boxes weigh 40 pounds when packed. Steven’s customer has ordered equal quantities of both the lighter and heavier products. How many boxes of products can Steven ship to his customer in each delivery?"""
    # Define the weight of the lighter and heavier products
    lighter_weight = 10
    heavier_weight = 40

    # Define the maximum weight that each truck can carry
    max_weight = 2000

    # Calculate the maximum number of lighter boxes that can be shipped in one truck
    lighter_boxes_per_truck = max_weight // lighter_weight

    # Calculate the maximum number of heavier boxes that can be shipped in one truck
    heavier_boxes_per_truck = max_weight // heavier_weight

    # Calculate the total number of boxes that can be shipped in one truck
    total_boxes_per_truck = lighter_boxes_per_truck + heavier_boxes_per_truck

    # Calculate the total number of boxes that can be shipped in all three trucks
    total_boxes = total_boxes_per_truck * 3

    # Calculate the number of lighter boxes and heavier boxes that can be shipped in each delivery
    lighter_boxes_per_delivery = total_boxes // 2
    heavier_boxes_per_delivery = total_boxes // 2

    # Return the result
    result = (lighter_boxes_per_delivery, heavier_boxes_per_delivery)
    return result

print(solution())