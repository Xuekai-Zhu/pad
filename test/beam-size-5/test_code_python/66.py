def solution():
    num_classes_per_day = 5
    num_days_per_week = 5
    num_classes_per_saturday = 8
    num_students_per_class = 15
    price_per_student = 15.00

    # Calculate the total number of dance classes Judy teaches in a week
    total_classes = num_classes_per_day * num_days_per_week

    # Calculate the total number of dance classes Judy teaches in a week
    total_classes = num_classes_per_day * num_days_per_week

    # Calculate the total number of dance students Judy teaches in a week
    total_students = total_classes * num_students_per_class

    # Calculate the total revenue Judy makes in a week
    total_revenue = total_students * price_per_student
    result = total_revenue
    return result

print(solution())