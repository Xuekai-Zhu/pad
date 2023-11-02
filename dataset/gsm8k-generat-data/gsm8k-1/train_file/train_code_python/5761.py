def solution():
    """The school nurse must conduct lice checks at the elementary school. She must check 26 Kindergarteners, 19 first graders, 20 second graders, and 25 third graders. If each check takes 2 minutes, how many hours will it take the nurse to complete all the checks?"""
    k_count = 26
    f_count = 19
    s_count = 20
    t_count = 25
    checks_total = k_count + f_count + s_count + t_count
    check_time = 2
    total_time_minutes = checks_total * check_time
    total_time_hours = total_time_minutes / 60
    result = total_time_hours
    return result

print(solution())