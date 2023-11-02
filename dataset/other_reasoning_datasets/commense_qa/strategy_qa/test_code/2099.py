def solution():
    lack_of_oxygen = True
    extreme_cold = True
    if lack_of_oxygen or extreme_cold:
        result = "no, blue lips are not normal"
    else:
        result = "yes, blue lips can be normal in certain situations"
    return result

print(solution())