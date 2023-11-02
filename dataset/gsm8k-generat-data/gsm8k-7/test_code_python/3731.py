def solution():
    num_uniforms = 12
    num_labcoats = 6 * num_uniforms
    num_labtechs = num_uniforms / 2

    # Calculate the total number of labcoats and uniforms per lab tech
    total_items_per_tech = num_uniforms + num_labcoats
    items_per_tech = total_items_per_tech / num_labtechs

    result = items_per_tech
    return result

print(solution())