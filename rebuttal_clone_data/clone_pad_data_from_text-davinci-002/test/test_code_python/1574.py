def solution():
     score_1 = 80
     score_2 = 70
     score_3 = 90
     desired_average = 85
     average_score = (score_1 + score_2 + score_3) / 3
     score_4 = desired_average * 4 - (score_1 + score_2 + score_3)
     result = score_4
     return result

print(solution())