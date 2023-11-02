def solution():
     cards_transcribed = 200
     pay_per_card = 0.7
     bonus = 10
     total_pay = (cards_transcribed * pay_per_card) + (bonus * (cards_transcribed / 100))
     result = total_pay
     return result

print(solution())