def solution():
    num_instant_cameras = 2
    instant_camera_price = 110

    num_digital_frames = 3
    digital_frame_price = 120

    discount = 0.05

    # Calculate the total cost of all instant cameras
    total_instant_camera_cost = num_instant_cameras * instant_camera_price

    # Calculate the total cost of all digital photo frames
    total_digital_frame_cost = num_digital_frames * digital_frame_price

    # Calculate the total cost before discount
    total_cost_before_discount = total_instant_camera_cost + total_digital_frame_cost

    # Calculate the amount of discount
    total_discount_amount = discount * total_cost_before_discount

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount - total_discount_amount
    result = total_cost_after_discount
    return result

print(solution())