def solution():
    total_students = 450  # Sarah interviewed 450 students
    oranges = 70  # 70 students said they liked oranges
    pears = 120  # 120 students said they liked pears
    apples = 147  # 147 students said they liked apples

    # Calculate the number of students who picked strawberries as their favorite fruit
    strawberries = total_students - oranges - pears - apples
    result = strawberries
    return result

print(solution())