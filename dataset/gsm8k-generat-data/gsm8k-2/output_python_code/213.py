def solution():
    """Mike and Ted planted tomatoes. In the morning, Mike planted 50 tomato seeds while Ted planted twice as much as Mike.
    In the afternoon, Mike planted 60 tomato seeds while Ted planted 20 fewer tomato seeds than Mike. 
    How many tomato seeds did they plant altogether?"""
    mike_morning_planted = 50
    ted_morning_planted = 2 * mike_morning_planted
    mike_afternoon_planted = 60
    ted_afternoon_planted = mike_afternoon_planted - 20
    total_planted = mike_morning_planted + ted_morning_planted + mike_afternoon_planted + ted_afternoon_planted
    result = total_planted
    return result

print(solution())