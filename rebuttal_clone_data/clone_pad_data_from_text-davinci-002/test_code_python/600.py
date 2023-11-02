def solution():
     initial_wpm = 65
     wpm_decrease = 20
     new_wpm = initial_wpm - wpm_decrease
     document_length = 810
     minutes_to_type = document_length / new_wpm
     result = minutes_to_type
     return result

print(solution())