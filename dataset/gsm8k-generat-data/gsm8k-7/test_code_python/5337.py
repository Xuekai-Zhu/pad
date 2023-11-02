def solution():
    total_earned = 37
    evan_earned = (total_earned + 5) / 2  # since Markese earned 5 fewer dollars than Evan, Evan's earnings = (Markese's earnings + 5)
    markese_earned = evan_earned - 5
    result = markese_earned
    return result

print(solution())