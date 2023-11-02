def solution():
    calories_planned = 1800  # Jacob planned to eat less than 1800 calories a day
    calories_breakfast = 400  # Jacob ate 400 calories for breakfast
    calories_lunch = 900  # Jacob ate 900 calories for lunch
    calories_dinner = 1100  # Jacob ate 1100 calories for dinner

    # Calculate the total calories Jacob ate
    calories_eaten = calories_breakfast + calories_lunch + calories_dinner

    # Calculate how many more calories Jacob ate than he planned
    calories_over = calories_eaten - calories_planned
    result = calories_over
    return result

print(solution())