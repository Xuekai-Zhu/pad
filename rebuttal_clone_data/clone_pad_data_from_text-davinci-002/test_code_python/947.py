def solution():
    current_practice = 2
    goal_practice = current_practice * 3
    days_passed = 0
    while current_practice < goal_practice:
        days_passed += 1
        current_practice += 1
    result = days_passed
    return result

print(solution())