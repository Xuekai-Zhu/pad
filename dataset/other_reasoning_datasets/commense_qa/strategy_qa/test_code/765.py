def solution():
    maya_angelou_children = ["Guy Johnson"]
    guy_johnson_explores_civil_rights = True
    for child in maya_angelou_children:
        if "author" in child.lower() and guy_johnson_explores_civil_rights:
            result = "yes"
            break
    else:
        result = "no"
    return result

print(solution())