def solution():
    """Bill is trying to dig a well in his backyard. He can dig 4 feet/hour through soil and half that fast through clay. If he has to dig through 24 feet of soil and 8 feet of clay, how long will it take him to dig the well?"""
    soil_depth = 24
    clay_depth = 8
    soil_speed = 4
    clay_speed = soil_speed / 2
    total_time = (soil_depth/soil_speed) + (clay_depth/clay_speed)
    result = total_time
    return result

print(solution())