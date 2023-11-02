def solution():
    iowa_test_grades = ["kindergarten", "1st grade", "2nd grade", "3rd grade", "4th grade", "5th grade", "6th grade", "7th grade", "8th grade"]
    explicit_warning = True
    guest = "Nine Inch Nails"
    if guest not in iowa_test_grades and explicit_warning:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())