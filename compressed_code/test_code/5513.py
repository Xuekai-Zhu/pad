def solution():
    
    money_in_wallet = (2 * 20) + (4 * 10)
    remaining_amount = 90 - money_in_wallet
    bottles_needed = remaining_amount / 0.5
    result = bottles_needed
    return result

print(solution())