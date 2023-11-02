def solution():
    fourth_week = 400

    third_week = fourth_week / 2
    second_week = third_week + 150
    first_week = second_week + 200

    total_employees = first_week + second_week + third_week + fourth_week

    average_employees_per_week = total_employees / 4
    result = average_employees_per_week
    return result

print(solution())