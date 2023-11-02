def solution():
    
    total_businesses = 72
    fired_businesses = total_businesses / 2
    quit_businesses = total_businesses / 3
    remaining_businesses = total_businesses - fired_businesses - quit_businesses
    result = remaining_businesses
    return result

print(solution())