def solution():
    """Suzanne wants to raise money for charity by running a 5-kilometer race. Her parents have pledged to donate $10 for her first kilometer and double the donation for every successive kilometer. If Suzanne finishes the race, how much money will her parents donate?"""
    total_distance = 5
    donation_per_km = 10
    total_donation = 0
    
    for km in range(1, total_distance+1):
        donation = donation_per_km * (2**(km-1))
        total_donation += donation
    
    result = total_donation
    return result

print(solution())