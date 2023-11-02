def solution():
    """Running for 2 hours, Jonah burnt 30 calories every hour. How many more calories would he have lost if he would have run five hours?"""
    # Define the initial number of calories burned and the number of hours run
    calories_burned = 30 * 2
    hours_run = 5

    # Calculate the new number of calories burned if running for 5 hours
    new_calories_burned = 30 * hours_run

    # Calculate the difference in calories burned between running for 2 hours and running for 5 hours
    difference = new_calories_burned - calories_burned

    # return the result
    result = difference
    return result

print(solution())