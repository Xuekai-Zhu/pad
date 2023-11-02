def solution():
    sheets_per_class_per_week = 200 * 5  # 1000 sheets used by one class in a week
    total_sheets_per_week = 9000
    num_classes = total_sheets_per_week / sheets_per_class_per_week
    result = num_classes
    return result

print(solution())