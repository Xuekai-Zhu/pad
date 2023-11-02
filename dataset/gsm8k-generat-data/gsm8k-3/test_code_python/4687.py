def solution():
    """Delaney has to catch a bus that leaves at 8:00. a.m to school every day. He always takes 30 minutes to reach the pick-up point from his home. One day he woke up late and left his home at 7:50. How much time did he miss the bus by when he reached the pick-up point?"""
    # Define the time Delaney needs to reach the pick-up point from his home
    TIME_TO_PICKUP = 30 # in minutes

    # Define the time the bus leaves
    BUS_LEAVES = "08:00"

    # Define the time Delaney left his home
    DELANEY_LEFT = "07:50"

    # Convert the time strings to minutes
    bus_leaves_minutes = int(BUS_LEAVES[:2]) * 60 + int(BUS_LEAVES[3:])
    delaney_left_minutes = int(DELANEY_LEFT[:2]) * 60 + int(DELANEY_LEFT[3:])

    # Calculate the time difference in minutes
    time_difference = bus_leaves_minutes - (delaney_left_minutes + TIME_TO_PICKUP)

    # Convert the time difference to "hours:minutes" format
    hours = time_difference // 60
    minutes = time_difference % 60
    time_missed = "{}:{}".format(hours, str(minutes).zfill(2))

    return time_missed

print(solution())