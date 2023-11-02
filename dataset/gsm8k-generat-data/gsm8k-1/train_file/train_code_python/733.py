def solution():
    """Chang's Garden has two kinds of apples. Sweet ones and sour ones. He can sell the sweet ones for $.5 an apple. The sour ones sell for $.1 an apple. 75% of the apples he gets are sweet and the rest are sour. If he earns $40, how many apples did his trees give him?"""
    sweet_apples_percentage = 0.75
    sour_apples_percentage = 1 - sweet_apples_percentage
    sweet_apple_price = 0.5
    sour_apple_price = 0.1
    total_earnings = 40
    total_apples = (total_earnings - (sour_apples_percentage * sour_apple_price * total_earnings)) / (sweet_apples_percentage * sweet_apple_price)
    result = total_apples
    return result

print(solution())