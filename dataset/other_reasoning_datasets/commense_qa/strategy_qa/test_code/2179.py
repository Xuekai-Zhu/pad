def solution():
    coumadin_patient = True
    vitamin_k_rich_foods = ["Brussels sprouts"]
    if coumadin_patient and any(food in vitamin_k_rich_foods for food in vitamin_k_rich_foods):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())