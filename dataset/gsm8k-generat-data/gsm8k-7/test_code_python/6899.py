def solution():
    elvie_age = 10
    total_sum_product = 131
    
    # Let a be Arielle's age
    # We know that elvie_age + a = total_sum_product / 10 because elvie_age = 10
    # And we know that elvie_age * a = total_sum_product - 10^2
    
    a = (total_sum_product / 10) - elvie_age
    a *= 2  # Multiply by 2 to get the actual value of a instead of 2a
    
    result = int(a)
    return result

print(solution())