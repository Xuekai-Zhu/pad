def solution():
     milligrams_per_pill = 50
     recommended_amount = 200
     amount_per_week = recommended_amount * 7
     pills_needed = amount_per_week / milligrams_per_pill
     result = pills_needed
     
     return result

print(solution())