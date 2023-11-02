def solution():
    # Calculate the total number of cans collected yesterday
    sarah_yesterday = 50
    lara_yesterday = sarah_yesterday + 30
    total_yesterday = sarah_yesterday + lara_yesterday

    # Calculate the total number of cans collected today
    sarah_today = 40
    lara_today = 70
    total_today = sarah_today + lara_today

    # Calculate the difference between yesterday and today
    difference = total_yesterday - total_today
    result = difference
    return result

print(solution())