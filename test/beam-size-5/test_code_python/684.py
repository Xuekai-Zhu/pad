def solution():
    
    math_homework = 20
    reading_homework = 40
    history_homework = 20
    total_homework_time = math_homework + reading_homework + history_homework
    hours_to_eat_dinner = 3 * 60
    nap_time = total_homework_time - hours_to_eat_dinner
    result = nap_time
    return result

print(solution())