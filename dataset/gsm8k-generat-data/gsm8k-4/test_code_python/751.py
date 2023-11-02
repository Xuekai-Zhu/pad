def solution():
    """Harry is joining a marathon that's why he practices and varies his workouts from day to day. He ran 10 meters per hour on Monday. From Tuesday to Thursday he ran 50% faster than on Monday. Then on Friday, he ran 60% faster than he ran on Thursday. How fast did Harry run on Friday?"""
    # Define Harry's base speed on Monday
    monday_speed = 10

    # Calculate Harry's speed from Tuesday to Thursday
    tues_thurs_speed = monday_speed * 1.5

    # Calculate Harry's speed on Friday
    friday_speed = tues_thurs_speed * 1.6

    result = friday_speed
    return result

print(solution())