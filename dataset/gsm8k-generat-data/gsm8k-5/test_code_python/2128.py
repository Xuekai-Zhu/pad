def solution():
    cups_for_students = 200 * 10  # 200 students drink 10 cups each, so total cups needed for students is 2000
    jugs_needed = cups_for_students / 40  # Each jug is filled with 40 cups, so total jugs needed is cups needed divided by 40
    result = jugs_needed
    return result

print(solution())