def solution():
    salt = 2
    parmesan_cheese = 8
    sodium_in_salt = 50
    sodium_in_parmesan = 25
    total_sodium = salt * sodium_in_salt + parmesan_cheese * sodium_in_parmesan
    desired_total_sodium = total_sodium * 2/3
    sodium_to_eliminate = total_sodium - desired_total_sodium
    cheese_to_eliminate = sodium_to_eliminate / sodium_in_parmesan
    result = parmesan_cheese - cheese_to_eliminate
    
    return result

print(solution())