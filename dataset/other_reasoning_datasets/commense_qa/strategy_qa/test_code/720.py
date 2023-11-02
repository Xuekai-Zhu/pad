def solution():
    loves_roses = True
    allergic_to_flowers = False
    if loves_roses and not allergic_to_flowers:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())