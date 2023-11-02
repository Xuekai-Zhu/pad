def solution():
    """Allyn is a golfer. At the starting tee, he hit the golf ball and it traveled 180 yards straight toward the hole. On his second turn, he hit the ball again straight toward the hole and it traveled half as far as it did on his first turn, but the ball landed 20 yards beyond the hole. On his third swing, he hit the ball onto the green and it rolled into the hole. What is the distance, in yards, from the starting tee to the hole?"""
    # Define the distance traveled on the first swing and the distance to the hole after the second swing
    first_swing_distance = 180
    second_swing_distance = first_swing_distance / 2 + 20

    # Calculate the total distance from the starting tee to the hole
    total_distance = first_swing_distance + second_swing_distance + 2

    # Return the result
    result = total_distance
    return result

print(solution())