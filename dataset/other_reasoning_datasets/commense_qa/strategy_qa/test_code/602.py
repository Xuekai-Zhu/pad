def solution():
    vegan = True
    natural_material = "leather"
    synthetic_materials = ["plastic", "leather substitutes"]
    # Check if the natural material is vegan-friendly
    if vegan and natural_material != "leather":
        result = "yes"
    # If the natural material is not vegan-friendly, check if the synthetic material is
    # Note: if the vegan doesn't want to use any animal products at all, they might not want to use any leather substitutes either
    elif vegan and all(material not in synthetic_materials for material in ["leather", "leather substitutes"]):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())