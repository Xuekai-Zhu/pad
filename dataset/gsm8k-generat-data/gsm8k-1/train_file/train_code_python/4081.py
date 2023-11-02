def solution():
    """Tom and his friends were filling up water balloons. Tom filled up 3 times as many water balloons as Luke. Luke filled up one fourth as many balloons as Anthony. If Anthony filled up 44 water balloons, how many did Tom fill up?"""
    
    anthony_balloons = 44
    luke_balloons = anthony_balloons / 4
    tom_balloons = 3 * luke_balloons
    
    result = tom_balloons
    return result

print(solution())