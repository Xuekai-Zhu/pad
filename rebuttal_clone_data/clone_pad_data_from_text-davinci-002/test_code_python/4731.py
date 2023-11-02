def solution():
    apples_eaten = 20
    apples_eaten_on_monday = 2
    apples_eaten_on_tuesday = apples_eaten_on_monday*2
    apples_eaten_on_thursday = apples_eaten_on_tuesday*4
    apples_eaten_on_friday = apples_eaten_on_monday/2
    apples_eaten_on_wednesday = apples_eaten - (apples_eaten_on_monday + apples_eaten_on_tuesday + apples_eaten_on_thursday + apples_eaten_on_friday)
    result = apples_eaten_on_wednesday
    return result

print(solution())