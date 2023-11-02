def solution():
    inexperienced_pay = 10
    experienced_pay = inexperienced_pay * 5
    weekly_hours = 60
    number_of_inexperienced_sailors = 5
    number_of_experienced_sailors = 12
    total_inexperienced_pay = inexperienced_pay * weekly_hours * number_of_inexperienced_sailors
    total_experienced_pay = experienced_pay * weekly_hours * number_of_experienced_sailors
    result = total_inexperienced_pay + total_experienced_pay
    return result

print(solution())