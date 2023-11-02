def solution():
    """Tanya is teaching at school. She earns $15 for every hour and an additional $5 per day if she teaches more than 3 classes. On Monday she teaches 4 classes for 5 hours, and on Wednesday 2 classes for 2 hours. How much did Tanya earn for these two days of teaching?"""
    class_rate = 15
    extra_pay = 5
    monday_classes = 4
    monday_hours = 5
    wednesday_classes = 2
    wednesday_hours = 2
    monday_pay = monday_classes * class_rate * monday_hours + extra_pay
    wednesday_pay = wednesday_classes * class_rate * wednesday_hours
    total_pay = monday_pay + wednesday_pay
    result = total_pay
    return result

print(solution())