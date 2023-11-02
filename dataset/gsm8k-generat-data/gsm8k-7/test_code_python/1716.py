def solution():
    toby_balls = 5
    toby_rotations_per_ball = 80
    friend_apples = 4
    friend_rotations_per_apple = 101
    contest_time = 4  # minutes

    # Calculate the total number of rotations for Toby's balls
    toby_total_rotations = toby_balls * toby_rotations_per_ball

    # Calculate the total number of rotations for friend's apples
    friend_total_rotations = friend_apples * friend_rotations_per_apple

    # Calculate the total number of rotations for the winner
    winner_total_rotations = max(toby_total_rotations, friend_total_rotations)

    # Calculate the total number of rotations for the winner in 4 minutes
    total_rotations = winner_total_rotations * contest_time
    result = total_rotations
    return result

print(solution())