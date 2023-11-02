def solution():
    # Set up system of equations
    # Let x be my current age and y be my brother's current age
    # In ten years, I'll be x + 10 and my brother will be y + 10
    # According to problem, x + 10 = 2(y + 10) and x + y + 20 = 45
    # Solve for x
    # x + 10 = 2y + 20 => x = 2y + 10
    # Substitute into second equation
    # 2y + 10 + y + 20 = 45 => 3y = 15 => y = 5
    # So my brother is currently 5 years old
    # Substitute into first equation to get my age
    # x + 10 = 2(5 + 10) => x = 25
    # So I am currently 25 years old
    result = 25
    return result

print(solution())