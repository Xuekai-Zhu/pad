def solution():
    """Tim drops a ball off the roof of a 96-foot tall building. The ball bounces to half the height from which it fell on each bounce. How high will it bounce on the fifth bounce?"""
    building_height = 96
    bounce_height = building_height
    for i in range(5):
        bounce_height /= 2
    result = bounce_height
    return result

print(solution())