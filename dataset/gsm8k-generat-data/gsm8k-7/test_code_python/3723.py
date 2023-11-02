def solution():
    # Let's assume that Cameron's speed is 2x and Chase's speed is x
    cameron_speed = 2
    chase_speed = 1

    # Danielle's speed is 3 times Cameron's speed
    danielle_speed = 3 * cameron_speed

    # As distance is same, we can set Danielle's travel time as 30 minutes
    # and calculate the distance from Granville to Salisbury
    danielle_time = 30
    distance = danielle_time * danielle_speed

    # Now we can calculate Chase's travel time using the distance and his speed
    chase_time = distance / chase_speed
    result = chase_time
    return result

print(solution())