def solution():
     total_questions = 100
     lowella_score = 35
     pamela_score = lowella_score + (lowella_score * 20 / 100)
     mandy_score = pamela_score * 2
     result = mandy_score
     return result

print(solution())