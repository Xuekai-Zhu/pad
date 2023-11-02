def solution():
    """Steven is preparing a shipment of boxes to deliver to a customer for his chemical supply business. The products are very delicate and must be carefully packed, so partially filled boxes can’t be shipped. Steven has three trucks that can be sent on each delivery. Each truck can carry a load of no more than 2,000 pounds of cargo. Some of the boxes weigh 10 pounds after being packed, and some of the boxes weigh 40 pounds when packed. Steven’s customer has ordered equal quantities of both the lighter and heavier products. How many boxes of products can Steven ship to his customer in each delivery?"""
    # Define the weight of each type of box
    LIGHT_BOX = 10
    HEAVY_BOX = 40

    # Define the maximum weight each truck can carry
    MAX_WEIGHT = 2000

    # Calculate the maximum number of light boxes that can fit in a truck
    max_light_boxes = MAX_WEIGHT // LIGHT_BOX

    # Calculate the maximum number of heavy boxes that can fit in a truck
    max_heavy_boxes = MAX_WEIGHT // HEAVY_BOX

    # Calculate the maximum number of boxes (of both types) that can fit in a truck
    max_total_boxes = max_light_boxes + max_heavy_boxes

    # Calculate the total number of boxes that can be shipped in one delivery
    total_boxes = 3 * max_total_boxes

    # Calculate the number of boxes of each type that can be shipped in one delivery
    light_boxes = max_light_boxes * 3
    heavy_boxes = max_heavy_boxes * 3

    # Display the number of boxes that can be shipped in one delivery
    result = light_boxes, heavy_boxes, total_boxes
    return result

print(solution())