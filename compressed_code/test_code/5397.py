def solution():
    
    friends_toys = 18 + 42 + 2 + 13
    total_toys = 108
    remaining_toys = total_toys - friends_toys
    sister_toys = remaining_toys / 3
    joel_toys = 2 * sister_toys
    result = joel_toys
    return result

print(solution())