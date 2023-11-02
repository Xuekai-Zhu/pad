def solution():
    """Kylie and Kayla pick apples together and take home 340 apples total. If Kayla picked 10 more than 4 times the amount of apples that Kylie picked, how many apples did Kayla pick?"""
    total_apples = 340
    kylie_picked = x
    kayla_picked = 4*kylie_picked + 10
    
    # We can use substitution to solve for x:
    kylie_picked + kayla_picked = total_apples
    kylie_picked + 4*kylie_picked + 10 = 340
    5*kylie_picked = 330
    kylie_picked = 66
    kayla_picked = 4*kylie_picked + 10
    
    result = kayla_picked
    return result

print(solution())