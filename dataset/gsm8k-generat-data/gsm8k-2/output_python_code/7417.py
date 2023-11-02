def solution():
    """Josh found out that 7 bottle caps weigh exactly one ounce. Josh's entire bottle cap collection weighs 18 pounds exactly. How many bottle caps does Josh have in his collection?"""
    ounce_per_cap = 1 / 7
    pound_per_ounce = 1 / 16
    total_ounces = 18 / pound_per_ounce
    total_caps = total_ounces / ounce_per_cap
    result = total_caps
    return result

print(solution())