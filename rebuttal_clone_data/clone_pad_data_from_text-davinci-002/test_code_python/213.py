def solution():
    """Mike and Ted planted tomatoes. In the morning, Mike planted 50 tomato seeds while Ted planted twice as much as Mike. In the afternoon, Mike planted 60 tomato seeds while Ted planted 20 fewer tomato seeds than Mike. How many tomato seeds did they plant altogether?"""
    mike_seeds_morning = 50
    ted_seeds_morning = mike_seeds_morning * 2
    mike_seeds_afternoon = 60
    ted_seeds_afternoon = mike_seeds_afternoon - 20
    total_mike_seeds = mike_seeds_morning + mike_seeds_afternoon
    total_ted_seeds = ted_seeds_morning + ted_seeds_afternoon
    total_seeds = total_mike_seeds + total_ted_seeds
    result = total_seeds
    return result

print(solution())