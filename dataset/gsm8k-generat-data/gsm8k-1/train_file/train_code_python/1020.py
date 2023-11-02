def solution():
    """Porche has 3 hours to get all her homework done. Her math homework takes her 45 minutes. Her English homework takes her 30 minutes. Her science homework takes her 50 minutes. Her history homework takes her 25 minutes. She also has a special project due the next day. How much time does she have left to get that project done?"""
    total_time = 3 * 60  # 3 hours in minutes
    math_time = 45
    english_time = 30
    science_time = 50
    history_time = 25
    homework_time = math_time + english_time + science_time + history_time
    special_project_time = total_time - homework_time
    result = special_project_time
    return result

print(solution())