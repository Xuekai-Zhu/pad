def solution():
    need_for_curling = ["curling brooms", "stones (rocks)", "curling shoes"]
    need_for_curly hair = ["curling iron"]
    overlap = [item for item in need_for_curling if item in need_for_curly hair]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())