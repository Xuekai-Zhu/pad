def solution():
    """Archie is playing with his marbles outside. He loses 60% of them into the street. Of the remaining ones, he loses half down a sewer. If he has 20 left, how many did he start with?"""
    marbles_left_after_street = 20
    marbles_left_after_sewer = marbles_left_after_street * 2
    total_marbles_after_street = marbles_left_after_street / 0.4
    total_marbles_before_sewer = total_marbles_after_street * 2
    total_marbles_before_loss = total_marbles_before_sewer / 0.5
    result = total_marbles_before_loss
    
    return result

print(solution())