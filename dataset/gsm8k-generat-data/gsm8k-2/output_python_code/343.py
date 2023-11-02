def solution():
    """Archie is playing with his marbles outside. He loses 60% of them into the street. Of the remaining ones, he loses half down a sewer. If he has 20 left, how many did he start with?"""
    remaining_marbles = 20
    lost_in_street = 0.6
    lost_in_sewer = 0.5
    marbles_after_street_loss = remaining_marbles / (1 - lost_in_street)
    marbles_before_sewer_loss = marbles_after_street_loss / (1 - lost_in_sewer)
    result = marbles_before_sewer_loss
    return result

print(solution())