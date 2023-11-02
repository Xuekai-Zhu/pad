def solution():
    """Phillip is taking a math test and an English test on Monday. The math test has 40 questions and he gets 75% of them right. The English test has 50 questions and he gets 98% of them right. How many total questions does he get right?"""
    math_questions = 40
    math_percent_correct = 75
    english_questions = 50
    english_percent_correct = 98
    
    math_correct = math_questions * (math_percent_correct/100)
    english_correct = english_questions * (english_percent_correct/100)
    
    total_correct = math_correct + english_correct
    result = total_correct
    
    return result

print(solution())