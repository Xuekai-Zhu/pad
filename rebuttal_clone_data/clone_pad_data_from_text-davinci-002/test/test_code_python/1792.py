def solution():
    trim_up_cost = 5
    trim_into_shape_cost = 15
    number_of_boxwoods = 30
    number_of_spheres = 4
    total_cost = (number_of_boxwoods * trim_up_cost) + (number_of_spheres * trim_into_shape_cost)
    result = total_cost
    return result

print(solution())