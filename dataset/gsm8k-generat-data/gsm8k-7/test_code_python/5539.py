def solution():
    wednesday_study_time = 2
    thursday_study_time = wednesday_study_time * 3
    friday_study_time = thursday_study_time / 2
    weekend_study_time = (wednesday_study_time + thursday_study_time + friday_study_time) * 2
    total_study_time = wednesday_study_time + thursday_study_time + friday_study_time + weekend_study_time
    result = total_study_time
    return result

print(solution())