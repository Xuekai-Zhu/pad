def solution():
    money_daily = 40
    deduction = 10
    money_earned = money_daily * 30
    money_after_taxes = money_earned - (money_earned * (deduction / 100))
    result = money_after_taxes
    return result

print(solution())