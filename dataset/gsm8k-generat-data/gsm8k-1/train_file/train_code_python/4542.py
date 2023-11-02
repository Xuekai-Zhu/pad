def solution():
    """Sarah interviewed 450 students at her school and asked them which fruit they liked best - oranges, apples, pears or strawberries. 70 students said they liked oranges, 120 students said they liked pears, and 147 students said they liked apples. How many students picked strawberries as their favorite fruit from the list?"""
    total_students = 450
    oranges = 70
    pears = 120
    apples = 147
    strawberries = total_students - (oranges + pears + apples)
    result = strawberries
    return result

print(solution())