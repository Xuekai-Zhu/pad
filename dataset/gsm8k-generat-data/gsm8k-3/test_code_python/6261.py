def solution():
    """At the same store, Peter bought 2 pairs of pants and 5 shirts for $62 total, and Jessica bought 2 shirts for $20 total. Each pair of pants cost the same price, and each shirt cost the same price. How much does 1 pair of pants cost?"""
    # Let's assume the cost of one pair of pants is x, and the cost of one shirt is y
    # From the first part of the problem, we have:
    2x + 5y = 62
    
    # From the second part of the problem, we have:
    2y = 20
    
    # Solving for y, we get:
    y = 10
    
    # Substituting y back into the first equation and solving for x, we get:
    2x + 5(10) = 62
    2x + 50 = 62
    2x = 12
    x = 6
    
    # Therefore, one pair of pants costs $6
    result = 6
    return result

print(solution())