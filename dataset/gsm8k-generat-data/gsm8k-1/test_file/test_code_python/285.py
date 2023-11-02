def solution():
    """A car in the fast lane is traveling at 60 miles/hour. A car in the slow lane is traveling at half that speed. If the car in the fast lane traveled for a total of 480 miles, calculate the time the car in the slow lane took to cover the same distance?"""
    fast_lane_speed = 60
    slow_lane_speed = 30
    distance = 480
    time_slow_lane = distance / slow_lane_speed
    result = time_slow_lane
    return result

print(solution())