def solution():
    """Becky bought 20 apples for 45 cents each and received a $1 discount. Kelly bought 20 apples for 50 cents each and received a 10 percent discount. How much more did Kelly pay than Becky?"""
    becky_cost = (20 * 45) - 100
    kelly_cost = (20 * 50) * 0.9
    difference = kelly_cost - becky_cost
    result = difference
    return result

print(solution())