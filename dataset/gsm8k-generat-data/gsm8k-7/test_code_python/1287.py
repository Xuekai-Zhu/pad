def solution():
    # Let's assume that Susan walks forwards at a speed of 1 mph
    susan_speed = 1

    # Pete walks backwards 3 times faster than Susan walks forwards
    pete_speed_backwards = susan_speed * 3

    # Tracy does one-handed cartwheels twice as fast as Susan walks forwards
    tracy_speed_cartwheels = susan_speed * 2

    # Pete can walk on his hands only one quarter the speed that Tracy can do cartwheels
    pete_speed_hands = tracy_speed_cartwheels / 4

    # We know that Pete's speed on his hands is 2 mph
    # So we can use this to calculate Tracy's speed:
    # 2 = tracy_speed_cartwheels / 4
    # tracy_speed_cartwheels = 8 mph
    tracy_speed_cartwheels = 8

    # Now we can use Tracy's speed to calculate Pete's speed backwards:
    # pete_speed_backwards = tracy_speed_cartwheels / 2
    pete_speed_backwards = tracy_speed_cartwheels / 2
    result = pete_speed_backwards
    return result

print(solution())