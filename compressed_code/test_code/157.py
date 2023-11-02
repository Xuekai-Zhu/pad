def solution():
    
    mike_morning_planted = 50
    ted_morning_planted = 2 * mike_morning_planted
    mike_afternoon_planted = 60
    ted_afternoon_planted = mike_afternoon_planted - 20
    total_planted = mike_morning_planted + ted_morning_planted + mike_afternoon_planted + ted_afternoon_planted
    result = total_planted
    return result

print(solution())