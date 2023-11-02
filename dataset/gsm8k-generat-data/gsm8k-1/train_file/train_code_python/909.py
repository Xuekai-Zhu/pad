def solution():
    """John buys 1/2 gallon jugs of cold brew coffee every 4 days. How many cups of coffee does he drink a day?"""
    jugs_per_day = 1/2 / 4
    cups_per_jug = 16
    cups_per_day = jugs_per_day * cups_per_jug
    result = cups_per_day
    return result

print(solution())