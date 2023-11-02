def solution():
    # Calculate the caffeine in the first drink
    drink1_caffeine = 250

    # Calculate the caffeine per ounce in the second drink
    drink2_caffeine_per_ounce = 3 * drink1_caffeine / 1

    # Calculate the caffeine in the second drink
    drink2_caffeine = drink2_caffeine_per_ounce * 2

    # Calculate the total caffeine from the drinks
    drinks_total_caffeine = drink1_caffeine + drink2_caffeine

    # Calculate the caffeine in the pill
    pill_caffeine = drinks_total_caffeine

    # Calculate the total caffeine John consumed
    total_caffeine = drinks_total_caffeine + pill_caffeine

    result = total_caffeine
    return result

print(solution())