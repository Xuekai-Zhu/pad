def solution():
    # Calculate the number of tomato seeds planted by Mike and Ted in the morning
    mike_morning = 50
    ted_morning = 2 * mike_morning

    # Calculate the number of tomato seeds planted by Mike and Ted in the afternoon
    mike_afternoon = 60
    ted_afternoon = mike_afternoon - 20

    # Calculate the total number of tomato seeds planted by Mike and Ted
    total_seeds = mike_morning + ted_morning + mike_afternoon + ted_afternoon
    result = total_seeds
    return result

print(solution())