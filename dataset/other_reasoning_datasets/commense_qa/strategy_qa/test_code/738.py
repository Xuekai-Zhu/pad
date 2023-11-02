def solution():
    qwertyuiop = "qwertyuiop"
    if qwertyuiop == qwertyuiop[::-1]:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())