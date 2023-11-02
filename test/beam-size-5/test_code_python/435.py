def solution():
    
    # Define the time it takes for Wayne to reach the theater
    wayadette_time = 5

    # Define the time it takes for the drive from Wayne's hotel
    drive_time = 4 * wayadette_time

    # Calculate the time it takes for Bernadette to stay at the hotel
    bernadette_hotel_time = drive_time / 4

    # Calculate the time it takes for Bernadette to stay at the premiere theater
    bernadette_high_rise_time = bernadette_hotel_time

    # Calculate the total time it takes for Wayne to reach the theater
    total_time = wayadette_time + bernadette_hotel_time + drive_time + bernadette_high_rise_time

    # Display the total time
    result = total_time
    return result

print(solution())