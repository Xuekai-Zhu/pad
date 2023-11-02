def solution():
    """In 6 years, Carla will be 30 years old. The sum of the current ages of Carla and Louis is 55. How old is Louis now?"""
    carla_future_age = 30
    carla_current_age = carla_future_age - 6
    total_age = 55
    louis_current_age = total_age - carla_current_age
    result = louis_current_age
    return result

print(solution())