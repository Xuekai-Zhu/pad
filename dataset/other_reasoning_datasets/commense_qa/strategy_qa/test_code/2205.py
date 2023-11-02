def solution():
    silicon_properties = ["solid", "natural lustre"]
    bromine_properties = ["liquid", "toxic to the touch"]
    if "natural lustre" in silicon_properties and "toxic to the touch" not in bromine_properties:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())