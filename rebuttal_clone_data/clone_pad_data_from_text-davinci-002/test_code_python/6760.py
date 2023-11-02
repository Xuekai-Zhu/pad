def solution():
    hotdogs_ella = 2
    hotdogs_emma = 2
    hotdogs_luke = 2 * (hotdogs_ella + hotdogs_emma)
    hotdogs_hunter = (hotdogs_ella + hotdogs_emma) * 1.5
    total_hotdogs = hotdogs_ella + hotdogs_emma + hotdogs_luke + hotdogs_hunter
    result = total_hotdogs
    return result

print(solution())