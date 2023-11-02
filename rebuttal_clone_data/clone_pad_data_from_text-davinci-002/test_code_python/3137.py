def solution():
     num_students = 10
     score1 = 92
     score2 = 80
     Average_score = 85
     
     answer = (num_students * Average_score - (score1 + score2)) / (num_students - 2)
     result = answer
     return result

print(solution())