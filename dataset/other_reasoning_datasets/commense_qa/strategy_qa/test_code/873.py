def solution():
    has_celiac_disease = True
    is_gluten_free = True
    if has_celiac_disease and is_gluten_free:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())