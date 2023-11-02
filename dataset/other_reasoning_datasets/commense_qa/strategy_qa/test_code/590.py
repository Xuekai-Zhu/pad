def solution():
    attend_university_prep_school = ["Humans"]
    worry_about_Abitur = ["Students"]
    if "German Shepherds" in attend_university_prep_school and "German Shepherds" not in worry_about_Abitur:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())