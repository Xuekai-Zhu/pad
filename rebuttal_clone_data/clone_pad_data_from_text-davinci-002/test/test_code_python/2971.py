def solution():
    initial_deposit = 90
    interest_rate = 10
    interest_earned = initial_deposit * (interest_rate / 100)
    total_deposit = initial_deposit + interest_earned
    result = total_deposit
    
    return result

print(solution())