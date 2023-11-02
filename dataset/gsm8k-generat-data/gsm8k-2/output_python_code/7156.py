def solution():
    """Haley is making cider. It takes 20 golden delicious apples and 40 pink lady apples to make one pint of cider. Each of her 6 farmhands can pick 240 apples per hour and will work 5 hours today. How many pints of cider can Haley make with the apples gathered today, provided that the ratio of golden delicious apples to pink lady apples gathered is 1:2?"""
    golden_ratio = 1
    pink_ratio = 2
    total_ratio = golden_ratio + pink_ratio
    total_hours = 5
    apples_per_hour = 240
    total_apples = total_hours * apples_per_hour * 6
    golden_apples = (golden_ratio/total_ratio) * total_apples
    pink_apples = (pink_ratio/total_ratio) * total_apples
    cider_per_pint = 20 + 40
    total_cider = min(golden_apples/20, pink_apples/40)
    result = total_cider
    return result

print(solution())