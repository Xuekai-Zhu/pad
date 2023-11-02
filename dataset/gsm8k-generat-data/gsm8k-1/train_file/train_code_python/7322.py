def solution():
    """Amber and Josh are flying to France for vacation. Their flight leaves at 8:00 pm and as an international flight, it's recommended that they check in 2 hours early. It will take 45 minutes to drive to the airport and another 15 minutes to park their vehicle and make their way to the terminal. What is the latest time they can leave their house to make it to the airport in time?"""
    check_in_time = 2
    drive_time = 0.75 # 45 minutes
    park_time = 0.25 # 15 minutes
    total_time = check_in_time + drive_time + park_time
    latest_departure_time = datetime.datetime(2021, 10, 1, 20) - datetime.timedelta(hours=total_time)
    result = latest_departure_time.strftime('%I:%M %p')
    return result

print(solution())