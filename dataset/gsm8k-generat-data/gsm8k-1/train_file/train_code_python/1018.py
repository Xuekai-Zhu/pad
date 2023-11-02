def solution():
    """Alice and Bob decided to bake cookies for their first date. Alice baked 74 chocolate chip cookies and Bob baked 7 peanut butter cookies. After accidentally throwing some on the floor, Alice baked 5 more cookies and Bob baked 36 more. If they had 93 edible cookies at the end, how many were accidentally thrown on the floor?"""
    
    alice_cookies = 74
    bob_cookies = 7
    alice_baked = 5
    bob_baked = 36
    total_cookies = 93
    
    num_accidentally_thrown = alice_cookies + bob_cookies + alice_baked + bob_baked - total_cookies
    
    result = num_accidentally_thrown
    
    return result

print(solution())