def solution():
    """Marco has $24. Mary has $15. If Marco gives Mary half of what he has, Mary will have more than Marco. But Mary spends $5. How much more money does Mary have than Marco?"""
    marco_money = 24
    mary_money = 15
    marco_money_after_gift = marco_money - (marco_money / 2)
    mary_money_after_gift = mary_money + (marco_money / 2)
    mary_money_after_spending = mary_money_after_gift - 5
    difference = mary_money_after_spending - marco_money_after_gift
    result = difference
    return result

print(solution())