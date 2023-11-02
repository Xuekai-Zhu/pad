def solution():
    """The rainstorm flooded the wetlands and washed Phineas Frog 200 yards away from his home in the swamp. To return home, he will need to hop and swim his way back. If he hops on land at a speed of 20 yards per minute, and swims through water at a speed of 10 yards per minute, how long will it take Phineas, in minutes, to return home if half of the distance is on land and the other half is in water?"""
    total_distance = 200
    land_distance = total_distance / 2
    water_distance = total_distance / 2
    land_speed = 20
    water_speed = 10
    time_on_land = land_distance / land_speed
    time_on_water = water_distance / water_speed
    total_time = time_on_land + time_on_water
    result = total_time
    return result

print(solution())