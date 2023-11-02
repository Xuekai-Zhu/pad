def solution():
    fear = True
    caffeine = True
    espresso = True
    if fear and caffeine and not espresso:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())