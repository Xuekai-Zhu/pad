def solution():
    bee_species = {"barbed stingers": "honeybees", "no barbed stingers": "bumblebees"}
    aggression_and_suicide = {"aggressive": "no", "suicidal": "no"}
    if bee_species["no barbed stingers"] == "bumblebees" and aggression_and_suicide["aggressive"] == "no" and aggression_and_suicide["suicidal"] == "no":
        result = "no"
    else:
        result = "not enough information"
    return result

print(solution())