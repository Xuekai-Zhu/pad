def solution():
    """James takes a spinning class 3 times a week.  He works out for 1.5 hours each class and burns 7 calories per minute.  How many calories does he burn per week?"""
    # Define the number of spinning classes per week, workout time per class, and burn rate
    NUM_CLASSES = 3
    WORKOUT_TIME = 1.5 * 60  # 1.5 hours converted to minutes
    BURN_RATE = 7

    # Calculate the total calories burned per week
    calories_burned = NUM_CLASSES * WORKOUT_TIME * BURN_RATE

    # Display the total number of calories burned per week
    result = calories_burned
    return result

print(solution())