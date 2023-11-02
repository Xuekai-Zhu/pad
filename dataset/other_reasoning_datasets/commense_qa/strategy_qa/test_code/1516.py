def solution():
    location = "Atacama Desert"
    dangerous_conditions = ["extreme heat", "lack of water"]
    if location == "Atacama Desert" and dangerous_conditions:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())