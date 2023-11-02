def solution():
    """Simon has 20% more legos than Bruce, who has 20 more than Kent. If Kent has 40 legos, how many does Simon have?"""
    kent_legos = 40
    bruce_legos = kent_legos + 20
    simon_legos = int(bruce_legos * 1.2)
    result = simon_legos
    return result

print(solution())