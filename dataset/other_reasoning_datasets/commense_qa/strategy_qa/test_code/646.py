def solution():
    gluten_percentage = 9
    has_celiac_disease = True
    if has_celiac_disease and gluten_percentage > 0:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())