def solution():
    mario_profession = "plumber"
    jurisdiction_requirement = {"Illinois": ["plumber"]}
    if mario_profession in jurisdiction_requirement.get("Illinois", []):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())