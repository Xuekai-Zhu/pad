def solution():
    """Mike and Ted planted tomatoes. In the morning, Mike planted 50 tomato seeds while Ted planted twice as much as Mike. In the afternoon, Mike planted 60 tomato seeds while Ted planted 20 fewer tomato seeds than Mike. How many tomato seeds did they plant altogether? """
    # Calculate the number of tomato seeds planted by Mike in the morning and afternoon
    mike_morning = 50
    mike_afternoon = 60

    # Calculate the total number of tomato seeds planted by Mike
    mike_total = mike_morning + mike_afternoon

    # Calculate the number of tomato seeds planted by Ted in the morning and afternoon
    ted_morning = 2 * mike_morning
    ted_afternoon = mike_afternoon - 20

    # Calculate the total number of tomato seeds planted by Ted
    ted_total = ted_morning + ted_afternoon

    # Calculate the total number of tomato seeds planted by both Mike and Ted
    total_seeds = mike_total + ted_total

    result = total_seeds
    return result

print(solution())