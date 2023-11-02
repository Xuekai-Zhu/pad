def solution():
    """Running for 2 hours, Jonah burnt 30 calories every hour. How many more calories would he have lost if he would have run for five hours?"""
    # Define the calories burnt per hour
    CALORIES_PER_HOUR = 30

    # Calculate the total number of calories burnt in two hours
    calories_2_hours = CALORIES_PER_HOUR * 2

    # Calculate the total number of calories burnt in five hours
    calories_5_hours = CALORIES_PER_HOUR * 5

    # Calculate the difference in calories burnt between 5 and 2 hours
    calories_difference = calories_5_hours - calories_2_hours

    # Display the difference in calories burnt
    result = calories_difference
    return result

print(solution())