def solution():
    allergic_to_tricarboxylic_acid = True
    found_in_citrus_fruits = True
    watermelon_is_citrus_fruit = False
    # Check if watermelon is safe for people with tricarboxylic acid allergy
    if allergic_to_tricarboxylic_acid and not found_in_citrus_fruits or not watermelon_is_citrus_fruit:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())