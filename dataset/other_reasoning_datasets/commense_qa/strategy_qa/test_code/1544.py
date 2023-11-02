def solution():
    che_class = "Chemistry 101"
    maya_angelou_subjects = ["history", "literature"]
    if che_class not in maya_angelou_subjects:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())