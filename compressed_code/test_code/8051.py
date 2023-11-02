def solution():
    
    salt_amount = 2 * 50  
    parmesan_amount = 8 * 25  
    total_sodium = salt_amount + parmesan_amount  

    reduced_sodium = total_sodium * (2/3)  
    reduced_parmesan = (reduced_sodium - salt_amount) / 25  

    reduction = 8 - reduced_parmesan  

    result = reduction
    return result

print(solution())