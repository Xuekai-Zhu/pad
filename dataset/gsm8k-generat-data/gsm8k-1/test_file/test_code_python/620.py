def solution():
    """Two sports coaches went shopping together. The baseball coach bought 9 new baseballs for $3 each. 
    The basketball coach bought 8 new basketballs for $14 each. How much more did the basketball coach spend than the baseball coach?"""
    baseball_balls = 9
    baseball_price = 3
    basketball_balls = 8
    basketball_price = 14
    baseball_total_cost = baseball_balls * baseball_price
    basketball_total_cost = basketball_balls * basketball_price
    difference = basketball_total_cost - baseball_total_cost
    result = difference
    return result

print(solution())