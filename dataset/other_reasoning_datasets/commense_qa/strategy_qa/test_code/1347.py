def solution():
    yin_yang_colors = ["black", "white"]
    rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    mix_of_yin_yang = set(yin_yang_colors) & set(rainbow_colors)
    if mix_of_yin_yang == {"black", "white"}:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())