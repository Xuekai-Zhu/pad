def solution():
    recommended_check_in_time = 2  # Check in time is recommended 2 hours before the flight
    drive_to_airport_time = 0.75  # It will take 45 minutes to drive to the airport (in hours)
    parking_and_terminal_time = 0.25  # It will take 15 minutes to park and make it to the terminal (in hours)
    total_prep_time = recommended_check_in_time + drive_to_airport_time + parking_and_terminal_time  # Total prep time (in hours)

    # Calculate the latest time they can leave their house
    latest_departure_time = '5:00 PM'  # Their flight leaves at 8:00 PM, so they should leave no later than 5:00 PM

    result = latest_departure_time
    return result

print(solution())