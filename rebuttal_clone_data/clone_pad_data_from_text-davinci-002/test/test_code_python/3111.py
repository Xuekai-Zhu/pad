def solution():
    kwame_study_time = 2.5 * 60
    connor_study_time = 1.5 * 60
    lexia_study_time = 97
    total_study_time = kwame_study_time + connor_study_time + lexia_study_time
    kwame_and_connor_study_time = kwame_study_time + connor_study_time
    difference = kwame_and_connor_study_time - lexia_study_time
    return difference

print(solution())