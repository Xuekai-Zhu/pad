def solution():
    max_caffeine = 500
    caffeine_per_drink = 120
    num_drinks = 4

    # Calculate the total caffeine Brandy consumed
    total_caffeine = caffeine_per_drink * num_drinks

    # Calculate how much more caffeine Brandy can safely consume
    remaining_caffeine = max_caffeine - total_caffeine
    result = remaining_caffeine
    return result

print(solution())