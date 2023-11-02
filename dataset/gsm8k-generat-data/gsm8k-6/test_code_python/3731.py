def solution():
    # Find the number of lab coats and lab techs
    num_uniforms = 12
    num_labcoats = 6 * num_uniforms
    num_techs = num_uniforms / 2

    # Calculate the total number of coats and uniforms each lab tech gets
    total_items = num_uniforms + num_labcoats
    items_per_tech = total_items / num_techs
    result = items_per_tech
    return result

print(solution())