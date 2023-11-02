def solution():
    # Convert Pete's hand-walking speed to cartwheels per hour
    pete_hand_speed_cw = 2 / 1.5  # Pete can walk on his hands one quarter as fast as Tracy does cartwheels
    # Convert Susan's walking speed to backwards walking speed for Pete
    susan_back_speed = pete_hand_speed_cw / 3  # Pete walks backwards three times faster than Susan walks forwards
    # Convert backwards walking speed to miles per hour
    pete_back_speed = susan_back_speed * 0.681818  # There are approximately 0.681818 miles per kilometer
    result = pete_back_speed
    return result

print(solution())