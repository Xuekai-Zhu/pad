def solution():
    uniforms = 12  # Given that there are 12 uniforms in the lab
    lab_coats = 6 * uniforms  # Given that there are 6 times as many lab coats as uniforms in the lab
    lab_techs = uniforms / 2  # Given that the number of lab techs is half of the number of uniforms

    # Calculate the total number of coats and uniforms that each lab tech will get
    total_items = uniforms + lab_coats
    items_per_tech = total_items / lab_techs
    result = items_per_tech
    return result

print(solution())