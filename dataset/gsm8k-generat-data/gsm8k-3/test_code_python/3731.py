def solution():
    """There are 6 times as many lab coats as uniforms in the lab. The number of lab techs is half of the number of uniforms. If there are 12 uniforms in the lab, and the lab techs share the coats and uniforms equally among them, how many coats and uniforms in total does each lab tech get?"""
    # Define the number of lab coats per uniform
    COATS_PER_UNIFORM = 6

    # Define the number of lab techs per uniform
    TECHS_PER_UNIFORM = 0.5

    # Define the number of uniforms in the lab
    uniforms = 12

    # Calculate the number of lab coats in the lab
    coats = COATS_PER_UNIFORM * uniforms

    # Calculate the number of lab techs in the lab
    techs = TECHS_PER_UNIFORM * uniforms

    # Calculate the total number of coats and uniforms each lab tech gets
    total = (coats + uniforms) / techs

    # Display the result
    result = total
    return result

print(solution())