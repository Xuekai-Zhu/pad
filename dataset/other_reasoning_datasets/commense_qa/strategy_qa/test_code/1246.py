def solution():
    dracula_birthplace = "Sighișoara, Romania"
    bucharest_distance = 276
    if "Bucharest" in dracula_birthplace or bucharest_distance < 0:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())