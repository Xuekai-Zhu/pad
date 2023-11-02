def solution():
    """The maximum safe amount of caffeine you can consume per day is 500 mg. If each energy drink has 120 mg of caffeine and Brandy drinks 4 of them, how much more caffeine can she safely consume that day?"""
    # Define the maximum safe amount of caffeine and the amount of caffeine in one energy drink
    MAX_SAFE_CAFFEINE = 500
    CAF_IN_ONE_DRINK = 120

    # Calculate the total amount of caffeine in the energy drinks Brandy consumed
    total_caffeine = CAF_IN_ONE_DRINK * 4

    # Calculate how much more caffeine Brandy can safely consume
    remaining_caffeine = MAX_SAFE_CAFFEINE - total_caffeine

    # Return the result
    result = remaining_caffeine
    return result

print(solution())