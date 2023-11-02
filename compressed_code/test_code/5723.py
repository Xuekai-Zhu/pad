def solution():
    
    boy_squirrel_walnuts = 6
    girl_squirrel_walnuts = 5
    initial_walnuts = 12
    dropped_walnuts = 1
    eaten_walnuts = 2

    total_walnuts = initial_walnuts + boy_squirrel_walnuts + girl_squirrel_walnuts - dropped_walnuts - eaten_walnuts
    result = total_walnuts
    return result

print(solution())