def solution():
    pittsburgh_steelers_colors = ["red", "gold", "blue"]
    doctor_strange_colors = ["red", "gold", "blue"]
    if set(doctor_strange_colors) == set(pittsburgh_steelers_colors):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())