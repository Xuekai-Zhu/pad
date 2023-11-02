def solution():
    requires_materials = True
    requires_knowledge = True
    requires_society = True
    if requires_materials and requires_knowledge and requires_society:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())