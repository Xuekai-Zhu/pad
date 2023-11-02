def solution():
    """Allyn is a golfer. At the starting tee, he hit the golf ball and it traveled 180 yards straight toward the hole.  On his second turn, he hit the ball again straight toward the hole and it traveled half as far as it did on his first turn, but the ball landed 20 yards beyond the hole.  On his third swing, he hit the ball onto the green and it rolled into the hole.  What is the distance, in yards, from the starting tee to the hole?"""
    # Define the distance Allyn hit the ball on his first turn
    first_turn_distance = 180

    # Calculate the distance Allyn hit the ball on his second turn
    second_turn_distance = first_turn_distance / 2 + 20

    # Calculate the total distance Allyn hit the ball
    total_distance = first_turn_distance + second_turn_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())