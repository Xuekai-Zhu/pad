def solution():
    mickey_wears_shirt = False
    zazzle_specializes_in_shirts = True
    if mickey_wears_shirt or not zazzle_specializes_in_shirts:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())