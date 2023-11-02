def solution():
    
    meatballs_per_pound = 16
    total_meatballs = 80
    total_pounds = total_meatballs / meatballs_per_pound
    secret_seasoning_needed = total_pounds * 2
    result = secret_seasoning_needed
    return result

print(solution())