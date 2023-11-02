def solution():
    jenny_age = charlie_age + 5
    bobby_age = charlie_age - 3
    
    # Let x be the number of years until Charlie is twice as old as Bobby
    # We set up the equation: (charlie_age + x + 5) = 2(bobby_age + x)
    # Solving for x, we get: x = (jenny_age - 2*bobby_age - 5) / 3
    
    x = (jenny_age - 2*bobby_age - 5) / 3
    
    # Charlie's age in x years will be charlie_age + x
    charlie_future_age = charlie_age + x
    
    result = charlie_future_age
    return result

print(solution())