def solution():
    golf_balls_by_dozen = 3
    charge_by_dozen = 30
    dozens_bought_by_dan = 5
    dozens_bought_by_gus = 2
    golf_balls_bought_by_chris = 4
    total_golf_balls = (dozens_bought_by_dan * golf_balls_by_dozen) + (dozens_bought_by_gus * golf_balls_by_dozen) + (golf_balls_bought_by_chris * golf_balls_by_dozen)
    result = total_golf_balls
    return result

print(solution())