def solution():
    jennifer_middle_name = "Shrader"
    scorsese_collaborators = ["Schrader"]
    overlap = [name for name in scorsese_collaborators if name in jennifer_middle_name]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())