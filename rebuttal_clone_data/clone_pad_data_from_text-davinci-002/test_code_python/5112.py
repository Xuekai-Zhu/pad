def solution():
     pieces_of_paper = 5
     folds = 3
     notes_per_day = 10
     days_per_notepad = pieces_of_paper * folds / notes_per_day
     result = days_per_notepad
     return result

print(solution())