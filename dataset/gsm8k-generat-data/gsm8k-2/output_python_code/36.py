def solution():
    """Lisa, Jack, and Tommy earned $60 from washing cars all week. However, half of the $60 was earned by Lisa. Tommy earned half of what Lisa earned. How much more money did Lisa earn than Tommy?"""
    total_earned = 60
    lisa_earned = total_earned / 2
    tommy_earned = lisa_earned / 2
    difference = lisa_earned - tommy_earned
    result = difference
    return result

print(solution())