def solution():
    swallow_weight = 1 # In ounces
    ostrich_weight = 32000 # In ounces
    if ostrich_weight < swallow_weight:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())