def solution():
    """Pete walks backwards three times faster than Susan walks forwards, and Tracy does one-handed cartwheels twice as fast as Susan walks forwards. But Pete can walk on his hands only one quarter the speed that Tracy can do cartwheels. If Pete walks on his hands at 2 miles per hour, how fast can Pete walk backwards, in miles per hour?"""
    susan_speed = 1
    pete_backwards_speed = 3 * susan_speed
    tracy_cartwheel_speed = 2 * susan_speed
    pete_hands_speed = 0.25 * tracy_cartwheel_speed

    # Let x be Pete's backwards walking speed
    # Total combined speed = Susan's speed + Pete's backwards speed + Tracy's cartwheel speed + Pete's hands speed
    # x + pete_backwards_speed + tracy_cartwheel_speed + pete_hands_speed = 2

    x = 2 - pete_backwards_speed - tracy_cartwheel_speed - pete_hands_speed
    result = x
    return result

print(solution())