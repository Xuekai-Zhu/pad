def solution():
    
    drink1_ounces = 12
    drink1_caffeine = 250
    drink2_ounces = 2
    drink2_caffeine_per_ounce = 3 * drink1_caffeine / drink1_ounces
    drink2_caffeine = drink2_caffeine_per_ounce * drink2_ounces
    total_caffeine = drink1_caffeine + drink2_caffeine
    caffeine_pill = total_caffeine
    total_caffeine += caffeine_pill
    result = total_caffeine
    return result

print(solution())