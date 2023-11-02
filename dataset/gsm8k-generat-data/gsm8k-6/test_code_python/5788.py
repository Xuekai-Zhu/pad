def solution():
    # Calculate the average speed and time of the group
    average_speed = 21 / 3.5
    average_time = 60 / average_speed  # convert kilometers per hour to minutes per kilometer

    # Calculate Birgit's speed and time
    birgit_speed = average_speed + (4 / 60)  # add 4 minutes per kilometer to the average speed
    birgit_time = 60 / birgit_speed  # convert kilometers per hour to minutes per kilometer

    # Calculate how long it would take Birgit to travel 8 kilometers at the same pace
    time_8_kilometer = birgit_time * 8 / 21  # use proportion to find the time for 8 kilometers
    result = time_8_kilometer
    return result

print(solution())