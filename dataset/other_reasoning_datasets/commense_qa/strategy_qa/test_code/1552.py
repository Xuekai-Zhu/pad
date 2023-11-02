def solution():
    toyota_stadium_capacity = 45000
    gothenburg_population = 500000
    tenth_of_population = gothenburg_population/10
    if toyota_stadium_capacity >= tenth_of_population:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())