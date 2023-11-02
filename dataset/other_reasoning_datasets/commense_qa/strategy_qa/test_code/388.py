def solution():
    homeless_population = 8575
    stadium_capacity = 45000
    if stadium_capacity >= homeless_population:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())