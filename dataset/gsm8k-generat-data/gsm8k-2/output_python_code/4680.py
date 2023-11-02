def solution():
    """Coby went on a road trip. He is traveling from Washington to Nevada but he needs to stop in Idaho which is 640 miles away from Washington and 550 miles away from Nevada to pick up some friends. If Coby is traveling at a speed of 80 miles per hour going to Idaho and at a speed of 50 miles per hour from Idaho to Nevada, how many hours did it take for him to arrive at the destination?"""
    idaho_distance = 640
    nevada_distance = 550
    idaho_speed = 80
    nevada_speed = 50
    total_time = (idaho_distance / idaho_speed) + (nevada_distance / nevada_speed)
    result = total_time
    return result

print(solution())