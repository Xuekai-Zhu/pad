def solution():
    cpu_has_dedicated_fan = True
    if cpu_has_dedicated_fan:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())