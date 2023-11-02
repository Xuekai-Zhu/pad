def solution():
    """Mike decides to buy a new camera. He wants to buy a top-of-the-line camera but he decides to wait for the new model to come out. The new model costs 30% more than the current model. The old camera cost $4000. He gets $200 off a $400 lens he bought. How much did he pay for the camera and lens?"""
    # Define the cost of the old camera and the cost of the lens
    old_camera_cost = 4000
    lens_cost = 400

    # Calculate the discount on the lens
    lens_discount = 200

    # Calculate the cost of the lens after the discount
    lens_final_cost = lens_cost - lens_discount

    # Calculate the cost of the new camera
    new_camera_cost = old_camera_cost * 1.3

    # Calculate the total cost of the camera and the lens
    total_cost = new_camera_cost + lens_final_cost

    result = total_cost
    return result

print(solution())