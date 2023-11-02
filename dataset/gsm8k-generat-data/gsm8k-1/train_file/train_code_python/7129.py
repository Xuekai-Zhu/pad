def solution():
    """Bethany is working at the front desk at Joe’s Gym. There were some people lifting weights when she started her shift. Then 5 more people came in and started running on the treadmill and 2 people left. There are now 19 people in the gym. How many people were lifting weights at the start of Bethany’s shift?"""
    total_people = 19
    treadmill_users = 5
    people_left = 2
    weightlifters = total_people - treadmill_users - people_left
    result = weightlifters
    return result

print(solution())