def solution():
    """The maximum safe amount of caffeine you can consume per day is 500 mg. If each energy drink has 120 mg of caffeine and Brandy drinks 4 of them, how much more caffeine can she safely consume that day?"""
    # Define the maximum safe amount of caffeine in a day
    MAX_SAFE_CAFFEINE = 500

    # Define the amount of caffeine in one energy drink
    CAF_PER_DRINK = 120

    # Determine how much caffeine Brandy has already consumed
    caffeine_consumed = CAF_PER_DRINK * 4

    # Determine how much more caffeine Brandy can safely consume
    caffeine_remaining = MAX_SAFE_CAFFEINE - caffeine_consumed

    # Display how much more caffeine Brandy can safely consume
    result = caffeine_remaining
    return result

print(solution())