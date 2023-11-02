def solution():
    marvin_yesterday = 40  # Marvin solved 40 problems yesterday
    marvin_today = 3 * marvin_yesterday  # Marvin solved 3 times as many problems as yesterday
    arvin_today = 2 * marvin_today  # Arvin solved twice as many problems as Marvin today

    # Calculate the total number of problems they solved altogether
    total_problems = marvin_yesterday + marvin_today + arvin_today
    result = total_problems
    return result

print(solution())