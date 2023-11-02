def solution():
    """Milo's parents tell him that he can win cash rewards for good grades. He will get $5 times the average grade he gets. He gets three 2s, four 3s, a 4, and a 5. How much cash does he get?"""
    grades = [2, 2, 2, 3, 3, 3, 3, 4, 5]
    average_grade = sum(grades) / len(grades)
    cash_reward = average_grade * 5
    result = cash_reward
    return result

print(solution())