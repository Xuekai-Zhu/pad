def solution():
    """Mike and Ted planted tomatoes. In the morning, Mike planted 50 tomato seeds while Ted planted twice as much as Mike. In the afternoon, Mike planted 60 tomato seeds while Ted planted 20 fewer tomato seeds than Mike. How many tomato seeds did they plant altogether?"""
    mike_morning = 50
    ted_morning = 2 * mike_morning
    mike_afternoon = 60
    ted_afternoon = mike_afternoon - 20
    total_seeds = mike_morning + ted_morning + mike_afternoon + ted_afternoon
    result = total_seeds
    return result

print(solution())