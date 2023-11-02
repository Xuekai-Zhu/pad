def solution():
    """Maurice had only been horseback riding a handful of times in his life. His best friend, Matt, goes horseback riding regularly. 
    When Maurice went to visit Matt for two weeks, he rode another 8 times. Each time, Matt went with him. Meanwhile, besides the times 
    that Matt accompanied Maurice, he rode an additional 16 times. If the total number of times Matt rode during that two weeks is 
    three times the number of times Maurice had ridden before his visit, how many times had Maurice been horseback riding before 
    visiting Matt?"""
    # Let's assume that Maurice had ridden 'x' times before visiting Matt
    # According to the problem, Matt rode a total of 3*x times during Maurice's visit
    # Maurice rode 8 times during his visit, and Matt accompanied him in all of those rides.
    # Therefore, Matt rode 8 additional times apart from the ones he accompanied Maurice in.
    # So, we can set up the equation as follows:
    # 3*x = 8 + x + 16
    # Solving for x gives us:
    x = 8 + 16
    # Therefore, Maurice had ridden a total of 24 times before visiting Matt.
    result = x
    return result

print(solution())