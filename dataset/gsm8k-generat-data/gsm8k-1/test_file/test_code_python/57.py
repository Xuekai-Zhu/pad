def solution():
    """Janet buys a brooch for her daughter. She pays $500 for the material to make it and then another $800 for the jeweler to construct it. After that, she pays 10% of that to get it insured. How much did she pay?"""
    material_cost = 500
    construction_cost = 800
    total_cost = material_cost + construction_cost
    insurance_cost = total_cost * 0.1
    total_price = total_cost + insurance_cost
    result = total_price
    return result

print(solution())