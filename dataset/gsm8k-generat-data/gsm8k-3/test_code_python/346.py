def solution():
    """Archie is playing with his marbles outside. He loses 60% of them into the street. Of the remaining ones, he loses half down a sewer. If he has 20 left, how many did he start with?"""
    
    # Start with 20 marbles remaining
    marbles_remaining = 20
    
    # Undo losing half down the sewer
    marbles_remaining *= 2
    
    # Undo losing 40% into the street
    marbles_remaining /= (1 - 0.6)
    
    # The result is the number of marbles Archie started with
    result = marbles_remaining
    return result

print(solution())