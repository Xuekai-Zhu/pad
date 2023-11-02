def solution():
    # Define David Duchovny's dietary restrictions and check if Atlantic Salmon is allowed
    duchovny_diet = ["chicken", "pork", "beef"]
    if "salmon" not in duchovny_diet:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())