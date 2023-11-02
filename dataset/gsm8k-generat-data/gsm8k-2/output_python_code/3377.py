def solution():
    """Krista started raising chickens. She has 10 hens who lay eggs. She sells the eggs for $3 a dozen. In four weeks, she sold $120 worth of eggs. If she sold all the eggs her hens laid, how many eggs does each hen lay a week?"""
    hens = 10
    egg_price = 3 / 12
    total_egg_count = 120 / egg_price
    egg_per_week_per_hen = total_egg_count / (hens * 4)
    result = egg_per_week_per_hen
    return result

print(solution())