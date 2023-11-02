def solution():
    lab_coats = 6 * uniforms
    lab_techs = uniforms / 2
    total_uniforms = lab_coats + uniforms
    total_coats = lab_coats
    each_uniform = total_uniforms / lab_techs
    each_coat = total_coats / lab_techs
    result = [each_coat, each_uniform]
    
    return result

print(solution())