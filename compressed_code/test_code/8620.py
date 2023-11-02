def solution():
    
    old_camera_cost = 4000
    lens_cost = 400
    discount = 200
    
    new_camera_cost = old_camera_cost * 1.3
    total_cost = new_camera_cost + lens_cost - discount
    result = total_cost
    return result

print(solution())