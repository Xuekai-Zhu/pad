def solution():
    """Steven is preparing a shipment of boxes to deliver to a customer for his chemical supply business.
    The products are very delicate and must be carefully packed, so partially filled boxes can’t be shipped.
    Steven has three trucks that can be sent on each delivery.
    Each truck can carry a load of no more than 2,000 pounds of cargo.
    Some of the boxes weigh 10 pounds after being packed, and some of the boxes weigh 40 pounds when packed.
    Steven’s customer has ordered equal quantities of both the lighter and heavier products.
    How many boxes of products can Steven ship to his customer in each delivery?"""
    max_weight_per_delivery = 3 * 2000
    weight_per_box = 10 + 40
    boxes_per_delivery = max_weight_per_delivery // weight_per_box // 2
    result = boxes_per_delivery
    return result

print(solution())