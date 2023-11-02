def solution():
    historic_enemies = ["Protestants", "Evangelicals"]
    christianity_in_china = ["Protestants", "Catholics", "Evangelicals", "Orthodox Christians"]
    overlap = [group for group in christianity_in_china if group in historic_enemies]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())