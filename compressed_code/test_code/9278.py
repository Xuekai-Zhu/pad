def solution():
    
    regular_bikes = 7
    children_bikes = 11
    regular_wheels = 2
    children_wheels = 4
    total_regular_wheels = regular_bikes * regular_wheels
    total_children_wheels = children_bikes * children_wheels
    total_wheels = total_regular_wheels + total_children_wheels
    result = total_wheels
    return result

print(solution())