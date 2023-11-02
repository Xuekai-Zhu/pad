def solution():
    usual_assembly_time = 1
    usual_baking_time = 1.5
    usual_decorating_time = 1
    double_baking_time = 2 * usual_baking_time
    total_time = usual_assembly_time + double_baking_time + usual_decorating_time
    result = total_time
    return result

print(solution())