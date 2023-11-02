def solution():
    """Charles is moving from Springfield, which has 482,653 people, to Greenville, which has 119,666 fewer people. What is the total population of Springfield and Greenville?"""
    springfield_pop = 482653
    greenville_pop = springfield_pop - 119666
    total_pop = springfield_pop + greenville_pop
    
    return total_pop

print(solution())