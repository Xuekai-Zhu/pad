def solution():
    """Pete has to take a 10-minute walk down to the train station and then board a 1hr 20-minute train to LA. When should he leave if he cannot get to LA later than 0900 hours? (24-hr time)"""
    departure_time = "09:00"
    train_travel_time = "01:20"
    train_departure_time = datetime.datetime.strptime(departure_time, "%H:%M")
    train_travel_time = datetime.datetime.strptime(train_travel_time, "%H:%M")
    total_travel_time = train_travel_time + datetime.timedelta(minutes=10)
    departure_time = (train_departure_time - total_travel_time).strftime("%H:%M")
    result = departure_time
    return result

print(solution())