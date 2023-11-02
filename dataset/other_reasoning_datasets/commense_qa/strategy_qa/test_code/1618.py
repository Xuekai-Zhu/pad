def solution():
    grew_up_on_Gallifrey = True
    Gallifrey_was_destroyed = True
    ship_doesnt_require_docking = True
    if grew_up_on_Gallifrey and not Gallifrey_was_destroyed and not ship_doesnt_require_docking:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())