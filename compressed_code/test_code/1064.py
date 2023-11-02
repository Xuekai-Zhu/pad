def solution():
    
    susy_followers = 100 + 40 + 20 + 10  
    sarah_followers = 50 + 90 + 30 + 10  
    if susy_followers > sarah_followers:
        result = susy_followers
    else:
        result = sarah_followers
    return result

print(solution())