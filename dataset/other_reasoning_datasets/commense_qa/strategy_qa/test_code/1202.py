def solution():
    wembley_capacity = 90000
    descendants_of_Genghis_Khan = wembley_capacity / 200
    if descendants_of_Genghis_Khan >= 1:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())