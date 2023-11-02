def solution():
    """Carter has a 14-hour road trip.  He wants to stop every 2 hours to stretch his legs.  He also wants to make 2 additional stops for food and 3 additional stops for gas.  If each pit stop takes 20 minutes, how many hours will his road trip become?"""
    # Define the duration of each pit stop in hours
    PIT_STOP_DURATION = 20 / 60

    # Define the number of stops for stretching
    stretching_stops = 14 // 2

    # Define the number of additional stops for food and gas
    additional_stops = 2 + 3

    # Calculate the total number of pit stops
    total_stops = stretching_stops + additional_stops

    # Calculate the total duration of all pit stops
    total_duration = total_stops * PIT_STOP_DURATION

    # Calculate the total duration of the road trip including pit stops
    total_duration += 14

    # Display the total duration of the road trip
    result = total_duration
    return result

print(solution())