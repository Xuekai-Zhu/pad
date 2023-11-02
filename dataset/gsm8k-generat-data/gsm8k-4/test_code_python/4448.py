def solution():
    """Daniel works for a sports stadium filling water bottles for athletes. He filled 254 water bottles this season.
    The football team had 11 players that wanted 6 bottles each. The soccer team had him fill 53 bottles. 
    The lacrosse team needed 12 more bottles than the football team. Each team coach during the season also wanted two bottles apiece. 
    How many bottles did he fill for the rugby team during the final game he worked this season?"""
    
    # Calculate the number of bottles used by the football team
    football_bottles = 11 * 6

    # Calculate the number of bottles used by the lacrosse team
    lacrosse_bottles = football_bottles + 12
    
    # Calculate the number of bottles used by the coaches
    coach_bottles = 2 * 4
    
    # Calculate the total number of bottles used by the football, lacrosse, and coach teams
    total_bottles_used = football_bottles + lacrosse_bottles + coach_bottles + 53
    
    # Calculate the number of bottles filled for the rugby team
    rugby_bottles = 254 - total_bottles_used
    
    return rugby_bottles

print(solution())