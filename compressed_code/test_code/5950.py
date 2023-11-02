def solution():
    
    mike_morning = 50
    ted_morning = 2 * mike_morning
    mike_afternoon = 60
    ted_afternoon = mike_afternoon - 20
    total_seeds = mike_morning + ted_morning + mike_afternoon + ted_afternoon
    result = total_seeds
    return result

print(solution())