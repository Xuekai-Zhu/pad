def solution():
 
    percent = 80
    mistakes = 5
    quiz_length = mistakes / (1 - (percent/100))
    result = quiz_length
 
    return result

print(solution())