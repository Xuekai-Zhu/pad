def solution():
    # Sarah and Lara's collection yesterday
    sarah_yesterday = 50
    lara_yesterday = 50 + 30  # Lara collected 30 more than Sarah

    # Sarah and Lara's collection today
    sarah_today = 40
    lara_today = 70

    # Calculate the difference in collections today and yesterday
    difference = (sarah_yesterday + lara_yesterday) - (sarah_today + lara_today)
    result = difference
    return result

print(solution())