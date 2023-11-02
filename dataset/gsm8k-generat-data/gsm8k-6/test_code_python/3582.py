def solution():
    # Calculate the cost of the camera before discount
    camera_cost = 4000 * 1.3  # 30% more than the current model

    # Add the cost of the lens and subtract the discount
    total_cost = camera_cost + 400
    total_cost -= 200  # $200 off the lens

    result = total_cost
    return result

print(solution())