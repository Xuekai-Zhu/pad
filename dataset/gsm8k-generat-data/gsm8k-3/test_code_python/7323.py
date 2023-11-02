def solution():
    """Amber and Josh are flying to France for vacation.  Their flight leaves at 8:00 pm and as an international flight, it's recommended that they check in 2 hours early.  It will take 45 minutes to drive to the airport and another 15 minutes to park their vehicle and make their way to the terminal.  What is the latest time they can leave their house to make it to the airport in time?"""
    # Define the time they need to be at the airport
    airport_time = datetime.datetime(2022, 6, 1, 18, 0, 0) # 6:00 pm on June 1st, 2022

    # Calculate the latest time they can leave their house
    leave_time = airport_time - datetime.timedelta(hours=2) - datetime.timedelta(minutes=45) - datetime.timedelta(minutes=15)

    # Display the latest time they can leave their house
    result = leave_time.strftime("%I:%M %p")
    return result

print(solution())