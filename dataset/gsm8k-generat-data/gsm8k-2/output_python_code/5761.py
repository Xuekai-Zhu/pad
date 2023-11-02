def solution():
    """The school nurse must conduct lice checks at the elementary school. She must check 26 Kindergarteners, 19 first graders, 20 second graders, and 25 third graders. If each check takes 2 minutes, how many hours will it take the nurse to complete all the checks?"""
    num_kinder = 26
    num_first = 19
    num_second = 20
    num_third = 25
    time_per_check = 2
    total_time = (num_kinder + num_first + num_second + num_third) * time_per_check
    hours = total_time / 60
    result = hours
    return result

print(solution())