def solution():
    original_balloons = 250  # There were initially 250 balloons
    friends = 5  # The balloons were shared evenly among 5 friends

    # Calculate how many balloons each friend received initially
    balloons_per_friend = original_balloons / friends

    # Dante asked each friend to give him 11 balloons
    balloons_given_to_Dante = 11 * friends

    # Calculate how many balloons each friend has now
    balloons_per_friend_now = (original_balloons - balloons_given_to_Dante) / friends
    result = balloons_per_friend_now
    return result

print(solution())