def solution():
    """Allyn is a golfer. At the starting tee, he hit the golf ball and it traveled 180 yards straight toward the hole. On his second turn, he hit the ball again straight toward the hole and it traveled half as far as it did on his first turn, but the ball landed 20 yards beyond the hole. On his third swing, he hit the ball onto the green and it rolled into the hole. What is the distance, in yards, from the starting tee to the hole?"""
    first_shot = 180
    second_shot = first_shot / 2
    second_shot += 20 # Adding the extra distance the ball traveled beyond the hole
    total_distance = first_shot + second_shot
    result = total_distance
    return result

print(solution())