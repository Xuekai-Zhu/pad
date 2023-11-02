def solution():
    """Sara makes cakes during the five weekdays to sell on weekends. She makes 4 cakes a day and sells her cakes for $8. In 4 weeks she managed to sell all the cakes. How much money did she collect during that time?"""
    weekdays = 5
    cakes_per_day = 4
    price_per_cake = 8
    total_cakes = weekdays * cakes_per_day * 4
    total_money = total_cakes * price_per_cake
    result = total_money
    return result

print(solution())