def solution():
    total_students = 500
    percent_juniors = 40
    percent_sporty_juniors = 70
    juniors = total_students * (percent_juniors / 100)
    sporty_juniors = juniors * (percent_sporty_juniors / 100)
    result = sporty_juniors
    
    return result

print(solution())