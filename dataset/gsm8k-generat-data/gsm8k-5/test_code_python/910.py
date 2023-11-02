def solution():
    jugs_per_day = 1/2  # John buys 1/2 gallon jugs of coffee every 4 days, so he drinks 1/2 jug per day
    cups_per_jug = 16  # There are 16 cups in a half-gallon jug
    cups_per_day = jugs_per_day * cups_per_jug  # Calculate the number of cups John drinks per day

    result = cups_per_day
    return result

print(solution())