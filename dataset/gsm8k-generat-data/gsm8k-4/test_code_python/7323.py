def solution():
    """Amber and Josh are flying to France for vacation. Their flight leaves at 8:00 pm and as an international flight, it's recommended that they check in 2 hours early. It will take 45 minutes to drive to the airport and another 15 minutes to park their vehicle and make their way to the terminal. What is the latest time they can leave their house to make it to the airport in time?"""
    # Define the departure time of their flight
    departure_time = "8:00 pm"

    # Calculate the recommended check-in time
    checkin_time = "6:00 pm"

    # Calculate the time needed to get to the airport
    driving_time = 45
    parking_time = 15
    total_time_to_airport = driving_time + parking_time

    # Calculate the latest time they can leave their house
    latest_departure_time = datetime.datetime.strptime(departure_time, "%I:%M %p") - datetime.timedelta(hours=2, minutes=total_time_to_airport)
    latest_departure_time = datetime.datetime.strftime(latest_departure_time, "%I:%M %p")

    # return the result
    result = latest_departure_time
    return result

print(solution())