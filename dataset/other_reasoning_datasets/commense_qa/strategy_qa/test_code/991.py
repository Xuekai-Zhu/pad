def solution():
    founder = "George Fox"
    beliefs = ["peace", "nonviolence"]
    punishment = "stoning"
    if punishment not in beliefs:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())