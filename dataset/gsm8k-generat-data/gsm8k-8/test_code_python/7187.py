def solution():
    # Let's assume there are "c" cookies in the jar
    c = 0
    
    # If we take 1 cookie away, we have (c-1) cookies left
    # If we add 5 cookies, we have (c+5) cookies
    # The problem tells us that (c-1) is half of (c+5)
    # So we can set up the following equation and solve for c:
    # (c-1) = 0.5 * (c+5)
    # c-1 = 0.5c + 2.5
    # 0.5c = 3.5
    # c = 7
    
    # Therefore, there are 7 cookies in the jar
    result = 7
    return result

print(solution())