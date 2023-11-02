def solution():
    
    salt_sodium = 50 * 2
    parmesan_sodium = 25 * 8
    total_sodium = salt_sodium + parmesan_sodium
    target_sodium = total_sodium * (2/3)
    reduced_parma_sodium = target_sodium - salt_sodium
    reduced_parma_oz = reduced_parma_sodium / 25
    result = 8 - reduced_parma_oz
    return result

print(solution())