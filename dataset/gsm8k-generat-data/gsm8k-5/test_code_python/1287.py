def solution():
    pete_hands_speed = 2  # Pete walks on his hands at 2 miles per hour
    tracy_cartwheel_speed = 2 * susan_forward_speed  # Tracy does cartwheels twice as fast as Susan walks forwards
    pete_backwards_speed = 3 * susan_forward_speed  # Pete walks backwards three times faster than Susan walks forwards
    pete_hands_speed_ratio = 1/4  # Pete can walk on his hands only one quarter the speed that Tracy can do cartwheels

    # Calculate Susan's forward speed
    susan_forward_speed = (pete_hands_speed / pete_hands_speed_ratio) / (2 + 3 + 1)  

    # Calculate Pete's backwards speed
    pete_backwards_speed = 3 * susan_forward_speed

    result = pete_backwards_speed
    return result

print(solution())