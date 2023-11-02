def solution():
     mistakes_sylvia = 1/5
     mistakes_sergio = 4
     total_questions = 50
     mistakes_sylvia_total = total_questions * mistakes_sylvia
     mistakes_sergio_total = total_questions * mistakes_sergio
     correct_sylvia = total_questions - mistakes_sylvia_total
     correct_sergio = total_questions - mistakes_sergio
     result = correct_sergio - correct_sylvia
     return result

print(solution())