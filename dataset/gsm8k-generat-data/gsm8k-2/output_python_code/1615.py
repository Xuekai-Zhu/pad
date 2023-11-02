def solution():
    """It’s exam season and Tristan has several exams to prepare for. On Monday, he studies for 4 hours then studies for twice this long on Tuesday. On Wednesday, Thursday, and Friday he studies for 3 hours each day. He wants to study for a total of 25 hours over the week and divides the remaining amount of study time evenly between Saturday and Sunday. How many hours does Tristan spend studying on Saturday?"""
    monday_study_time = 4
    tuesday_study_time = 2 * monday_study_time
    wednesday_study_time = 3
    thursday_study_time = 3
    friday_study_time = 3
    total_study_time = monday_study_time + tuesday_study_time + wednesday_study_time + thursday_study_time + friday_study_time
    remaining_study_time = 25 - total_study_time
    saturday_study_time = remaining_study_time / 2
    result = saturday_study_time
    return result

print(solution())