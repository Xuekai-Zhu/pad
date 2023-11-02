def solution():
    giant_monument_height = 55.5
    pyrenees_height = 11168
    pyrenees_width = 305
    if giant_monument_height < pyrenees_height and giant_monument_height > pyrenees_width:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())