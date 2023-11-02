def solution():
    is_keelhauling_cruel = True
    is_keelhauling_unusual = True
    is_forbidden_by_Eighth_Amendment = True
    if is_keelhauling_cruel and is_keelhauling_unusual and is_forbidden_by_Eighth_Amendment:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())