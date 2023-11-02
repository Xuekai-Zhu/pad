def solution():
    """Sarah interviewed 450 students at her school and asked them which fruit they liked best - oranges, apples, pears or strawberries. 70 students said they liked oranges, 120 students said they liked pears, and 147 students said they liked apples. How many students picked strawberries as their favorite fruit from the list?"""
    # Define the total number of students interviewed
    total_students = 450

    # Calculate the number of students who picked oranges, pears, and apples
    orange_students = 70
    pear_students = 120
    apple_students = 147

    # Calculate the number of students who picked strawberries
    strawberry_students = total_students - orange_students - pear_students - apple_students

    # Return the result
    result = strawberry_students
    return result

print(solution())