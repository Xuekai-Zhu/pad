def solution():
    oculudentavis_skull_size = 0.5 # in inches
    allosaurus_teeth = "saws"
    if oculudentavis_skull_size < 1 and allosaurus_teeth == "saws":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())