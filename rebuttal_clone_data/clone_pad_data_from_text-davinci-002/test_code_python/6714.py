def solution():
    grades = ["B+", "A", "A", "A", "A", "A", "A", "A", "A", "A+"]
    rewards = []
    for grade in grades:
        if grade == "B+":
            rewards.append(5)
        elif grade == "A":
            rewards.append(10)
        elif grade == "A+":
            rewards.append(15)
    print(rewards)
    result = sum(rewards)
    return result

print(solution())