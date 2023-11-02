def solution():
    has_uterus_and_vagina = True
    identifies_as_male = True
    experiences_menstruation = True
    
    if has_uterus_and_vagina and identifies_as_male and experiences_menstruation:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())