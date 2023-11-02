def solution():
     grades = [2, 2, 2, 3, 3, 3, 3, 4, 5]
     average = sum(grades) / len(grades)
     cash_reward = 5 * average
     result = cash_reward
     return result

print(solution())