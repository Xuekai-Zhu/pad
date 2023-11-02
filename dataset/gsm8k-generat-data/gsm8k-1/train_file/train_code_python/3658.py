def solution():
    """Radhika got a new gaming system and asked everyone to get her games as gifts to add to the games she already has 
    that she bought with her gaming system. On Christmas, she is given 12 new video games. On her birthday in February, 
    she is given 8 more video games. Radhika already owned 1/2 the number of games as what she was given on Christmas and 
    her birthday. How many video games does she own now?"""
    
    christmas_games = 12
    birthday_games = 8
    total_games = (christmas_games + birthday_games) * 2
    result = total_games
    return result

print(solution())