def solution():
    # Define the materials needed to make a parachute and nylon
    parachute_materials = ["nylon"]
    nylon_materials = ["coal"]
    # Check if coal is needed to practice parachuting
    if "coal" in nylon_materials:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())