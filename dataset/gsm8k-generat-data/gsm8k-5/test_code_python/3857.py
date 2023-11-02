def solution():
    total_plays = 80  # The quarterback steps back to throw 80 times in a game
    no_pass_plays = 0.3 * total_plays  # 30% of the time he does not get a pass thrown
    sacked_plays = 0.5 * no_pass_plays  # Half of the times he does not throw the ball he is sacked for a loss

    result = sacked_plays
    return result

print(solution())