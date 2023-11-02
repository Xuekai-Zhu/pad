def solution():
    number_students = 30
    desired_percent = 60
    actual_number = number_students * (desired_percent / 100)
    money_spent = actual_number * 2
    total_money = 40
    percentage_spent = (money_spent / total_money) * 100
    result = percentage_spent
    return result

print(solution())