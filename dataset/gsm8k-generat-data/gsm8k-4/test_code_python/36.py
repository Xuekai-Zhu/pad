def solution():
    """Lisa, Jack, and Tommy earned $60 from washing cars all week. However, half of the $60 was earned by Lisa. Tommy earned half of what Lisa earned. How much more money did Lisa earn than Tommy?"""
    # Calculate the amount earned by Lisa
    lisa_earnings = 60 * 0.5

    # Calculate the amount earned by Tommy
    tommy_earnings = lisa_earnings * 0.5

    # Calculate the difference in earnings between Lisa and Tommy
    earnings_difference = lisa_earnings - tommy_earnings

    # Return the result
    result = earnings_difference
    return result

print(solution())