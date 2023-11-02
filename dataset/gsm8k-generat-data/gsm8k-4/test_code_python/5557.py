def solution():
    """Marcus has three times as many cheese crackers as Mona. Nicholas has 6 more crackers than Mona. If Marcus has 27 crackers, how many crackers does Nicholas have?"""
    # Calculate the number of crackers Mona has
    mono_crackers = 27 / 3
    
    # Calculate the number of crackers Nicholas has
    nicholas_crackers = mono_crackers + 6
    
    result = nicholas_crackers
    return result

print(solution())