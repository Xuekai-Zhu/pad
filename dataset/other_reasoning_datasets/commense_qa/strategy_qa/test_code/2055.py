def solution():
    scar_minions = "hyenas"
    broadway_version = True
    if broadway_version:
        result = f"Yes, {scar_minions} appear in the Broadway musical."
    else:
        result = "No, there are no hyenas in the Broadway musical."
    return result

print(solution())