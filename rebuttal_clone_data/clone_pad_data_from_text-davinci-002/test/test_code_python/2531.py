def solution():
    initial_mms = 25
    mms_after_lunch = 7
    mms_after_dinner = 5
    total_mms_eaten = mms_after_lunch + mms_after_dinner
    mms_given_to_sister = initial_mms - total_mms_eaten
    result = mms_given_to_sister
    return result

print(solution())