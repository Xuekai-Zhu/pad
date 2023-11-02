def solution():
    boy_squirrel_walnuts = 6
    girl_squirrel_walnuts = 5
    initial_walnuts = 12
    walnuts_dropped = 1
    walnuts_eaten = 2
    total_walnuts = boy_squirrel_walnuts + girl_squirrel_walnuts + initial_walnuts - walnuts_dropped - walnuts_eaten
    result = total_walnuts
    return result

print(solution())