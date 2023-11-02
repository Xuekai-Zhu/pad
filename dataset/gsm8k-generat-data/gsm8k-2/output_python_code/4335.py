def solution():
    """Running for 2 hours, Jonah burnt 30 calories every hour. How many more calories would he have lost if he would have run for five hours?"""
    current_time = 2
    current_calories = current_time * 30
    new_time = 5
    new_calories = new_time * 30
    difference = new_calories - current_calories
    result = difference
    return result

print(solution())