def solution():
    """Pete has to take a 10-minute walk down to the train station and then board a 1hr 20-minute train to LA. When should he leave if he cannot get to LA later than 0900 hours? (24-hr time)"""
    train_time = 80
    total_time = train_time + 10
    arrival_time = "09:00"
    arrival_hour, arrival_minute = map(int, arrival_time.split(":"))

    # subtract total time from arrival time
    hour = arrival_hour - (total_time // 60)
    minute = arrival_minute - (total_time % 60)

    # adjust time if minute is negative
    if minute < 0:
        minute += 60
        hour -= 1

    # format time as string
    departure_time = "{:02d}:{:02d}".format(hour, minute)
    result = departure_time
    return result

print(solution())