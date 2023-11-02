def solution():
    animals_require_oxygen = True
    mount_sharp_has_no_oxygen = True
    if animals_require_oxygen and mount_sharp_has_no_oxygen:
        result = "no"
    else:
        result = "uncertain"
    return result

print(solution())