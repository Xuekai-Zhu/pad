def solution():
    total_time_in_a_day = 24 * 60  # Convert 24 hours a day to minutes
    tv_time = total_time_in_a_day * (1/5)  # Mia spent 1/5 of her day watching TV
    study_time = (total_time_in_a_day - tv_time) * (1/4)  # Mia spent 1/4 of the remaining time on studying
    result = study_time
    return result

print(solution())