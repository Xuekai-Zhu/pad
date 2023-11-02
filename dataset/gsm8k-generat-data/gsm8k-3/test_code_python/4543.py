def solution():
    """Sarah interviewed 450 students at her school and asked them which fruit they liked best - oranges, apples, pears or strawberries. 70 students said they liked oranges, 120 students said they liked pears, and 147 students said they liked apples. How many students picked strawberries as their favorite fruit from the list?"""
    # Define the number of students who liked each fruit
    ORANGE_LOVERS = 70
    PEAR_LOVERS = 120
    APPLE_LOVERS = 147

    # Calculate the number of students who picked strawberries as their favorite
    strawberry_lovers = 450 - ORANGE_LOVERS - PEAR_LOVERS - APPLE_LOVERS

    # Display the number of students who picked strawberries
    result = strawberry_lovers
    return result

print(solution())