def solution():
    """Mike and Ted planted tomatoes.  In the morning, Mike planted 50 tomato seeds while Ted planted twice as much as Mike.  In the afternoon, Mike planted 60 tomato seeds while Ted planted 20 fewer tomato seeds than Mike. How many tomato seeds did they plant altogether?"""
    # Calculate the number of seeds planted by Mike and Ted in the morning
    mike_morning_seeds = 50
    ted_morning_seeds = mike_morning_seeds * 2

    # Calculate the number of seeds planted by Mike and Ted in the afternoon
    mike_afternoon_seeds = 60
    ted_afternoon_seeds = mike_afternoon_seeds - 20

    # Calculate the total number of seeds planted by Mike and Ted
    total_seeds_planted = mike_morning_seeds + ted_morning_seeds + mike_afternoon_seeds + ted_afternoon_seeds

    # Display the total number of seeds planted
    result = total_seeds_planted
    return result

print(solution())