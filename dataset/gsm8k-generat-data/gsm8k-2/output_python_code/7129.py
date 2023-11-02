def solution():
    """Bethany is working at the front desk at Joe’s Gym. There were some people lifting weights when she started her shift. Then 5 more people came in and started running on the treadmill and 2 people left. There are now 19 people in the gym. How many people were lifting weights at the start of Bethany’s shift?"""
    current_num = 19
    treadmill_num = current_num - 2 - initial_weightlifting_num - 5
    initial_weightlifting_num = treadmill_num + 5
    result = initial_weightlifting_num
    return result

print(solution())