def solution():
    """To have the car for the weekend, Wilson's report card needs to show that he received 80 or higher in his math class. His math grade is calculated by the average of 5 test scores. On those tests, he received: 65, 94, 81, 86 and 74. What is his current math grade?"""
    test_scores = [65, 94, 81, 86, 74]
    total_score = sum(test_scores)
    grade = total_score / len(test_scores)
    result = grade
    return result

print(solution())