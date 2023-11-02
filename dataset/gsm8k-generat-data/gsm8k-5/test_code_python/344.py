def solution():
    marbles_remaining = 20  # Archie has 20 marbles remaining
    marbles_after_street_loss = marbles_remaining / 0.4  # Archie lost 60% of his marbles, so he has 40% left
    marbles_before_sewer_loss = marbles_after_street_loss * 2  # Archie lost half of the remaining marbles down the sewer
    marbles_starting = marbles_before_sewer_loss
    result = marbles_starting
    return result

print(solution())