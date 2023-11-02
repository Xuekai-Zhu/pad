def solution():
    """Pete has to take a 10-minute walk down to the train station and then board a 1hr 20-minute train to LA. When should he leave if he cannot get to LA later than 0900 hours? (24-hr time)"""
    # Define the time Pete needs to arrive by
    arrival_time = "09:00"

    # Convert arrival time to minutes
    arrival_minutes = int(arrival_time[:2]) * 60 + int(arrival_time[3:])

    # Subtract the travel time from the arrival time to get the departure time
    departure_minutes = arrival_minutes - 80 - 10

    # Convert departure time back to hours and minutes
    departure_hours = departure_minutes // 60
    departure_minutes = departure_minutes % 60

    # Format the departure time as a string in 24-hour format
    departure_time = "{:02d}:{:02d}".format(departure_hours, departure_minutes)

    # Return the result
    result = departure_time
    return result

print(solution())