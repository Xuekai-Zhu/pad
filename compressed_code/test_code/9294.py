def solution():
    
    mms_after_lunch = 7
    mms_after_dinner = 5
    total_mms_eaten = mms_after_lunch + mms_after_dinner
    mms_left = 25 - total_mms_eaten
    mms_given_away = mms_left
    result = mms_given_away
    return result

print(solution())