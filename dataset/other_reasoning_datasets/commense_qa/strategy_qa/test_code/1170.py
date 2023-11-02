def solution():
    children_killed_by_Heracles = ["his children by Megara"]
    children_present_at_funeral_pyre = ["not specified"]
    if all(child in children_killed_by_Heracles for child in children_present_at_funeral_pyre):
        result = "no"
    else:
        result = "unsure"
    return result

print(solution())