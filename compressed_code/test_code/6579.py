def solution():
    
    
    alice_cookies = 74
    bob_cookies = 7
    alice_baked = 5
    bob_baked = 36
    total_cookies = 93
    
    num_accidentally_thrown = alice_cookies + bob_cookies + alice_baked + bob_baked - total_cookies
    
    result = num_accidentally_thrown
    
    return result

print(solution())