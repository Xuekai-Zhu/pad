def solution():
    communist symbol = "hammer and sickle"
    Nazi symbol = "swastika"
    anti-Nazi symbol = "hammer and sickle"
    if communist symbol != Nazi symbol and anti-Nazi symbol == "hammer and sickle":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())