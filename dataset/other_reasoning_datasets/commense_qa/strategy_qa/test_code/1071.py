def solution():
    job_type = "sofer"
    material_used = "vellum"
    contains_animal_product = "calfskin"
    is_vegan = False
    
    if contains_animal_product in material_used and not is_vegan:
        result = "yes"
    else:
        result = "no"
    
    return result

print(solution())