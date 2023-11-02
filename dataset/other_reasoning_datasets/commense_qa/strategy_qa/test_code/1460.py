def solution():
    swiss_guard_members = 135
    marines_active_duty_as_of_2017 = 186000
    if swiss_guard_members > marines_active_duty_as_of_2017:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())