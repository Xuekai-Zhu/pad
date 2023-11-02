def solution():
    # Calculate the amount of caffeine Brandy consumed from energy drinks
    caffeine_consumed = 120 * 4  # each energy drink has 120 mg of caffeine

    # Calculate the amount of caffeine Brandy can still consume safely
    caffeine_safely_consumed = 500 - caffeine_consumed
    result = caffeine_safely_consumed
    return result

print(solution())