def solution():
    
    sally_eggs_per_week = 10
    ben_eggs_per_week = 14
    ked_eggs_per_week = ben_eggs_per_week / 2
    eggs_per_week = sally_eggs_per_week + ben_eggs_per_week + ked_eggs_per_week
    eggs_per_month = eggs_per_week * 4
    result = eggs_per_month
    return result

print(solution())