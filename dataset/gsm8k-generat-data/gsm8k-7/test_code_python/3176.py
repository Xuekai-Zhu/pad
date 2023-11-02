def solution():
    total_age = 35
    
    # Let's assume Rebecca's age to be x
    
    # Matthew is 2 years older than Rebecca
    matthew_age = x + 2
    
    # Freddy is 4 years younger than Matthew
    freddy_age = matthew_age - 4
    
    # Total age is the sum of all three children's ages
    # So, Rebecca's age + Matthew's age + Freddy's age = total_age
    # Substitute above equations and simplify
    x + (x+2) + (x+2-4) = total_age
    x = 9
    
    # Freddy's age is 4 years younger than Matthew, which means we can simply add 4 to Rebecca's age
    freddy_age = x + 6
    result = freddy_age
    return result

print(solution())