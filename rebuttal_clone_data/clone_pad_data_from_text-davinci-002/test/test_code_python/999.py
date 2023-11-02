def solution():
     lizzie_score = 4
     nathalie_score = lizzie_score + 3
     aimee_score = (lizzie_score + nathalie_score) * 2
     total_score = 50
     teammates_score = total_score - (lizzie_score + nathalie_score + aimee_score)
     result = teammates_score
     return result

print(solution())