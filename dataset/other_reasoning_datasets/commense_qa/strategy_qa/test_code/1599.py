def solution():
    panda_colors = ["black", "white"]
    yin_yang_colors = ["black", "white"]
    if set(panda_colors) == set(yin_yang_colors):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())