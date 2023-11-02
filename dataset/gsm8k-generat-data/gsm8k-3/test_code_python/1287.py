def solution():
    """Pete walks backwards three times faster than Susan walks forwards, and Tracy does one-handed cartwheels twice as fast as Susan walks forwards. But Pete can walk on his hands only one quarter the speed that Tracy can do cartwheels. If Pete walks on his hands at 2 miles per hour, how fast can Pete walk backwards, in miles per hour?"""
    # Define Susan's walking speed as the reference speed
    susan_speed = 1

    # Pete's backward walking speed
    pete_backwards_speed = susan_speed * 3

    # Tracy's cartwheel speed
    tracy_cartwheel_speed = susan_speed * 2

    # Pete's hand-walking speed
    pete_handwalking_speed = 2  # miles per hour

    # Use ratios to find Pete's backward walking speed as a multiple of Susan's speed
    backward_cartwheel_ratio = pete_backwards_speed / tracy_cartwheel_speed
    handwalking_cartwheel_ratio = pete_handwalking_speed / tracy_cartwheel_speed
    backward_speed_ratio = backward_cartwheel_ratio / handwalking_cartwheel_ratio

    # Calculate Pete's backward walking speed
    pete_backwards_speed = tracy_cartwheel_speed * backward_speed_ratio

    # Display Pete's backward walking speed
    result = pete_backwards_speed
    return result

print(solution())