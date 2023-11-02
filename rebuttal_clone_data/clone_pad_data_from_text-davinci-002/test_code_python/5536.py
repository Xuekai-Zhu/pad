def solution():
    
    total_earnings = 380
    broccoli_earnings = 57
    carrot_earnings = 2 * broccoli_earnings
    spinach_earnings = carrot_earnings + 16
    cauliflower_earnings = total_earnings - (broccoli_earnings + carrot_earnings + spinach_earnings)
    result = cauliflower_earnings
    return result

print(solution())