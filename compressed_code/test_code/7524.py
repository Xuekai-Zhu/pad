def solution():
    
    total_distance = 5
    donation_per_km = 10
    total_donation = 0
    
    for km in range(1, total_distance+1):
        donation = donation_per_km * (2**(km-1))
        total_donation += donation
    
    result = total_donation
    return result

print(solution())