def solution():
    # Calculate the total number of tomato seeds planted by Mike and Ted
    morning_seeds = 50 + 2 * 50  # Mike planted 50 seeds while Ted planted twice as much as Mike
    afternoon_seeds = 60 + 50 - 20  # Mike planted 60 seeds while Ted planted 20 fewer tomato seeds than Mike
    total_seeds_planted = morning_seeds + afternoon_seeds  # total number of tomato seeds planted
    result = total_seeds_planted
    return result

print(solution())