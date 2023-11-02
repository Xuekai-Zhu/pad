def solution():
    """Josh found out that 7 bottle caps weigh exactly one ounce. Josh's entire bottle cap collection weighs 18 pounds exactly. How many bottle caps does Josh have in his collection?"""
    ounces_per_cap = 1/7
    pounds_per_ounce = 1/16
    total_ounces = 18/pounds_per_ounce
    total_caps = total_ounces/ounces_per_cap
    result = total_caps
    return result

print(solution())