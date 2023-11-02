def solution():
    will_ferrell_birthday = 16
    dean_cain_birthday = 31
    july_fourth = 4
    july_days_in_month = 31
    
    if dean_cain_birthday - july_fourth < will_ferrell_birthday - july_fourth:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())