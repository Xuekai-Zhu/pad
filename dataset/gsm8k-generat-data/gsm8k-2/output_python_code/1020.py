def solution():
    """ Porsche has 3 hours to get all her homework done. Her math homework takes her 45 minutes. Her English homework takes her 30 minutes. Her science homework takes her 50 minutes. Her history homework takes her 25 minutes. She also has a special project due the next day. How much time does she have left to get that project done? """
    total_homework_time = (45 + 30 + 50 + 25) / 60
    time_left = 3 - total_homework_time
    result = time_left
    return result

print(solution())