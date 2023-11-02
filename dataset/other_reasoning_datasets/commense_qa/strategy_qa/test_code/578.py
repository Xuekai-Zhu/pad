def solution():
    brain_location = "head"
    torso_contents = ["heart", "lungs", "stomach"]
    if brain_location not in torso_contents:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())