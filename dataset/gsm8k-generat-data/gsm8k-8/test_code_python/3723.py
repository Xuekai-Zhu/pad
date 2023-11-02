def solution():
    # Define Cameron's speed as 2x and Chase's speed as x
    cameron_speed = 2
    chase_speed = 1

    # Define Danielle's speed as 3 times Cameron's speed
    danielle_speed = 3 * cameron_speed

    # Calculate the distance from Granville to Salisbury
    distance = 30 * danielle_speed / 60

    # Calculate Chase's travel time using distance = speed * time
    chase_time = distance / chase_speed

    result = chase_time * 60
    return result

print(solution())