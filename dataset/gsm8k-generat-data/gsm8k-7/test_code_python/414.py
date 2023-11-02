def solution():
    # First drink
    drink1_size = 12  # ounces
    drink1_caffeine = 250  # grams

    # Second drink
    drink2_size = 2  # ounces
    drink2_caffeine_per_ounce = drink1_caffeine / (drink1_size * 3)

    # Total caffeine from second drink
    drink2_caffeine = drink2_size * drink2_caffeine_per_ounce

    # Total caffeine from both drinks
    total_caffeine = drink1_caffeine + drink2_caffeine

    # Caffeine pill
    caffeine_pill_caffeine = total_caffeine

    # Total caffeine consumed
    caffeine_consumed = total_caffeine + caffeine_pill_caffeine
    result = caffeine_consumed
    return result

print(solution())