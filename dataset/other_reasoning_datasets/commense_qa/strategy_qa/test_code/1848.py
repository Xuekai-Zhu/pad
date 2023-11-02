def solution():
    mother_age_at_birth = 16
    minimum_tobacco_purchase_age = 21
    if mother_age_at_birth < minimum_tobacco_purchase_age:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())