def solution():
    weight = 30
    ml_per_kg = 5
    total_ml = weight * ml_per_kg
    equal_parts = 3
    ml_per_part = total_ml / equal_parts
    mg_per_ml = 1000
    total_mg = ml_per_part * mg_per_ml
    result = total_mg
    return result

print(solution())