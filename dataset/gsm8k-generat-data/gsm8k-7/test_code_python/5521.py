def solution():
    time_to_come_to_room_temp = 1  # in hours
    time_to_shape_dough = 0.25  # in hours (15 minutes)
    time_to_proof = 2  # in hours
    time_to_bake = 0.5  # in hours (30 minutes)
    time_to_cool = 0.25  # in hours (15 minutes)
    bakery_open_time = "6:00 AM"

    # Calculate the total time needed to prepare the bread
    total_time = (time_to_come_to_room_temp + time_to_shape_dough +
                  time_to_proof + time_to_bake + time_to_cool)

    # Convert bakery open time to 24-hour format
    bakery_open_time_24 = datetime.strptime(bakery_open_time, '%I:%M %p').strftime('%H:%M')

    # Calculate the latest time the head baker can arrive at the store
    latest_time = datetime.strptime(bakery_open_time_24, '%H:%M') - timedelta(hours=total_time)

    # Convert latest time to 12-hour format
    latest_time_12 = datetime.strftime(latest_time, '%I:%M %p')
    result = latest_time_12
    return result

print(solution())