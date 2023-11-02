def solution():
    stove_type = "glass top"
    if stove_type == "flat top":
        result = "no" # cast iron skillet should not be used
    else:
        result = "yes" # it is okay to use cast iron skillet
    return result

print(solution())