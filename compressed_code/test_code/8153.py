def solution():
    
    bottles_per_crate = 12
    total_bottles = 130
    total_crates = 10
    bottles_in_crates = bottles_per_crate * total_crates
    bottles_not_in_crate = total_bottles - bottles_in_crates
    result = bottles_not_in_crate
    return result

print(solution())