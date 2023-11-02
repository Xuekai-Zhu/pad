def solution():
    """Allyn is a golfer. At the starting tee, he hit the golf ball and it traveled 180 yards straight toward the hole. On his second turn, he hit the ball again straight toward the hole and it traveled half as far as it did on his first turn, but the ball landed 20 yards beyond the hole. On his third swing, he hit the ball onto the green and it rolled into the hole. What is the distance, in yards, from the starting tee to the hole?"""
    first_turn_distance = 180
    second_turn_distance = first_turn_distance / 2
    third_turn_distance = 0  # since it rolled into the hole
    total_distance = first_turn_distance + (second_turn_distance + 20) + third_turn_distance
    result = total_distance
    return result

print(solution())