def solution():
    """There are 6 times as many lab coats as uniforms in the lab. The number of lab techs is half of the number of uniforms. If there are 12 uniforms in the lab, and the lab techs share the coats and uniforms equally among them, how many coats and uniforms in total does each lab tech get?"""
    # Define the number of uniforms and lab coats
    uniforms = 12
    labcoats = uniforms * 6

    # Define the number of lab techs
    labtechs = uniforms / 2

    # Calculate the total number of items per lab tech
    total_items = (uniforms + labcoats) / labtechs

    # Calculate the number of coats and uniforms per lab tech
    uniform_per_tech = total_items / 2
    coat_per_tech = total_items / 2

    # return the result
    result = (uniform_per_tech, coat_per_tech)
    return result

print(solution())