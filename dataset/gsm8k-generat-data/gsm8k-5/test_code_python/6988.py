def solution():
    max_caffeine = 500  # The maximum safe amount of caffeine per day is 500 mg
    caffeine_per_drink = 120  # Each energy drink has 120 mg of caffeine
    drinks_consumed = 4  # Brandy drinks 4 energy drinks

    # Calculate the total amount of caffeine Brandy has consumed
    total_caffeine = caffeine_per_drink * drinks_consumed

    # Calculate how much more caffeine Brandy can safely consume
    remaining_caffeine = max_caffeine - total_caffeine
    result = remaining_caffeine
    return result

print(solution())