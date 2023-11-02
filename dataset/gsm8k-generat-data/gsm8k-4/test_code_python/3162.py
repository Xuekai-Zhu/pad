def solution():
    """If I give my brother 2 marbles I will have double his number of marbles, but my friend will have triple the number I do. The total number of marbles we have together is 63. How many marbles do I have?"""
    # Let x be the number of marbles I have
    # Let y be the number of marbles my brother has
    # Let z be the number of marbles my friend has
    
    # Based on the first statement, we can write the equation: 
    # x - 2 = 2(y + 2)
    # This can be simplified to:
    # x - 2 = 2y + 4
    # x = 2y + 6
    
    # Based on the second statement, we can write the equation:
    # z = 3(x - 2)
    # This can be simplified to:
    # z = 3x - 6
    
    # Finally, we know that the total number of marbles is 63:
    # x + y + z = 63
    
    # substituting the equations for x and z into the third equation:
    # (2y + 6) + y + (3x - 6) = 63
    # Simplifying and solving for y:
    # y = 17
    
    # Substituting y=17 into the equation for x:
    x = 2*17 + 6
    result = x
    return result

print(solution())