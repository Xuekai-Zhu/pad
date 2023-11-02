def solution():
    """Tim drops a ball off the roof of a 96-foot tall building. The ball bounces to half the height from which it fell on each bounce. How high will it bounce on the fifth bounce?"""
    initial_height = 96
    bounce_height = initial_height / 2
    num_bounces = 5
    final_bounce_height = bounce_height ** num_bounces
    result = final_bounce_height
    return result

print(solution())