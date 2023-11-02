def solution():
    """Running for 2 hours, Jonah burnt 30 calories every hour. How many more calories would he have lost if he would have run for five hours?"""
    hours_run = 2
    calories_per_hour = 30
    total_calories_burnt = hours_run * calories_per_hour
    
    additional_hours = 5 - hours_run
    additional_calories_burnt = additional_hours * calories_per_hour
    
    total_additional_calories_burnt = additional_calories_burnt - total_calories_burnt
    
    result = total_additional_calories_burnt
    return result

print(solution())