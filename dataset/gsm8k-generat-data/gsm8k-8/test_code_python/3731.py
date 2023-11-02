def solution():
    # Define the number of uniforms and lab coats
    uniforms = 12
    coats = 6 * uniforms

    # Calculate the number of lab techs
    lab_techs = uniforms / 2

    # Calculate the total number of coats and uniforms
    total = coats + uniforms

    # Calculate the number of coats and uniforms per lab tech
    per_lab_tech = total / (2 * lab_techs)

    result = per_lab_tech
    return result

print(solution())