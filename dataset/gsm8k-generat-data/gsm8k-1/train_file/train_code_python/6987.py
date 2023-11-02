def solution():
    """The maximum safe amount of caffeine you can consume per day is 500 mg. If each energy drink has 120 mg of caffeine and Brandy drinks 4 of them, how much more caffeine can she safely consume that day?"""
    max_caffeine = 500
    caffeine_per_drink = 120
    drinks_consumed = 4
    total_caffeine = caffeine_per_drink * drinks_consumed
    remaining_caffeine = max_caffeine - total_caffeine
    result = remaining_caffeine
    return result

print(solution())