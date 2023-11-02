def solution():
    """Chance boarded a plane departing from London to New York at 6:00 a.m. ET on Monday. He arrived in New York 18 hours later. If he took another plane flying to Cape town the day he arrived in New York and arrived in Cape town at 10:00 a.m ET on Tuesday, calculate the number of hours his flight took from New York to cape town."""
    # Define the time difference between London and New York
    LNY_TIME_DIFF = 5

    # Define the time difference between New York and Cape Town
    NYC_CT_TIME_DIFF = 7

    # Define the time of arrival in New York in New York time
    arrival_NY_time = "12:00 a.m."

    # Convert the arrival time to New York time
    arrival_NY_time = convert_to_NY_time(arrival_NY_time, LNY_TIME_DIFF)

    # Calculate the departure time from New York in New York time
    departure_NY_time = add_hours_to_time(arrival_NY_time, 18)

    # Convert the departure time to Cape Town time
    departure_CT_time = convert_to_CT_time(departure_NY_time, NYC_CT_TIME_DIFF)

    # Calculate the total flight time from New York to Cape Town
    flight_time = calculate_time_difference(departure_CT_time, "10:00 a.m.")

    # Display the total flight time
    result = flight_time
    return result

# Helper functions

def convert_to_NY_time(time_str, time_diff):
    """Convert a time string in London time to New York time"""
    # Parse the time string
    time = datetime.datetime.strptime(time_str, "%I:%M %p.")

    # Calculate the time difference between London and New York
    time_diff = datetime.timedelta(hours=time_diff)

    # Apply the time difference
    time_NY = time - time_diff

    # Format the time as a string
    time_str_NY = time_NY.strftime("%I:%M %p.")

    return time_str_NY

def add_hours_to_time(time_str, hours):
    """Add a number of hours to a time string in New York time"""
    # Parse the time string
    time = datetime.datetime.strptime(time_str, "%I:%M %p.")

    # Calculate the time delta
    time_delta = datetime.timedelta(hours=hours)

    # Add the time delta to the time
    time_new = time + time_delta

    # Format the time as a string
    time_str_new = time_new.strftime("%I:%M %p.")

    return time_str_new

def convert_to_CT_time(time_str, time_diff):
    """Convert a time string in New York time to Cape Town time"""
    # Parse the time string
    time = datetime.datetime.strptime(time_str, "%I:%M %p.")

    # Calculate the time difference between New York and Cape Town
    time_diff = datetime.timedelta(hours=time_diff)

    # Apply the time difference
    time_CT = time + time_diff

    # Format the time as a string
    time_str_CT = time_CT.strftime("%I:%M %p.")

    return time_str_CT

def calculate_time_difference(time_str1, time_str2):
    """Calculate the time difference between two time strings"""
    # Parse the time strings
    time1 = datetime.datetime.strptime(time_str1, "%I:%M %p.")
    time2 = datetime.datetime.strptime(time_str2, "%I:%M %p.")

    # Calculate the time delta
    time_delta = time2 - time1

    # Calculate the total number of hours
    hours = time_delta.days * 24 + time_delta.seconds // 3600

    return hours

print(solution())