def solution():
    
    monday_spent = 6
    tuesday_spent = 2 * monday_spent
    wednesday_spent = 2 * (monday_spent + tuesday_spent)
    total_spent = monday_spent + tuesday_spent + wednesday_spent
    result = total_spent
    return result

print(solution())