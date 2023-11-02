def solution():
    """Lisa, Jack, and Tommy earned $60 from washing cars all week. However, half of the $60 was earned by Lisa. Tommy earned half of what Lisa earned. How much more money did Lisa earn than Tommy?"""
    total_earnings = 60
    lisa_earnings = total_earnings / 2
    tommy_earnings = lisa_earnings / 2
    difference = lisa_earnings - tommy_earnings
    result = difference
    return result

print(solution())