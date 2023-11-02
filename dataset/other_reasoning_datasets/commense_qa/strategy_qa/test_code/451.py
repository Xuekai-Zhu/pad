def solution():
    # Define the materials used for modern pennies, the 1943-S penny, and modern silverware
    modern_penny_materials = ["zinc", "copper"]
    penny_1943S_materials = ["steel", "zinc"]
    silverware_materials = ["stainless steel"]
    # Check if the 1943-S penny has the same materials as modern silverware
    if set(penny_1943S_materials) == set(silverware_materials):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())