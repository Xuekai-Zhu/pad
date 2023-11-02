def solution():
    canidae_members = ["dogs", "foxes", "coyotes"]
    aesops_fables_characters = ["fox"]
    overlap = [member for member in canidae_members if member in aesops_fables_characters]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())