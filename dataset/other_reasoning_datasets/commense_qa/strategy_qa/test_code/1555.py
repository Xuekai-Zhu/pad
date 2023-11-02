def solution():
    shuttlecock_material = "feathers"
    birds_have_feathers = True
    if shuttlecock_material in ("feathers", "bird feathers") and birds_have_feathers:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())