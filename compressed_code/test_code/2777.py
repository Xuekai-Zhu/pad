def solution():
    
    total_planted = 1200
    first_day_planted = 200
    second_day_planted = 2 * first_day_planted
    remi_planted = first_day_planted + second_day_planted
    father_planted = total_planted - remi_planted
    result = father_planted
    return result

print(solution())