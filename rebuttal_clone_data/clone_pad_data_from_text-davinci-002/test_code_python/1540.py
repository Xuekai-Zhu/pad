def solution():
     money_ invested = 10000
     interest_rate = 20
     years = 3
     money_ tripled = money_invested * 3
     interest_earned = money_tripled * (interest_rate / 100)
     money_after_four_years = money_tripled + interest_earned
     money_at_15_percent = money_after_four_years * 1.15
     result = money_at_15_percent
     return result

print(solution())