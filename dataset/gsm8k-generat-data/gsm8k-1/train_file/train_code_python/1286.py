def solution():
    """Pete walks backwards three times faster than Susan walks forwards, and Tracy does one-handed cartwheels twice as fast as Susan walks forwards. But Pete can walk on his hands only one quarter the speed that Tracy can do cartwheels. If Pete walks on his hands at 2 miles per hour, how fast can Pete walk backwards, in miles per hour?"""
    susan_speed = 1
    pete_backward_speed = 3 * susan_speed
    tracy_speed = 2 * susan_speed
    pete_hand_speed = 0.25 * tracy_speed
    pete_hand_speed_mph = 2
    pete_backward_speed_mph = pete_backward_speed * susan_speed * pete_hand_speed_mph / pete_hand_speed
    result = pete_backward_speed_mph
    return result

print(solution())