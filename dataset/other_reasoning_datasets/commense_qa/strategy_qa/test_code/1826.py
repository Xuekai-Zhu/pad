def solution():
    potentially_lethal_projects = ["deep fried turkey", "home roofing repair"]
    safety_gear_required = {"deep fried turkey": False, "home roofing repair": True}
    result = ""
    for project in potentially_lethal_projects:
        if safety_gear_required[project]:
            result += f"{project} can be lethal without proper safety gear. "
        else:
            result += f"{project} can be dangerous if not done carefully. "
    return result

print(solution())