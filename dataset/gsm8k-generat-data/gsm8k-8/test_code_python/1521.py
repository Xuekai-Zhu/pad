def solution():
    # Define camera and photo frame costs
    camera_cost = 110
    photo_frame_cost = 120

    # Calculate the total cost before discount
    total_cost = 2 * camera_cost + 3 * photo_frame_cost

    # Calculate the discount amount
    discount = total_cost * 0.05

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost - discount

    result = total_cost_after_discount
    return result

print(solution())