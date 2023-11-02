def solution():
    nigella_is_chef = True
    chef_is_concerned_with_cooking_and_nutrition = True
    solubility_is_relevant_to_cooking_and_nutrition = True
    if nigella_is_chef and chef_is_concerned_with_cooking_and_nutrition and solubility_is_relevant_to_cooking_and_nutrition:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())