def solution():
    """Haley is making cider. It takes 20 golden delicious apples and 40 pink lady apples to make one pint of cider. Each of her 6 farmhands can pick 240 apples per hour and will work 5 hours today. How many pints of cider can Haley make with the apples gathered today, provided that the ratio of golden delicious apples to pink lady apples gathered is 1:2?"""
    apples_per_pint = 20 + 40*2  # 100 apples per pint
    farmhands = 6
    apples_per_hour_per_farmhand = 240
    hours_worked = 5
    total_apples = farmhands * apples_per_hour_per_farmhand * hours_worked
    golden_delicious_ratio = 1 / (1 + 2)  # 1/3
    pink_lady_ratio = 2 / (1 + 2)  # 2/3
    golden_delicious_apples = total_apples * golden_delicious_ratio
    pink_lady_apples = total_apples * pink_lady_ratio
    pints = min(golden_delicious_apples / 20, pink_lady_apples / 40)
    result = pints
    return result

print(solution())