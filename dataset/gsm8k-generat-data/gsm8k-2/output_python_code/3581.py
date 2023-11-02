def solution():
    """Mike decides to buy a new camera. He wants to buy a top-of-the-line camera but he decides to wait for the new model to come out. The new model costs 30% more than the current model. The old camera cost $4000. He gets $200 off a $400 lens he bought. How much did he pay for the camera and lens?"""
    camera_cost = 4000
    lens_cost = 400 - 200
    new_camera_cost = camera_cost * 1.3
    total_cost = new_camera_cost + lens_cost
    result = total_cost
    return result

print(solution())