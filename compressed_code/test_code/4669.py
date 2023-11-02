def solution():
    
    price_3_5 = 2.5
    price_6_8 = 4
    cargo_weights = [5, 5, 5, 5, 8, 8]
    total_earnings = 0
    for weight in cargo_weights:
        if weight <= 5:
            total_earnings += price_3_5
        elif weight <= 8:
            total_earnings += price_6_8
    weekly_earnings = total_earnings * 7
    result = weekly_earnings
    return result

print(solution())